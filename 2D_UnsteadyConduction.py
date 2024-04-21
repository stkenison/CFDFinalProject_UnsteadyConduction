import numpy as np; import os;import matplotlib.pyplot as plt;import math; import timeit; import tqdm
os.system('cls'); plt.rcParams['font.family'] = 'Times New Roman'

#user defined constants
gamma = 0.25; a = 1
temp_interval = [100, 200]
gridsize = [5, 10, 100]
time_interval = [0, 10]
XY_interval = [0, 1]

#define other constants (dx/dy and dt)
dxdy = np.zeros(len(gridsize))
for i in range (0,len(gridsize)):dxdy[i]=1/gridsize[i]
dt = np.zeros(len(gridsize))
for i in range(0,len(dt)):dt[i]=gamma*dxdy[i]*dxdy[i]/a
print("Starting simulations...\n")

#iterate for each gridsize
for k in range(0,len(gridsize)):

    #track simulation runtime
    print("Running gridsize {a}x{b}".format(a=gridsize[k],b=gridsize[k]))
    start = timeit.default_timer(); t = time_interval[0]
    
    #initialize arrays
    XY_values = np.linspace(XY_interval[0],XY_interval[1],gridsize[k]+1) #array of x/y values
    T_values = np.zeros((int(gridsize[k]+3),int(gridsize[k]+3))) #array to store temperature values
    for i in range(0,gridsize[k]+2): #assign initial values to temperature array
        for j in range(0,gridsize[k]+2): T_values[i,j]=temp_interval[0]
    for i in range(0,gridsize[k]+3):T_values[-1,i]=temp_interval[1]
    for i in range(0,gridsize[k]+3):T_values[i,-1]=temp_interval[1]
    TempOverTime = np.zeros((3,int((time_interval[1]-time_interval[0])/dt[k]+2))) #array to store temperature over time
    TempOverTime[0,0] = t;TempOverTime[1,0] = T_values[int(gridsize[k]*.4+1),int(gridsize[k]*.4+1)];TempOverTime[2,0] = T_values[int(gridsize[k]*.8+1),int(gridsize[k]*.8+1)]
    c = a*dt[k]/(dxdy[k]*dxdy[k]) #coefficient for explicit scheme
    T_values_new = T_values #array to hold new calculated temperature values

    #iterate through time
    for n in tqdm.tqdm(range(1,int((time_interval[1]-time_interval[0])/dt[k]+2))):
        t = dt[k]*n+time_interval[0]; TempOverTime[0,n] = t
        
        #iterate through x and y values
        for i in range(1,gridsize[k]+2):
            for j in range(1,gridsize[k]+2):
                T_values_new[i,j] = T_values[i,j]+c*(T_values[i+1,j]-2*T_values[i,j]+T_values[i-1,j])+c*(T_values[i,j+1]-2*T_values[i,j]+T_values[i,j-1])
        T_values = T_values_new

        #save new values to track temperature over time
        TempOverTime[1,n] = T_values[int(gridsize[k]*.4+1),int(gridsize[k]*.4+1)]
        TempOverTime[2,n] = T_values[int(gridsize[k]*.8+1),int(gridsize[k]*.8+1)]
    
    #print simulation runtime to consol
    end = timeit.default_timer()
    print("Simulation Time = {} sec \n".format(end-start))

    #generate temperature plot at 0.4*range
    plt.figure(1+(k*3))
    plt.plot(TempOverTime[0,:],TempOverTime[1,:])
    plt.title("Temperature over Time at (x = {xval})".format(xval = XY_values[int(0.4*gridsize[k])]))
    plt.xlabel("Time (s)");plt.ylabel("Temperature ($^\circ$C)"); plt.xscale('log');  
    #plt.xlim = ((time_interval[0],time_interval[1])); plt.ylim = ((temp_interval[0],temp_interval[1]))
    plt.savefig('Figure{}'.format(1+k*3)); plt.pause(0.00001)

    #generate temperature plot at 0.8*range
    plt.figure(2+(k*3))
    plt.plot(TempOverTime[0,:],TempOverTime[2,:])
    plt.title("Temperature over Time at (x = {xval})".format(xval = XY_values[int(gridsize[k]*0.8)]))
    plt.xlabel("Time (s)");plt.ylabel("Temperature ($^\circ$C)")
    plt.xscale('log'); 
    plt.savefig('Figure{}'.format(2+k*3)); plt.pause(0.00001)
    
    #create contour plot
    plt.figure(3+k*3)
    X, Y = np.meshgrid(XY_values, XY_values)
    T = T_values[1:gridsize[k]+2,1:gridsize[k]+2]
    countour = plt.contourf(X, Y, T, levels=gridsize[k], cmap='jet')
    plt.xlabel('X-axis');plt.ylabel('Y-axis')
    plt.title("Temperature Contour Plot at Time t = {}".format(int(t)))
    plt.colorbar(countour, label='Temperature Values'); 
    plt.savefig('Figure{}'.format(3+k*3));plt.pause(0.00001)

print("")