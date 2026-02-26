# ubuntu-adb-phone-toolkit
Python toolkit to manage Android phones via ADB on Ubuntu — screenshots, logs, battery, etc.

# Ubuntu ADB Phone Toolkit

Python scripts to interact with Android phones from Ubuntu using ADB.

**Tested on:**
- Ubuntu 24.04
- My Samsung Android phone (via USB + WiFi)

**Features**
- List connected devices
- Take screenshot
- Pull logs & battery info
- Install APK
- Wireless ADB setup

**Setup**
```bash
sudo apt install adb
adb devices   # connect your phone
