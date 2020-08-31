from django import forms

from cv.models import WorkExperience
from cv.models import Education
from cv.models import Project
from cv.models import Skill

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ('role', 'company', 'description',)
        
class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ('institution', 'description',)
        
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'description',)
        
class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ('name',)