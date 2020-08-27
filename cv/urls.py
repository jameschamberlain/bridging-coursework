from django.urls import path
from . import views
from cv.views import CVView

urlpatterns = [
    path('', CVView.as_view(), name='cv'),
    path('new-work-experience', views.work_experience_new, name='work_experience_new'),
    path('new-education', views.education_new, name='education_new'),
    path('new-project', views.project_new, name='project_new'),
    path('new-skill', views.skill_new, name='skill_new'),
]