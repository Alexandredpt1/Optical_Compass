import imageio.v2 as im
import numpy as np
import matplotlib.pyplot as plt

# Load the images and convert them from uint8 to int64
I0 = im.imread(r"C:\Users\stagiaire_biorob\Documents\Stage_Polarisation_UV\Logiciels\Traitement_image\0.tiff")
I0 = I0.astype(np.int64)
I45 = im.imread(r"C:\Users\stagiaire_biorob\Documents\Stage_Polarisation_UV\Logiciels\Traitement_image\45.tiff")
I45 = I45.astype(np.int64)
I90 = im.imread(r"C:\Users\stagiaire_biorob\Documents\Stage_Polarisation_UV\Logiciels\Traitement_image\90.tiff")
I90 = I90.astype(np.int64)
I135 = im.imread(r"C:\Users\stagiaire_biorob\Documents\Stage_Polarisation_UV\Logiciels\Traitement_image\135.tiff")
I135 = I135.astype(np.int64)

# Horizontal and vertical values
h, v = I0.shape

# Stokes parameters
S0 = (I0 + I45 + I90 + I135)/2 # Average value of total intensity
S01 = I0 + I90 # Total intensity
S02 = I45 + I135 # Total intensity

S1 = I0 - I90 # Vector of polarization in 0-90

S2 = I45 - I135 # Vector of polarization in 45-135


Z_global = (S1 + 1j * S2)/S0 # Global Stokes parameters
Z_global = Z_global * np.exp(2j * 19.8*np.pi/180) # Global Stokes parameters calibrated

dop = np.abs(Z_global) # Degree of Polarization

aopg = 1/2*np.angle(Z_global) # Global Angle of Polarization


# Pixel coordinates
# Make a column array 1 to v of shape v*1
column = np.arange(1, v+1)

# Make an array h*v by duplicating the previous column
matrix_x = np.tile(column, (h, 1))

# Make a row array 1 to h of shape 1*h
row = np.arange(1, h+1)

# Make an array h*v by duplicating the previous row
matrix_y = -1*np.tile(row.reshape(h, 1), v)

# Search the center of the image
x_centre = h/2
y_centre = -v/2

# Centering the pixel coordinates
matrix_x = matrix_x - x_centre
matrix_y = matrix_y - y_centre

# Matrix to calculate the local AOP
mat_azimut = np.angle(matrix_x + matrix_y * 1j)

Z_local = Z_global * np.exp(-2j*mat_azimut) # Local Stokes Parameters

#Local AOP
aopl = 1/2*np.angle(Z_local)



aopl_deg = aopl * 180/np.pi

new =0.5*(1- np.cos(2*aopl))

# Save matrices to CSV files
#np.savetxt("dop.csv", dop, delimiter=";")
#np.savetxt("aopg.csv", aopg, delimiter=";")
#np.savetxt("aopl.csv", aopl, delimiter=";")


# Plotting the results
fig, axs = plt.subplots(4, 1, figsize=(10, 10))

# Plot Local AoP
cax1 = axs[0].imshow(aopl_deg, cmap='hsv', vmin=-90, vmax=90)
fig.colorbar(cax1, ax=axs[0])
axs[0].set_title('Local Degree of Polarization (AoPL)')

# Plot Global AoP
cax2 = axs[1].imshow(aopg, cmap='hsv', vmin=-np.pi/2, vmax=np.pi/2)
fig.colorbar(cax2, ax=axs[1])
axs[1].set_title('Global Angle of Polarization (AoPG)')

# Plot DoP
cax2=axs[2].imshow(dop, cmap='rainbow',vmin=0,vmax=1)
axs[2].set_title('DOP')
fig.colorbar(cax2, ax=axs[2])

# Plot DoP
cax2=axs[3].imshow(new, cmap='gray',vmin=0,vmax=1)
axs[3].set_title('new')
fig.colorbar(cax2, ax=axs[3])

plt.show()