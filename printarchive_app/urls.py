from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show_pdf, name='show_pdf'),
]