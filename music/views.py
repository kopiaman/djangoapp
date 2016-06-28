from django.shortcuts import render, get_object_or_404 ,redirect

from .models import music

from .forms import musicForm

# 1- model 2- ModelObject  3-appname

def music_list(request):
    musiclist = music.objects.all()
    return render(request, 'music/list.html', {'musics': musiclist})

def music_detail(request, pk):
    music_pk = get_object_or_404(music, pk=pk)
    return render(request, 'music/detail.html', {'music': music_pk })

def music_new(request):
    if request.method == "POST":
        form = musicForm(request.POST)
        if form.is_valid():
            music = form.save(commit=False)
            music.author = request.user
            music.save()
            return redirect('music_detail', pk=music.pk)
    else:
        form = musicForm()

    return render(request, 'music/new.html', {'form': form})

def music_edit(request, pk):
    music = get_object_or_404(music, pk=pk)
    if request.method == "POST":
        form = musicForm(request.POST, instance=music)  #we create a form we pass this music as an instance both when we save the form:
        if form.is_valid():
            music = form.save(commit=False)
            music.author = request.user
            music.save()
            return redirect('music_detail', pk=music.pk)
    else:
        form = musicForm(instance=music)  #opened a form with this music to edit:
    return render(request, 'music/edit.html', {'form': form})

def music_delete(request, pk):
    music = get_object_or_404(music, pk=pk)    
    if request.method=='POST':
        music.delete()
        return redirect('music_list')
    return render(request, 'music/delete.html', {'music':music})    

