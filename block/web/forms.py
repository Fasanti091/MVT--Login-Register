from  django.forms import Form, CharField

# Formulario de busqueda

class Busqueda(Form):
    buscar = CharField(max_length=150)
    
