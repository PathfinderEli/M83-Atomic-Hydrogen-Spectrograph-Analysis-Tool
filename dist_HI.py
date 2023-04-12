import matplotlib.pyplot as plt
import numpy as np

HI, HI_err, dist = np.loadtxt("DATA.txt", usecols=(1,2,3), unpack=True)

curve = np.polyfit(np.log(dist), HI, 1)


plt.errorbar(dist, HI, yerr=HI_err, fmt="ob", marker=(5, 1))
#plt.plot(dist, curve[0]*np.log(dist) + curve[1])


plt.title("HI vs. Distance from Galactic Center")
plt.xlabel("Galactocentric Distance (parsec)")
plt.ylabel("log(N)")
plt.show()