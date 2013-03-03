from visual.controls import *

c = controls(x=0, y=0, width=200, height=600, range=60)

#ctrl = slider(pos=(-50,20), width=7, length=100, 
#        text='Temperature', min=0., max=100., value=20)
s1 = slider(pos=(-50,40), width=7, text='AngularVelocity')

while True:
    c.interact()
