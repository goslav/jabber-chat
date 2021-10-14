from django.shortcuts import render


def home(request):
    return render(request, 'chat/home.html', {})


def room(request, room_name):
    return render(request, 'chat/chatroom.html', {
        'room_name':room_name
    })