"""
=========================
Simple animation examples
=========================

This example contains two animations. The first is a random walk plot. The
second is an image animation.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update_line(num, data, line):
    line.set_data(data[..., num])
    return line,


#buildings
class Points():
    x=[]
    y=[]

groceries=Points()
houses=Points()
groceries.x=[0.2,-0.4,-0.1]
groceries.y=[0.4,0.5,0.6]
tempx= [(-5+0.1*i)/10 for i in range(0,400,7)]
houses.y=[]
#houses.x=[-0.5+0.1*k for k in range(40)]
for i in range(40):
#    houses.y=[0.6 for k in range(40)]
    break
for k in range(3):
    yval=0.1*k+0.5
    tempy=[yval for x in range(len(tempx))]
    houses.y+=tempy
    houses.x+=tempx

fig1 = plt.figure()
data=np.ndarray((2,25))
data[0] = np.zeros(25)
data[1]= np.linspace(0,1,25)
l, = plt.plot([], [], 'ro')

plt.plot(0,0.3,'ro')
plt.plot(groceries.x,groceries.y,'bo')
plt.plot(houses.x,houses.y,'go')
plt.plot([0,0],[0,1],'k')
plt.xlim(-0.5, 0.5)
plt.ylim(0, 1)
plt.xlabel('x')
plt.title('test')

line_ani = animation.FuncAnimation(fig1, update_line, 25, fargs=(data, l),
                                   interval=50, blit=True)

# To save the animation, use the command: line_ani.save('lines.mp4')

plt.show()


