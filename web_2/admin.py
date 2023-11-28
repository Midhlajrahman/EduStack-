from django.contrib import admin
from .models import ContactForm, ProfileForm, DTeacherProfile, Course1, Playlist1, DPlaylistHead, DWatchVideo

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    # list_display = ('name', 'email', 'number', 'message')
    pass

@admin.register(ProfileForm)
class ProfileFormAdmin(admin.ModelAdmin):
    # list_display = ('name', 'email', 'image')
    pass

@admin.register(DTeacherProfile)
class DTeacherProfileAdmin(admin.ModelAdmin):
    # list_display = ('teacher_name', 'teacher_image', 'teacher_position', 'insta_url', 'linkedin_url')
    pass

@admin.register(Course1)
class Course1Admin(admin.ModelAdmin):
    # list_display = ('category', 'video_title', 'video_thumbnail')
    # list_filter = ('category',)
    pass

@admin.register(Playlist1)
class Playlist1Admin(admin.ModelAdmin):
    # list_display = ('category', 'video_title', 'thumbnail', 'authername', 'auther_image', 'date', 'howmany_videos')
    # list_filter = ('category',)
    pass

@admin.register(DPlaylistHead)
class DPlaylistHeadAdmin(admin.ModelAdmin):
    # list_display = ('category', 'topic_title', 'topic_thumb', 'how_many_videos', 'tutor_image', 'tutor_name', 'date', 'topic_title', 'topic_description')
    # list_filter = ('category',)
    pass

@admin.register(DWatchVideo)
class DWatchVideoAdmin(admin.ModelAdmin):
    # list_display = ('category', 'title', 'video_thumb', 'Course', 'video', 'date', 'tutor_image', 'tutor_name', 'tutor_position', 'description')
    # list_filter = ('category',)
    pass
