from typing import Any
from django.views.generic import ListView, DetailView

from .models import Article 

class ArticleListView(ListView):
    model = Article
    template_name = 'blog/articles_list.html'
    context_object_name = 'articles'
#назледуемся от лист вью класса, это представление будет обрабатывать наш список объектов
#context_object_name - переменная, в которой мы будем хранить список для вывода в шаблоне
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context
    
# class ArticleDetailView(DetailView):
#     model = Article
#     template_name = 'blog/articles_deatail.html' #название шаблона
#     context_object_name = 'article' #представленная переменная в шаблон

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = self.object.title #наш заголовок
#         return context #это наш объект, т.е наша статья, у которой мы получаем заголовок.
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/articles_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context