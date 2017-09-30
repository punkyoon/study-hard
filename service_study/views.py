from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from service_study.models import Notice
from study_hard.tool import _get_study, _get_notice, _list_members, _is_already_admin


@login_required
def study_main(request, url):
    study = _get_study(url)

    if study is None:
        return redirect('study_list')
    
    notices = _get_notice(study)[:3]
    is_admin = _is_already_admin(study, request.user)
    info = {
        'study_info': study,
        'new_notice': notices,
        'members': _list_members(study)
    }
    return render(request, 'service/main.html', info)

@login_required
def kick_out_member(request, url):
    study = _get_study(url)

    if study is None:
        return redirect('study_list')

    if request.method == 'POST':
        pass
    
    return render(request, 'service/manage.html')


@login_required
def manage_fine(request, url):
    study = _get_study(url)

    if study is None:
        return redirect('study_list')

    if request.method == 'POST':
        pass
    
    return render(request, 'service/manage.html')


@login_required
def manage_deposit(request, url):
    study = _get_study(url)

    if study is None:
        return redirect('study_list')

    if request.method == 'POST':
        pass
    
    return render(request, 'service/manage.html')


@login_required
def manage_attandance(request):
    study = _get_study(url)

    if study is None:
        return redirect('study_list')

    if request.method == 'POST':
        pass
    
    return render(request, 'service/manage.html')


@login_required
def list_notice(request, url):
    study = _get_study(url)

    if study is None:
        return redirect('study_list')

    is_admin = _is_already_admin(study, request.user)
    if request.method == 'POST' and is_admin:
        Notice.objects.create(study=study, contents=request.POST['notice'])

    print(_get_notice(study))

    info = {
        'study_info': study,
        'notices': _get_notice(study),
        'is_admin': is_admin,
    }

    return render(request, 'service/notice.html', info)