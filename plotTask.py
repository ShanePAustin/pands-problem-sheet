#plotTask.py
#A program that plots the function x, x^2 and x^3
#Author: Shane Austin

import matplotlib.pyplot as plt
import numpy as np

#define dataset
lowRange = 0
highRange = 4
#I decided to make the step 10 * the high range, this means it will plot 10 points for each whole number on the x axis
#this makes the "markevery" consistent and easy to configure
step = (highRange*10)+1

#set axes area, i extended the y limit to 70 otherwise in cuts off at 60 and the highest value is 64
ax = plt.axes()
plt.ylim(-2,70)

#create dataset, I used linspace as it plots evenly spaced samples over the interval range
xpoints = np.linspace(lowRange,highRange,step)

#calculations for x, xsquared and xcubed
fx = xpoints
gx = xpoints**2
hx = xpoints**3

#plots x and y, using $""$ denote LaTeX math notation for labels, colours chosen from CSS color
#markevery plots a point at every whole number on the x axis
plt.plot(xpoints, fx,label = "$f(x)= x$", color="firebrick", linewidth = 2, marker = "o", markevery = 10)
plt.plot(xpoints, gx,label = "$g(x)= x^{2}$", color="royalblue", linewidth = 2, marker = "o", markevery = 10)
plt.plot(xpoints, hx, label = "$h(x)= x^{3}$", color="forestgreen", linewidth = 2, marker = "o", markevery = 10)

#labels, using LaTeX math notation
plt.title ("Values of $x$, $x^{}$, and $x^{}$ in the range {}-{}".format(2,3,lowRange,highRange))
plt.xlabel("$x$")
plt.ylabel("$x^{n}$")
plt.legend()

#style, sets background colour and a dashed grid

plt.grid(linestyle ="dashed")
ax.set_facecolor("lightgrey")


#show and/or save
plt.show()
#plt.savefig("plotTask.png")