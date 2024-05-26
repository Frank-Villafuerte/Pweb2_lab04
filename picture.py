from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    vertical = []
    for value in self.img:
      vertical.append(value[::-1])
    return Picture(vertical)

  def horizontalMirror(self):
    horizontal = []
    for i in range(len(self.img)):
      horizontal.append(self.img[len(self.img)-i-1])
        
    return Picture(horizontal)

  def negative(self):
    negativo=[]
    linea=""
    for i in range(len(self.img)):
        for j in range(len(self.img[i])):
            if self.img[i][j]=='#' or self.img[i][j]==" ":
                linea+=self.img[i][j]
            else:
                linea+=self._invColor(self.img[i][j])
        negativo.append(linea)
        linea=""
    return Picture(negativo)

  def join(self, p):
    unido=[]
    linea=""
    for i in range(len(p.img)):
        linea=self.img[i]
        for j in range(len(p.img[i])):
          linea+=p.img[i][j]
        unido.append(linea)
    return Picture(unido)

  def up(self, p):
    arriba=p.img
    for i in range(len(self.img)):
      arriba.append(self.img[i])
    return Picture(arriba)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    sobre=[]
    for i in range(len(p.img)):
        linea=""
        for j in range(len(p.img[i])):
            if p.img[i][j]== ' ':
                linea+=self.img[i][j]
            else:
                linea+=(p.img[i][j])
        sobre.append(linea)
        
    return Picture(sobre)
  
  def horizontalRepeat(self, n):
    repeticionH=self
    for i in range(n-1):
      repeticionH=repeticionH.join(self)
    return repeticionH

  def verticalRepeat(self, n):
    repeticionV=[]
    for i in range(n):
      for line in self.img:
         repeticionV.append(line)
    return Picture(repeticionV)
 
  def rotate(self):
    rotado=[]
    for i in range(len(self.img)):
      linea=""
      for j in range(len(self.img[i])):
        linea+=self.img[j][i]    
      rotado.append(linea)
    
    return Picture(rotado).horizontalMirror()

