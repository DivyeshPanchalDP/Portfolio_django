from django.contrib import admin
from django.urls import path,include
from home import views
from django.views.generic import TemplateView
from django.views.static import serve
from django.conf.urls import url




urlpatterns = [
    path('', views.home, name='home'),
    path('education', views.education, name='education'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    #path('contact', TemplateView.as_view(template_name="contact.html")),
]