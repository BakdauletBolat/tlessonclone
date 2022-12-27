from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/users/login')
def main_page_view(request):
    return render(request, 'mainapp/index.html')
