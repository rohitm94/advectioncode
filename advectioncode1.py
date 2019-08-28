import datetime

def advectioncode1():
	#Simulation parameters Intialization
	t_max = 2.0
	
	N= 103
	dt=0.0009
	
	x_min = 0.0
	x_max= 1.0
	v=1.0
	xc = 0.25
	dx = (x_max-x_min)/2
	nbstep = t_max / dt
	alpha= v*dt/(2*dx)
	
	x=[0]*(N+3)
	u_0=[0]*(N+3)
	u=[0]*(N+3)
	u_new=[0]*(N+3)
	#Simulation Domain
	for i in range(0,N+3):
		x[i]= x_min + ((i-1)*dx)
	
	for i in range(0,N+3):
		u_0[i] = -200*((x[i]-xc)**2)
	
	u=u_0
	u_new =u_0
	for timestep in range(1,int(nbstep)):
		for j in range(1,N+2):
			u_new[j] = u[j+1]*(0.5-alpha) + u[j-1]*(0.5+alpha)

		u = u_new
		u[0] = u[N+1]
		u[N+2] = u[1]
	
def advectioncode2():
	#Simulation parameters Intialization
	t_max = 2.0
	
	N= 1003
	dt=0.00009
	
	x_min = 0.0
	x_max= 1.0
	v=1.0
	xc = 0.25
	dx = (x_max-x_min)/2
	nbstep = t_max / dt
	alpha= v*dt/(2*dx)
	
	x=[0]*(N+3)
	u_0=[0]*(N+3)
	u=[0]*(N+3)
	u_new=[0]*(N+3)
	#Simulation Domain
	for i in range(0,N+3):
		x[i]= x_min + ((i-1)*dx)
	
	for i in range(0,N+3):
		u_0[i] = -200*((x[i]-xc)**2)
	
	u=u_0
	u_new =u_0
	for timestep in range(1,int(nbstep)):
		for j in range(1,N+2):
			u_new[j] = u[j+1]*(0.5-alpha) + u[j-1]*(0.5+alpha)

		u = u_new
		u[0] = u[N+1]
		u[N+2] = u[1]
		
start =datetime.datetime.now()

advectioncode1()
	
end =datetime.datetime.now()


start1 =datetime.datetime.now()

advectioncode2()
	
end1 =datetime.datetime.now()

print('Runtime for N-103 and dt-0.0009')
print(end-start)
print('Runtime for N-1003 and dt-0.00009')
print(end1-start1)