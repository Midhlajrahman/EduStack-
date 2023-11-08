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
from django.urls import path,include
from.import views
from . views import playlist_view
from . views import css_playlist_view
from . views import js_playlist_view
from . views import bootstrap_playlist_view
from . views import react_playlist_view
from . views import python_playlist_view
from . views import psql_playlist_view


from . views import topics
from . views import watch_video_view
from . views import css_watch_video_view
from . views import js_watch_video_view
from . views import bootstrap_watch_video_view
from . views import react_watch_video_view
from . views import python_watch_video_view
from . views import psql_watch_video_view

from .views import CreateStripeCheckoutSessionView
app_name='web'
urlpatterns = [
 path("home",views.home,name='home'),
 path("about",views.about,name='about'),
 path("contact",views.contact,name='contact'),
 path("topics",topics.as_view(),name='topics'),
 path("profile",views.profile,name="profile"),

#  play lists

#  path("html_playlist",views.html_playlist,name='html_playlist'),
#  path("css_playlist",views.css_playlist,name='css_playlist'),
#  path("bootstrap_playlist",views.bootstrap_playlist,name='bootstrap_playlist'),
#  path("react_playlist",views.react_playlist,name='react_playlist'),
#  path("js_playlist",views.js_playlist,name='js_playlist'),
#  path("git_playlist",views.git_playlist,name='git_playlist'),
#  path("python_playlist",views.python_playlist,name='python_playlist'),
 path('playlist/<int:pk>',playlist_view.as_view(),name='playlist'),
 path('css_playlist/<int:pk>',css_playlist_view.as_view(),name='css_playlist'),
 path('js_playlist/<int:pk>',js_playlist_view.as_view(),name='js_playlist'),
 path('bootstrap_playlist/<int:pk>',bootstrap_playlist_view.as_view(),name='bootstrap_playlist'),
 path('react_playlist/<int:pk>',react_playlist_view.as_view(),name='react_playlist'),
 path('python_playlist/<int:pk>',python_playlist_view.as_view(),name='python_playlist'),
  path('psql_playlist/<int:pk>',psql_playlist_view.as_view(),name='psql_playlist'),







# watch video 

 path("js_watch_video/<int:pk>",js_watch_video_view.as_view(),name='js_watch_video'),

 path("watch_video_5",views.watch_video_5,name='watch_video_5'),
 path("watch_video_6",views.watch_video_6,name='watch_video_6'),
 path('watch_video/<int:pk>',watch_video_view.as_view(),name='watch_video'),
 path('css_watch_video/<int:pk>',css_watch_video_view.as_view(),name='css_watch_video'),
 path('bootstrap_watch_video/<int:pk>',bootstrap_watch_video_view.as_view(),name='bootstrap_watch_video'),
 path('react_watch_video/<int:pk>',react_watch_video_view.as_view(),name='react_watch_video'),
 path('python_watch_video/<int:pk>',python_watch_video_view.as_view(),name='python_watch_video'),
 path('psql_watch_video/<int:pk>',psql_watch_video_view.as_view(),name='psql_watch_video'),


 path("teachers",views.teachers,name='teachers'),
 path("update",views.update,name='update'),
 path("signin",views.student_signin,name='student_signin'),
 path("",views.signup,name='signup'),
 





path(
        "create-checkout-session",
        CreateStripeCheckoutSessionView.as_view(),
        name="create-checkout-session",
    ),
path("success",views.success,name='success'),
path("cancel",views.cancel,name='cancel'),
]

