from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from accounts.models import Profile


def register_view(request):
    error = None

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = request.POST['e-mail']
            user.save()
            
            Profile.objects.create(
                user=user,
                gender=request.POST['gender'],
                phone='+82'+request.POST['phone'],
                institution=request.POST['institution']
            )

            login(request, user)
            return redirect('/accounts/profile')
        error = 'Wrong ID or Password mismatch'
    
    return render(request, 'registration/register.html', {'error': error})


@login_required
def profile_view(request):
    return render(request, 'registration/profile.html')


@login_required
def delete_account_view(request):
    if request.method == 'POST':
        if request.user.username == request.POST['username']:
            return redirect('delete_account_done')
    return render(request, 'registration/delete_account.html')


@login_required
def delete_account_done_view(request):
    User.objects.get(username=request.user.username).delete()
    return render(request, 'registration/delete_account_done.html')