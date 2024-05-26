from interpreter import draw
from chessPictures import *

a=(Picture(SQUARE).join(Picture(SQUARE).negative())).horizontalRepeat(4)
b=a.negative()
peones=Picture(PAWN).horizontalRepeat(8)
grandes=Picture(ROCK).join(Picture(KNIGHT)).join(Picture(BISHOP)).join(Picture(QUEEN)).join(Picture(KING)).join(Picture(BISHOP)).join(Picture(KNIGHT)).join(Picture(ROCK))
negras=b.under(peones.negative()).up(b.negative().under(grandes.negative()))
blancas=b.under(grandes).up(b.negative().under(peones))
tablero=blancas.up(b.up(b.negative()).verticalRepeat(2)).up(negras)
draw(tablero)