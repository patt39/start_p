from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get_response('username')
            messages.success(request, f'account created for {username}!')
            return redirect('darry-home')
        else:
            form = UserCreationForm()
            {'form': form}
    return render(request, 'users/register.html')



