from django.conf.urls import url
from django.conf.urls import include


from . import views
urlpatterns = [
    url(r'^register/$', views.register,name="register"),
    url(r'^contact/$', views.contact,name="contact"),
    url(r'^doregister/$', views.do_register,name="do_register"),

    url(r'^$', views.index,name="index"),

    url(r'^reset/password_reset/$', 'django.contrib.auth.views.password_reset', name='reset_password_reset'),
    url(r'^reset/password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),

    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': '/'},name="logout"),
     url(r'^do_login/$', 'django.contrib.auth.views.login',name="login"),
]
