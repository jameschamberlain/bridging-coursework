from django.shortcuts import render
from django.views.generic.list import ListView
from django.shortcuts import redirect

from .forms import WorkExperienceForm
from .forms import EducationForm
from .forms import ProjectForm
from .forms import SkillForm

from cv.models import WorkExperience
from cv.models import Education
from cv.models import Project
from cv.models import Skill

# Create your views here.
def cv(request):
    return render(request, 'cv/base.html')

def work_experience_new(request):
    if request.method == "POST":
        form = WorkExperienceForm(request.POST)
        if form.is_valid:
            work_experience = form.save(commit=False)
            work_experience.save()
            return redirect('cv')
    else:
        form = WorkExperienceForm()
    return render(request, 'cv/work_experience_new.html', {'form': form})

def education_new(request):
    if request.method == "POST":
        form = EducationForm(request.POST)
        if form.is_valid:
            education = form.save(commit=False)
            education.save()
            return redirect('cv')
    else:
        form = EducationForm()
    return render(request, 'cv/education_new.html', {'form': form})

def project_new(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid:
            project = form.save(commit=False)
            project.save()
            return redirect('cv')
    else:
        form = ProjectForm()
    return render(request, 'cv/project_new.html', {'form': form})

def skill_new(request):
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid:
            skill = form.save(commit=False)
            skill.save()
            return redirect('cv')
    else:
        form = SkillForm()
    return render(request, 'cv/skill_new.html', {'form': form})

class CVView(ListView):
    context_object_name = 'cv_list'
    template_name = 'cv/cv_list.html'
    queryset = WorkExperience.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CVView, self).get_context_data(**kwargs)
        context['educations'] = Education.objects.all()
        context['projects'] = Project.objects.all()
        context['skills'] = Skill.objects.all()
        return context