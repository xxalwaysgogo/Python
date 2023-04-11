import os
import re
path = 'C:/Users/92898/Desktop/수업/1-1_지능제어/CHENMEICEN/Cats'
filelist = os.listdir(path)
for i,file in enumerate(filelist):
    # data = re.sub('[A-Za-z0-9\!\%\[\]\,\。\ ]', '', file)
    src = os.path.join(path, file)
    dst = os.path.join(os.path.abspath(path), 'Cats-'+(format(str(i+1), '0>2s')+'.jpg'))
    os.rename(src, dst)