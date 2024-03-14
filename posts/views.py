from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib import messages

def contatti(request):
    if request.method == 'POST':
        nome = request.POST.get('nome', '')
        email = request.POST.get('email', '')
        testo = request.POST.get('testo', '')

        # Compila il file HTML con i dati forniti dall'utente
        html_content = render_to_string('email_template.html', {'nome': nome, 'email': email, 'testo': testo})

        # Invia l'email
        send_mail(
            'Oggetto dell\'email',
            '',
            'mittente@example.com',
            ['destinatario@example.com'],
            html_message=html_content,
        )

        messages.success(request, 'Email inviata con successo!')

        # Reindirizza l'utente alla home
        return redirect('/')  # Assicurati che 'home' sia il nome del percorso della tua home page nel file urls.py

    return render(request, 'contatti.html')
