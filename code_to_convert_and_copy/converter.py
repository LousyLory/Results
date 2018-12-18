from PIL import Image
from glob import glob
import os
from tqdm import tqdm
import shutil

dump_dir = 'SegLink_pretrained_ICDAR'

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

# copying necessary html/php files
src = '../root_htmls/'
dest = '../'+dump_dir+'/'
src_files = os.listdir(src)
for file_name in src_files:
    full_file_name = os.path.join(src, file_name)
    if (os.path.isfile(full_file_name)):
        shutil.copy(full_file_name, dest)
