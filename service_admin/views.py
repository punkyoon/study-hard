from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from service_main.models import StudyRequest
from study_hard import tool


@login_required
def manage_join_request(request, url):
    study = tool._get_study(url)

    if not _is_already_admin(study, request.user):
        return redirect('my_study')
    
    if request.method == 'POST':
        pass

    info = {
        'study': study,
        'user_list': tool._get_study_request_list(study),
    }
    return render(request, 'service/manage_join_request.html')


@login_required
def remove_study(request, url):
    if request.method == 'POST':
        study = tool._get_study(url)
        if tool._is_already_admin(study, request.user)
            study.delete()
        else:
            tool._remove_my_study(study, request.user)
        return redirect('my_study')

    return render(request, 'service/remove_study.html')