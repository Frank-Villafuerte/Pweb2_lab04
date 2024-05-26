from interpreter import draw
from chessPictures import *

a=(Picture(SQUARE).join(Picture(SQUARE).negative())).horizontalRepeat(4)
draw(a)