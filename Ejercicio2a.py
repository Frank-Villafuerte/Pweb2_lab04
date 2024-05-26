from interpreter import draw
from chessPictures import *


a=(Picture(KNIGHT).negative().join(Picture(KNIGHT))).up(Picture(KNIGHT).join(Picture(KNIGHT).negative()))
draw(a)
