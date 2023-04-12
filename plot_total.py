import matplotlib.pyplot as plt
import numpy as np

HI, HI_err, dist = np.loadtxt("DATA.txt", usecols=(1,2,3), unpack=True)
dirs = ["M83-1","M83-2","M83-3","M83-4","M83-6","M83-7","M83-8","M83-9","M83-10","M83-11","M83-12","M83-13","M83-14","M83-15","M83-16","M83-POS1","M83-POS2"]


point1 = str(input("Pick Pointing 1\n> "))
point2 = str(input("Pick Pointing 2\n> "))

point = [point1, point2]

fig, axs = plt.subplots(2, sharex=True)
    

for i in range(len(axs)):
    
    wl, fits = np.loadtxt(point[i]+"/"+point[i]+"_total.reg", usecols=(0,3), unpack=True)
    wl2, comp_1, comp_2 = np.loadtxt(point[i]+"/"+point[i]+"_components.dat", usecols=(0,1,2), unpack=True)
    
    
    axs[i].title.set_text(point[i]+"\nHI density: "+str(HI[dirs.index(point[i])])+"\nDistance from center: "+str(dist[dirs.index(point[i])])+" parsecs")
    
    
    axs[i].plot(wl2, comp_1, "c", label="Milky Way | Component 1")
    axs[i].plot(wl2, comp_2, "b", label="M83 | Component 2")
    axs[i].plot(wl, fits, "r", label="Total", zorder=1)


    #adjust plot limits
    axs[i].set_xlim([1175, 1250])
    #axs[i].set_ylim([-0.5, 1.7])
    
    
    #HI line
    axs[i].axvline(x=1216, color = "r", ls = "--", label="HI line: 1216")
    #show legend 
    if i == 1:
        axs[i].legend()
    
    plt.ylabel("Normalized Flux")

#baseline
#plt.axhline(y=1, color = "k", ls = "--")

plt.xlabel("Wavelength (nm)")


plt.show()