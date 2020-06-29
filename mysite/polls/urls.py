from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index, name="index"),
    # 127.0.0.1:8000/
    url(r'^(?P<question_id>[0-9]+)/$', views.details, name="details"),
    # 127.0.0.1:8000/1
    url(r'^(?P<question_id>[0-9]+)/results$', views.results, name="results"),
    # 127.0.0.1:8000/1/results
    url(r'^(?P<question_id>[0-9]+)/votes$', views.votes, name="votes"),
    # 127.0.0.1:8000/1/votes
]

