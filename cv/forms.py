from django import forms

from cv.models import WorkExperience
from cv.models import Education
from cv.models import Project
from cv.models import Skill

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ('role', 'company', 'details',)
        
class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ('institution', 'details',)
        
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'details',)
        
class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ('name',)