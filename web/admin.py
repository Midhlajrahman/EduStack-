from django.contrib import admin
from .models import Course, Playlist, PlaylistHead, Video, TeacherProfile, Contact, ProfileDetails

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # list_display = ('category', 'video_title', 'video_thumbnail')
    # list_filter = ('category',)
    pass


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    # list_display = ('category', 'video_title', 'thumbnail', 'authername', 'auther_image', 'date', 'howmany_videos')
    # list_filter = ('category',)
    pass

@admin.register(PlaylistHead)
class PlaylistHeadAdmin(admin.ModelAdmin):
    # list_display = ('category', 'topic_title', 'topic_thumb', 'how_many_videos', 'tutor_image', 'tutor_name', 'date', 'topic_title', 'topic_description')
    # list_filter = ('category',)
    pass

@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    # list_display = ('teacher_name', 'teacher_image', 'teacher_position', 'insta_url', 'linkedin_url')
    pass

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    # list_display = ('category', 'title', 'video_thumb', 'Course', 'video', 'date', 'tutor_image', 'tutor_name', 'tutor_position', 'description')
    # list_filter = ('category',)
    pass

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    # list_display = ('name', 'email', 'number', 'message')
    pass

@admin.register(ProfileDetails)
class ProfileDetailsAdmin(admin.ModelAdmin):
    # list_display = ('name', 'email', 'image')
    pass

