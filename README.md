Mitsuba2 python packages
==========================
This repository provide python packages for [Mitsuba2 renderer](https://mitsuba2.readthedocs.io/en/latest/)(v2.1.0) to be used with our Optical Tactile Simulation tool for simulating vision-based tactile sensors. This repository is meant for quick reproducing results in our repository present [here](https://github.com/CMURoboTouch/tactile_optical_simulation). Please refer to official Mitsuba2 documentation for more details. 

Usage
=====
The system configurations are mentioned for debugging purposes. However, only the python version is the crutial requirement for proper function of mitsuba 

# Linux
Tested and Build with following system configurations 
- Ubuntu 18.04
- Clang 9.0.0-2~ubuntu18.04.2 (tags/RELEASE_900/final)
- Cmake 3.16.0
- ninja 1.8.2
- Python 3.7.7
```bash
source setpath_linux.sh
``` 

# Mac
Tested and Build with following system configurations 
- MacOs Catalina 10.17.5
- Xcode 12.1
- Clang 11.0.0
- Cmake 3.18.4
- ninja 1.10.0
- Python 3.7.7
```bash
source setpath_mac.sh
``` 

Test
=====
To test if the mitsuba2 is properly functioning use the following command
```bash
python test_mitsuba.py
```