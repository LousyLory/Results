from PIL import Image
from glob import glob
import os
from tqdm import tqdm

dump_dir = 'FRCNN'

if not os.path.isdir('../'+dump_dir):
	os.mkdir('../'+dump_dir)
else:
	pass

path_ = '../'+dump_dir+'/img/'
if not os.path.isdir(path_):
	os.mkdir(path_)
else:
	pass

for files in tqdm(glob('../../current_results/*')):
	_,_,filename = files.rpartition('/')
	filename,_,_ = filename.rpartition('.')
	im = Image.open(files)
	im = im.convert('RGB')
	im.save(path_+filename+'.jpg', quality=10)