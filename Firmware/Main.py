import time
import board
import usb_hid
import digitalio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

#led
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT


# define buttons. these can be any physical switches/buttons, but the values
button_1 = digitalio.DigitalInOut(board.GP16)
button_1.direction = digitalio.Direction.INPUT
button_1.pull = digitalio.Pull.DOWN

button_2 = digitalio.DigitalInOut(board.GP27)
button_2.direction = digitalio.Direction.INPUT
button_2.pull = digitalio.Pull.DOWN

button_3 = digitalio.DigitalInOut(board.GP9)
button_3.direction = digitalio.Direction.INPUT
button_3.pull = digitalio.Pull.DOWN

button_4 = digitalio.DigitalInOut(board.GP17)
button_4.direction = digitalio.Direction.INPUT
button_4.pull = digitalio.Pull.DOWN

button_5 = digitalio.DigitalInOut(board.GP28)
button_5.direction = digitalio.Direction.INPUT
button_5.pull = digitalio.Pull.DOWN

button_6 = digitalio.DigitalInOut(board.GP8)
button_6.direction = digitalio.Direction.INPUT
button_6.pull = digitalio.Pull.DOWN

button_7 = digitalio.DigitalInOut(board.GP18)
button_7.direction = digitalio.Direction.INPUT
button_7.pull = digitalio.Pull.DOWN

button_8 = digitalio.DigitalInOut(board.GP15)
button_8.direction = digitalio.Direction.INPUT
button_8.pull = digitalio.Pull.DOWN

button_9 = digitalio.DigitalInOut(board.GP7)
button_9.direction = digitalio.Direction.INPUT
button_9.pull = digitalio.Pull.DOWN

button_10 = digitalio.DigitalInOut(board.GP19)
button_10.direction = digitalio.Direction.INPUT
button_10.pull = digitalio.Pull.DOWN

button_11 = digitalio.DigitalInOut(board.GP14)
button_11.direction = digitalio.Direction.INPUT
button_11.pull = digitalio.Pull.DOWN

button_12 = digitalio.DigitalInOut(board.GP6)
button_12.direction = digitalio.Direction.INPUT
button_12.pull = digitalio.Pull.DOWN

button_13 = digitalio.DigitalInOut(board.GP20)
button_13.direction = digitalio.Direction.INPUT
button_13.pull = digitalio.Pull.DOWN

button_14 = digitalio.DigitalInOut(board.GP13)
button_14.direction = digitalio.Direction.INPUT
button_14.pull = digitalio.Pull.DOWN

button_15 = digitalio.DigitalInOut(board.GP3)
button_15.direction = digitalio.Direction.INPUT
button_15.pull = digitalio.Pull.DOWN

button_16 = digitalio.DigitalInOut(board.GP21)
button_16.direction = digitalio.Direction.INPUT
button_16.pull = digitalio.Pull.DOWN

button_17 = digitalio.DigitalInOut(board.GP12)
button_17.direction = digitalio.Direction.INPUT
button_17.pull = digitalio.Pull.DOWN

button_18 = digitalio.DigitalInOut(board.GP2)
button_18.direction = digitalio.Direction.INPUT
button_18.pull = digitalio.Pull.DOWN

button_19 = digitalio.DigitalInOut(board.GP22)
button_19.direction = digitalio.Direction.INPUT
button_19.pull = digitalio.Pull.DOWN

button_20 = digitalio.DigitalInOut(board.GP11)
button_20.direction = digitalio.Direction.INPUT
button_20.pull = digitalio.Pull.DOWN

button_21 = digitalio.DigitalInOut(board.GP1)
button_21.direction = digitalio.Direction.INPUT
button_21.pull = digitalio.Pull.DOWN

button_22 = digitalio.DigitalInOut(board.GP26)
button_22.direction = digitalio.Direction.INPUT
button_22.pull = digitalio.Pull.DOWN

button_23 = digitalio.DigitalInOut(board.GP10)
button_23.direction = digitalio.Direction.INPUT
button_23.pull = digitalio.Pull.DOWN

button_24 = digitalio.DigitalInOut(board.GP0)
button_24.direction = digitalio.Direction.INPUT
button_24.pull = digitalio.Pull.DOWN


while True:
    #turn on led on bootup to see if it's working, or if it has finished uploading code
    led.value = True
    # Push Keycode(The letter that you want to use Make sure that they are always Capital letters)
    if button_1.value:
        kbd.send(Keycode.ONE,)
    time.sleep(0.2)
    
    if button_2.value:
        kbd.send(Keycode.TWO,)

    
    if button_3.value:
        kbd.send(Keycode.THREE,)

    
    if button_4.value:
        kbd.send(Keycode.FOUR,)

    
    if button_5.value:
        kbd.send(Keycode.FIVE,)

    
    if button_6.value:
        kbd.send(Keycode.SIX,)

    if button_7.value:
        kbd.send(Keycode.SEVEN,)

    if button_8.value:
        kbd.send(Keycode.EIGHT,)

    if button_9.value:
        kbd.send(Keycode.NINE,)

    if button_10.value:
        kbd.send(Keycode.A,)

    if button_11.value:
        kbd.send(Keycode.B,)
    
    if button_12.value:
        kbd.send(Keycode.C,)

    if button_13.value:
        kbd.send(Keycode.D,)

    if button_14.value:
        kbd.send(Keycode.E,)

    if button_15.value:
        kbd.send(Keycode.F,)

    if button_16.value:
        kbd.send(Keycode.G,)

    if button_17.value:
        kbd.send(Keycode.H,)

    if button_18.value:
        kbd.send(Keycode.I,)

    if button_19.value:
        kbd.send(Keycode.J,)

    if button_20.value:
        kbd.send(Keycode.K,)

    if button_21.value:
        kbd.send(Keycode.L,)

    if button_22.value:
        kbd.send(Keycode.M,)

    if button_23.value:
        kbd.send(Keycode.N,)

    if button_24.value:
        kbd.send(Keycode.O,)