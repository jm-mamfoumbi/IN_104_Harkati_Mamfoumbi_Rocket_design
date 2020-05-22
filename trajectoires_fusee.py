from math import *
from matplotlib import pyplot as plt
from classe import Fusee

##original rockets in the database
sputnik = Fusee('Sputnik')
miura = Fusee("Miura 1")
ariane = Fusee("Ariane 5")
soyuz = Fusee("Soyuz")
saturn = Fusee("Saturn V")
falcon = Fusee("Falcon 9")


def trajectoire_1_etage(fusee, theta):
    """the function takes in argument a rocket item
    and an angle and returns
    """
    if type(fusee)!=Fusee:
        raise Badtype(fusee)
    if theta< 0 :
        raise Badvalue(theta)
    if theta > pi :
        raise Badvalue(theta)
    x = []
    z = []
    dt = 10 ** (-1)
    t = dt
    n = 0
    g0 = 9.81
    T = fusee.configuration[fusee.config_type['S1 thrust [kN]']]* 1000
    isp = fusee.configuration[fusee.config_type['S1 Isp [s]']]
    D = T / (isp * g0) #propellant mass flow rate
    mp = fusee.configuration[fusee.config_type['S1 mp [tons]']] * 1000
    tb = mp / D  # burning time
    m0 = fusee.configuration[fusee.config_type['lift-off mass [tons]']] * 1000
    mf = m0 - mp
    while t < tb and n < 1000000:
        xt = (((m0 * (isp * g0) ** 2) / T) * (1 - ((m0 - t * D) / m0) * (log((m0) / (m0 - t * D)) + 1)) *
                cos(theta)) * 10 ** -3  # x in kilometers
        x.append(xt)
        zt= (((m0 * (isp * g0) ** 2) / T) * (1 - ((m0 - t * D) / m0) * (log((m0) / (m0 - t * D)) + 1)) *
                sin(theta) - 0.5 * g0 * t ** 2) * 10 ** -3  # z in kilometers
        z.append(zt)
        n = n + 1
        t = t + dt
    vx = isp * g0 * log(m0 / mf) * cos(theta)
    vz = isp * g0 * log(m0 / mf) * sin(theta) - g0 * tb
    nb = n #index to get the position in x and z at the extinction time
    t = t - tb
    while z[n -1] > 0 :
        xt = x[nb - 1] + vx * t * 10 ** -3
        x.append(xt)
        zt = z[nb - 1] + vz * t * 10** -3 - 0.5 * g0 * (t**2) * 10 ** -3
        z.append(zt)
        n = n + 1
        t = t + dt
    return [x[:n],z[:n],t,n]


def trajectoire_2_etages(fusee, theta):
    """the function takes in argument a rocket item
    and an angle and returns
    """
    if type(fusee)!=Fusee:
        raise Badtype(fusee)
    x = []
    z = []
    dt = 10 ** (-1)
    t = dt
    n = 0
    g0 = 9.81
    print(fusee.config_type)
    T = (fusee.configuration[fusee.config_type['S1 thrust [kN]']] +fusee.configuration[fusee.config_type['S2 thrust [kN]']]) * 1000
    isp =fusee.configuration[fusee.config_type['S1 Isp [s]']] + fusee.configuration[fusee.config_type['S2 Isp [s]']]
    D = T / (isp * g0) #propellant mass flow rate
    mp = (fusee.configuration[fusee.config_type['S1 mp [tons]']] + fusee.configuration[fusee.config_type['S2 mp [tons]']]) * 1000   # burning time
    tb = mp / D
    m0 = fusee.configuration[fusee.config_type['Lift-off mass [tons]']] * 1000
    mf = m0 - mp
    while t < tb and n < 1000000:
        xt = (((m0 * (isp * g0) ** 2) / T) * (1 - ((m0 - t * D) / m0) * (log((m0) / (m0 - t * D)) + 1)) * cos(theta)) * 10 ** -3  # x in kilometers
        x.append(xt)
        zt= (((m0 * (isp * g0) ** 2) / T) * (1 - ((m0 - t * D) / m0) * (log((m0) / (m0 - t * D)) + 1)) * sin(theta) - 0.5 * g0 * t ** 2) * 10 ** -3  # z in kilometers
        z.append(zt)
        n = n + 1
        t = t + dt
    vx = isp * g0 * log(m0 / mf) * cos(theta)
    vz = isp * g0 * log(m0 / mf) * sin(theta) - g0 * tb
    nb = n #index to get the position in x and z at the extinction time
    t = t - tb
    while z[n - 1] > 0 and n < 100000:
        xt = x[nb - 1] +  vx * t * 10 ** -3
        zt = z[nb - 1] +  vz * t * 10** -3 - 0.5 * g0 * (t**2) * 10 ** -3
        x.append(xt)
        z.append(zt)
        n = n + 1
        t = t + dt
    return [x[:n],z[:n],t,n]


def trajectoire(fusee, theta):
    """the function takes in argument a rocket item
    and an angle and returns
    """
    if type(fusee)!=Fusee:
        raise Badtype(fusee)
    if fusee.configuration[fusee.config_type['Stages number']] == 1:
        return trajectoire_1_etage(fusee, theta)
    elif fusee.configuration[fusee.config_type['Stages number']] == 2:
        return trajectoire_2_etages(fusee,theta)
    else :
        print("Unkown rocket object")

def affichage_trajectoire(fusee,theta):
    """the function takes in argument a rocket item
    and an angle and returns
    """
    if type(fusee)!=Fusee:
        raise Badtype(fusee)
    L = trajectoire(fusee, theta)
    x = L[0]
    z = L[1]
    n = len(x)
    q = n/200
    q = int(q)
    for i in range(200):
        plt.xlabel(' axe des x (en km)')
        plt.ylabel(' axe des y (en km)')
        plt.title('trajectoire de {} pour un angle de {} radians'.format(fusee.configuration[fusee.config_type['Name']], round(theta, 3)))
        plt.plot(x[:i*q],z[:i*q])
        plt.pause(0.01)
        plt.close()
    plt.xlabel(' axe des x (en km)')
    plt.ylabel(' axe des y (en km)')
    plt.title('trajectoire de {} pour un angle de {} radians'.format(fusee.configuration[fusee.config_type['Name']], round(theta, 3)))
    plt.plot(x,z)
    plt.show()
