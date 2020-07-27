# Andrea Abril Palencia Gutierrez, 18198
# SR3: modelo Obj --- Graficas por computadora, seccion 20
# 20/07/2020 - 27/07/2020

from gl import Render
from obj import Obj 

modelo = Render(800,800)

modelo.Model('./models/PrimroseP.obj', (400,200), (700,700))
modelo.glFinish('modelo_obj.bmp')
print("¡Listo! La imagen esta creada con el nombre de 'modelo_obj.bmp'.")