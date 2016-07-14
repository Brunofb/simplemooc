from django.conf.urls import url
from django.contrib.auth import views
from accounts import views as accounts_views

urlpatterns = [

    url(r'^$', accounts_views.dashboard, name='dashboard'),

    url(r'^entrar/$', views.login,
        {'template_name': 'accounts/login.html'}, name='login'),

    url(r'^sair/$', views.logout,
        {'next_page': 'core:home'}, name='logout'),

    url(r'^cadastre-se/$', accounts_views.register, name='register'),

    url(r'^editar/$', accounts_views.edit, name='edit'),

]
