#encoding: utf-8
import sys #para operaciones sobre el sistema
from inspect import getargspec #para reflexión: http://docs.python.org/library/inspect.html


def search(linea, criterio):
    if criterio in linea:
        #aquí usamos formato con nombres, es más explícito que el formato que ya conocíamos
        print "Encontrado '%(criterio)s' en '%(linea)s'" % {'criterio': criterio, 'linea': linea.strip()}
    return linea

def replace(linea, original, reemplazo):
    if original in linea:
        print "reemplazando %s por %s en %s" % (original, reemplazo, linea)
        return linea.replace(original, reemplazo)
    return linea

def copy(linea):
    return linea

#construimos un diccionario con las operaciones posibles
operaciones = {'copiar': copy,
               'reemplazar': replace,
               'buscar': search,
              }

def operar_en_archivo(nombre_de_archivo, operacion="copiar", *args):
    archivo = open(nombre_de_archivo)
    salida  = open("copy_"+nombre_de_archivo, 'w') #lo abrimos en modo write (escritura)
    for linea in archivo:
        #aplicamos la operacion
        if operacion in operaciones:
            salida.write(operaciones[operacion](linea, *args))
        else:
            salida.write(linea)
def usage(script, operation, params):
    print "python %s archivo %s %s" % (script, operation, " ".join([e for e in params if e != "linea"]))

#esta técnica se usa para sólo correr el módulo cuando se ejecuta directamente, en lugar de hacerlo siempre
if __name__ == "__main__":
    #argv es la lista de argumentos que el módulo recibe: http://docs.python.org/library/sys.html
    #argv[0] es el nombre de este script
    #a diferencia de java, argv ya es algo fijo, no arbitrario
    print "bienvenido al operador de archivos %s" %sys.argv[0]
    if len(sys.argv) > 2:
        print "elegiste ejecutar la operación %s" % sys.argv[2] 
        operar_en_archivo(sys.argv[1], *sys.argv[2:]) 
    else:
        print "Uso:\n\t%s archivo [parámetros]" % sys.argv[0]
        print "por ejemplo:"
        for key,value in operaciones.items():
            usage(sys.argv[0], key, getargspec(value)[0])

        

    

