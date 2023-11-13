from django.contrib import admin

from .models import (
    BootstrapCourse,
    BootstrapPlaylist,
    BootstrapWatchVideo,
    ContactForm,
    CssCourse,
    CssPlaylist,
    CssWatchVideo,
    HtmlCourse,
    HtmlPlaylist,
    JsCourse,
    JsPlaylist,
    JsWatchVideo,
    PlaylistHead,
    ProfileDetails,
    PsqlCourse,
    PsqlPlaylist,
    PsqlWatchVideo,
    PythonCourse,
    PythonPlaylist,
    PythonWatchVideo,
    ReactCourse,
    ReactPlaylist,
    ReactWatchVideo,
    SelectboxCourse,
    TeacherProfile,
    WatchVideo,
)

# from . models import signup_form

# Register your models here.
admin.site.register(HtmlCourse)
admin.site.register(HtmlPlaylist)
admin.site.register(CssCourse)
admin.site.register(CssPlaylist)
admin.site.register(JsCourse)
admin.site.register(JsPlaylist)
admin.site.register(BootstrapCourse)
admin.site.register(BootstrapPlaylist)
admin.site.register(ReactCourse)
admin.site.register(ReactPlaylist)
admin.site.register(PythonCourse)
admin.site.register(PythonPlaylist)
admin.site.register(PsqlCourse)
admin.site.register(PsqlPlaylist)

# admin.site.register(flutter_course)
admin.site.register(ContactForm)
admin.site.register(SelectboxCourse)
admin.site.register(TeacherProfile)


admin.site.register(PlaylistHead)
admin.site.register(WatchVideo)
admin.site.register(CssWatchVideo)
admin.site.register(JsWatchVideo)
admin.site.register(BootstrapWatchVideo)
admin.site.register(ReactWatchVideo)
admin.site.register(PythonWatchVideo)
admin.site.register(PsqlWatchVideo)

admin.site.register(ProfileDetails)