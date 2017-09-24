from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from service_study.models import Notice
from study_hard.tool import _get_study, _list_members


@login_required
def study_main(request, url):
    study = _get_study(url)

    if study is None:
        return redirect('study_list')

    if request.method == 'POST' and request.user == study.admin:
        Notice.objects.create(study=study, contents=request.POST['notice'])
    
    notices = Notice.objects.filter(study=study).order_by('-upload_time')[:3]
    is_admin = True if request.user == study.admin else False;
    info = {
        'study_info': study,
        'new_notice': notices,
        'is_admin': is_admin,
        'members': _list_members(study)
    }
    return render(request, 'service/main.html', info)

@login_required
def kick_out_member(request):
    pass


@login_required
def manage_fine(request):
    pass


@login_required
def manage_deposit(request):
    pass


@login_required
def manage_attandance(request):
    pass


@login_required
def upload_notice(request):
    if request.method == 'POST':
        Notice.objects.create()


@login_required
def list_notice(request):
    pass