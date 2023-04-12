
import matplotlib.pyplot as plt
import numpy as np

#telling it to load info from a file and put it into two arrays
#first arg is the location of file
#second arg is which columns to use
#third arg tells the command that this file uses columns
wavelength, flux = np.loadtxt("M83-POS1/M83-POS1_HI_1215_lsf_mask_testerrors.reg", usecols=(0,1), unpack=True)

plt.plot(wavelength, flux)

#M83-1
#plt.xlim([1175, 1264])
#plt.ylim([-0.1, 2])

#M83-POS1
plt.xlim([1175, 1300])
plt.ylim([-0.1, 1.5])

plt.axhline([1])
plt.show()