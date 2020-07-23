# Andrea Abril Palencia Gutierrez, 18198
# SR3: modelo Obj --- Graficas por computadora, seccion 20
# 20/07/2020 - 27/07/2020

from gl import Render

from obj import Obj 

r = Render(800,800)


r.loadModel('./models/PrimroseP.obj', (400,200), (700,700))
#r.loadModel('./models/face.obj', (0,0 ), (1,1) )


r.glFinish('modelo_obj.bmp')