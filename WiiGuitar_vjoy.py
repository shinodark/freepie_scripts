# Constants
WHAMMY_TRESHOLD 	= 1	
POLLING_PERIOD 		= 1    	#interval in ms

def map_guitar_button(n, guitar_button, vjoy_button):
	vJoy[n].setButton(vjoy_button, wiimote[n].guitar.buttons.button_down(guitar_button))
	
def map_guitar_pov(n, guitar_button, vjoy_pov):
	if wiimote[n].guitar.buttons.button_down(guitar_button):
		vJoy[n].setDigitalPov(0, vjoy_pov)
	else:
		vJoy[n].setDigitalPov(0, VJoyPov.Nil)
	
def map_guitar(n):
	map_guitar_button(n, GuitarButtons.Green, 0)
	map_guitar_button(n, GuitarButtons.Red, 1)
	map_guitar_button(n, GuitarButtons.Yellow, 2)
	map_guitar_button(n, GuitarButtons.Blue, 3)
	map_guitar_button(n, GuitarButtons.Orange, 4)
	map_guitar_button(n, GuitarButtons.Minus, 5)
	map_guitar_button(n, GuitarButtons.Plus, 6)
	
	if wiimote[n].guitar.buttons.button_down(GuitarButtons.StrumUp):
		vJoy[n].setDigitalPov(0, VJoyPov.Up)	
	elif wiimote[n].guitar.buttons.button_down(GuitarButtons.StrumDown):
		vJoy[n].setDigitalPov(0, VJoyPov.Down)
	else:
		vJoy[n].setDigitalPov(0, VJoyPov.Nil)
	
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