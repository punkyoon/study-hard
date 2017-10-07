from django.http import HttpResponseRedirect
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
            'study_info': study,
            'member_list': tool._list_members(study),
            'join_requests': tool._get_study_request_list(study),
            'attandance_list': tool._get_study_attendance_list(study, user_list),
        }
    
    return render(request, 'service/study_service_manage.html', info)


@login_required
def approve_join_request(request, url, username):
    study = tool._get_study(url)
    user = tool._get_user(username)
    
    if user == None or study == None:
        return redirect('my_study')
    
    if request.user == study.admin:
        study_request = tool._get_study_request(study, user)
        if study_request != None:
            study_request.approval = True
            study_request.save()
            StudyUser.objects.create(study=study, user=user)
        else:
            return redirect('my_study')

    return redirect('/service_admin/' + study.url)


@login_required
def reject_join_request(request, url, username):
    study = tool._get_study(url)
    user = tool._get_user(username)

    if user == None or study == None:
        return redirect('my_study')

    if request.user == study.admin:
        study_request = tool._get_study_request(study, user)
        if study_request is not None:
            study_request.delete()

    return redirect('/service_admin/' + study.url)


@login_required
def manage_deposit(request, url, username):
    study = tool._get_study(url)
    user = tool._get_user(username)

    if study is None or user is None:
        return redirect('my_study')

    tool._manage_deposit(study, user)
    
    return redirect('/service_admin/' + study.url)


@login_required
def kickout_member(request, url, username):
    study = tool._get_study(url)
    user = tool._get_user(username)

    if study is None or user is None:
        return redirect('my_study')

    if request.method == 'POST':
        tool._remove_my_study(study, user)
        return redirect('/service_admin/' + study.url)

    info = {
        'study_info': study,
        'member': user,
    }
    
    return render(request, 'service/kickout_member.html', info)


@login_required
def remove_study(request, url):
    study = tool._get_study(url)

    if tool._is_already_admin(study, request.user) is False or study is None:
        return redirect('my_study')

    info = {
        'study_info': study,
        'error': None
    }

    if request.method == 'POST':
        if request.POST['title'] == study.title:
            study.delete()
            return redirect('my_study')
        info['error'] = 'Please write study title correctly..'

    return render(request, 'service/remove_study.html', info)