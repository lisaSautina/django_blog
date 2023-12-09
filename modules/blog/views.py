from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Article, Category

from django.shortcuts import render
from django.core.paginator import Paginator

from django.views.generic import CreateView
from .forms import ArticleCreateForm, ArticleUpdateForm

from django.urls import reverse_lazy

#Встроенный класс Paginator в Django сообщает, какую страницу запрашивать и сколько строк получать из базы данных.
def articles_list(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, per_page=2)#требуемое кол-во элементов для вывода
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    context = {'page_obj': page_object}
    return render(request, 'blog/articles_func_list.html', context)

class ArticleListView(ListView):
    model = Article
    template_name = 'blog/articles_list.html'
    context_object_name = 'articles'
    paginate_by=2
   
#наcледуемся от лист вью класса, это представление будет обрабатывать наш список объектов
#context_object_name - переменная, в которой мы будем хранить список для вывода в шаблоне
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context
    

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/articles_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context
    
class ArticleByCategoryListView(ListView):
    model = Article
    template_name = 'blog/articles_list.html'
    context_object_name = 'articles'
    category = None

    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['slug'])
        queryset = Article.objects.all().filter(category__slug=self.category.slug)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Статьи из категории: {self.category.title}' 
        return context
    # template_name - наш шаблон, тот же что и у других представлений
# category - переменная, по которой мы будем работать
# context_object_name - словарь для перебирания в шаблоне
# def get_queryset - метод обработки qs, здесь мы получаем категорию по определенному slug, а после мы фильтруем qs статей по категории и возвращаем qs.
# def get_context_data - в этом методе передаем <title></title> категории
class ArticleCreateView(CreateView):
    """
    Представление: создание материалов на сайте
    """
    model = Article
    template_name = 'blog/articles_create.html'
    form_class = ArticleCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи на сайт'
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)
#     В get_context_data() передаем заголовок для <title> нашего шаблона.
# В методе form_valid() валидируем нашу форму, а также сохраняем автором текущего пользователя на странице, 
# которого получаем из запроса self.request.user
class ArticleUpdateView(UpdateView):
    #Представление: обновления материала на сайте
    model = Article
    template_name = 'blog/articles_update.html'
    context_object_name = 'article'
    form_class = ArticleUpdateForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Обновление статьи: {self.object.title}'
        return context
    
    def form_valid(self, form):
        # form.instance.updater = self.request.user
        form.save()
        return super().form_valid(form)
    
class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('home')
    context_object_name = 'article'
    template_name = 'blog/articles_delete.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Удаление статьи: {self.object.title}'
        return context
    # В свойстве success_url мы использовали переход после удаления статьи 
    # на страницу со всеми статьями с помощью функции reverse_lazy()