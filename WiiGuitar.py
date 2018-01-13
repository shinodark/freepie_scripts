# Constants
WHAMMY_TRESHOLD 	= 1	
POLLING_PERIOD 		= 1    	#interval in ms
JOY_DEADZONE		= 5
TAPBAR_ENABLE		= False

def tapbar_mapping(n, guitar_button):
	result = False
	if TAPBAR_ENABLE == True:
	    result = {
	         GuitarButtons.Green: wiimote[n].guitar.tapbar.isGreen(),
	         GuitarButtons.Red: wiimote[n].guitar.tapbar.isRed(),
	         GuitarButtons.Yellow: wiimote[n].guitar.tapbar.isYellow(),
	         GuitarButtons.Blue: wiimote[n].guitar.tapbar.isBlue(),
	         GuitarButtons.Orange: wiimote[n].guitar.tapbar.isOrange(),
	    }.get(guitar_button, False)
	return result

def map_guitar_button(n, guitar_button, keyboard_key):
   if wiimote[n].guitar.buttons.button_down(guitar_button) or tapbar_mapping(n, guitar_button):
      keyboard.setKeyDown(keyboard_key)
   else:
      keyboard.setKeyUp(keyboard_key)
      
def map_guitar_joyaxis(axis, keyboard_key_left, keyboard_key_right):
	if axis > JOY_DEADZONE:
		keyboard.setKeyDown(keyboard_key_right)
	else:
		keyboard.setKeyUp(keyboard_key_right)
	
	if axis < -JOY_DEADZONE:
		keyboard.setKeyDown(keyboard_key_left)
	else:
		keyboard.setKeyUp(keyboard_key_left)

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
		
	# use joystick as left / right arrow
	# diagnostics.watch(wiimote[n].guitar.stick.x)
	map_guitar_joyaxis(wiimote[n].guitar.stick.x, Key.LeftArrow, Key.RightArrow)
	
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