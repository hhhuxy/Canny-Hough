import cv2
import argparse
import numpy as np

# 命令行选项
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input_file', default='picture.jpg', type=str)  # 输入文件名
parser.add_argument('--guassian_kernel_size', type=int, default=3)  # 高斯模糊卷积核大小，若输入小于等于0则不进行高斯模糊
parser.add_argument('--default_kernel_size', type=int, default=5)
parser.add_argument('--canny_max_lowThreshold', type=int, default=1000)  # canny方法的最大低threshold
parser.add_argument('--canny_max_highThreshold', type=int, default=2500)  # canny方法的最大低threshold
parser.add_argument('--output_file', type=str, default='canny_result.npy')  # 输出文件名
args = parser.parse_args()
# 图片路径
path_result = 'result_pic/'
path_origin = 'source_pic/'
max_lowThreshold = args.canny_max_lowThreshold
max_highThreshold = args.canny_max_highThreshold
# 默认参数
low_threshold = 200
high_threshold = 600
kernel_size = args.default_kernel_size
guassian_kernel_size = args.guassian_kernel_size
# 读取原图
img = cv2.imread(path_origin+args.input_file)
assert img is not None, 'origin picture do not exist!'
# 高斯模糊
if guassian_kernel_size > 0:
    img = cv2.GaussianBlur(img, (guassian_kernel_size, guassian_kernel_size), 0)
# 转灰度图
gray_img = cv2.imread(path_origin+args.input_file, cv2.IMREAD_GRAYSCALE)

detected_edges = None


def main():
    def canny_low_threshold(lowThreshold):
        global low_threshold, high_threshold, detected_edges, kernel_size
        low_threshold = lowThreshold
        detected_edges = cv2.Canny(gray_img, low_threshold, high_threshold, apertureSize=kernel_size)
        cv2.imshow('canny demo', detected_edges)

    def canny_high_threshold(highThreshold):
        global low_threshold, high_threshold, detected_edges, kernel_size
        high_threshold = highThreshold
        detected_edges = cv2.Canny(gray_img, low_threshold, high_threshold, apertureSize=kernel_size)
        cv2.imshow('canny demo', detected_edges)

    def canny_kernel_size(s):
        if s < 3 or s > 7 or s % 2 != 1:
            return
        global low_threshold, high_threshold, detected_edges, kernel_size
        kernel_size = s
        detected_edges = cv2.Canny(gray_img, low_threshold, high_threshold, apertureSize=kernel_size)
        cv2.imshow('canny demo', detected_edges)

    #创建窗口与滑动条
    cv2.namedWindow('canny demo', 0)
    cv2.createTrackbar('min threshold', 'canny demo', low_threshold, max_lowThreshold, canny_low_threshold)
    cv2.createTrackbar('high threshold', 'canny demo', high_threshold, max_highThreshold, canny_high_threshold)
    cv2.createTrackbar('kernel_size', 'canny demo', kernel_size, 7, canny_kernel_size)
    # initialization
    canny_high_threshold(high_threshold)
    # 摁下Esc退出并输出识别结果
    if cv2.waitKey(0) == 27:
        np.save(path_result+args.output_file, detected_edges)  # houge的输入数据
        cv2.imwrite(path_result+'canny_pic.jpg', detected_edges)  # 可视图片
        cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
