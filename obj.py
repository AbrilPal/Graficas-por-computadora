# Andrea Abril Palencia Gutierrez, 18198
# SR6: Transformations --- Graficas por computadora, seccion 20
# 17/08/2020 - 24/08/2020

# carga de archivo obj
class Obj(object):
    def __init__(self, filename):
        # leer el archivo obj
        with open(filename, 'r') as file:
            self.lines = file.read().splitlines()
        self.vertices = []
        self.normals = []
        self.texcoords = []
        self.faces = []
        self.read()

    def read(self):
        for line in self.lines:
            # esto depende del modelo, porque no todos tienen la misma estructura
            if line:
                prefix, value = line.split(' ', 1)
                if prefix == 'v': # vertices
                    self.vertices.append(list(map(float,value.split(' '))))
                elif prefix == 'vn':
                    self.normals.append(list(map(float,value.split(' '))))
                elif prefix == 'vt':
                    self.texcoords.append(list(map(float,value.split(' '))))
                elif prefix == 'f':
                    self.faces.append([list(map(int,vert.split('/'))) for vert in value.split(' ')])

