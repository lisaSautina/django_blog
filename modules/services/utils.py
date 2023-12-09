from uuid import uuid4
from pytils.translit import slugify

def unique_slugify(instance, slug):
    
    #Генератор уникальных SLUG для моделей, в случае существования такого SLUG.

    model = instance.__class__
    unique_slug = slugify(slug)
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = f'{unique_slug}-{uuid4().hex[:8]}'
    return unique_slug
# Сначала он проверяет, существует ли уже объект с таким slug в базе данных, используя model.objects.filter(slug=unique_slug).exists().
# Если существует, цикл while генерирует новый уникальный slug, добавляя
# к исходному значению - и 8 символов из шестнадцатеричного представления случайного UUID (uuid4().hex[:8]).
# Цикл продолжается, пока не будет найден уникальный slug.