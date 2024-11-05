from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls

from . import views

app_name = "core"
urlpatterns = [
    # # ex: /core/
    # path("", views.index, name="index"),
    # # ex: /core/5/
    # # the 'name' value as called by the {% url %} template tag
    # path("<int:question_id>/", views.detail, name="detail"),
    # # ex: /core/5/results/
    # path("<int:question_id>/results/", views.results, name="results"),
    # # ex: /core/5/vote/
    # path("<int:question_id>/vote/", views.vote, name="vote"),

    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
] + debug_toolbar_urls()