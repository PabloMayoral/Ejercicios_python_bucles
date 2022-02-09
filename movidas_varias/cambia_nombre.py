import glob
import os

j=0

path = 'C:/Users/Pablo Martin/Documents/movidas_python/images/'
for i, filename in enumerate(glob.glob(path + '*.jpg')):
    os.rename(filename, os.path.join(path, 'img_' + str(i+j) + '.jpg'))

path = 'C:/Users/Pablo Martin/Documents/movidas_chulas/carrousel3D+musica_fondo/img/'
for i, filename in enumerate(glob.glob(path + '*.png')):
   os.rename(filename, os.path.join(path, 'img_' + str(i+j) + '.png'))

