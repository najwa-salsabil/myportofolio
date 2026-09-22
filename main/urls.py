from django.urls import path

from main.views import (
    show_main, 
    show_experience, 
    show_projects, 
    show_achievements,
    create_project,
    get_projects_json,
    delete_project,
    create_experience,
    update_experience,
    delete_experience,
    get_experience_json,
    create_achievement,
    update_achievement,
    delete_achievement,
    get_achievement_json,
    register,
    login_user,
    logout_user,
    toggle_star,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("projects/", show_projects, name="show_projects"),
    path("achievements/", show_achievements, name="show_achievements"),
    path("projects/add/", create_project, name="create_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/", delete_project, name="delete_project"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/<uuid:experience_id>/edit/", update_experience, name="update_experience"),
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("achievements/add/", create_achievement, name="create_achievement"),
    path("achievements/<uuid:achievement_id>/edit/", update_achievement, name="update_achievement"),
    path("achievements/<uuid:achievement_id>/delete/", delete_achievement, name="delete_achievement"),
    path("api/achievements/", get_achievement_json, name="get_achievement_json"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path(
        "projects/<uuid:project_id>/star/",
        toggle_star,
        name="toggle_star",
    ),
]