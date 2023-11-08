from django.contrib import admin
from . models import contact_form
from . models import profile_form
from . models import course_1
from . models import course_2
from . models import course_3
from . models import playlist_1
from . models import playlist_2
from . models import playlist_3
from . models import d_playlist_head
from . models import d_teacher_profile
from . models import d_watch_video
from . models import d_watch_video_2
from . models import d_watch_video_3

# from . models import test_details
# from . models import js_course
# from . models import css_course
# from . models import html_course
# Register your models here.
admin.site.register(contact_form)
admin.site.register(profile_form)
admin.site.register(d_teacher_profile)
admin.site.register(course_1)
admin.site.register(course_2)
admin.site.register(course_3)
admin.site.register(playlist_1)
admin.site.register(playlist_2)
admin.site.register(playlist_3)
admin.site.register(d_playlist_head)
admin.site.register(d_watch_video)
admin.site.register(d_watch_video_2)
admin.site.register(d_watch_video_3)

# admin.site.register(test_details)
# admin.site.register(html_course)
# admin.site.register(html_playlist)
# admin.site.register(css_course)
# admin.site.register(css_playlist)
# admin.site.register(js_course)
# admin.site.register(js_playlist)