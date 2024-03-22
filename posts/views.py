from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import get_template
from django.contrib import messages
from decouple import config


def contatti(request):
    if request.method == 'POST':
        message_name = request.POST.get('message_name')
        message_email = request.POST.get('message_email')
        message = request.POST.get('message')

        try:
            from_email = config('MY_EMAIL_HOST_USER')

            send_mail(
                message_name,
                "Ciao " + message_name + ", la tua email è " + message_email + ". Il messaggio è stato ricevuto con successo.",
                message_email,
                [message_email]
            )

            template = get_template('email_template.html')
            context = {'message_name': message_name, 'message_email': message_email, 'message': message}
            email_content = template.render(context)

            send_mail(
                'Nuovo messaggio dal modulo di contatto',
                email_content,
                from_email,
                [from_email],
                html_message=email_content
            )

            messages.success(request, 'Messaggio inviato con successo!, Controlla la tua email')

        except Exception as e:
            messages.error(request, 'Si è verificato un errore durante l\'invio del messaggio. Riprova più tardi.')

        return redirect('/')

    else:
        return render(request, 'contatti.html')
