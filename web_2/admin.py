from django.contrib import admin

from .models import (
    ContactForm,
    Course1,
    DPlaylistHead,
    DTeacherProfile,
    DWatchVideo,
    Playlist1,
    ProfileForm,
)

admin.site.register(ContactForm)
admin.site.register(ProfileForm)
admin.site.register(DTeacherProfile)
admin.site.register(Course1)
admin.site.register(Playlist1)
admin.site.register(DPlaylistHead)
admin.site.register(DWatchVideo)

