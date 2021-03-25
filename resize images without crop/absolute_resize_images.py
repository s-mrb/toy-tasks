from PIL import Image
from resizeimage import resizeimage


# folder_A is folder with images of A category
# folder_B is folder with images of B category
# ofolder_A is folder where resized A will be stored
# ofolder_B is folder where resized B will be stored


folder_A	=	'path'
folder_B	=	'path'



ofolder_A	=	'path'
ofolder_B	=	'path'

# to list name of files and directories
from os import walk

walked = []
row = float('inf')
col = float('inf')

for (all) in walk (folder_A):
    walked.extend(all)
    

filenames = walked[2]

for img_name in filenames:
	img_A 	= 	open( folder_A + '\\' + img_name, 'rb' )  
		
	img_A 	=	Image.open( img_A )

	s_A		=	img_A.size

	row		=	s_A[0] if (s_A[0] < row) else row
	col		=	s_A[1] if (s_A[1] < col) else col


	img_A.close()


filenames=[]
walked=[]

for (all) in walk (folder_B):
    walked.extend(all)
    

filenames = walked[2]

for img_name in filenames:
	img_B 	= 	open( folder_B + '\\' + img_name, 'rb' )  
		
	img_B 	=	Image.open( img_B )

	s_B		=	img_B.size

	row		=	s_B[0] if (s_B[0] < row) else row
	col		=	s_B[1] if (s_B[1] < col) else col


	img_B.close()


	for img_name in filenames:
		img_A 	= 	open( folder_A + '\\' + img_name, 'rb' )  
		img_B	=	open( folder_B + '\\' + img_name, 'rb' )
			
		img_A 	=	Image.open( img_A )
		img_B 	=	Image.open( img_B )



		img_A 	= 	resizeimage.resize_contain(img_A, [row, col])

		img_B 	= 	resizeimage.resize_contain(img_B, [row, col])

		##img_A 	=	img_A.convert("RGBA")

		# NOTE: keep it PNG for ML
		img_A.save(ofolder_A + '\\' + img_name[0:len(img_name)-3]+'PNG', img_A.format)
		img_B.save(ofolder_B + '\\' + img_name[0:len(img_name)-3]+'PNG', img_B.format)

		img_A.close()
		img_B.close()
