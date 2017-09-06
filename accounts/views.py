from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def register_view(request):
    return render(request, 'registration/register.html')


@login_required
def profile_view(request):
    return render(request, 'registration/profile.html')