# Constants
POLLING_PERIOD 		= 1    	#interval in ms

def map_snes_button(n, snes_button, vjoy_button):
	vJoy[n].setButton(vjoy_button, wiimote[0].classicController.buttons.button_down(snes_button))

	
def map_pov(n):
    if wiimote[0].classicController.buttons.button_down(ClassicControllerButtons.DPadUp):
        vJoy[n].setDigitalPov(0, VJoyPov.Up)
    elif wiimote[0].classicController.buttons.button_down(ClassicControllerButtons.DPadDown):
        vJoy[n].setDigitalPov(0, VJoyPov.Down)
    elif wiimote[0].classicController.buttons.button_down(ClassicControllerButtons.DPadLeft):
        vJoy[n].setDigitalPov(0, VJoyPov.Left)
    elif wiimote[0].classicController.buttons.button_down(ClassicControllerButtons.DPadRight):
        vJoy[n].setDigitalPov(0, VJoyPov.Right)
    else:
		vJoy[n].setDigitalPov(0, VJoyPov.Nil)		

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