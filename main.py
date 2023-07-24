import subprocess
import cv2
import queue
import threading
import numpy as np
import sys
import tracker
from detector import Detector
import cv2
from PIL import Image
rtmp = "rtmp://10.151.51.2/live/livestream7-1"
urlurl=['rtsp://admin:hik12345+@10.1.125.6:554/Streaming/Channels/101']
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
               '-r', '25',
               '-i', '-',
               '-c:v', 'libx264',
               '-pix_fmt', 'yuv420p',
               '-preset', 'ultrafast',
               '-f', 'flv',
               rtmp]

pipe = subprocess.Popen(command
                            , shell=False
                            , stdin=subprocess.PIPE)
def pass_by():
    mask_image_temp = np.zeros((1080, 1920), dtype=np.uint8)

    list_pts_blue = [[650, 550], [550, 650], [1500, 900], [1550, 700]]

    ndarray_pts_blue = np.array(list_pts_blue, np.int32)
    polygon_blue_value_1 = cv2.fillPoly(mask_image_temp, [ndarray_pts_blue], color=1)
    #在NumPy中，数组的维度可以通过在索引操作中使用np.newaxis来扩展。它实际上是一个None的别名，用于表示增加一个维度。
    polygon_blue_value_1 = polygon_blue_value_1[:, :, np.newaxis]

    mask_image_temp = np.zeros((1080, 1920), dtype=np.uint8)
    list_pts_yellow = [[500, 650], [450, 750], [1450, 900], [1500, 800]]

    ndarray_pts_yellow = np.array(list_pts_yellow, np.int32)
    polygon_yellow_value_2 = cv2.fillPoly(mask_image_temp, [ndarray_pts_yellow], color=2)
    polygon_yellow_value_2 = polygon_yellow_value_2[:, :, np.newaxis]

    polygon_mask_blue_and_yellow = polygon_blue_value_1 + polygon_yellow_value_2

    polygon_mask_blue_and_yellow = cv2.resize(polygon_mask_blue_and_yellow, (960, 540))

    # 蓝 色盘 b,g,r
    blue_color_plate = [10, 0, 0]
    # 蓝 polygon图片
    blue_image = np.array(polygon_blue_value_1 * blue_color_plate, np.uint8)

    # 黄 色盘
    yellow_color_plate = [0, 10, 10]
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

    # 进入数量
    in_count = 0
    # 离开数量
    out_count = 0

    font_draw_number = cv2.FONT_HERSHEY_SIMPLEX
    draw_text_postion = (int(960 * 0.01), int(540 * 0.05))

    # 初始化 yolov5
    detector = Detector()

    # 打开视频
    capture = cv2.VideoCapture(urlurl[0])

    index = 0
    videoWriter = None
    fps = 25
    while True:
        # 读取每帧图片
        _, im = capture.read()
        if im is None:
            break

        im = cv2.resize(im, (960, 540))

        list_bboxs = []
        bboxes = detector.detect(im)

        # 如果画面中 有bbox
        if len(bboxes) > 0:
            list_bboxs = tracker.update(bboxes, im)

            output_image_frame = tracker.draw_bboxes(im, list_bboxs, line_thickness=None)
            pass
        else:
            # 如果画面中 没有bbox
            output_image_frame = im
        pass

        # 输出图片
        output_image_frame = cv2.add(output_image_frame, color_polygons_image)

        if len(list_bboxs) > 0:
            # ----------------------判断撞线----------------------
            for item_bbox in list_bboxs:
                x1, y1, x2, y2, _, track_id = item_bbox

                # 撞线检测点，(x1，y1)，y方向偏移比例 0.0~1.0
                y1_offset = int(y1 + ((y2 - y1) * 0.8))

                # 撞线的点
                y = y1_offset
                x = x1

                if polygon_mask_blue_and_yellow[y, x] == 1:
                    # 如果撞 蓝polygon
                    if track_id not in list_overlapping_blue_polygon:
                        list_overlapping_blue_polygon.append(track_id)
                    pass

                    if track_id in list_overlapping_yellow_polygon:
                        # 外出+1
                        out_count += 1

                        print('out count:', out_count, ', out id:', list_overlapping_yellow_polygon)

                        list_overlapping_yellow_polygon.remove(track_id)

                        pass
                    else:

                        pass

                elif polygon_mask_blue_and_yellow[y, x] == 2:
                    # 如果撞 黄polygon
                    if track_id not in list_overlapping_yellow_polygon:
                        list_overlapping_yellow_polygon.append(track_id)
                    pass

                    if track_id in list_overlapping_blue_polygon:
                        # 进入+1
                        in_count += 1

                        print('in count:', in_count, ', in id:', list_overlapping_blue_polygon)

                        # 删除 蓝polygon list 中的此id
                        list_overlapping_blue_polygon.remove(track_id)

                        pass
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
                    pass
                    if id1 in list_overlapping_blue_polygon:
                        list_overlapping_blue_polygon.remove(id1)
                    pass
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
        output_image_frame = cv2.putText(img=output_image_frame, text=text_draw,
                                         org=draw_text_postion,
                                         fontFace=font_draw_number,
                                         fontScale=0.8, color=(255, 255, 255), thickness=2)
        index = index + 1
        fileName = './images/' + 'frame_' + str(index) + '.jpg'
        # if videoWriter is None:
        #     fourcc = cv2.VideoWriter_fourcc(
        #         'm', 'p', '4', 'v')  # opencv3.0
        #     videoWriter = cv2.VideoWriter(
        #         './video/result.mp4', fourcc, fps, (output_image_frame.shape[1], output_image_frame.shape[0]))
        #
        # videoWriter.write(output_image_frame)

        # cv2.imshow('demo', output_image_frame)
        # cv2.waitKey(10)
        pipe.stdin.write(output_image_frame.tostring())

        pass
    pass
    pipe.terminate()
    # capture.release()
    # cv2.destroyAllWindows()


if __name__ == '__main__':

    pass_by()
