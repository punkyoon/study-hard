from django.shortcuts import render


def find_study(request):
    if request.method == 'POST':
        return render(request, 'service/find_result.html')
    return render(request, 'service/lobby.html')


def join_request_study(request):
    if request.method == 'POST':
        return render(request, 'service/request_list.html')
    return render(request, 'service/join_request_form.html')


def create_study(request):
    if request.method == 'POST':
        return render(request, 'service/lobby.html')
    return render(request, 'service/create_study.html')


def list_study(request):
    return render(request, 'service/lobby.html')