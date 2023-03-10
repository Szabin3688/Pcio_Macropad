# Pcio_Macropad
24 button macropad with programmable oled screen and buttons using the raspberry pi pico


## Getting Started

First you'll nedd to order a pcb with the included pcb files, and get some components.
Component list:
-	24x CHERRY MX switches with support for backlight
-	1x Raspberry pi pico
- 1x SSD1306 (OLED screen)
- 24x LED's with the color of your choosing


### Installing

Steps from fresh Pico:
1) Download the Cirtuitphyton files from here:
	UF2 file: https://downloads.circuitpython.org/bin/raspberry_pi_pico/nl/adafruit-circuitpython-raspberry_pi_pico-nl-7.3.0.uf2
	.HID files: https://github.com/adafruit/Adafruit_CircuitPython_HID/archive/refs/heads/main/adafruit_hid.zip
2) Unzip the adafruit_hid.zip
3) Plug in the pico while holding down the BOOTSEL button
4) Copy the downloaded .UF2 file to the RPI_RPI2 drive
5) Open the unzipped folder, and copy the adafruit_hid folder to the CIRCUITPY drive
6) Replug the pico normaly
7) Download the Main.py file from my github from here:
	Main.py file: Pico_Macropad/Firmware/Main.py
8) Copy the Main.py file to the CIRCUITPY drive
9) Remove the code.py file from the pico
10) Replug the pico
-- The device should work, if not hit me up on github or on my social media platforms :) --
-- The uploading is complete if the pico's led is on --


## Built With

  - [Programming language] circuitpython.org 


## Authors

  - **Szabin3688** - 
    (https://github.com/Szabin3688 / www.linktr.ee/b.szabin)

## Other info 

For ducumentation on how to reprogram the button actions check ducumentation/eng/Reprogram_buttons_info.txt
For ducumentation on how to reprogram the button actions in hungarian check documentation/hu/Gombok_újraprogarmozása.info

## Working on

- Windows / Linux software for easy reprogramming
- Implementing oled support in the firmware
- Making a 3d model for the housing

## The PCB itself
![Picture of the board](https://github.com/Szabin3688/Pcio_Macropad/blob/main/PCB_Version_1.png?raw=true)
