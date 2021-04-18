from django.urls import path

from movie import views

urlpatterns = [
    path('', views.index, name="index"),

    path('signup/', views.signup, name="signup"),

    path("new/director/", views.DirectorCreate.as_view(), name="new-director"),

    path("new/genre/", views.GenreCreate.as_view(), name="new-genre"),

]