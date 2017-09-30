

if starting:
	x = 0
	y = 0
	z = 0
	t = 0
	looktoggle = 0
	pitchtrim = 0
	yawtrim = 0
	
x = filters.mapRange(midi[0].data.buffer[1], 127, 0,  17873, -17873)

if keyboard.getPressed(Key.D4):
	if looktoggle == 0:
		looktoggle = 1
	else:
		looktoggle = 0

if looktoggle == 0:
	trackIR.yaw += mouse.deltaX*0.1
	trackIR.pitch -= mouse.deltaY*0.1
else:
	trackIR.pitch = pitchtrim
	trackIR.yaw = yawtrim 
	y += mouse.deltaX*20
	z += mouse.deltaY*20

if mouse.middleButton:
	z = 0
	y = 0
if abs(x) < 150:
	x = 0
	
if y > 17873:
	y = 17873
if y < -17873:
	y = -17873
	
	
if z > 17873:
	z = 17873
if z < -17873:
	z = -17873
	
if mouse.wheelUp:
	t += 10
if mouse.wheelDown:
	t -= 10
	
if t > 100:
	t = 100
if t < 0:
	t = 0
vJoy[0].x = x
vJoy[0].y = y
vJoy[0].z = z
vJoy[0].rx = t

diagnostics.watch(trackIR.pitch)
diagnostics.watch(trackIR.yaw)
diagnostics.watch(vJoy[0].x)
diagnostics.watch(vJoy[0].y)
diagnostics.watch(vJoy[0].z)
diagnostics.watch(vJoy[0].rx)
diagnostics.watch(looktoggle)