# Pillow: redimensionando imagens com Python
# Essa biblioteca é o Photoshop do Python 😂
from logging import root
from PIL import Image
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / 'original.jpeg'
NEW_IMAGE = ROOT_FOLDER / 'new.jpeg'

pil_image = Image.open(ORIGINAL)
width, height = pil_image.size
exif = pil_image.info['exif']
# print(exif)
 
new_width = 640
new_height = round(height * new_width / width)

new_image = pil_image.resize(size=(new_width, new_height))
new_image.save(
    NEW_IMAGE,
    optimize=True,
    qualaity=70,
    exif=exif,
)
