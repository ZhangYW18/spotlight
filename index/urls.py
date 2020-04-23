from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', views.index),
    path('train/', views.train_feedback),
    path(r'^favicon\.ico$', RedirectView.as_view(url='/index/images/favicon.ico')),
]
