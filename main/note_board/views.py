from django.shortcuts import render


def home_page(request):
    return render (request, 'note_board/home.html')


def notes_page(request):
    return render (request, 'note_board/notes.html')
