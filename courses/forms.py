from django import forms


class ContactCourse(forms.Form):
    """docstring for ContactCourse"""
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(
        label='Mensagem', widget=forms.Textarea
    )
