Mitsuba2 python packages
==========================
This repository provide python packages for [Mitsuba2 renderer](https://mitsuba2.readthedocs.io/en/latest/)(v2.1.0) to be used with our Optical Tactile Simulation tool for simulating vision-based tactile sensors. This repository is meant for quick reproducing results in our repository present [here](https://github.com/CMURoboTouch/tactile_optical_simulation). Please refer to official Mitsuba2 documentation for more details. 

Usage
=====
Use the OS specific instructions to setup mitsuba2 in your terminal. This step needs to be done when you start a new terminal window. The system configurations are mentioned for debugging purposes. However, only the python version is the crutial requirement for proper function of mitsuba 

# Linux
Tested and Build with following system configurations 
- Ubuntu 20.04
- Clang 10.0.1-++20200708122807+ef32c611aa2-1~exp1~20200707223407.61
- Cmake 3.19.4
- ninja 1.10.0
- Python 3.7.7
Use following command to activate mitsuba2 python packages on linux
```bash
source setpath_linux.sh
``` 

# Mac
Tested and Build with following system configurations 
- MacOs Catalina 11.2.1
- Xcode 12.4
- Clang 11.0.0
- Cmake 3.18.4
- ninja 1.10.0
- Python 3.7.7
Use the following command to activate mitsuba2 python package on mac
```bash
source setpath_mac.sh
``` 

# Windows
Currently building with system python or installing python through Windows app store is not supported. Therefore to use windows build, the user need to install Anaconda python 3.8.6 
Tested and Build with following system configurations
- Windows SDK 10.0.18362.0
- MS Visual Studio 2019 16.8.5
- Anaconda python 3.8.6
- cmake 3.19.2
Use the following command to activate mitsuba2 python package on windows
```bash
setpath_win
```
Test
=====
To test if the mitsuba2 is properly functioning use the following command
```bash
python3 test_mitsuba.py
```