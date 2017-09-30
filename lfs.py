


x = filters.mapRange(midi[0].data.buffer[1], 127, 0,  17873, -17873)
diagnostics.watch(x)

if x > 0:
	vJoy[0].x = x
	vJoy[0].y = 0
else:
	vJoy[0].y = -x
	vJoy[0].x = 0