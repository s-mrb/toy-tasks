from cairosvg import svg2png

import os
from os import walk

input = ""
output = ""

files = []
for (all) in os.walk(input):
  files.extend(all)

files = files[2]
name = ""
code = ""
code_flag = False

for f in files:
  with open(input+f,'r') as smiles:
    for line in smiles:
      if line[0:3]=="db:":
        tok = line.split()
        db  = tok[1].split('.')[0]
        no  = tok[3]
        name = db + "_" + no
        continue

      if line[0:3]=='"""':
          if code_flag:
              code_flag = False

              svg2png(bytestring=code, write_to=output+name+".png")


              code = ""
              name = ""
              continue


      if line[0:3]=='"""':
          code_flag = True
          continue

      if code_flag:
          code += line


