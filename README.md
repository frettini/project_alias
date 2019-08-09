# Project Alias Mod UoG

<p float="left">
<img src="imgs/alias.jpg" width="49%"> <img src="imgs/short_alias_explained.gif" width="49%">
</p>

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is a fork of the original project alias which can be found here : https://github.com/bjoernkarmann/project_alias

This fork has for objective to use and extend project alias to implement new modes of activation. A separate application has been developed which connects to project Alias and remotely activates the device, which can be found [here](https://github.com/frettini/kinect-gesture). 

Project Alias is an open-source parasite to hack smart home devices. Train custom wake-up names and commands for your devices while disturbing their built-in microphone with noise. Introduce false labelling to their algorithm by changing gender or nationality. Read more about the project **[here](http://bjoernkarmann.dk/project_alias)**.

The aim of this fork is to explore different ways of activation of alias, and therefore of the voice assistant. The fork implements code to accomodate connection with that additional application, and to add few functionalities with the browser client

This repository has been updated to 2.0. Find the old version **[here](http://bjoernkarmann.dk/project_alias)**.

### 2.0 Features
- Multiple trigger words
- Custom whisper commands
- New and better word detection
- Change gender
- Change language
- Adjust trigger sensitivity and delay

### Fork features
- Trigger Button in browser
- Voice Speed Setting
- Additional communication functions for separate applications


### Build Guide
For the complete step-by-step guide and 3D files see our **[Instructables](https://www.instructables.com/id/Project-Alias)**.


### Easy Setup 🔧

*As of right now, the link to the image doesn't seem to work, the installation should be done using the RaspberryPi setup and Installation section below.

We have made the setup even easier with a SD-card clone of our working Alias.
1. **[Download]()** the latest .img file
2. Use **[Etcher](https://etcher.io/)** to flash a micro SD card with the .img file.
3. Insert the micro SD card into the Raspberry Pi A+.
4. Log on to the wifi name **"Project Alias"** and open the browser.

*We recommend to use the Easy Setup but if you wish to install the project from scratch use the [Raspberry Pi Setup]() instrucrtions.*


### Using Alias  🍄
1. To start using Alias, while on the same network as Alias, go on your browser and connect to (http://raspberrypi.local:5050).

2. Set up the wake up words and whispers you want to use for your device.

3. Click on Update Alias, and try it out.

4. You can also trigger the device from the Trigger button.

5. You can configure your device by going in the settings, make sure to click on Update Alias to update again.


### Settings ⚙️

Setting | Description | Default
--- | --- | ---
Noise | This will turn on/off the looping noise| `ON`
Gender | -- | `Female`
Language | Change the language Alias uses to | `English`
Volume | Change the volume of the speakers. This needs to be heigh enough for the noise to block the assistant, but low enough not to be audible. | `10`
Sensitivity | This setting changes the sensitivity of the word detection. The lower the number the less sensitive. This setting can be helpful for short words. | `3`
Noise Delay | This increase the delay after from the trigger word to the restart of the noise. This is used as a noise free window, when asking the assistant a equation. | `10s`
Voice Speed | This modifies the speed of alias' voice. This is used to have the device faster or slower | 200


### Raspberry Pi Setup

How to prepare and setup a Raspberry Pi for this project:

1. Download the latest version of [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) and flash your micro SD card with [Etcher](https://etcher.io/)

2. Copy the **ssh** and **wpa_supplicant.conf** files from the [setup folder](setup/) to the SD card (boot)


3. Edit the **wpa_supplicant.conf** in a text editor to match your wifi settings. Insert the card to the raspberry pi


4. In terminal ssh into the pi: ```sudo ssh pi@raspberrypi.local```<br>*Default password is 'raspberry'. To change password use the 'passwd' command*

5. Update the pi: ```sudo apt-get update && sudo apt-get upgrade```<br>

7. Reboot ```sudo reboot```


#### Installing


On the Rapsberry Pi: clone and install the sound driver for the [ReSpeaker](http://wiki.seeedstudio.com/ReSpeaker_2_Mics_Pi_HAT/) hat:<br>
*This is only required when using the ReSpeaker hat, this code will also work with other sound drivers.*

```
cd && git clone https://github.com/respeaker/seeed-voicecard.git
cd seeed-voicecard && sudo ./install.sh
```

Install **Tensorflow** and **Keras**:

```
sudo apt-get install python3-dev python3-pip git libatlas-base-dev
sudo pip3 install tensorflow keras
```

Install the required modules:

```
sudo apt-get install python3-numpy python3-spidev python-h5py
sudo apt-get install python3-pyaudio libsdl-ttf2.0-0 python3-pygame
sudo pip3 install flask flask_socketio python_speech_features
sudo pip3 install pocketsphinx
```
Install espeak:

```
sudo apt-get install espeak
```

Clone the **Alias** project:

```
git clone https://github.com/bjoernkarmann/project_alias.git
```

Setup a bootscript. Open this file:

```
sudo nano /etc/rc.local
```
 and add at the end of the command just before **exit 0**, like:

```
cd project_alias && python3 app.py &
```
Now reboot the Pi to test it:

```
sudo reboot
```

## Calibration

- If you are using a **Amazon Alexa**, please change line 21 in **app.py** to: ```wakeup = sound.audioPlayer("data/alexa.wav",0,"wakeup", False)```

- To set the volume of the speaker you can change the line 32 in **modules/sound.py** ```os.system('sudo amixer -c 1 sset Speaker 83')```

## Changes

The main changes were made in app.py and the index.html

index.html :
- New Trigger Button which which activates the Voice Assistant
- New Voice Speed Slider which changes the speed of the voice in sound.py

app.py :
- New socketio handler for any packet of name "ComputerMessage", no namespaces on the handler because the computer application doesn't support namespaces


## Contributors
Made by [Bjørn Karmann](http://bjoernkarmann.dk) and [Tore Knudsen](http://www.toreknudsen.dk/).


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
