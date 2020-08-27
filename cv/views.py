from django.shortcuts import render
from django.views.generic.list import ListView

from cv.models import WorkExperience
from cv.models import Education
from cv.models import Project
from cv.models import Skill

# Create your views here.
def cv(request):
    return render(request, 'cv/base.html')

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