# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 14:46:34 2022

@author: Elijah Emory, Britney Whittington
"""

#Libaries

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

#names of targets
points = ["M83-1","M83-2","M83-3","M83-4","M83-6","M83-7","M83-8","M83-9","M83-10","M83-11","M83-12","M83-13","M83-14","M83-15","M83-16","M83-POS1","M83-POS2"]

# Grand dictionary of file locations for M83 spectrograph data points. Notice 5 is excluded (data was unusable)
spectra_files = {'M83-1' : 'M83-1_HI_1215_lsf_mask.reg',
'M83-2' : 'M83-2_HI_1215_vel_mask.reg',
'M83-3' : 'M83-3_HI_1215_vel_mask.reg',
'M83-4' : 'M83-4_HI_1215_lsf_mask_testerrors2.reg',
'M83-6' : 'M83-6_HI_1215_vel_mask.reg',
'M83-7' : 'M83-7_HI_1215_vel_mask.reg',
'M83-8' : 'M83-8_HI_1215_vel_mask.reg',
'M83-9' : 'M83-9_HI_1215_vel_mask.reg',
'M83-10' : 'M83-10_HI_1215_vel_mask.reg',
'M83-11' : 'M83-11_HI_1215_lsf_mask_testerrors.reg',
'M83-12' : 'M83-12_HI_1215_vel_mask.reg',
'M83-13' : 'M83-13_HI_1215_vel_mask.reg',
'M83-14' : 'M83-14_HI_1215_vel_mask.reg',
'M83-15' : 'M83-15_HI_1215_vel_mask.reg',
'M83-16' : 'M83-16_HI_1215_vel_mask.reg',
'M83-POS1' : 'M83-POS1_HI_1215_lsf_mask_testerrors.reg',
'M83-POS2' : 'M83-POS2_HI_1215_vel_mask.reg'}

#imports data
HI, HI_err, dist = np.loadtxt("DATA.txt", usecols=(1,2,3), unpack=True)



#integer checking function
def getint(_min, _max):
    userin = input('> ')
    
    try:
        userout = int(userin)
        if userout > _max or userout < _min:
            print("====ERROR====\nPlease pick a variable between: "+str(_min)+"-"+str(_max)+".") 
            return(getint(_min,_max))
        else:
            return(userout)
    except ValueError:
        print("====ERROR====\nPlease select an interger.")
        return(getint(_min, _max))
    
#string checking
def getstr():
    strin = input('Please input a point M83-[1-16], M83-POS1, or M83-POS2:\n> ')
    
    if strin == "M83-5":
        print("====ERROR====\nHubble didn't like this point, please try a different one:")
        return(getstr())
    
    if strin not in points:
        print('====ERROR====\nPlease pick from one of the listed points')
        return(getstr())

    return(strin)



"""
Menu:
1 = look at raw spectrograph data of up to 17 points
2 = look at VoigtFit's best fit line data compared to the Milky Way
3 = HI data
4 = M83 map of points
0 = Quit
"""

loop = True


print("Welcome to the M83 point plotter tool!")

# loop for menu

while (loop):

    print('\n====MENU====\n1. Look at raw spectrograph data\n2. Look at VoigtFit best fit lines\n3. Look at total HI data\n4. M83 plot locations image\n0. Exit and credits')
    
    #input for menu
    print('\nPlease make a selection on the menu:')
    pick = getint(0,4)
 
    #raw spectra data of many points
    if pick == 1:
        
        #get number of points wanting to get mapped and make a list
        print("\n====SPECTRA====\nPlease choose how many points you wish to plot at one time (max 17)")
        num = getint(1, 17)
        
        selected_points = []
        
        #populate list with chosen points
        for i in range(num):
            choice = getstr()
            selected_points.append(choice)
            
            
        #plot the list of selected points
        for i in range(len(selected_points)):
            path = selected_points[i]+"/"+spectra_files[selected_points[i]] #get to file location
            wavelength, flux = np.loadtxt(path, usecols=(0,1),unpack=True) #load data from file
            plt.plot(wavelength, flux, label = selected_points[i]) #add to plot
            
        #format plot
        plt.legend()
        plt.xlabel("Wavelength (nm)")
        plt.ylabel("Normalized Flux")
        plt.xlim([1130,1280])
        plt.axhline([1])
        plt.title("Comparison of spectra of selected points")

        plt.show(block=True) #deleted the plot, need to remake it
        
        
        #plot the list of selected points ZOOMED IN
        for i in range(len(selected_points)):
            path = selected_points[i]+"/"+spectra_files[selected_points[i]]
            wavelength, flux = np.loadtxt(path, usecols=(0,1),unpack=True)
            plt.plot(wavelength, flux, label = selected_points[i])
            
        plt.legend()
        plt.xlabel("Wavelength (nm)")
        plt.ylabel("Normalized Flux")
        plt.xlim([1130,1280])
        plt.axhline([1])
        plt.title("Comparison of spectra of selected points")
        
        
        plt.ylim([-0.30,2.40])
        plt.show(block=True)


    #best fit lines
    if pick == 2:
        
        print("\n====HI BEST FITS====\nPlease choose 2 points to compare")
        selected_points = []
        
        selected_points.append(getstr())
        selected_points.append(getstr())
        
        fig, axs = plt.subplots(2, sharex=True)
            
        for i in range(len(axs)):
            
            wl, fits = np.loadtxt(selected_points[i]+"/"+selected_points[i]+"_total.reg", usecols=(0,3), unpack=True)
            wl2, comp_1, comp_2 = np.loadtxt(selected_points[i]+"/"+selected_points[i]+"_components.dat", usecols=(0,1,2), unpack=True)
            
            
            axs[i].title.set_text(selected_points[i]+"\nHI density: "+str(HI[points.index(selected_points[i])])+"\nDistance from center: "+str(dist[points.index(selected_points[i])])+" parsecs")
            
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
        
        plt.show(block=True)
        
        

#Displays Error bar enabled graph of Hydrogen distribution

    if pick == 3:
        x = np.linspace(0,5.1,100)
        plt.errorbar(dist, HI, yerr = HI_err, fmt = 'ob', label="data", ecolor="r", capsize=3)
        plt.plot(x, 0.4872*np.log(x) + 19.942, ls="--", label="fit")
        plt.xlabel('Galactictocentric Distance (kpc)')
        plt.ylabel('# of Hydrogen log(n) in cm^2')
        plt.title("HI Distribution over Distance from Center")
        plt.legend()
        plt.grid()
        plt.show(block=True)

#M83 image with all the points
    
    if pick == 4:
        image = Image.open('M83roadmap.jfif')
        image.show()
        
    if pick == 0:
        print("====CREDITS====\nData: Hubble\nData interpretation: Dr. Svea Hermandez\nProgram creators: Britney Whittington and Elijah Emory")
        loop = False

        