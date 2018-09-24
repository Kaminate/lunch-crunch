import glob

imagefilepaths = []
imagefilepaths += glob.glob( "*.png" )
imagefilepaths += glob.glob( "*.jpg" )
imagefilepaths.sort()

def writeline( file, line ):
  file.write( line )
  file.write( "\n" )
  return

file = open( "readme.md", 'w' )
writeline( file, "This file is autogenerated from generate_readme.py" )
for imagefilepath in imagefilepaths:
  writeline( file, "![](" + imagefilepath + ")" )
file.close()
