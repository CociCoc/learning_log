
# Create your views here.
from django.contrib.auth import logout, login
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    logout(request)
    return redirect('/')

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Показати порожню форму реєстрації
        form = UserCreationForm()
    else:
        #Опрацювати заповнення
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Авторизувати користувача та скерувати його на головну сторінку
            login(request, new_user)
            return redirect('learning_logs:index')

    # Показати порожню або недійсну форму
    context = {'form': form}
    return render(request, 'registration/register.html', context)