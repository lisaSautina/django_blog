from django.contrib import admin

from mptt.admin import DraggableMPTTAdmin
from .models import Category, Article


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):#возможность скрывать вложенную категорию
    """
    Админ-панель модели категорий
    """
    list_display = ('tree_actions', 'indented_title', 'id', 'title', 'slug')
    # Чтобы различить их или просто отобразить более интересную информацию 
    # о каждом авторе, можно использовать list_display (для добавления 
    # дополнительных полей).
    list_display_links = ('title', 'slug')
    # Используйте list_display_links, чтобы указать какие поля в 
    # list_display будут ссылками на страницу редактирования объекта.
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        ('Основная информация', {'fields': ('title', 'slug', 'parent')}),
        ('Описание', {'fields': ('description',)})
    )
    # prepopulated_fields позволяет определить поля, 
    # которые получают значение основываясь на значениях других полей:

@admin.register(Article)#регистрация модели в админке
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    #Мы добавили параметр prepopulated_fields, который позволяет с помощью
    # JS обрабатывать заголовок в реальном времени, конвертирует даже кириллицу.