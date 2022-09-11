

from django.forms import Form, PasswordInput, EmailField,CharField,ModelForm,Textarea,ImageField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post

class UserRegisterForm(UserCreationForm):
    email = EmailField()
    password1 = CharField(label='Contraseña',widget=PasswordInput)
    password2 = CharField(label='Confirma Contraseña',widget=PasswordInput)
    
    class Meta: 
        model = User
        fields = ['username','email','password1','password2']
        help_text = {k:"" for k in fields}
        
        
class PostForm(ModelForm):
    content = CharField(label='',widget=Textarea(attrs={'rows':2, 'placeholder':'¿Que estas pensando?'}),required=True)
    
    class Meta:
        model = Post
        fields = ['content']
    
class UserEditForm(UserCreationForm):
    email = EmailField()
    password1 = CharField(label='Contraseña',widget = PasswordInput)
    password2 = CharField(label=' Reetir la contraseña',widget = PasswordInput)
    
    class Meta:
        model= User
        fields = ["email","password1","password2"]
        help_texts = {k: "" for k in fields} 
        
        
class AvatarForm(Form):
    imagen = ImageField()
    