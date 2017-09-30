from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from service_main.models import StudyRequest, StudyUser
from study_hard import tool


@login_required
def study_admin_main(request, url):
    study = tool._get_study(url)

    if tool._is_already_admin(study, request.user):
        user_list = tool._list_members(study)
        info = {
            'study': study,
            'user_list': tool._list_members(study),
            'manage_request': tool._get_study_request_list(study),
            'manage_attandance': tool._get_study_attendance_list(study, user_list),
        }
    
    return render(request, 'service/study_service_manage.html', info)


@login_required
def manage_join_request(request, url):
    study = tool._get_study(url)

    if not tool._is_already_admin(study, request.user):
        return redirect('my_study')
    
    if request.method == 'POST':
        study_request = StudyRequest.objects.get(user=request.user)
        if request.POST['is_approve'] == 'Approve':
            study_request.approval = True
            study_request.save()
            StudyUser.objects.create(user=request.user)
        else:
            study_request.delete()

    info = {
        'study': study,
        'user_list': tool._get_study_request_list(study),
    }

    return render(request, 'service/manage_join_request.html')


@login_required
def exit_study(request, url):
    if request.method == 'POST':
        study = tool._get_study(url)
        tool._remove_my_study(study, request.user)
        return redirect('my_study')
    
    return render(request, 'service/exit_study.html')


@login_required
def kick_out_member(request, url):
    study = _get_study(url)

    if study is None:
        return redirect('study_list')

    if request.method == 'POST':
        user = tool._get_user(request.POST['username'])
        if user is not None:
            tool._remove_my_study(study, user)
            return redirect('service/study_service_manage.html')
    
    info = {
        'members': _list_members(study)
    }
    
    return render(request, 'service/study_service_manage.html', info)


@login_required
def remove_study(request, url):
    if request.method == 'POST':
        study = tool._get_study(url)
        if tool._is_already_admin(study, request.user)
            study.delete()
            return redirect('my_study')

    return render(request, 'service/remove_study.html')