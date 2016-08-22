from django.contrib import admin
from .models import Course, Enrollment


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date', 'create_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['user', 'course']

admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
