v = vJoy[0]
v.setButton(0,mouse.leftButton)
v.setButton(1,mouse.rightButton)
v.setButton(2,mouse.middleButton)

# Constants
WHAMMY_TRESHOLD 	= 1	
POLLING_PERIOD 		= 1    	#interval in ms
JOY_DEADZONE		= 5

def map_guitar_button(n, guitar_button, vjoy_button):
	vJoy[n].setButton(vjoy_button, wiimote[n].guitar.buttons.button_down(guitar_button))
	
def map_guitar_pov(n, guitar_button, vjoy_pov):
	if wiimote[n].guitar.buttons.button_down(guitar_button):
		vJoy[n].setDigitalPov(0, vjoy_pov)
	else:
		vJoy[n].setDigitalPov(0, VJoyPov.Nil)
		
def map_guitar_joyaxis(n, axis, joy_left, joy_right):
	if axis > JOY_DEADZONE:
		vJoy[n].setDigitalPov(0, joy_right)	
	elif axis < -JOY_DEADZONE:
		vJoy[n].setDigitalPov(0, joy_left)
	else:
		vJoy[n].setDigitalPov(0, VJoyPov.Nil)

def map_guitar(n):
	map_guitar_button(n, GuitarButtons.Green, 0)
	map_guitar_button(n, GuitarButtons.Red, 1)
	map_guitar_button(n, GuitarButtons.Yellow, 2)
	map_guitar_button(n, GuitarButtons.Blue, 3)
	map_guitar_button(n, GuitarButtons.Orange, 4)
	map_guitar_pov(n, GuitarButtons.StrumUp, VJoyPov.Up)
	map_guitar_pov(n, GuitarButtons.StrumDown, VJoyPov.Down)
	map_guitar_button(n, GuitarButtons.Minus, 5)
	map_guitar_button(n, GuitarButtons.Plus, 6)
		
	# use joystick as left / right arrow
	# diagnostics.watch(wiimote[n].guitar.stick.x)
	map_guitar_joyaxis(n, wiimote[n].guitar.stick.x, VJoyPov.Left, VJoyPov.Right)
	
	whammyX = wiimote[n].guitar.whammy.x
	# diagnostics.watch(whammyX)
	if whammyX > WHAMMY_TRESHOLD:
		vJoy[n].slider = whammyX
	else:
		vJoy[n].slider = 0
	
def updateGuitar1():
	map_guitar(0)

if starting:
	# set hires input polling
	system.setThreadTiming(TimingTypes.HighresSystemTimer)
	system.threadExecutionInterval = POLLING_PERIOD
	wiimote[0].guitar.update += updateGuitar1