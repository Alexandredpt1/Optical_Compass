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

fig, axs = plt.subplots(2, 2, figsize=(15, 15))

# Display the original images I0, I45, I90, I135
axs[0,0].imshow(I0, cmap='gray')
axs[0,0].set_title('I0 Image')
axs[0,1].imshow(I45, cmap='gray')
axs[0,1].set_title('I45 Image')
axs[1,0].imshow(I90, cmap='gray')
axs[1,0].set_title('I90 Image')
axs[1,1].imshow(I135, cmap='gray')
axs[1,1].set_title('I135 Image')

plt.show()