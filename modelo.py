# Andrea Abril Palencia Gutierrez, 18198
# SR4: Flat Shading --- Graficas por computadora, seccion 20
# 27/07/2020 - 04/08/2020

from gl import Render
from obj import Obj 

modelo = Render(2000,2000)
modelo.loadObjModel('./models/PrimroseP.obj', (1000, 500, 0), (1600, 1600, 1600))
modelo.glFinish('modelo_obj.bmp')
modelo.glZBuffer('outputZbuffer.bmp')
print("¡Listo! La imagen esta creada con el nombre de 'modelo_obj.bmp'.")