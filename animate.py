import os
import subprocess
#subprocess.run(['ls'])

cwd = os.getcwd()
mesh_path = cwd + '/img/'

folders = os.listdir(mesh_path)

for folder in folders:
	img_path = mesh_path + folder
	img_name = img_path + '/test_human-_*.jpg'
	animation_name =  cwd + '/animations/animate_test_human_' + folder + '.gif'
	delay = '-delay 15' 
	loop = '-loop 0'
	subprocess.run(['convert', img_name, animation_name])