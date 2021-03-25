from PIL import Image
from resizeimage import resizeimage
from PIL import Image



source_folder	=	'path'
destn_folder	=	'path'


# to list name of files and directories
from os import walk

def black_and_white(input_image_path,
    output_image_path):
   color_image = Image.open(input_image_path)
   bw = color_image.convert('L')
   bw.save(output_image_path)

if __name__ == '__main__':  

    walked = []

    for (all) in walk (source_folder):
        walked.extend(all)
        

    filenames = walked[2]

    for img_name in filenames:

        black_and_white(source_folder+ img_name,
            destn_folder+img_name)
