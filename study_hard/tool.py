from django.contrib.auth.models import User
from service_main.models import Study, StudyUser, StudyRequest
from service_study.models import Notice, Attendance


def _get_study(url):
    try:
        return Study.objects.get(url=url)
    except:
        return None


def _get_notice(study):
    try:
        return Notice.objects.filter(study=study)
    except:
        return None


def _is_repeat_request(study, user):
    try:
        StudyRequest.objects.get(study=study, user=user)
        return True    # repeat
    except:
        return False    # repeat not


def _is_already_admin(study, user):
    if study.admin == user:
        return True    # admin
    else:
        return False    # admin not


def _check_request_avaliable(study, user):
    if _is_already_admin(study, user) or _is_repeat_request(study, user):
        return False    # avaliable
    else:
        return True    # avaiable not


def _approve_study(study, user, is_ok=True):
    if is_ok:
        study_request = StudyRequest.objects.get(study=study, user=user)
        StudyUser.objects.create(study=study, user=user)
        
        study_request.approval = True
        study_request.save()

    else:
        study_request = StudyRequest.objects.get(study=study, user=user).delete()


def _list_members(study):
    return StudyUser.objects.filter(study=study)