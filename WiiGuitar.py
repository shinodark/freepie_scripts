# Constants
WHAMMY_TRESHOLD 	= 1	
POLLING_PERIOD 		= 1    	#interval in ms

def map_guitar_button(n, guitar_button, keyboard_key):
   if wiimote[n].guitar.buttons.button_down(guitar_button):
      keyboard.setKeyDown(keyboard_key)
   else:
      keyboard.setKeyUp(keyboard_key)

def map_guitar(n):
	map_guitar_button(n, GuitarButtons.Green, Key.A)
	map_guitar_button(n, GuitarButtons.Red, Key.S)
	map_guitar_button(n, GuitarButtons.Yellow, Key.J)
	map_guitar_button(n, GuitarButtons.Blue, Key.K)
	map_guitar_button(n, GuitarButtons.Orange, Key.L)
	map_guitar_button(n, GuitarButtons.StrumUp, Key.UpArrow)
	map_guitar_button(n, GuitarButtons.StrumDown, Key.DownArrow)
	map_guitar_button(n, GuitarButtons.Minus, Key.H)
	map_guitar_button(n, GuitarButtons.Plus, Key.Return)
	
	whammyX = wiimote[n].guitar.whammy.x
	# diagnostics.watch(whammyX)
	if whammyX > WHAMMY_TRESHOLD:
		mouse.deltaX = whammyX
		
def updateGuitar1():
	map_guitar(0)


if starting:
	# set hires input polling
	system.setThreadTiming(TimingTypes.HighresSystemTimer)
	system.threadExecutionInterval = POLLING_PERIOD
	wiimote[0].guitar.update += updateGuitar1