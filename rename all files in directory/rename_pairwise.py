
# In case you have same but long/complex named A and B but you want their names to be simpler


folder_A	=	'path'
folder_B	=	'path'


# for rename
import os

# to list name of files and directories
from os import walk

walked = []

for (all) in walk (folder_A):
    walked.extend(all)
    

filenames = walked[2]

count = 1

for old_name in filenames:
  image_a = folder_A + "\\"
  image_b  = folder_B + "\\"
  new     = str(count)   + ".jpg"
  os.rename( image_a + old_name, image_a + new )
  os.rename( image_b + old_name, image_b + new )
  count+=1
