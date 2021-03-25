from PIL import Image
from resizeimage import resizeimage


folder_A	=	'path'
# folder_B	=	'sss'

# ofolder_A	=	'ss'
ofolder_A	=	'path'

# to list name of files and directories
from os import walk

walked = []

for (all) in walk (folder_A):
    walked.extend(all)
    
# print(walked)
# exit(1)
filenames = walked[2]

for img_name in filenames:
	img_A 	= 	open( folder_A + '\\' + img_name, 'rb' )
	# img_B	=	open( folder_B + '\\' + img_name, 'rb' )
		
	img_A 	=	Image.open( img_A )
	# img_B 	=	Image.open( img_B )

	s_A		=	img_A.size
	# s_B		=	img_B.size

	row		=	256
	col		=	256

	img_A 	= 	resizeimage.resize_contain(img_A, [row, col])

	# img_B 	= 	resizeimage.resize_contain(img_B, [row, col])

	##img_A 	=	img_A.convert("RGBA")

	img_A.save(ofolder_A + '\\' + img_name[0:len(img_name)-3]+'PNG', img_A.format)
	# img_B.save(ofolder_B + '\\' + img_name[0:len(img_name)-3]+'PNG', img_B.format)

	img_A.close()
	# img_B.close()

