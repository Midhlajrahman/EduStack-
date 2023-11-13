"""
URL configuration for edusite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import  path
from . import views
from .views import (
    CreateStripeCheckoutSessionView1,
    DWatchVideo2View,
    DWatchVideo3View,
    DWatchVideoView,
    Playlist1View,
    Playlist2View,
    Playlist3View,
)

app_name = "web_2"
urlpatterns = [
    path("d_home", views.d_home, name="d_home"),
    path("d_about", views.d_about, name="d_about"),
    path("d_contact", views.d_contact, name="d_contact"),
    path("d_profile", views.d_profile, name="d_profile"),
    path("d_teachers", views.d_teachers, name="d_teachers"),
    path("d_update", views.d_update, name="d_update"),
    path("d_topics" ,views.d_topics_view,name='d_topics' ),
    # watch video
    path("d_watch_video/ <int:pk>", DWatchVideoView.as_view(), name="d_watch_video"),
    path(
        "d_watch_video_2/ <int:pk>",
        DWatchVideo2View.as_view(),
        name="d_watch_video_2",
    ),
    path(
        "d_watch_video_3/ <int:pk>",
        DWatchVideo3View.as_view(),
        name="d_watch_video_3",
    ),
    path("playlist_1/<int:pk>", Playlist1View.as_view(), name="playlist_1"),
    path("playlist_2/<int:pk>", Playlist2View.as_view(), name="playlist_2"),
    path("playlist_3/<int:pk>", Playlist3View.as_view(), name="playlist_3"),
    path("playlist_4", views.playlist_4, name="playlist_4"),
    path("playlist_5", views.playlist_5, name="playlist_5"),
    path("playlist_6", views.playlist_6, name="playlist_6"),
    path("playlist_7", views.playlist_7, name="playlist_7"),
    path(
        "create-checkout-session1",
        CreateStripeCheckoutSessionView1.as_view(),
        name="create-checkout-session1",
    ),
]
