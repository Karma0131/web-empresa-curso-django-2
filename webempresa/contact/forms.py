from django import forms

class ContactForm(forms.Form):
    name =forms.CharField(label='Nombre', required=True, widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Escribe tu nombre'}
    ))
    email = forms.EmailField(label='Correo electónico', required=True, widget=forms.EmailInput(
        attrs={'class':'form-control','placeholder':'escribe@tu.correo'}
        ))
    content = forms.CharField(label='Mensaje', required=True, widget=forms.Textarea(
        attrs={'class':'form-control','placeholder':'Escribe tu mensaje','rows':4}
        ))

    pass