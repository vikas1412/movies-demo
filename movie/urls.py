from django.urls import path

from movie import views

urlpatterns = [
    path('', views.index, name="index"),

    path('signup/', views.signup, name="signup"),

    path("new/director/", views.create_new_director, name="new-director"),

    path("directors/", views.DirectorList.as_view(), name="directors"),

    path("director/<int:pk>/", views.DirectorDetail.as_view(), name="director"),

    path("new/genre/", views.GenreCreate.as_view(), name="new-genre"),

    path("genre/all/", views.GenreList.as_view(), name="genres"),

    path("new/movie/", views.new_movie, name="new-movie"),

    path("all/", views.MoviesList.as_view(), name="movies"),

    path("movie/<int:pk>/", views.MovieDetail.as_view(), name="movie"),

    path("new/studio/", views.new_studio, name="new-studio"),

    path("studio/<int:pk>/", views.StudioDetail.as_view(), name="studio"),

    path("studios/", views.StudioList.as_view(), name="studios"),

]