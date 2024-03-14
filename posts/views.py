from django.shortcuts import render
from .models import Post
from django.core.mail import send_mail

def contatti(request):
    if request.method == 'POST':
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        message = request.POST['message']
        
        send_mail(
            message_name,
            message,
            message_email,
            ['reinad2510@gmail.com', 'sandbox.smtp.mailtrap.io']
        )
        
        return render(request, 'contatti.html', {'message_name': message_name})
    else:
        return render(request, 'contatti.html')