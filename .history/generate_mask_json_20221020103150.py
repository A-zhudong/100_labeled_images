import numpy as np
import base64
import json, os

def generate_coords_from_points(txtpath, name):
    coords = []
    with open(os.path.join(txtpath,name), 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.split(',')
            coords.append([float(line[1]),float(line[0])])
    coords = np.array(coords)
    return coords

r = 2; label = 'O3'
img_path = '/hardisk/image_process/100images/100images_png/high_quality_100/0004_crop.png'
img_encoded = base64.b64encode(open(img_path, "rb").read())
print(img_encoded)
jpath = '/hardisk/image_process/100images/100images_png/high_quality_100/0004_crop.json'
jsonproto = {
  "version": "3.16.7",
  "flags": {},
  "shapes": [],
  "lineColor": [
    0,
    255,
    0,
    128
  ],
  "fillColor": [
    255,
    0,
    0,
    128
  ],
  "imagePath": "0004_crop.png",
  "imageData": '',
  "imageHeight": 512,
  "imageWidth": 512
}
shape_proto = {
      "label": "O3",
      "line_color": None,
      "fill_color": None,
      "points": [
        [
          461.039408866995,
          322.66009852216746
        ],
        [
          462.51724137931024,
          326.1083743842364
        ]
      ],
      "shape_type": "circle",
      "flags": {}
    }
shape_proto['points'] = [[461.039408866995, 322.66009852216746], 
                         [462.51724137931024, 326.1083743842364]]
shape_proto['label'] = 'O1'
jsonproto['shapes'] = shape_proto
# print(jsonproto['shapes'])

with open('test.json', 'w') as wf:
    json.dump(jsonproto, wf)

with open('test.json', 'r') as rf:
    load_json = json.load(rf)
    print(load_json['shapes'])