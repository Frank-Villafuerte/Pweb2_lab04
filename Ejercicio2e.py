from interpreter import draw
from chessPictures import *

a=(Picture(SQUARE).negative().join(Picture(SQUARE))).horizontalRepeat(4)
draw(a)