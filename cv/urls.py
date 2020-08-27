from django.urls import path
from . import views
from cv.views import CVView

urlpatterns = [
    path('', CVView.as_view(), name='cv'),
]