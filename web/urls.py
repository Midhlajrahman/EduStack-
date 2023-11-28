from django.urls import path

from . import views
from .views import (
    CreateStripeCheckoutSessionView,
    PlaylistView,
    TopicsView,
    WatchVideoView,
)

app_name = "web"
urlpatterns = [
    path("home", views.home, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("topics",     TopicsView.as_view(), name="topics"),
    path("profile", views.profile, name="profile"),
    path("playlist/<int:pk>", PlaylistView.as_view(), name="playlist"),
    # watch video
    path(
        "watch_video/<int:pk>", WatchVideoView.as_view(), name="watch_video"
    ),
    path("teachers", views.teachers, name="teachers"),
    path("update", views.update, name="update"),
    path("signin", views.student_signin, name="student_signin"),
    path("", views.signup, name="signup"),
    path(
        "create-checkout-session",
        CreateStripeCheckoutSessionView.as_view(),
        name="create-checkout-session",
    ),
    path("success", views.success, name="success"),
    path("cancel", views.cancel, name="cancel"),
]
