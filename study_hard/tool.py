from service_main.models import Study, StudyUser, StudyRequest
from service_study.models import Notice, Attendance


def _get_study(url):
    try:
        return Study.objects.get(url=url)
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
    print(_is_already_admin(study, user))
    print(_is_repeat_request(study, user))
    if _is_already_admin(study, user) or _is_repeat_request(study, user):
        return False    # avaliable
    else:
        return True    # avaiable not