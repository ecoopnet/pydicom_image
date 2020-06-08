import pydicom
from pydicom import dcmread
from pydicom.pixel_data_handlers.util import apply_voi_lut

#def get_window_set(dcm):
#  cs = dcm['WindowCenter'].value
#  ws = dcm['WindowWidth'].value
#  return [(cs[x],ws[x]) for x in range(len(cs))]

def set_window(dcm, c,w):
   dcm['WindowCenter'].value = c
   dcm['WindowWidth'].value = w

# https://www.kaggle.com/dcstang/see-like-a-radiologist-with-systematic-windowing
def window_image(img, window_center,window_width, intercept, slope, rescale=True):
    img = (img*slope +intercept)
    img_min = window_center - window_width//2
    img_max = window_center + window_width//2
    img[img<img_min] = img_min
    img[img>img_max] = img_max

    if rescale:
        # Extra rescaling to 0-1, not in the original notebook
        img = (img - img_min) / (img_max - img_min)

    return img

def get_first_of_dicom_field_as_int(x):
    #get x[0] as in int is x is a 'pydicom.multival.MultiValue', otherwise get int(x)
    if type(x) == pydicom.multival.MultiValue:
        return int(x[0])
    else:
        return int(x)

def get_windowing(data):
    dicom_fields = [data[('0028','1050')].value, #window center
                    data[('0028','1051')].value, #window width
                    data[('0028','1052')].value, #intercept
                    data[('0028','1053')].value] #slope
    return [get_first_of_dicom_field_as_int(x) for x in dicom_fields]

