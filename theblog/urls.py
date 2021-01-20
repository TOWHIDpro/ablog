from django.urls import path
from . views import HomeView, Articalview, Addpostview, Updatepostview


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('artical/<int:pk>', Articalview.as_view(), name="articaldetail"),
    path('add_post/', Addpostview.as_view(), name="add_post"),
    path('artical/edit/<int:pk>', Updatepostview.as_view(), name="update_post")


]
