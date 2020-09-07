# Andrea Abril Palencia Gutierrez, 18198
# SR6: Transformations --- Graficas por computadora, seccion 20
# 17/08/2020 - 24/08/2020

from gl import Render
from obj import Obj 
from textura import Texture


modelo = Render(800,800)
textura = Texture('./models/model.bmp')
posModel = ( 0, 0, 3)
modelo.lookAt(posModel, (-2, -2, -0.25))
# modelo.loadModel('./models/model.obj', posModel, (1,1,1),(0,0,0))
modelo.loadModel('./models/model.obj', posModel, (1, 1, 1), textura, (0, 0, 1))
modelo.glFinish('modelo_obj.bmp')
print("¡Listo! La imagen esta creada con el nombre de 'modelo_obj.bmp'.")