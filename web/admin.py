from django.contrib import admin
from . models import html_course
from . models import css_course
from . models import js_course
from . models import bootstrap_course
from . models import react_course
from . models import python_course
from . models import psql_course
from . models import flutter_course
from . models import contact_form
from . models import selectbox_course
from . models import teacher_profile
from . models import html_playlist
from . models import css_playlist
from . models import js_playlist
from . models import bootstrap_playlist
from . models import react_playlist
from . models import python_playlist
from . models import psql_playlist
from . models import playlist_head
from . models import watch_video
from . models import css_watch_video
from . models import js_watch_video
from . models import bootstrap_watch_video
from . models import react_watch_video
from . models import python_watch_video
from . models import psql_watch_video


from . models import profile_details
# from . models import signup_form

# Register your models here.
admin.site.register(html_course)
admin.site.register(html_playlist)
admin.site.register(css_course)
admin.site.register(css_playlist)
admin.site.register(js_course)
admin.site.register(js_playlist)
admin.site.register(bootstrap_course)
admin.site.register(bootstrap_playlist)
admin.site.register(react_course)
admin.site.register(react_playlist)
admin.site.register(python_course)
admin.site.register(python_playlist)
admin.site.register(psql_course)
admin.site.register(psql_playlist)

# admin.site.register(flutter_course)
admin.site.register(contact_form)
admin.site.register(selectbox_course)
admin.site.register(teacher_profile)


admin.site.register(playlist_head)
admin.site.register(watch_video)
admin.site.register(css_watch_video)
admin.site.register(js_watch_video)
admin.site.register(bootstrap_watch_video)
admin.site.register(react_watch_video)
admin.site.register(python_watch_video)
admin.site.register(psql_watch_video)

admin.site.register(profile_details)
# admin.site.register(signup_form)