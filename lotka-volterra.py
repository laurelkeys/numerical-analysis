import math
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

# lotka volterra model
# | u1' = c1*u1 - d1*u1*u2 = f1
# | u2' = c2*u1*u2 - d2*u2 = f2
# | u1(0) = u1_0
# | u2(0) = u2_0

# u1_0 is the initial amount of prey
# u2_0 is the initial number of predators

# c1 is the rate of prey population increase
# d1 is the predation rate coefficient
# c2 is the reproduction rate of predators per 1 prey eaten
# d2 is the predator mortality rate

# the interval of analysis is [0, T]
# and it is divided in N subintervals of size dt = T/N

class Model:
    def show(self):
        print(f'| u1\' = {self.c1}*u1 - {self.d1}*u1*u2')
        print(f'| u2\' = {self.c2}*u1*u2 - {self.d2}*u2')
        print(f'| u1(0) = {self.u1_0}')
        print(f'| u2(0) = {self.u2_0}')

def euler(dt, u1_i, u2_i, f1, f2):
    # euler's method for the lotka volterra model
    u1 = u1_i + dt*f1(u1_i, u2_i) # u1_i+1
    u2 = u2_i + dt*f2(u1_i, u2_i) # u2_i+1
    return (u1, u2)

def modified_euler(dt, u1_i, u2_i, f1, f2):
    # calculates u2_i+1 using u1_i+1 instead of u1_i
    u1 = u1_i + dt*f1(u1_i, u2_i) # u1_i+1
    u2 = u2_i + dt*f2(u1, u2_i) # u2_i+1
    return (u1, u2)

def rk4(dt, u1_i, u2_i, f1, f2):
    # runge-kutta's method for the lotka volterra model
    p1 = f1(u1_i, u2_i)
    p2 = f2(u1_i, u2_i)

    q1 = f1(u1_i + (dt/2)*p1, u2_i + (dt/2)*p2)
    q2 = f2(u1_i + (dt/2)*p1, u2_i + (dt/2)*p2)
    
    r1 = f1(u1_i + (dt/2)*q1, u2_i + (dt/2)*q2)
    r2 = f2(u1_i + (dt/2)*q1, u2_i + (dt/2)*q2)
    
    s1 = f1(u1_i + dt*r1, u2_i + dt*r2)
    s2 = f2(u1_i + dt*r1, u2_i + dt*r2)
    
    u1 = u1_i + (dt/6)*(p1 + 2*(q1 + r1) + s1) # u1_i+1
    u2 = u2_i + (dt/6)*(p2 + 2*(q2 + r2) + s2) # u2_i+1
    return (u1, u2)

def lotka_volterra(N, T, model, methods=[euler], uvt='u_vs_t', uvu='u_vs_u'):
    model.show()

    dt = T/N
    print(f'\n[0, T] = [0, {T}]')
    print(f'Δt = {dt}')

    f1 = lambda u1, u2: model.c1*u1 - model.d1*u1*u2 # u1' = f1
    f2 = lambda u1, u2: model.c2*u1*u2 - model.d2*u2 # u2' = f2

    comparison = []
    for method in methods:
        ts = [0] # t_0, t_1, ..., t_N where [t_0, t_N] = [0, T]
        u1s = [model.u1_0] # u1_0, u1_1, ..., u1_N
        u2s = [model.u2_0] # u2_0, u2_1, ..., u2_N
        
        t, u1_i, u2_i = 0, model.u1_0, model.u2_0
        for i in range(N):
            t += dt
            ts.append(t)
            u1_i, u2_i = method(dt, u1_i, u2_i, f1, f2)
            u1s.append(u1_i)
            u2s.append(u2_i)

        fig1 = plt.figure(figsize=(10, 10))
        ax1 = fig1.add_subplot(111)
        ax1.plot(ts, u1s) # plot u1 vs t
        ax1.plot(ts, u2s) # plot u2 vs t
        fig1.savefig(f'{method.__name__}-{uvt}.png' if len(methods) > 1 else f'{uvt}.png')
        
        fig2 = plt.figure(figsize=(10, 10))
        ax2 = fig2.add_subplot(111)
        ax2.plot(u1s, u2s) # plot u2 vs u1
        fig2.savefig(f'{method.__name__}-{uvu}.png' if len(methods) > 1 else f'{uvu}.png')
        
        comparison.append((u1s, u2s, method.__name__))
    
    if len(methods) > 1:
        fig3 = plt.figure(figsize=(10, 10))
        ax3 = fig3.add_subplot(111)
        for x, y, m in comparison:
            ax3.plot(x, y, label=m) # plot u2 vs u1
        ax3.legend()
        fig3.savefig('comparison.png')
    
    return u1s, u2s, ts

# m1 = Model()
# m1.c1 = 0.08
# m1.d1 = 0.09
# m1.c2 = 0.07
# m1.d2 = 0.075
# m1.u1_0 = 3
# m1.u2_0 = 1
# lotka_volterra(T=200, N=2000, model=m1)
# lotka_volterra(T=200, N=20000, model=m1)

m2 = Model()
m2.c1 = 1
m2.d1 = 1
m2.c2 = 1
m2.d2 = 1
m2.u1_0 = 0.5
m2.u2_0 = 0.5
n = lambda T, dt: math.ceil(T/dt)
lotka_volterra(T=20, N=n(T=20, dt=0.1), model=m2, methods=[euler, modified_euler, rk4])
