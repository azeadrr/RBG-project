welcome="""
----------------------------------------------------------------------
Remove background by Azead
----------------------------------------------------------------------
"""
print(welcome)
from rembg import remove
import easygui
from PIL import Image

inputPath =easygui.fileopenbox(title='rem.jpg')
outputPath=easygui.filesavebox(title='rem.png')
input = Image.open(inputPath)
output = remove(input)
output.save(outputPath)