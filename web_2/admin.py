from django.contrib import admin

from .models import (
    ContactForm,
    Course1,
    Course2,
    Course3,
    DPlaylistHead,
    DTeacherProfile,
    DWatchVideo,
    DWatchVideo2,
    DWatchVideo3,
    Playlist1,
    Playlist2,
    Playlist3,
    ProfileForm,
)

admin.site.register(ContactForm)
admin.site.register(ProfileForm)
admin.site.register(DTeacherProfile)
admin.site.register(Course1)
admin.site.register(Course2)
admin.site.register(Course3)
admin.site.register(Playlist1)
admin.site.register(Playlist2)
admin.site.register(Playlist3)
admin.site.register(DPlaylistHead)
admin.site.register(DWatchVideo)
admin.site.register(DWatchVideo2)
admin.site.register(DWatchVideo3)
