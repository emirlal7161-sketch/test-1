import sys, io, json, numpy as np, cv2
from PIL import Image, ImageCms
srgb = ImageCms.createProfile("sRGB")
def load(p):
    im = Image.open(p); icc = im.info.get("icc_profile"); im = im.convert("RGB")
    if icc: im = ImageCms.profileToProfile(im, ImageCms.ImageCmsProfile(io.BytesIO(icc)), srgb, outputMode="RGB")
    return im
def job(src, out, crop, holes, radius=12, pad=6):
    im = load(src); arr = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
    mask = np.zeros(arr.shape[:2], np.uint8)
    for (x0,y0,x1,y1) in holes: mask[y0-pad:y1+pad, x0-pad:x1+pad] = 255
    if holes: arr = cv2.inpaint(arr, mask, radius, cv2.INPAINT_TELEA)
    x0,y0,x1,y1 = crop; arr = arr[y0:y1, x0:x1]
    cv2.imwrite(out, arr, [cv2.IMWRITE_JPEG_QUALITY, 94]); print(out.split('/')[-1], arr.shape[1], 'x', arr.shape[0])
R, A = sys.argv[1], sys.argv[2]
job(R+'/09247-fiche.png', A+'/salon-east-park.jpg', (0,312,1284,1160), [(30,340,170,475),(965,340,1105,475),(1115,340,1255,475)])
job(R+'/09229-logements.png', A+'/chambre-toub-ramli.jpg', (52,614,1234,1349), [(1095,628,1220,750),(535,1270,750,1335)])
job(R+'/09257-recentes.png', A+'/iphone-16-pro-max.jpg', (52,332,615,897), [(482,350,602,468),(272,825,395,875)])
job(R+'/09257-recentes.png', A+'/video-porte.jpg', (668,331,1235,898), [])
job(R+'/09257-recentes.png', A+'/video-couloir.jpg', (51,1458,616,2024), [])
job(R+'/09257-recentes.png', A+'/video-compound.jpg', (668,1458,1235,2024), [])
job(R+'/09256-accueil.png', A+'/banniere-caire.jpg', (590,940,1232,1368), [])
