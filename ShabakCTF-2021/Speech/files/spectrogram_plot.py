#%%
# ShabakCTF@2021 

import numpy as np
import matplotlib.pyplot as plot
 
# {'descr': '<f4', 'fortran_order': False, 'shape': (138, 80), }
# 
# '<f4' -> '<' = Little endian, 'f4' = float32  (8x4) --> Little Endian 32 bit float
# 'fortran_order' -> False -> dont care
# 'shape': (138, 80) -> 138 dimensions, each dimension has 80 elements


# Remove the header inside "Speech.txt" as np.fromfile doesnt have 'skip_rows' or smth in the likes
data = np.fromfile("Speech_without_header.txt", dtype='<f4').reshape(138,80)

# 'plasma' is the colormap that is seen in the question's image, see also these colormaps: https://matplotlib.org/examples/color/colormaps_reference.html
# setting origin='lowest' has the same effect than replacing np.transpose(Z) by np.transpose(Z)[::-1,]
# vmin, vmax give the scale. After briefly looking at the data we can understand that the limits are -5/2db
# extent gives the limits of the x-axis (here 0 to 138 units) and y-axis (0 to 80 units) (in this example I'm plotting the spectrogram of 138 dimensions with each dimension having 80 elements)
# if aspect='auto' is not set, the plot would be very thin and very high
# 
# Source: https://stackoverflow.com/questions/20069545/2d-plot-of-a-matrix-with-colors-like-in-a-spectrogram

plot.imshow(np.transpose(data), extent=[0,138,0,80], cmap='plasma',
           vmin=-5, vmax=2, origin='lowest', aspect='auto')
plot.colorbar()
plot.savefig("spectrogram_matplotlib.png", dpi=2000)
plot.show()

exit()

# %%
