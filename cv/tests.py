from django.test import TestCase
from cv.models import WorkExperience
from cv.models import Education
from cv.models import Project
from cv.models import Skill

# Create your tests here.
class CVPageTest(TestCase):

    def test_cv_page_returns_correct_html(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'cv/base.html')
        self.assertTemplateUsed(response, 'cv/cv_list.html')


class WorkEperienceModelTest(TestCase):

    def test_saving_and_retrieving_work_experiences(self):
        experience_1 = WorkExperience()
        experience_1.company = 'Webmoco'
        experience_1.description = 'I did some work experience there'
        experience_1.save()

        experience_2 = WorkExperience()
        experience_2.company = 'Dough and Brough'
        experience_2.description = 'I worked there over summer 2018'
        experience_2.save()

        saved_experiences = WorkExperience.objects.all()
        self.assertEqual(saved_experiences.count(), 2)

        first_saved_experience = saved_experiences[0]
        self.assertEqual(first_saved_experience.company, 'Webmoco')
        self.assertEqual(first_saved_experience.description, 'I did some work experience there')

        second_saved_experience = saved_experiences[1]
        self.assertEqual(second_saved_experience.company, 'Dough and Brough')
        self.assertEqual(second_saved_experience.description, 'I worked there over summer 2018')


class EducationModelTest(TestCase):

    def test_saving_and_retrieving_educations(self):
        education_1 = Education()
        education_1.institution = 'Trinity'
        education_1.description = 'This was my secondary school'
        education_1.save()

        education_2 = Education()
        education_2.institution = 'University of birmingham'
        education_2.description = 'This is my university'
        education_2.save()

        saved_educations = Education.objects.all()
        self.assertEqual(saved_educations.count(), 2)

        first_saved_education = saved_educations[0]
        self.assertEqual(first_saved_education.institution, 'Trinity')
        self.assertEqual(first_saved_education.description, 'This was my secondary school')

        second_saved_education = saved_educations[1]
        self.assertEqual(second_saved_education.institution, 'University of birmingham')
        self.assertEqual(second_saved_education.description, 'This is my university')


class ProjectTest(TestCase):

    def test_saving_and_retrieving_projects(self):
        project_1 = Project()
        project_1.name = 'Football Team Tracker'
        project_1.description = 'An Android app for tracking your football team.'
        project_1.save()

        project_2 = Project()
        project_2.name = 'Portfolio'
        project_2.description = 'A website to showcase my CV and a blog.'
        project_2.save()

        saved_projects = Project.objects.all()
        self.assertEqual(saved_projects.count(), 2)

        first_saved_project = saved_projects[0]
        self.assertEqual(first_saved_project.name, 'Football Team Tracker')
        self.assertEqual(first_saved_project.description, 'An Android app for tracking your football team.')

        second_saved_project = saved_projects[1]
        self.assertEqual(second_saved_project.name, 'Portfolio')
        self.assertEqual(second_saved_project.description, 'A website to showcase my CV and a blog.')


class SkillTest(TestCase):

    def test_saving_and_retrieving_skills(self):
        skill_1 = Skill()
        skill_1.name = 'Kotlin'
        skill_1.save()

        skill_2 = Skill()
        skill_2.name = 'Python'
        skill_2.save()

        saved_skills = Skill.objects.all()
        self.assertEqual(saved_skills.count(), 2)

        first_saved_skill = saved_skills[0]
        self.assertEqual(first_saved_skill.name, 'Kotlin')

        second_saved_skill = saved_skills[1]
        self.assertEqual(second_saved_skill.name, 'Python')
