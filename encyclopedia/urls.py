from django.urls import path

from . import views

app_name = "encyclo"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.title, name="title"),
    path("new", views.new_page, name="new_page"),

]
