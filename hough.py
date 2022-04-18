import cv2
import argparse
import numpy as np

# 命令行选项
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--origin_file', default='picture.jpg', type=str)
parser.add_argument('-c', '--canny_file', default='canny_result.npy', type=str)
args = parser.parse_args()

# 图片路径
path_result = 'result_pic/'
path_origin = 'source_pic/'
# 读取图片
img = cv2.imread(path_origin+args.origin_file)
# 读取canny的输出
canny_img = np.load(path_result+args.canny_file)
assert img is not None, 'origin picture do not exist!'
assert canny_img is not None, 'origin picture do not exist!'

# 创建窗口
cv2.namedWindow('hough demo', 0)
circles = None
# 默认参数
param1 = 80
param2 = 60
min_radius = 70
max_radius = 250
min_distance = 200


# 根据识别的圆与原始图像进行绘制
def draw(circle, img):
    global circles
    if circle is None:
        return
    circles = np.uint16(np.around(circle))[0]
    cimg = np.array(img)
    for i in circles:
        cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)  # 绘制外圈圆（蓝色）
        cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)  # 绘制圆心（红色）
    cv2.imshow('hough demo', cimg)


def param1Set(p1):
    global param1, param2, min_radius, max_radius, circles, min_distance, img
    param1 = p1
    cv2.imshow('hough demo', canny_img)
    circle = cv2.HoughCircles(canny_img, cv2.HOUGH_GRADIENT, dp=1, minDist=min_distance,
                           param1=param1, param2=param2, minRadius=min_radius, maxRadius=max_radius)
    draw(circle, img)


def param2Set(p2):
    global param1, param2, min_radius, max_radius, circles, img, min_distance
    param2 = p2
    circle = cv2.HoughCircles(canny_img, cv2.HOUGH_GRADIENT, dp=1, minDist=min_distance,
                           param1=param1, param2=param2, minRadius=min_radius, maxRadius=max_radius)
    draw(circle, img)


def minRadius(r):
    global param1, param2, min_radius, max_radius, circles, img, min_distance
    min_radius = r
    circle = cv2.HoughCircles(canny_img, cv2.HOUGH_GRADIENT, dp=1, minDist=min_distance,
                              param1=param1, param2=param2, minRadius=min_radius, maxRadius=max_radius)
    draw(circle, img)


def maxRadius(r):
    global param1, param2, min_radius, max_radius, circles, img, min_distance
    max_radius = r
    circle = cv2.HoughCircles(canny_img, cv2.HOUGH_GRADIENT, dp=1, minDist=min_distance,
                              param1=param1, param2=param2, minRadius=min_radius, maxRadius=max_radius)
    draw(circle, img)


def minDistance(d):
    global param1, param2, min_radius, max_radius, circles, img, min_distance
    min_distance = d
    circle = cv2.HoughCircles(canny_img, cv2.HOUGH_GRADIENT, dp=1, minDist=min_distance,
                              param1=param1, param2=param2, minRadius=min_radius, maxRadius=max_radius)
    draw(circle, img)


# 创建滑动条
cv2.createTrackbar('param1', 'hough demo', param1, 200, param1Set)
cv2.createTrackbar('param2', 'hough demo', param2, 200, param2Set)
cv2.createTrackbar('min radius', 'hough demo', min_radius, 1000, minRadius)
cv2.createTrackbar('max radius', 'hough demo', max_radius, 2000, maxRadius)
cv2.createTrackbar('min distance', 'hough demo', min_distance, 2000, minDistance)
# 摁下Esc退出并打印圆的信息
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
    print(f'一共检测到了{len(circles)}个圆环，它们的x,y坐标与r半径分别为：')
    print(circles)
# 输出图像
if circles is not None:
    circles = np.uint16(np.around(circles))
    cimg = np.array(img)
    for i in circles:
        cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)  # 绘制外圈圆（绿色）
        cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)  # 绘制圆心（红色）
    cv2.imwrite(path_result+'hough_result.jpg', cimg)
