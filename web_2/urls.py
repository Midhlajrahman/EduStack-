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
from . views import d_topics_view
from . views import playlist_1_view
from . views import playlist_2_view
from . views import playlist_3_view
# from . views import css_playlist_view
# from . views import d_topics
from . views import d_watch_video_view
from . views import d_watch_video_2_view
from . views import d_watch_video_3_view
# from . views import test_view
# from . views import css_watch_video_view
# from . views import d_update_view
from .views import CreateStripeCheckoutSessionView1
app_name='web_2'
urlpatterns = [
 path("d_home",views.d_home,name='d_home'),
 path("d_about",views.d_about,name='d_about'),
 path("d_contact",views.d_contact,name='d_contact'),
path("d_profile",views.d_profile,name='d_profile'),
path("d_teachers",views.d_teachers,name='d_teachers'),
# path("d_topics",views.d_topics_view,name='d_topics'),
path("d_update",views.d_update,name='d_update'),
# path('d_topics',d_topics_view.as_view(),name='d_topics'),
#  path("d_profile",views.d_profile,name="d_profile"),

#  play lists

#  path("html_playlist",views.html_playlist,name='html_playlist'),
#  path("css_playlist",views.css_playlist,name='css_playlist'),
#  path("bootstrap_playlist",views.bootstrap_playlist,name='bootstrap_playlist'),
#  path("react_playlist",views.react_playlist,name='react_playlist'),
#  path("js_playlist",views.js_playlist,name='js_playlist'),
#  path("git_playlist",views.git_playlist,name='git_playlist'),
#  path("python_playlist",views.python_playlist,name='python_playlist'),
#  path('playlist/<int:pk>',playlist_view.as_view(),name='playlist'),
#  path('css_playlist/<int:pk>',css_playlist_view.as_view(),name='css_playlist'),







# watch video 

 path("d_watch_video/ <int:pk>",d_watch_video_view.as_view(),name='d_watch_video'),
 path("d_watch_video_2/ <int:pk>",d_watch_video_2_view.as_view(),name='d_watch_video_2'),
  path("d_watch_video_3/ <int:pk>",d_watch_video_3_view.as_view(),name='d_watch_video_3'),
#  path("watch_video_2",views.watch_video_2,name='watch_video_2'),
#  path("watch_video_3",views.watch_video_3,name='watch_video_3'),
#  path("watch_video_4",views.watch_video_4,name='watch_video_4'),
#  path("watch_video_5",views.watch_video_5,name='watch_video_5'),
#  path("watch_video_6",views.watch_video_6,name='watch_video_6'),
#  path('d_watch_video/<int:pk>',d_watch_video_view.as_view(),name='d_watch_video'),
#  path('css_watch_video/<int:pk>',css_watch_video_view.as_view(),name='css_watch_video'),


#  path("teachers",views.teachers,name='teachers'),
#  path("update",views.update,name='update'),
#  path("",views.student_signin,name='student_signin'),

path("d_topics",d_topics_view.as_view(),name='d_topics'),
path("playlist_1/<int:pk>",playlist_1_view.as_view(),name='playlist_1'),
path("playlist_2/<int:pk>",playlist_2_view.as_view(),name='playlist_2'),
path("playlist_3/<int:pk>",playlist_3_view.as_view(),name='playlist_3'),
path("playlist_4",views.playlist_4,name='playlist_4'),
path("playlist_5",views.playlist_5,name='playlist_5'),
path("playlist_6",views.playlist_6,name='playlist_6'),
path("playlist_7",views.playlist_7,name='playlist_7'),
# path("test/<int:pk>",test_view.as_view(),name="test"),
path(
        "create-checkout-session1",
        CreateStripeCheckoutSessionView1.as_view(),
        name="create-checkout-session1",
    ),

]


