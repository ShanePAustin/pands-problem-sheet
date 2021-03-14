#plotTask.py
#A program that plots the function x, x^2 and x^3
#Author: Shane Austin

import matplotlib.pyplot as plt
import numpy as np

#define dataset
lowRange = 0
highRange = 4
step = (highRange*10)+1

#set axes area
ax = plt.axes()
plt.ylim(-2,70)

#create dataset
xpoints = np.linspace(lowRange,highRange,step)

fx = xpoints
gx = xpoints**2
hx = xpoints**3

#plots
plt.plot(xpoints, fx,label = "$f(x)= x$", color="firebrick", linewidth = 2, marker = "o", markevery = 10)
plt.plot(xpoints, gx,label = "$g(x)= x^{2}$", color="royalblue", linewidth = 2, marker = "o", markevery = 10)
plt.plot(xpoints, hx, label = "$h(x)= x^{3}$", color="forestgreen", linewidth = 2, marker = "o", markevery = 10)

#labels
plt.title ("Values of $x$, $x^{}$, and $x^{}$ in the range {}-{}".format(2,3,lowRange,highRange))
plt.xlabel("$x$")
plt.ylabel("$x^{n}$")
plt.legend()

#style

plt.grid(linestyle ="dashed")
ax.set_facecolor("lightgrey")


#show and save
#plt.show()
plt.savefig("plotTask.png")