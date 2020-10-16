from django.core.mail import EmailMessage
from django.shortcuts import render


def index(request):

    email = EmailMessage(
        request.POST.get('subject'),
        request.POST.get('message'),
        from_email = request.POST.get('email'),
        to = ['luiz-fernando@outlook.com'],
    )
    file = request.FILES['anexo']
    email.attach(file.name, file.read(), file.content_type)
    email.send()

    return render(request, 'core/index.html')
