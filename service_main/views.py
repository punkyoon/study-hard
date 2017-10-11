from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from study_hard import tool
from service_main.models import Study, StudyRequest


@login_required
def join_request_study(request, url):
    study = tool._get_study(url)
    if study is None or not tool._check_request_avaliable(study, request.user):
        return redirect('study_list')
    
    StudyRequest.objects.create(study=study, user=request.user)
    return redirect('my_study')


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
def my_study(request):
    study_list = {
        'manage_study_list': tool._get_study_list(request.user, 'manage'),
        'belong_study_list': tool._get_study_list(request.user, 'belong'),
        'requested_study_list': tool._get_study_list(request.user, 'requested'),
    }

    return render(request, 'service/my_study.html', study_list)


@login_required
def list_study(request):
    if request.method == 'POST':
        # Search result
        study_list = {
            'study_list': Study.objects.filter(
                title=request.POST['search-study'],
                is_available=True,
            )
        }
    else:
        study_list = {
            'study_list': Study.objects.filter(is_available=True)
        }

    return render(request, 'service/lobby.html', study_list)