#!/usr/bin/env python

import ..pydicom_image
from pydicom import dcmread

import cv2

dcm = dcmread('path/to/dcmfile')

# Load windowed image from pre-loaded dcm with windowCenter=45, windowWidth=350.
img = pydicom_image.dcm2img(dcm=dcm, window=(45, 350))
# Or directly pass DICOM filepath.
# img = pydicom_image.dcm2img(filepath='path/to/dcmfile', window=(45, 350))
# If window was omitted, it uses the first window center/width in the DICOM.
# img = pydicom_image.dcm2img(dcm=dcm)

print(img.min(), img.max()) # i.e. 0.0, 255.0 (the image is not normalized.)
print(img.shape) # 512, 512

# ----
# Save image to file.

# By matplotlib.pyplot (as grayscale)
import matplotlib
matplotlib.use('Agg') # -----(1)
import matplotlib.pyplot as plt
plt.imsave('pyplot.png',img, cmap='gray')

# By OpenCV2
cv2.imwrite('cv2.png', img)
