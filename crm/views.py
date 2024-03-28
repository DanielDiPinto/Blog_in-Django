from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginFrom
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.messages import error


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. You can now login.")
            return redirect("my-login")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

    context = {'registerform': form}
    return render(request, 'crm/register.html', context=context)




def my_login(request):
    form = LoginFrom()
    if request.method == 'POST':
        form = LoginFrom(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                messages.success(request, "Sei dentro")
                return redirect("/")
            else:
                messages.error(request, "errore")
            
    context = {'loginform':form}
    
    return render(request, 'crm/my-login.html', context=context)

def user_logout(request):
    auth.logout(request)
    return redirect("/")

@login_required(login_url="my-login")
def dashboard(request):
    if request.user.is_staff:
        users = User.objects.all()
        context = {'users': users}
        return render(request, 'crm/dashboard.html', context=context)
    else:
        return redirect(request, '/')



@login_required
def delete_user(request, user_id):
  user = User.objects.get(pk=user_id)
  if request.user.is_staff and user != request.user:
    user.delete()
    messages.success(request, "Utente eliminato correttamente.")
  else:
    messages.error(request, "Non hai il permesso di eliminare questo utente.")
  return redirect('dashboard')
