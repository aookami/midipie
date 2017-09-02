

if starting:
	x = 0
	y = 0

x = filters.mapRange(midi[0].data.buffer[1], 127, 0,  17873, -17873)

y += mouse.deltaX*3

if abs(x) < 150:
	x = 0
	
if y > 10000:
	y = 10000
if y < -10000:
	y = -10000
	
if mouse.wheelUp:
	keyboard.setPressed(Key.NumberPad4)
if mouse.wheelDown:
	keyboard.setPressed(Key.NumberPad1)
vJoy[0].x = x
vJoy[0].y = y

diagnostics.watch(x)
diagnostics.watch(y)