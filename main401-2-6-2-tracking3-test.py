import subprocess
import datetime
import threading
from PIL import Image
import numpy as np
import sys
import tracker
from detector import Detector
import cv2
import time
from copy import deepcopy

rtmp = "rtmp://10.151.51.2/live/livestream6-2"
urlurl=['rtsp://admin:hik12345+@10.1.125.6:554/Streaming/Channels/101']
#rtmp = "rtmp://10.151.51.2/live/livestream7-2"
#urlurl=['rtsp://admin:hik12345+@10.1.125.8:554/Streaming/Channels/101']
    #urlurl.append('')
video = cv2.VideoCapture(urlurl[0])
size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
sizeStr = str(size[0]) + 'x' + str(size[1])


command = ['ffmpeg',
               '-y', '-an',
               '-f', 'rawvideo',
               '-vcodec', 'rawvideo',
               '-pix_fmt', 'bgr24',
               '-s', '960x540',
               '-r', '15',              
               '-i', '-',
               '-c:v', 'libx264',
               '-pix_fmt', 'yuv420p',
               '-preset', 'ultrafast',
               '-f', 'flv',
               rtmp]

pipe = subprocess.Popen(command
                             , shell=False
                             , stdin=subprocess.PIPE)





mask_image_temp = np.zeros((1080, 1920), dtype=np.uint8)
#list_pts_blue = [[1050, 460], [1050, 790], [1730, 800], [1735, 460]]
#list_pts_blue = [[790, 450], [750, 650], [1300, 680], [1300, 450]]
list_pts_blue = [[755, 440], [755, 660], [1165, 660], [1160, 440]]

ndarray_pts_blue = np.array(list_pts_blue, np.int32)
polygon_blue_value_1 = cv2.fillPoly(mask_image_temp, [ndarray_pts_blue], color=10)
polygon_blue_value_1 = polygon_blue_value_1[:, :, np.newaxis]

mask_image_temp = np.zeros((1080, 1920), dtype=np.uint8)
#list_pts_yellow = [[250, 795], [150, 900], [1830, 1010], [1810, 890]]
#list_pts_yellow = [[180, 617], [107, 685], [1389, 835], [1335, 745]]
list_pts_yellow = [[1, 660], [1, 757], [1650, 890], [1660, 780]]
ndarray_pts_yellow = np.array(list_pts_yellow, np.int32)
polygon_yellow_value_2 = cv2.fillPoly(mask_image_temp, [ndarray_pts_yellow], color=200)
polygon_yellow_value_2 = polygon_yellow_value_2[:, :, np.newaxis]

polygon_mask_blue_and_yellow = polygon_blue_value_1 + polygon_yellow_value_2

polygon_mask_blue_and_yellow = cv2.resize(polygon_mask_blue_and_yellow, (960, 540))

# 蓝 色盘 b,g,r
blue_color_plate = [30, 0, 0]
# 蓝 polygon图片
blue_image = np.array(polygon_blue_value_1 * blue_color_plate, np.uint8)

# 黄 色盘
yellow_color_plate = [0, 15, 15]
# 黄 polygon图片
yellow_image = np.array(polygon_yellow_value_2 * yellow_color_plate, np.uint8)

# 彩色图片（值范围 0-255）
color_polygons_image = blue_image + yellow_image
# 缩小尺寸，1920x1080->960x540
color_polygons_image = cv2.resize(color_polygons_image, (960, 540))

# list 与蓝色polygon重叠
list_overlapping_blue_polygon = []

# list 与黄色polygon重叠
list_overlapping_yellow_polygon = []



# 初始化 yolov5
detector = Detector()

in_count = 0
out_count = 0
index = 0

font_draw_number = cv2.FONT_HERSHEY_SIMPLEX
draw_text_postion = (25, 80)


thread_lock = threading.Lock()
thread_exit = False

videoWriter = None

class myThread(threading.Thread):
    def __init__(self, camera_id, img_height, img_width):
        super(myThread, self).__init__()
        self.camera_id = camera_id
        self.img_height = img_height
        self.img_width = img_width
        self.frame = np.zeros((img_height, img_width, 3), dtype=np.uint8)

    def get_frame(self):
        return deepcopy(self.frame)

    def run(self):
        global thread_exit
        global videoWriter
        global index
        global in_count,out_count

        last_time = 0
        cap = cv2.VideoCapture(self.camera_id)
        while not thread_exit:
            ret, frame = cap.read()
            if ret:
                index = index +1
                frame = cv2.resize(frame, (self.img_width, self.img_height))
                list_bboxs = []
                bboxes = detector.detect(frame)

                now_time = datetime.datetime.now()

                # 如果画面中 有bbox
                if len(bboxes) > 0:
                    list_bboxs = tracker.update(bboxes, frame)

                    output_image_frame = tracker.draw_bboxes(frame, list_bboxs, line_thickness=None)
                else:
                    # 如果画面中 没有bbox
                    output_image_frame = frame

                # 输出图片
                output_image_frame = cv2.add(output_image_frame, color_polygons_image)

                if len(list_bboxs) > 0:
                    # ----------------------判断撞线----------------------
                    for item_bbox in list_bboxs:
                        x1, y1, x2, y2, _, track_id = item_bbox

                        # 撞线检测点，(x1，y1)，y方向偏移比例 0.0~1.0
                        y1_offset = int(y1 + ((y2 - y1) * 1))
                        x1_offset = int(x1 + ((x2 - x1) * 0.5))

                        # 撞线的点
                        y = y1_offset
                        x = x1_offset

                        if polygon_mask_blue_and_yellow[y, x] == 10:
                            # 如果撞 蓝polygon
                            if track_id not in list_overlapping_blue_polygon:
                                list_overlapping_blue_polygon.append(track_id)

                            if track_id in list_overlapping_yellow_polygon:
                                # 外出+1
                                out_count += 1
                                list_overlapping_yellow_polygon.remove(track_id)

                            else:
                                pass

                        elif polygon_mask_blue_and_yellow[y, x] == 200:
                            # 如果撞 黄polygon
                            if track_id not in list_overlapping_yellow_polygon:
                                list_overlapping_yellow_polygon.append(track_id)

                            if track_id in list_overlapping_blue_polygon:
                                # 进入+1
                                in_count += 1

                                print('in count:', in_count, ', in id:', list_overlapping_blue_polygon)

                                # 删除 蓝polygon list 中的此id
                                list_overlapping_blue_polygon.remove(track_id)
                            else:
                                pass
                            pass
                        else:
                            pass
                        pass

                    pass

                    # ----------------------清除无用id----------------------
                    list_overlapping_all = list_overlapping_yellow_polygon + list_overlapping_blue_polygon
                    for id1 in list_overlapping_all:
                        is_found = False
                        for _, _, _, _, _, bbox_id in list_bboxs:
                            if bbox_id == id1:
                                is_found = True
                                break
                            pass
                        pass

                        if not is_found:
                            # 如果没找到，删除id
                            if id1 in list_overlapping_yellow_polygon:
                                list_overlapping_yellow_polygon.remove(id1)
                            if id1 in list_overlapping_blue_polygon:
                                list_overlapping_blue_polygon.remove(id1)
                        pass
                    list_overlapping_all.clear()
                    pass

                    list_bboxs.clear()

                    pass
                else:

                    list_overlapping_blue_polygon.clear()
                    list_overlapping_yellow_polygon.clear()
                    pass
                pass

                text_draw = 'IN: ' + str(in_count) + \
                            ' , OUT: ' + str(out_count)
                output_image_frame = cv2.putText(img=output_image_frame, text=str(text_draw),
                                                 org=draw_text_postion,
                                                 fontFace=font_draw_number,
                                                 fontScale=0.8, color=(0, 0, 150), thickness=2)

                fileName = './images/' + 'frame_' + str(index) + '.jpg'
               # cv2.imwrite(fileName, output_image_frame);

                if videoWriter is None:
                    fourcc = cv2.VideoWriter_fourcc(
                        'm', 'p', '4', 'v')  # opencv3.0
                    videoWriter = cv2.VideoWriter(
                        './video/result2.mp4', fourcc, 25,
                        (output_image_frame.shape[1], output_image_frame.shape[0]))

                videoWriter.write(output_image_frame)
                
                pipe.stdin.write(output_image_frame.tostring()) 
                #cv2.imshow('demo',output_image_frame)
                #cv2.waitKey(1)

                thread_lock.acquire()
                self.frame = output_image_frame
                #self.frame = frame
                thread_lock.release()
            else:
                thread_exit = True
            pipe.terminate()
        cap.release()
        


def main():
    global thread_exit
    camera_id = 0
    img_height = 540
    img_width = 960
    thread = myThread(urlurl[0], img_height, img_width)
    thread.start()

    while not thread_exit:
        thread_lock.acquire()
        frame = thread.get_frame()

       # cv2.imshow('Video', frame)
        thread_lock.release()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            thread_exit = True
    thread.join()


if __name__=='__main__':
    main()
    