from django.contrib import admin

from main.models import Experience, Project, Achievement


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_ongoing")
    list_filter = ("category",)
    search_fields = ("title",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "tech_stack")
    search_fields = ("title",)


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ("title", "rank", "year")
    list_filter = ("year",)
    search_fields = ("title",)