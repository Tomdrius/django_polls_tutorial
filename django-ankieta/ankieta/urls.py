from django.urls import path

from . import views

app_name = "ankieta"
urlpatterns = [
    # ex: /ankieta/
    path("", views.IndexView.as_view(), name="index"), # ""wzorzec URL dla pustej ścieżki (/ankieta); views.index funkcja index() z views.py; name="index" nazwa tego wzorca URL jak w input formach.
    # ex: /ankieta/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # ex: /ankieta/5/results/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # ex: /ankieta/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]