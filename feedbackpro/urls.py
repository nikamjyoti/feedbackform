from django.conf.urls import include, url
from django.contrib import admin
from feedbackapp import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'feedbackpro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', views.feedback_views),
]
