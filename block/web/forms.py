from  django.forms import Form, CharField, DateField

# Formulario de busqueda

class Busqueda(Form):
    buscar = CharField(max_length=150)
    
class FormularioPosteo(Form):

    titulo = CharField()
    contenido = CharField()
    fecha_publicacion = DateField()