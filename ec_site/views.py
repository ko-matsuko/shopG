from django.shortcuts import render
from django.shortcuts import redirect
from django.views import generic
from django.views.generic import View
# from ec_site.models import Article
# from ec_site.forms import ArticleCreateForm


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "ec_site/main.html")


# class ArticleCreate(View):
#     def get(self, request, *args, **kwargs):
#         pass

#     def post(self, request, *args, **kwargs):
#         form = ArticleCreateForm(request.POST)
#         if not form.is_valid():
#             queryset = Article.objects.all().order_by("-created_at")
#             context = {
#                 "form": form,
#                 "article_list": queryset,
#             }
#             return render(request, "message/board.html", context)
#         new_article = Article()
#         new_article.name = form.cleaned_data.get("name")
#         new_article.content = form.cleaned_data.get("content")
#         new_article.password = form.cleaned_data.get("password")
#         new_article.save()
#         # 画面に入力した内容をクリアするためformを生成
#         form = ArticleCreateForm()
#         queryset = Article.objects.all().order_by("-created_at")
#         context = {
#             "form": form,
#             "article_list": queryset,
#         }
#         return render(request, "message/board.html", context)
