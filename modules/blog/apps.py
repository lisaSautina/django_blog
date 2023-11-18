from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modules.blog'
    verbose_name = 'Блог'
# что он будет использоваться именно внутри 
# папки modules, а также добавим лейбл на русском языке 
# с помощью параметра 