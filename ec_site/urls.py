from django.urls import path
from . import views

app_name = "ec_site"

urlpatterns = [
    path("", views.IndexView.as_view()),
    # path("articleCreate/", views.ArticleCreate.as_view(), name="article_create"),
]
