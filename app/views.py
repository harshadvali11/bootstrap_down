from django.shortcuts import render

# Create your views here.


def bootstratp_download(request):
    return render(request,'bootstratp_download.html')