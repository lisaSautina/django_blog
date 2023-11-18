from uuid import uuid4
from pytils.translit import slugify

def unique_slugify(instanse, slug):
    #Генератор уникальных слаг, в случае существования такого слаг.
    model = instance.__class__
    unique