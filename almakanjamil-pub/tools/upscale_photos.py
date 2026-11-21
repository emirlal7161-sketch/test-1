import sys
from PIL import Image, ImageFilter
d = sys.argv[1]
for name, f in [("salon-east-park", 1.6), ("chambre-toub-ramli", 1.5), ("video-compound", 1.7), ("iphone-16-pro-max", 1.6), ("video-couloir", 1.5), ("video-porte", 1.5)]:
    im = Image.open(f"{d}/{name}.jpg").convert("RGB")
    up = im.resize((round(im.width*f), round(im.height*f)), Image.LANCZOS)
    up = up.filter(ImageFilter.UnsharpMask(radius=1.6, percent=70, threshold=2))
    up.save(f"{d}/{name}@hd.jpg", quality=93)
    print(name, up.size)
