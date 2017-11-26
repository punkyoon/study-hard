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
    fines = tool._get_study_fine_list(study)[:3]

    info = {
        'study_info': study,
        'new_notice': notices,
        'new_fine': fines,
        'members': tool._list_members(study),
        'total_fine': tool._get_total_fine_list(study),
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
def list_fine(request, url):
    study = tool._get_study(url)

    if study is None:
        return redirect('study_list')

    is_admin = tool._is_already_admin(study, request.user)
    if request.method == 'POST' and is_admin:
        user = tool._get_user(request.POST['username'])
        tool._impose_fine(
            study,
            user,
            request.POST['reason'],
            request.POST['rate']
        )

    user_list = tool._list_members(study)
    fines = tool._get_study_fine_list(study)
    info = {
        'study_info': study,
        'user_list': user_list,
        'fines': fines,
        'is_admin': is_admin,
    }

    return render(request, 'service/fine_list.html', info)


@login_required
def study_user_info(request, url, username):
    study = tool._get_study(url)
    user = tool._get_user(username)

    if study is None or user is None:
        return redirect('study_list')

    fine_info = tool._get_user_fine_list(study, user)
    info = {
        'study_info': study,
        'attendance_list': tool._get_user_attendance_list(study, user),
        'study_user': StudyUser.objects.get(study=study, user=user),
        'user_fine': fine_info['total'],
        'fine_list': fine_info['fine_list'],
    }

    return render(request, 'service/study_user_info.html', info)


@login_required
def exit_study(request, url, username):
    study = tool._get_study(url)
    user = tool._get_user(username)

    if study is None or user is None:
        return redirect('my_study')

    info = {
        'study_info': study,
        'member': user,
        'error': None
    }

    if request.method == 'POST':
        if request.POST['username'] == user.username:
            tool._remove_my_study(study, user)
            return redirect('my_study')
        info['error'] = 'Please write user username correctly..'

    return render(request, 'service/exit_study.html', info)


@login_required
def paid_fine(request, url, hash_value):
    study = tool._get_study(url)
    is_admin = tool._is_already_admin(study, request.user)

    if study is None or is_admin is False:
        return None

    tool._paid_fine(hash_value)
    return redirect('/' + study.url + '/fine/')


@login_required
def remove_fine(request, url, hash_value):
    study = tool._get_study(url)
    is_admin = tool._is_already_admin(study, request.user)

    if study is None or is_admin is False:
        return None

    tool._remove_fine(hash_value)
    return redirect('/' + study.url + '/fine/')


@login_required
def chat_study(request, url):
    study = tool._get_study(url)
    info = {
        'study_info': study,
        'user': request.user.username,
    }

    return render(request, 'service/chat_room.html', info)
