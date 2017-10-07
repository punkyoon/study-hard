from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from service_main.models import StudyUser
from service_study.models import Notice
from study_hard import tool


@login_required
def study_main(request, url):
    study = tool._get_study(url)

    if study is None:
        return redirect('study_list')
    
    notices = tool._get_notice(study)[:3]
    is_admin = tool._is_already_admin(study, request.user)
    info = {
        'study_info': study,
        'new_notice': notices,
        'members': tool._list_members(study)
    }
    return render(request, 'service/main.html', info)


@login_required
def study_info(request, url):
    study = tool._get_study(url)

    if study is None:
        return redirect('study_list')

    user_list = tool._list_members(study)
    info = {
        'study_info': study,
        'members': user_list,
        'attendance_list': tool._get_study_attendance_list(study, user_list),
    }

    return render(request, 'service/info.html', info)


@login_required
def manage_fine(request, url):
    study = tool._get_study(url)

    if study is None:
        return redirect('study_list')

    if request.method == 'POST':
        request.POST['username']
        request.POST['fine']
    
    return render(request, 'service/info.html')


@login_required
def manage_attandance(request):
    study = tool._get_study(url)

    if study is None:
        return redirect('study_list')

    if request.method == 'POST':
        request.POST['username']
        request.POST['status']
        request.POST['date']
    
    return render(request, 'service/info.html')


@login_required
def list_notice(request, url):
    study = tool._get_study(url)

    if study is None:
        return redirect('study_list')

    is_admin = tool._is_already_admin(study, request.user)
    if request.method == 'POST' and is_admin:
        Notice.objects.create(study=study, contents=request.POST['notice'])

    info = {
        'study_info': study,
        'notices': tool._get_notice(study),
        'is_admin': is_admin,
    }

    return render(request, 'service/notice.html', info)


@login_required
def study_user_info(request, url, username):
    study = tool._get_study(url)
    user = tool._get_user(username)

    if study is None or user is None:
        return redirect('study_list')

    info = {
        'study_info': study,
        'attendance_list': tool._get_user_attendance_list(study, user),
        'study_user': StudyUser.objects.get(study=study, user=user),
    }

    return render(request, 'service/study_user_info.html', info)