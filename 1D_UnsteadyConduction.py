import numpy as np; import os;import matplotlib.pyplot as plt;import math;
os.system('cls'); plt.rcParams['font.family'] = 'Times New Roman'

#user defined constants
dx = 0.25; gamma = [0.5, 1/6]; a = 1
T_i = 100; T_f = 200
length_beam = 10.125
t_range = [0,10]

#define other constants
dt = np.zeros(len(gamma)); t = t_range[0]
for i in range(0,int(len(dt))):dt[i]=gamma[i]*dx*dx/a

#iterate for each gamma value
for k in range(0,len(gamma)):

    #initialize arrays
    X_values = np.linspace(-dx/2,length_beam,int((length_beam+dx/2)/dx)+1)
    T_values = np.zeros(int((length_beam+dx/2)/dx)+1);T_values[-1]=T_f
    for i in range(0,len(T_values)-1):T_values[i] = T_i 
    
    #arrays to track temperature over time, [:,1] is midpoint temp and [:,2] is origin temp
    TempOverTime = np.zeros((int((t_range[1]-t_range[0])/dt[k])+1,3)); 
    TempOverTime[0,2] = T_i;TempOverTime[0,1] = T_i;TempOverTime[0,0] = t_range[0]

    #iterate through time
    for i in range(1,int((t_range[1]-t_range[0])/dt[k])+1):
        t = t_range[0]+dt[k]*i; TempOverTime[i,0] = t; #move time forward and record in plot array
        
        #iterate through temperature values from left to right
        T_values_new = T_values
        for j in range(1,len(T_values)-1):
            T_values_new[j] = T_values[j]+a*dt[k]/(dx*dx)*(T_values[j+1]-2*T_values[j]+T_values[j-1])
        T_values_new[0] = T_values_new[1] #assign mirrored value to mimic insulated wall
        T_values = T_values_new

        TempOverTime[i,1] = T_values[int(np.floor(len(T_values)/2))] #put midpoint temp in array
        TempOverTime[i,2] = T_values[1] #put midpoint temp in array

    #generate temperature origin plot
    plt.figure(1+(k*3))
    plt.plot(TempOverTime[:,0],TempOverTime[:,2])
    plt.title("Temperature over Time at Origin (x = {xval})".format(xval = (X_values[0]+X_values[1])/2))
    plt.xlabel("Time (s)");plt.ylabel("Temperature ($^\circ$C)")
    plt.savefig('OriginPlot_g={gamma}.png'.format(gamma=gamma[k]))
    
    #generate temperature midpoint plot
    plt.figure(2+(k*3))
    plt.plot(TempOverTime[:,0],TempOverTime[:,1])
    plt.title("Temperature over Time at Midpoint (x = {xval})".format(xval = X_values[int(len(T_values)/2)]))
    plt.xlabel("Time (s)");plt.ylabel("Temperature ($^\circ$C)")
    plt.savefig('MidpointPlot_g={gamma}.png'.format(gamma=gamma[k]))

    #generate temperate plot at end
    plt.figure(3+(k*3))
    plt.plot(X_values,T_values)
    plt.title("Temperature Plot at Time t = {time}".format(time=int(t)))
    plt.xlabel("Horizontal Position (m)");plt.ylabel("Temperature ($^\circ$C)")
    plt.savefig('TempPlot_g={gamma}.png'.format(gamma=gamma[k]))

plt.show()