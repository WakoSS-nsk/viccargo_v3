from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(initial='Имя', max_length=50)
    email = forms.EmailField(initial='E-mail', max_length=150)
    phone_number = forms.CharField(initial='Телефон', max_length=10)
