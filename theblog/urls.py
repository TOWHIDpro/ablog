from django.urls import path
from . views import HomeView, Articalview


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('artical/<int:pk>', Articalview.as_view(), name="articaldetail")


]
