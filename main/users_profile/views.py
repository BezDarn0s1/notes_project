from django.shortcuts import render

def regisration(request):
    return render (request, 'users_profile/reg.html')

