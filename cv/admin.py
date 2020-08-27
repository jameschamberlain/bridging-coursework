from django.contrib import admin
from cv.models import WorkExperience
from cv.models import Education
from cv.models import Project
from cv.models import Skill

# Register your models here.
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(Project)
admin.site.register(Skill)