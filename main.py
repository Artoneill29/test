from microbit import *
  x=0
while True:
if button_a.is_pressed():
display.show('A',clear=True)
x=x+1
if button_b.is_pressed():
display.show('B',clear=True)
x=x+1