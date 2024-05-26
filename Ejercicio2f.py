from interpreter import draw
from chessPictures import *

a=(Picture(SQUARE).join(Picture(SQUARE).negative())).horizontalRepeat(4)
b=a.negative()
b=b.up(a).verticalRepeat(2)
draw(b)