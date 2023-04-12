import matplotlib.pyplot as plt
import numpy as np

#filepaths
targets = ["M83-15/M83-15_HI_1215_vel_mask.reg", "M83-POS1/M83-POS1_HI_1215_lsf_mask_testerrors.reg", "M83-POS2/M83-POS2_HI_1215_vel_mask.reg"]
#names for labels
target_names = ["M83-15", "M83-POS1", "M83-POS2"]
#data for labels
data = ["20.81", "19.55", "18.19"]
#colors for lines
colors = ["c", "b", "m"]

#loop through the 3 values
for i in range(len(targets)):
    wavelength, flux = np.loadtxt(targets[i], usecols=(0,1), unpack=True)
    plt.plot(wavelength, flux, colors[i], label = target_names[i]+" | logN: "+data[i])

#adjust plot limits
plt.xlim([1175, 1250])
plt.ylim([-0.5, 1.7])

#baseline
plt.axhline(y=1, color = "k", ls = "--")
#HI line
plt.axvline(x=1216, color = "r", ls = "--", label="HI line: 1216")
#show legend 
plt.legend()


plt.show()