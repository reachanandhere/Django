
from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm

def home(request):
    roomsList = Room.objects.all()
    print(roomsList)
    context = {'roomsList' : roomsList}
    return render(request, 'base/home.html', context)

def room(request, pk):   
    selectedRoom = Room.objects.get(id=pk)   
    context = {'selectedRoom' : selectedRoom}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)