# Constants
POLLING_PERIOD 		= 1    	#interval in ms

def map_snes_button(n, snes_button, vjoy_button):
	vJoy[n].setButton(vjoy_button, wiimote[0].classicController.buttons.button_down(snes_button))

def map_pov(n):
	val = 0
	maxVal = vJoy[n].continuousPovMax
	if wiimote[n].classicController.buttons.button_down(ClassicControllerButtons.DPadUp):
		val = 0 # UP
		if wiimote[n].classicController.buttons.button_down(ClassicControllerButtons.DPadRight):
			val += maxVal/8 # UP/RIGHT
		elif wiimote[n].classicController.buttons.button_down(ClassicControllerButtons.DPadLeft):
			val = 7 * maxVal/8 # UP/LEFT
	elif wiimote[n].classicController.buttons.button_down(ClassicControllerButtons.DPadRight):
		val = maxVal/4 # RIGHT
		if wiimote[n].classicController.buttons.button_down(ClassicControllerButtons.DPadDown):
			val += maxVal/8 # DOWN/RIGHT
	elif wiimote[n].classicController.buttons.button_down(ClassicControllerButtons.DPadDown):
		val = maxVal/2 # DOWN
		if wiimote[n].classicController.buttons.button_down(ClassicControllerButtons.DPadLeft):
			val += maxVal/8 # DOWN/LEFT
	elif wiimote[n].classicController.buttons.button_down(ClassicControllerButtons.DPadLeft):
		val = 3 * maxVal/4 # LEFT
	else:
		val = -1
	vJoy[n].setAnalogPov(0, val)

def map_snes(n):
	map_snes_button(n, ClassicControllerButtons.A, 0)
	map_snes_button(n, ClassicControllerButtons.B, 1)
	map_snes_button(n, ClassicControllerButtons.X, 2)
	map_snes_button(n, ClassicControllerButtons.Y, 3)
	map_snes_button(n, ClassicControllerButtons.TriggerLeft, 4)
	map_snes_button(n, ClassicControllerButtons.TriggerRight, 5)
	map_snes_button(n, ClassicControllerButtons.Plus, 6)
	map_snes_button(n, ClassicControllerButtons.Minus, 7)
	map_pov(n)

def updateSnes1():
	map_snes(0)

if starting:
	# set hires input polling
	system.setThreadTiming(TimingTypes.HighresSystemTimer)
	system.threadExecutionInterval = POLLING_PERIOD
	wiimote[0].classicController.update += updateSnes1
	wiimote[0].enable(WiimoteCapabilities.Extension)