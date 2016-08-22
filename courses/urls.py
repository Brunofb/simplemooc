from django.conf.urls import url
from courses import views


urlpatterns = [

    url(r'^$', views.index, name='index'),

    url(r'^(?P<slug>[\w_-]+)/$', views.details, name='details'),

    url(r'^(?P<slug>[\w_-]+)/inscricao/$',
        views.enrollment, name='enrollment'),

    url(r'^(?P<slug>[\w_-]+)/cancelar_inscricao/$',
        views.undo_enrollment, name='undo_enrollment'),

    url(r'^(?P<slug>[\w_-]+)/anuncios/$',
        views.announcements, name='announcements'),
]
