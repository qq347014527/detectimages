import subprocess
import cv2
import queue
import threading
from PIL import Image
import numpy as np
import sys
import tracker
from detector import Detector
import cv2
import time
import datetime
from PIL import Image, ImageDraw, ImageFont
from copy import deepcopy

rtmp = "rtmp://10.151.51.2/live/livestream6-1"
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

font_draw_number = cv2.FONT_HERSHEY_SIMPLEX
draw_text_postion = (25, 80)


q=queue.Queue()


def ImgReceive():
    print("Start reveive")
    cap = cv2.VideoCapture(urlurl[0])
    print('cap.isOpened(): ',cap.isOpened())
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            q.put(frame)
        if not(ret): #若没有帧返回，则重新刷新rtsp视频流
           # cap = cv2.VideoCapture(urlurl[0])
           # print('refresh rtsp')
           break
        


 
def ImgProcess():
    
    print("Start process")
    
    # 进入数量
    in_count = 0
    # 离开数量
    out_count = 0
    
    while True:
    
        if q.empty() !=True:
         
            frame=q.get()

            if frame is None:
                print('illegal input ')
                break
                
            now_time = datetime.datetime.now()
            if now_time.hour == 0 and now_time.minute ==0:
                in_count = 0
                out_count = 0

            frame = cv2.resize(frame, (960, 540))

            list_bboxs = []
            bboxes = detector.detect(frame)

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

                            print('out count:', out_count, ', out id:', list_overlapping_yellow_polygon)

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
            
            
#            output_image_frame = cv2ImgAddText(output_image_frame, text_draw, 25, 80, (0, 0 , 150), 20)
            
            output_image_frame = cv2.putText(img=output_image_frame, text=text_draw,
                                             org=draw_text_postion,
                                            fontFace=font_draw_number,
                                            fontScale=0.8, color=(0, 0, 150), thickness=2)
                                             
            pipe.stdin.write(output_image_frame.tostring())                               
    pipe.terminate()
            

def cv2ImgAddText(img, text, left, top, textColor=(0, 255, 0), textSize=20):
    if (isinstance(img, np.ndarray)):  # 判断是否OpenCV图片类型
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(img)
    # 字体的格式
    fontStyle = ImageFont.truetype(
        "font/simsun.ttc", textSize, encoding="utf-8")
    # 绘制文本
    draw.text((left, top), text, textColor, font=fontStyle)
    # 转换回OpenCV格式
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)

 
if __name__=='__main__':
    p1 = threading.Thread(target=ImgReceive)
    p2 = threading.Thread(target=ImgProcess)
    p1.start()
    p2.start()
    
