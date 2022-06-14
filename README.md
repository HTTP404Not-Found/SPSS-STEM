
# Google Teachable Machine＋Raspberry Pi
Google Teachable Machine 匯出文件類型:
1.安裝CMake(配置安裝OpenCV)，GCC(編譯):
```
$ sudo apt-get install cmake
$ sudo apt-get install gcc g++
```
2.安裝python3：
```
$ sudo apt-get install python3-dev python3-numpy
```
3.安裝GUI 功能、相機支持（v4l）、媒體支持（ffmpeg、gstreamer）:
```
$ sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev
$ sudo apt-get install libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev
```
4.安裝GTK2/3
```
$ sudo apt-get install libgtk2.0-dev
$ sudo apt-get install libgtk-3-dev
```
5.依賴:
```
$ sudo apt-get install libpng-dev
$ sudo apt-get install libjpeg-dev
$ sudo apt-get install libopenexr-dev
$ sudo apt-get install libtiff-dev
$ sudo apt-get install libwebp-dev
```
6.下載 OpenCV(從 GitHub Repository下載最新源代碼。):
```
$ sudo apt-get install git
$ git clone https://github.com/opencv/opencv.git
```
7.先在opencv文件夾內命名為build的文件夾:
```
$ mkdir build
$ cd build
```
8.配置和安裝:
```
／opencv/build $ cmake ../
／opencv/build $ make
／opencv/build $ sudo install
```
9.重新开启SWAP服务:
```
$ sudo /etc/init.d/dphys-swapfile stop
$ sudo /etc/init.d/dphys-swapfile start
```
10.下載模型及文件解壓傳入raspberry pi
```
$ cd converted_tflite_quantized/
/ converted_tflite_quantized  $ ln -s /usr/local/python/cv2/python-3.7/cv2.cpython-37m-arm-linux-gnueabihf.so cv2.so
```
11.將[分類器](https://drive.google.com/file/d/1038KeQh4jaZtPvjM_syUbXHeocINXLG6/view?usp=sharing)放入 converted_tflite_quantized

12.執行

```
/ converted_tflite_quantized $ python3 TM2_tflite.py --model model.tflite --labels labels.txt
```
相關文章參考:
[TensorFlow](https://www.tensorflow.org/lite/guide/python)
[https://www.pyimagesearch.com/2018/09/26/install-opencv-4-on-your-raspberry-pi/](https://www.pyimagesearch.com/2018/09/26/install-opencv-4-on-your-raspberry-pi/)
[https://www.rs-online.com/designspark/google-teachable-machine-raspberry-pi-4-1-cn](https://www.rs-online.com/designspark/google-teachable-machine-raspberry-pi-4-1-cn)
[https://docs.opencv.org/4.5.2/d2/de6/tutorial_py_setup_in_ubuntu.html](https://docs.opencv.org/4.5.2/d2/de6/tutorial_py_setup_in_ubuntu.html)