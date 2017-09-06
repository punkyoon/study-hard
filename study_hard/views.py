from django.shortcuts import render


def main_view(request):
    return render(request, 'base.html')
