"""   1

                                            RENAME ALL FILES IN A DIRECTORY

                                                                                                                                              """                            

# Rename all files in a directory

# for rename
import os

# to list name of files and directories
from os import walk   

# to get current working directory
import pathlib 

current_path  = pathlib.Path().absolute()


walked = []

# NOte : do not use append, extend here convert all elemenets of tuple into elements of list
for (all) in walk (current_path):
    walked.extend(all)
    

filenames = walked[2]

# path appended with filename in os.rename
path = walked[0]+'\\'

for old_name in filenames:
  # in case you need to just slice name
    new = old_name[:4]+'.jpg'
    os.rename ( path+old_name, path+new )
    



"""   

                                                         NAME

                                                                                                                                              """                            




"""   

                                                         NAME

                                                                                                                                              """                            




"""   

                                                         NAME

                                                                                                                                              """                            




"""   

                                                         NAME

                                                                                                                                              """                            




"""   

                                                         NAME

                                                                                                                                              """                            




"""   

                                                         NAME

                                                                                                                                              """                            



"""   

                                                         NAME

                                                                                                                                              """                            



"""   

                                                         NAME

                                                                                                                                              """                            



"""   

                                                         NAME

                                                                                                                                              """                            



"""   

                                                         NAME

                                                                                                                                              """                            



"""   

                                                         NAME

                                                                                                                                              """                            



"""   

                                                         NAME

                                                                                                                                              """                            



"""   

                                                         NAME

                                                                                                                                              """                            






"""   

                                                         NAME

                                                                                                                                              """                            



"""   

                                                         NAME

                                                                                                                                              """                            


"""   

                                                         NAME

                                                                                                                                              """                            



"""   

                                                         NAME

                                                                                                                                              """                            
