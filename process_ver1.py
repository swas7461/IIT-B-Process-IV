import csv
import matplotlib.pyplot as plt
import numpy as np

Vl = []
Il = []

Vd = []
Id = []

filename1 = input('Enter file to extract the data under light (use 2 \\ for \\): ')
filename2 = input('Enter file to extract the data under dark (use 2 \\ for \\): ')

for d in csv.DictReader(open(filename1), delimiter=','):
    Vl.append(float(d['Smu1_V(1)(1)']))
    Il.append(float(d['Smu1_I(1)(1)']))
    
for d in csv.DictReader(open(filename2), delimiter=','):
    Vd.append(float(d['Smu1_V(1)(1)']))
    Id.append(float(d['Smu1_I(1)(1)']))
    
vl = np.array(Vl)
il = np.array(Il)
vd = np.array(Vd)
Id = np.array(Id)

a = 0.00036 #Effective area in cm^2
i = 100 #Irradiance in mW/cm^2

jl = il/a
jd = Id/a

jmod = np.absolute(jl)
vmod = np.absolute(vl)
imod = np.absolute(il)

indexv = np.argmin(vmod)
indexi = np.argmin(imod)

Voc = vmod[indexi]
Jsc = jmod[indexv]
Isc = imod[indexv]

for index in range(0, vd.size):
        if vd[index] == 0:
            x = index
        elif vd[index] == 0.01:
            xh = index

rsh = 0.01/(Id[xh] - Id[x])

P = vl*il
indexp = np.argmin(P)
Vm = vmod[indexp]
Im = imod[indexp]

ff = np.absolute(P[np.argmin(P)])/(Voc*Isc)
eff = (np.absolute(P[np.argmin(P)])/(i*a))*100

string = 'Jsc = ' + str(Jsc) + 'mA/cm^2\nVoc = ' + str(Voc) + 'V\n Fill Factor = ' + str(ff) + '\n Efficiency = ' + str(eff) + '%\nRsh = ' + str(rsh) + 'ohm'

plt.figure(1)
line1 = plt.plot(vl, jl, 'r')
line2 = plt.plot(vd, jd, 'k')
plt.xlabel('Voltage (V)')
plt.ylabel('Current Density (mA/cm^2)')
plt.xlim(0, 1.05*Voc)
plt.legend(['Light', 'Dark'], loc=4)
plt.text(0,-0.0001*Jsc,string)
plt.show()
