import time, machine, neopixel, gc

#define important bits
pin = 0
led_num = 46 * 13
b = 100
#constants
RED = (b,0,0)
WHITE = (b,b,b)
BLUE = (0,0,b)
#setup
np = neopixel.NeoPixel(machine.Pin(pin), led_num)


#Stripes starting from the bottom working up



for i in range(552,46*13):   #  46*12,46*13
    np[i] = RED

for i in range(506,552):  # 46*11, 46*12
    np[i] = WHITE

for i in range(460,46*11):
    np[i] = RED
    
for i in range(46*9,46*10):
    np[i] = WHITE
    
for i in range(46*8,46*9):
    np[i] = RED
    
for i in range(46*7,46*8):
    np[i] = WHITE
    
for i in range(46*6,46*6+20,2):
    np[i] = BLUE

for i in range((46*6)+ 1,(46*6+20)-1,2):
    np[i] = WHITE
    
for i in range((46*6+20)-1,46*7):
    np[i] = RED
    
for i in range((46*6)-1,(46*6)-20,-2):
    np[i] = WHITE

for i in range((46*6),(46*6)-19,-2):
    np[i] = BLUE

for i in range((46*6)-20,(46*5)-1,-1):
    np[i] = WHITE

for i in range((46*4),(46*4)+19,2):
    np[i] = BLUE

for i in range((46*4)+1,(46*4)+19,2):
    np[i] = WHITE
    
for i in range((46*4)+19,46*5):
    np[i] = RED
    
for i in range((46*4)-1,(46*4)-20,-2):
    np[i] = WHITE
    
for i in range((46*4),(46*4)-19,-2):
    np[i] = BLUE

for i in range((46*4)-20,46*3,-1):
    np[i] = WHITE

for i in range(46*2,(46*2)+19,2):
    np[i] = BLUE
    
for i in range((46*2)+1,(46*2)+18,2):
    np[i] = WHITE

for i in range((46*2)+19,46*3,1):
    np[i] = RED

for i in range((46*2)-1,(46*2)-20,-2):
    np[i] = WHITE

for i in range((46*2)-2,(46*2)-20,-2):
    np[i] = BLUE
    
for i in range((46*2)-20,46,-1):
    np[i] = WHITE

for i in range(0,20,2):
    np[i] = BLUE
    
for i in range(1,18,2):
    np[i] = WHITE

for i in range(19,46):
    np[i] = RED
np[(46*3)] = WHITE
np[46] = WHITE

np[0] = (0,0,0)

np.write()