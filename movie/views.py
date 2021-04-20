from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from movie.forms import SignupForm
from django.views import generic

from movie.models import Director, Genre, NewMovie


def index(request):
    return render(request, "movie/index.html")


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password1)
            if user is not None:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('index')
            else:
                return HttpResponse("Invalid username & password")

    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


class DirectorCreate(generic.CreateView):
    model = Director
    template_name = 'movie/new-director.html'
    fields = "__all__"
    success_url = "/"


class GenreCreate(generic.CreateView):
    model = Genre
    template_name = 'movie/new-genre.html'
    fields = ("title",)
    success_url = '/'


class NewMovieCreate(generic.CreateView):
    model = NewMovie
    template_name = 'movie/new-movie.html'
    fields = "__all__"
    success_url = "/"


class MoviesList(generic.ListView):
    model = NewMovie
    template_name = 'movie/movies.html'
    context_object_name = "movies"
