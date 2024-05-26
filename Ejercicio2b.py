from interpreter import draw
from chessPictures import *


a=(Picture(KNIGHT).negative().verticalMirror().join(Picture(KNIGHT).verticalMirror())).up(Picture(KNIGHT).join(Picture(KNIGHT).negative()))
draw(a)