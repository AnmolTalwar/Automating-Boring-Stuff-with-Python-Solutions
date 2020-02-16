import os
from PIL import Image


for foldername, subfolders, filenames in os.walk('C:\\'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    
    for filename in filenames:
        
        if not filename.endswith((".png",".jpg")):
            numNonPhotoFiles+= 1
            continue

        else:
            try:
                photo = Image.open(os.path.join(foldername, filename))
                height, width = photo.size
                if height and width > 500:
                    numPhotoFiles+= 1
                else:
                    numNonPhotoFiles+= 1
            except OSError:
                numNonPhotoFiles+= 1
            

    if numPhotoFiles > numNonPhotoFiles:
        print("Path of the Folder you are looking for is: %s"%os.path.join(foldername))

    

   
