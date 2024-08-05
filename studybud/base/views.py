
from django.shortcuts import render
from .models import Room

# roomsList = [
#     {
#         'id': 1, 'name' : 'Lets learn Django'
#     },
#      {
#         'id': 2, 'name' : 'Lets learn Javascript'
#     },
#      {
#         'id': 3, 'name' : 'Back End Development'
#     },

# ]

def home(request):
    roomsList = Room.objects.all()
    print(roomsList)
    context = {'roomsList' : roomsList}
    return render(request, 'base/home.html', context)

def room(request, pk):   
    selectedRoom = Room.objects.get(id=pk)   
    context = {'selectedRoom' : selectedRoom}
    return render(request, 'base/room.html', context)

