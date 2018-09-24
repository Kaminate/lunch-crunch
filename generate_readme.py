import glob

imagefilepaths = []
imagefilepaths += glob.glob( "*.png" )
imagefilepaths += glob.glob( "*.jpg" )
imagefilepaths.sort()

file = open( "readme.md", 'w' )
for imagefilepath in imagefilepaths:
  file.write( "![](" + imagefilepath + ")" )
  file.write( "\n" )
    
# foreach( "![]()" )
file.close()
