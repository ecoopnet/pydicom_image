from .core_functions import *
import pydicom
import numpy as np

# Convert DICOM pixel array to windowed pixel array.
# If window is None, default first window center/width of input DICOM.
# filepath or dcm: DICOM filepath or loaded DICOM instance (with pydicom). Only one of them is required.
# window: Tuple of (window_center, window_width).
def dcm2img(filepath=None, dcm=None, window=None):
      if (not filepath and not dcm) or (filepath and dcm):
          raise Exception("Only one of filepath/dcm is required.")
      if filepath:
          dcm = pydicom.dcmread(filepath)

      img = dcm.pixel_array
      window_center, window_width, intercept, slope = get_windowing(dcm)
      c = window_center if not window or window[0] == None else window[0]
      w = window_width  if not window or window[1] == None else window[1]
      return (window_image(img, c, w, intercept, slope) * 255.0).astype(np.uint8)

