
from django.contrib import admin
from django.conf.urls import url,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views
from rest_framework.urlpatterns import format_suffix_patterns
from articles import api


urlpatterns = [
    url(r'^$',views.home,name="home"),
    # url(r'^$',article_views.article_list,name="home"),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/',include('accounts.urls')),
    url(r'^articles/',include('articles.urls')),
    url(r'^about/$',views.about,name="about"),
    url(r'^api/articles/$',api.ArticleList.as_view()),
    url(r'^api/articles/(?P<pk>[0-9]+)/$',api.ArticleDetail.as_view())
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += format_suffix_patterns(urlpatterns)
