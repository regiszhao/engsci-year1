# -*- coding: utf-8 -*-
"""
This program imports data from the file specified by the string filename
The first line of the file is ignored (assuming it's the name of the variables)
After that the data file needs to be formatted: 
number space number space number space number newline
Do NOT put commas in your data file!!
The data file should be in the same directory as this python file
The data should be in the order:
x_data y_data x_uncertainty y_uncertainty

Then this program tries to fit a function to the data points
It plots the data as dots with errorbars and the best fit line
It then prints the best fit information
After that, it plots the "residuals": ydata - fittedfunction(xdata)
That is it subtracts your fitted ideal values from your actual data to see 
what is "left over" from the fit
Ideally your residuals graph should look like noise, otherwise there is more
information you could extract from your data (or you used the wrong fitting
function)

If you want to change the graph labels, look for the plt.xlabel() commands
If you want to change the file name, that's the next line below this comment
"""
filename="mydata.txt"
# change this if your filename is different


import scipy.optimize as optimize
import numpy as np
import matplotlib.pyplot as plt
from pylab import loadtxt


data=loadtxt(filename, usecols=(0,1,2,3), skiprows=1, unpack=True)
# load filename, take columns 0 & 1 & 2 & 3, skip 1 row, unpack=transpose x&y

xdata=data[0]
ydata=data[1]
xerror=data[2]
yerror=data[3]
# finished importing data, naming it sensibly

def my_func(L, k, L_0, n):
    return k * ((L_0 + L) ** n)
# this is the function we want to fit. the first variable must be the
# x-data (time), the rest are the unknown constants we want to determine

popt, pcov = optimize.curve_fit(my_func, xdata, ydata)
# we have the best fit values in popt[], while pcov[] tells us the uncertainties

k=popt[0]
L_0=popt[1]
n=popt[2]
# best fit values are named nicely
u_k=pcov[0,0]**(0.5)
u_L_0=pcov[1,1]**(0.5)
u_n=pcov[2,2]**(0.5)
# uncertainties of fit are named nicely

def fitfunction(L):  
    return k * ((L_0 + L) ** n)
#fitfunction(t) gives you your ideal fitted function, i.e. the line of best fit

start=min(xdata)
stop=max(xdata)    
xs=np.arange(start,stop,(stop-start)/1000) # fit line has 1000 points
curve=fitfunction(xs)
# (xs,curve) is the line of best fit for the data in (xdata,ydata) 

plt.rcParams["figure.figsize"] = (10,6)
# Change the size of your plot - numbers are inches because USA

plt.errorbar(xdata,ydata,yerr=yerror,xerr=xerror,fmt=".")
# plot the data, fmt makes it data points not a line
plt.plot(xs,curve)
# plot the best fit curve on top of the data points as a line

plt.xlabel("Time (s)")
plt.ylabel("Angle relative to equilibrium position, θ (rad)")
plt.title("Curve of best fit modelling the pendulum's angular position with time from t = 7s to t = 11s")
# HERE is where you change how your graph is labelled!

plt.show()
# show the graph


print("k:", k, "+/-", u_k)
print("L_0:", L_0, "+/-", u_L_0)
print("n:", n, "+/-", u_n)
# prints the various values with uncertainties

plt.rcParams["figure.figsize"] = (10,3)
# Change the size of your plot - numbers are inches because USA

residual=ydata-fitfunction(xdata)
# find the residuals
zeroliney=[0,0]
zerolinex=[start,stop]
# create the line y=0

plt.errorbar(xdata,residual,yerr=yerror,xerr=xerror,fmt=".")
# plot the residuals with error bars
plt.plot(zerolinex,zeroliney)
# plotnthe y=0 line on top

plt.xlabel("Time (s)")
plt.ylabel("Residuals of data of pendulum's angular position (rad)")
plt.title("Residuals of the pendulum's modelled angular position with time")
# HERE is where you change how your graph is labelled!

plt.show()
# show the graph