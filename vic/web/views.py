from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def send_msg(name, surname, email, phone):
    subject = f"Запрос с сайта"
    body = f"""Заявка от клиента {name} 

    Имя: {name}
    Фамилия: {surname}
    Телефон: {phone}
    E-mail: {email}
    
    """
    send_mail(
        subject, body, email, ["vic.gnrl@gmail.com", ],
    )


# Главная страница
def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                send_msg(form.cleaned_data['first_name'],
                         form.cleaned_data['last_name'],
                         form.cleaned_data['email'],
                         form.cleaned_data['phone_number'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            return redirect('web:web_main')
    form = ContactForm()
    return render(request, 'web/index.html', {'form': form})

