from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from service_main.models import Study


@login_required
def join_request_study(request):
    if request.method == 'POST':
        return render(request, 'service/request_list.html')
    return render(request, 'service/join_request_form.html')


@login_required
def create_study(request):
    if request.method == 'POST':
        Study.objects.create(
            title=request.POST['study-title'],
            deposit=request.POST['study-deposit'],
            description=request.POST['study-description'],
            admin=request.user,
        )
        return redirect('study_list')
    return render(request, 'service/create_study.html')


@login_required
def list_study(request):
    if request.method == 'POST':
        # Search result
        study_list = {
            'study_list': Study.objects.filter(
                title=request.POST['search-study'],
            )
        }
    else:
        study_list = {
            'study_list': Study.objects.all()
        }

    return render(request, 'service/lobby.html', study_list)