# Personal Catkin Playground!
```
This repository is a transient scratchpad for catkin tools. 
I will be using this for personal tests and stuff, so don't bother cloning this. 
Will not be of much use to you.
```

# ROS installation on Windows via WSL2

WSL1 is NOT recommended for ROS, as WSL2 provides superior integration with the kernel. Please refer to the following commands to install WSL2 and setup Ubuntu 18.04

* Open Powershell as admin first.

### Installing WSL2 - part one
```
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```
You then need to restart your machine to finish the WSL install and the upgrade to WSL2.

### Installing WSL2 - part two
```
wsl --set-default-version 2
```




![alt pic_go_brrr](cat.png "Random cat pic I found on the internet")
