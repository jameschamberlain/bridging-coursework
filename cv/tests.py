from django.test import TestCase

# Create your tests here.
class CVTest(TestCase):

    def test_cv_page_returns_correct_html(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'cv/base.html')