# 文件说明

`canny.py`：Canny边缘检测源代码

`hough.py`：Hough圆检测源代码

`/result_pic`文件夹下存储程序输出的结果

`/source_pic`文件夹下存储程序的输入文件

# 如何运行：

Requirements:

* Anaconda3
* Python 3.x

输入以下命令以创建运行所需的虚拟环境，并安装运行所需的包

````bash
conda create -n cv python=3.9
conda activate cv
conda install --channel https://conda.anaconda.org/menpo opencv
conda install argparse numpy
````

需先运行`canny.py`得到边缘提取的输出结果后再运行`hough.py`

先后运行以下命令可采用默认值运行一遍源程序并得到对`/source_pic/picture.jpg`图片进行识别硬币边缘与圆心的结果

````bash
python canny.py
python hough.py
````

**注意：**

* 以上程序运行后会弹出一个窗口，可以点击全屏以方便操作
* 可拉动窗口下方的滑动条来调整参数的数值，可即时观察输出结果

* <font color="red"> 调至满意的效果后，**请摁下`Esc`键**来正常退出程序，并保存输出的结果</font>

* 请先运行canny后运行hough
* 检测完成后将在命令行窗口中输出圆环的个数与每个圆环的坐标、半径
* **违背以上操作造成的程序无法正常运行并非程序编写者的过失**

程序运行截图：

canny.py:

<img src="D:\大三\大三下\cv\作业\钱币检测\img\canny_demo.png" alt="canny_demo" style="zoom:50%;" />

hough.py:

<img src="D:\大三\大三下\cv\作业\钱币检测\img\hough_demo.png" alt="hough_demo" style="zoom:50%;" />



## 可选参数

### canny

* `--input_file` 输入文件名，应为`/source`文件夹下存在的文件的文件名
* `--guassion_kernel_size` 若图像质量不佳，可设置大于0的高斯卷积核大小，对图像进行预处理（高斯模糊`cv2.GuassianBlur`），默认为3；当被设定为小于0的值时，不进行高斯模糊处理
* `--canny_kernel_size` Canny方法的卷积核默认大小，默认为5（该参数应为大于等于3，小于等于7的奇数，若设为其他数字，图像不会改变）
* `--canny_max_lowThreshold` Canny的低阈值的滚动条的最大值，默认为1000（在需要使用其他大小的卷积核时需调整）
* `--canny_max_highThreshold` Canny的高阈值的滚动条的最大值，默认为2000（在需要使用其他大小的卷积核时需调整）
* `--output_file` canny程序输出的数据文件名，不建议更改该文件，若需更改，则需同时更改hough程序的`--canny_file`文件名，使之保持一致

### hough

* `--origin_file` 原图文件名，应与canny的`--input_file`相同
* `--canny_file` canny程序的输出数据文件，应与canny的`--output_file`相同

