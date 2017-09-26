from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from service_main.models import StudyRequest
from study_hard.tool import _get_study, _get_study_request_list, _is_already_admin


@login_required
def manage_join_request(request, url):
    study = _get_study(url)

    if not _is_already_admin(study, request.user):
        return redirect('my_study')
    
    if request.method == 'POST':
        pass

    info = {
        'study': study,
        'user_list': _get_study_request_list(study),
    }
    return render(request, 'service/manage_join_request.html')


def exit_study(request):
    pass


def remove_study(request):
    pass