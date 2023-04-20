import numpy as np
import base64

r = 3; img_path  = 'a.png'
img_encoded = base64.b64encode(open(img_path, "rb").read())
