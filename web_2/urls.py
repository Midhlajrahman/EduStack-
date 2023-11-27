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
    DVideoView,
    Playlist1View,

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
    path("d_video/ <int:pk>", DVideoView.as_view(), name="d_video"),
    path("playlist_1/<int:pk>", Playlist1View.as_view(), name="playlist_1"),

    path(
        "create-checkout-session1",
        CreateStripeCheckoutSessionView1.as_view(),
        name="create-checkout-session1",
    ),
]
