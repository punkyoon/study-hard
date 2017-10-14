from django.utils import timezone
from django.contrib.auth.models import User

from service_main.models import Study, StudyUser, StudyRequest
from service_study.models import Notice, Attendance, Fine


def _get_study(url):
    try:
        return Study.objects.get(url=url)
    except:
        return None


def _get_notice(study):
    try:
        return Notice.objects.filter(study=study).order_by('-upload_time')
    except:
        return None


def _get_user(username):
    try:
        return User.objects.get(username=username)
    except:
        return None


def _get_user_attendance_list(study, user):
    try:
        return Attendance.objects.filter(study=study, user=user)
    except:
        return None


def _get_study_list(user, option):
    try:
        # Manage Study List
        if option == 'manage':
            return Study.objects.filter(admin=user)

        # Belong Study List
        elif option == 'belong':
            return StudyRequest.objects.filter(user=user, approval=True)

        # Reuqested Study List
        elif option == 'requested':
            return StudyRequest.objects.filter(user=user, approval=False)

        # Error
        else:
            raise

    except:
        return None


def _get_study_request(study, user):
    try:
        return StudyRequest.objects.get(study=study, user=user)
    except:
        return None


def _get_study_request_list(study):
    try:
        return StudyRequest.objects.filter(study=study, approval=False)
    except:
        return None


def _get_study_attendance_list(study, user_list):
    attendance_list = list()
    try:
        for study_user in user_list:
            attendance_list.append(
                Attendance.objects.filter(
                    study=study,
                    user=study_user.user
                )
            )
        attendance_list.sort()
        return attendance_list
    except:
        return None


def _get_user_fine_list(study, user):
    fines = Fine.objects.filter(study=study, user=user)
    total = 0
    for fine in fines:
        total += fine.fine_rate

    return {'total': total, 'fine_list': fines}


def _get_study_fine_list(study):
    return Fine.objects.filter(study=study)


def _get_total_fine_list(study):
    fines = Fine.objects.filter(study=study)
    total = 0
    for fine in fines:
        total += fine.fine_rate

    return total


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


def _manage_deposit(study, user):
    try:
        study_user = StudyUser.objects.get(study=study, user=user)
        if study_user.deposit_pay:
            study_user.deposit_pay = False
        else:
            study_user.deposit_pay = True
        study_user.save()
        return True    # Success
    except:
        return False    # Fail


def _manage_attendance(study, user, option, date=None):
    try:
        attendance = Attendance.objects.get(
            study=study,
            user=user,
            date=timezone.now().date()
        )

    except:
        attendance = Attendance.objects.create(study=study, user=user)

    if date is not None:
        attendance.date = date

    if option == 'attend':
        attendance.status = 'attend'

    elif option == 'late':
        attendance.status = 'late'

    elif option == 'absent':
        attendance.status = 'absent'

    else:
        return None

    attendance.save()


def _impose_fine(study, user, reason, rate):
    Fine.objects.create(
        study=study,
        user=user,
        fine_reason=reason,
        fine_rate=rate
    )


def _remove_fine(hash_value):
    try:
        Fine.objects.get(hash_value=hash_value).delete()
    except:
        return None


def _paid_fine(hash_value):
    try:
        fine = Fine.objects.get(hash_value=hash_value)
    except:
        return False

    if fine.fine_pay is False:
        fine.fine_pay = True
    else:
        fine.fine_pay = False

    fine.save()
    return True


def _approve_study(study, user, is_ok=True):
    if is_ok:
        study_request = StudyRequest.objects.get(study=study, user=user)
        StudyUser.objects.create(study=study, user=user)

        study_request.approval = True
        study_request.save()

    else:
        study_request = StudyRequest.objects.get(
            study=study,
            user=user
        ).delete()


def _list_members(study):
    members = StudyUser.objects.filter(study=study)
    if members.count() == 0:
        return None
    else:
        return members


def _remove_my_study(study, user):
    try:
        StudyUser.objects.get(study=study, user=user).delete()
        StudyRequest.objects.get(study=study, user=user).delete()
        return True    # Success
    except:
        return False    # Fail
