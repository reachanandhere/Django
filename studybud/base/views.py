
from django.shortcuts import render


roomsList = [
    {
        'id': 1, 'name' : 'Lets learn Django'
    },
     {
        'id': 2, 'name' : 'Lets learn Javascript'
    },
     {
        'id': 3, 'name' : 'Back End Development'
    },

]

def home(request):
    context = {'roomsList' : roomsList}
    return render(request, 'base/home.html', context)

def room(request, pk):
    selectedRoom = None
    for i in roomsList:
        if i['id'] == int(pk):
            selectedRoom = i

    context = {'selectedRoom' : selectedRoom}
    return render(request, 'base/room.html', context)

