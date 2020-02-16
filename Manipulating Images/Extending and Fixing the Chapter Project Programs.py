import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

for filename in os.listdir('.'):
    if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg') or filename.lower().endswith('.gif') or filename.lower().endswith('bmp')) or filename == LOGO_FILENAME:
        continue

    im = Image.open(filename)
    width, height = im.size

    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
            
    print('Resizing %s...' % (filename))
    im = im.resize((width, height))

    if width < logoWidth*2 or height < logoHeight*2:
        print("The logo will not fit %s file"%filename)
    else:
        print('Adding logo to %s...' % (filename))
        im.paste(logoIm, (width-logoWidth, height-logoHeight), logoIm)

    im.save(os.path.join('withLogo', filename))
