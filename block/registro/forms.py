from django.forms import Form, EmailField ,CharField, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class CustomUserCreationForm(UserCreationForm):
    email = EmailField()
    password1 = CharField(label='Contraseña',widget = PasswordInput)
    password2 = CharField(label=' Reetir la contraseña',widget = PasswordInput)
    
    class Meta:
        model= User
        fields = ["username","email","password1","password2"]
        help_texts = {k: "" for k in fields}
        
        
    

class UserEditForm(UserCreationForm):
    email = EmailField()
    password1 = CharField(label='Contraseña',widget = PasswordInput)
    password2 = CharField(label=' Reetir la contraseña',widget = PasswordInput)
    
    class Meta:
        model= User
        fields = ["email","password1","password2"]
        help_texts = {k: "" for k in fields}