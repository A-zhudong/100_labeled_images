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

r = 6; label = 'O3'
cropped_file = '0078_crop'
img_path = '/hardisk/image_process/100images/{}/{}.png'.format(cropped_file, cropped_file); img_name = cropped_file
txtpath = '/hardisk/image_process/100images/{}/'.format(cropped_file); name = f'{cropped_file}_pos_Gen1-noNoiseNoBackgroundSuperresolution.txt'
# jpath = '/hardisk/image_process/100images/100images_png/high_quality_100/0004_crop.json'

img_encoded = base64.b64encode(open(img_path, "rb").read()).decode('utf-8')
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
jsonproto['imageData'] = img_encoded
shapes = []
coords = generate_coords_from_points(txtpath, name).tolist()
for coord in coords:
    shape = shape_proto.copy()
    center = coord
    if coord[0]<r or abs(coord[0]-511)<r or coord[1]<r or abs(coord[1]-511)<r:
        r_now = min(coord[0], abs(coord[0]-511), coord[1], abs(coord[1]-511))
    else: r_now = r
    circle = [coord[0]-r_now, coord[1]]
    # print(r_now)
    shape['points'] = ([center, circle])
    shape['label'] = label
    shapes.append(shape)
jsonproto['shapes'] = shapes
# print(jsonproto['shapes'])

save_path = img_name+'.json'
with open(save_path, 'w') as wf:
    json.dump(jsonproto, wf)

with open(save_path, 'r') as rf:
    load_json = json.load(rf)
    print(load_json['shapes'][1])