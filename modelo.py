# Andrea Abril Palencia Gutierrez, 18198
# SR5: Textures --- Graficas por computadora, seccion 20
# 04/08/2020 - 10/08/2020

from gl import Render
from obj import Obj 

modelo = Render(3000,3000)
modelo.loadModel('./models/earth.obj', (500, 500, 0), (1, 1, 1))
modelo.glFinish('modelo_obj.bmp')
modelo.glZBuffer('zbuffer.bmp')
print("¡Listo! La imagen esta creada con el nombre de 'modelo_obj.bmp'.")