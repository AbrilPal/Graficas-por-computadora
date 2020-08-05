# Andrea Abril Palencia Gutierrez, 18198
# SR4: Flat Shading --- Graficas por computadora, seccion 20
# 27/07/2020 - 04/08/2020

from gl import Render
from obj import Obj 

modelo = Render(800,800)

modelo.Model('./models/PrimroseP.obj', (400,200), (700,700))
modelo.glFinish('modelo_obj.bmp')
print("¡Listo! La imagen esta creada con el nombre de 'modelo_obj.bmp'.")