# microbit
## ELECFREAKS Smart Home Kit 
[官方文檔](https://elecfreaks.com/learn-en/microbitKit/smart_home_kit/index.html)  
![e088b99f-b343-4e39-a607-145071c7d190 __CR0,0,970,600_PT0_SX970_V1___](https://user-images.githubusercontent.com/46433848/173605610-6904f3fc-1517-40f7-a3a9-29f90cfbe6af.jpg)

## smarthon(SMART CITY IOT STARTER KIT FOR MICRO:BIT)  
[官方文檔.pdf](https://github.com/HTTP404Not-Found/SPSS-STEM/files/8900716/Handbook.Micro.Bit.IoT.Smart.City.Final.pdf)  
![SS-M003-01-Smarthon-IoTbit-1](https://user-images.githubusercontent.com/46433848/173602793-4d466953-8d55-4d36-8c3e-72ad3ae5a496.jpg)  


# cocorobo
**ai模組,iot模組不可以同時一齊用** (可能因為兩個都是輸入模塊)   
[CocoBlockly X 二代上傳插件](https://api.cocorobo.hk/releases/pythonuploaderv1.0.17/download/windows)  
[模組介紹](https://cocorobo.hk/product)  
[編程網址](https://x.cocorobo.hk/?lang=en)  
## iot

## ai

# huskylens  
[官方文檔](https://wiki.dfrobot.com/HUSKYLENS_V1.0_SKU_SEN0305_SEN0336)  
![image](https://user-images.githubusercontent.com/46433848/173591895-ef17a82a-8ee3-4858-8743-f339ae945d40.png)  
![image](https://user-images.githubusercontent.com/46433848/173592005-a5b86fa3-4d6f-40e7-807b-75c5fd1b3f9d.png)  


# Raspberry Pi
## Google Teachable Machine＋Raspberry Pi  
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
# 活動/比賽
## 2019-2020JSSE  
mind+ 開啟文件 [2019-2020JSSE_code.zip](https://github.com/HTTP404Not-Found/SPSS-STEM/files/8900341/2019-2020JSSE_code.zip)  

## 21-22EdUHK Idea Contest
[模型設計圖.zip](https://github.com/HTTP404Not-Found/SPSS-STEM/files/8900539/System.Auto-save.Untitled20220505182022.zip)  
