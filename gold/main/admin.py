from django.contrib import admin
from .models import Project, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'year', 'is_featured')
    list_filter = ('is_featured', 'year')
    search_fields = ('title', 'client')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectImageInline]