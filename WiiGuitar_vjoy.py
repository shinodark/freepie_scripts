# Constants
WHAMMY_TRESHOLD 	= 1	
POLLING_PERIOD 		= 1    	#interval in ms

def map_guitar_button(n, guitar_button, vjoy_button):
	vJoy[n].setButton(vjoy_button, wiimote[n].guitar.buttons.button_down(guitar_button))
	
def map_guitar(n):
	map_guitar_button(n, GuitarButtons.Green, 0)
	map_guitar_button(n, GuitarButtons.Red, 1)
	map_guitar_button(n, GuitarButtons.Yellow, 2)
	map_guitar_button(n, GuitarButtons.Blue, 3)
	map_guitar_button(n, GuitarButtons.Orange, 4)
	map_guitar_button(n, GuitarButtons.Minus, 5)
	map_guitar_button(n, GuitarButtons.Plus, 6)
	
	maxVal = vJoy[n].continuousPovMax
	if wiimote[n].guitar.buttons.button_down(GuitarButtons.StrumUp):
		vJoy[n].setAnalogPov(0, 0)	
	elif wiimote[n].guitar.buttons.button_down(GuitarButtons.StrumDown):
		vJoy[n].setAnalogPov(0, maxVal/2)
	else:
		vJoy[n].setAnalogPov(0, -1)
	
	whammyX = wiimote[n].guitar.whammy.x
	# diagnostics.watch(whammyX)
	if whammyX > WHAMMY_TRESHOLD:
		vJoy[n].rx = vJoy[n].axisMax
	else:
		vJoy[n].rx = 0
	
def updateGuitar1():
	map_guitar(0)

if starting:
	# set hires input polling
	system.setThreadTiming(TimingTypes.HighresSystemTimer)
	system.threadExecutionInterval = POLLING_PERIOD
	wiimote[0].guitar.update += updateGuitar1