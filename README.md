<h1 align=center> Personal Catkin Playground!  </h1>

```
This repository is a transient scratchpad for catkin tools. 
I will be using this for personal tests and stuff, so don't bother cloning this.

What you may find useful are:

+ Scripts in InitScripts/
+ Stuff written in README.md
+ cat.png

I am fairly certain that the rest of the repo will not be of much use to you ¯\_(ツ)_/¯ 
```

### Table of Contents
* [ROS installation in Windows via WSL2](#ros-installation-on-windows-via-wsl2)


-------------------------------------------------------------------------------------------------------------------------
# ROS installation on Windows via WSL2
-------------------------------------------------------------------------------------------------------------------------

USB DEVICES DO NOT WORK IN THIS ROS SETUP, SO PLEASE DO NOT FOLLOW THIS IF YOU NEED USB DEVICES TO WORK. 
AT THE TIME OF WRITING THIS DOC, THE REASON FOR NOT INCLUDING USB DEVICE SUPPORT INSTRUCTIONS IS THAT 
THIS WSL2 ENVIRONMENT IS FOR CONNECTING TO A REMOTE ROS INSTALL THROUGH THE NETWORK AND RUNNING RVIZ/GAZEBO VIA XSERVER. 
PLEASE PROCEED AT YOUR OWN RISK!

The following will be categorized into several parts, use this to jump to your desired section:

   1.   [`Setting up WSL2 in Windows`](#installing-wsl2---part-one)
   2.   [`Setting up Ubuntu 18.04`](#install-ubuntu-1804-from-microsoft-store)
   3.   [`Filesystem access from inside Windows`](#filesystem-access-from-inside-windows)
   4.   [`Enabling GUI/Xserver stuff`](#gui-enabling-and-xserver-stuff)


#### Please note that step iv is not necessary if you want a minimal (CLI only) ROS environment later on.

WSL1 is NOT recommended for ROS, as WSL2 provides superior integration with the kernel. Please refer to the following commands to install WSL2 and setup Ubuntu 18.04


### Installing WSL2 - part one

Open Powershell as admin first, then enter the following commands:
```
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```
You then need to restart your machine to finish the WSL install and the upgrade to WSL2.

### Installing WSL2 - part two

In powershell, type in:
```
wsl --set-default-version 2
```
If you see an error message that involves having a missing kernel component, download and install this:

https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi

After that, re-run the command above.

### Install Ubuntu 18.04 from Microsoft Store

Just make sure you have MS Store, and click the link:
(If prompted with a "Sign in", don't worry, its not required)

https://www.microsoft.com/store/productId/9N9TNGVNDL3Q

When done, just launch it from inside the store, or from the Start menu.
You should be prompted with a username/password input. This is a user creation step. Remember these credentials.

### Verify WSL2 integration

After getting into your first Ubuntu prompt, type in `exit`, or close the terminal. Open powershell/cmd and enter the following:
```
wsl --list --verbose
```

You should see something like this:
```
C:\Users\Ishraq>wsl --list --verbose
  NAME            STATE           VERSION
* Ubuntu-18.04    Running         2
```

Look under the VERSION column. It should say 2. If it doesn't, run the following:

```
wsl --set-version Ubuntu-18.04 2
```
You should be good to go now. You can proceed with ROS (Melodic Morena) installation.

### Filesystem access from inside Windows

Inside your file explorer, go to the address bar, and type in:
```
\\wsl$\Ubuntu-18.04
```
This will open up a folder that is mapped to the `/` directory of your Ubuntu 18.04 filesystem. Use this responsibly, as the recommended approach to fs manipulation is doing it from inside the Ubuntu terminal, and not from Windows itself.

### GUI enabling and Xserver stuff

1. Install this in Windows: https://sourceforge.net/projects/vcxsrv/
2. Click next until you see the Extra Settings section. Make sure to provide the following selection:
```
[x] Clipboard
  [x] Primary Selection
[ ] Native opengl
[x] Disable access control
```
[x] represents checked
[ ] represents unchecked `( ._.)`

3. Keep clicking next until it finishes. For the Firewall message, make to check both Private and Public networks.
4. Launch Ubuntu 18.04 from the start menu.
5. In the Ubuntu terminal, run `nano ~/.bashrc`. At the end of the file, append the following line:
```
export LIBGL_ALWAYS_INDIRECT=0
```
6. Keeping this window as it is, open a cmd window, and type in `ipconfig` to check your PC's IP (needs to be Windows IP, not the one WSL2 produces). Let `___YOUR_IP___` represent your Windows IP address throughout this document.
7. Go back to the Ubuntu terminal which has `nano` open. After the line with your export statement from step 5, enter another line as follows:
```
export DISPLAY=___YOUR_IP___:0.0
```
PLEASE SUBSTITUE ___YOUR_IP___ with your actual IP address instead of copy-pasting the command as is. `(._. )`

8. Ctrl+S and Ctrl+X  to save and exit
9. Enter the following command inside the Ubuntu terminal:
```
source ~/.bashrc
```
10. Finally, install some X11 stuff to make sure everything connects properly (not mandatory, but worth the check):
```
sudo apt update
sudo apt install x11-apps
```
Run any X11 app like `xcalc` to test it out. If you see a calculator, you are good to go.

### Install ROS Melodic

1. Open Ubuntu terminal through the Start menu.
2. Run the following commands (Please note that this script installs the FULL-DESKTOP version of ROS, which is not what you want, if you are going for a minimal, cli-only install. In that case, please refer to the official installation doc, to see what commands to enter. If you are going for a full ROS environment, just proceed)
```
wget https://gist.githubusercontent.com/ishraq10199/ef12bf89f7f1a927e26d9e273e1c8d3e/raw/cbb768b6f0809482a956460da9084a6a0ceaa170/rosInstallMelodicMorena.sh
chmod +x rosInstallMelodicMorena.sh
./rosInstallMelodicMorena.sh
```
3. Enter your password (the one you were asked for at your first launch of Ubuntu) when prompted. This step is probably the longest, and depends mostly on your internet connection. Do check back once in a while to make sure things are going normally. If installation stops midway, just re-run the last command by pressing up arrow and enter. Should work fine.

4. Finally run `source /opt/ros/melodic/setup.bash` to finalize the ROS install

----------------------------------------------------------------------------------------------------------------

![alt pic_go_brrr](cat.png "Random cat pic I found on the internet")
