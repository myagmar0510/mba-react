# cookbook/ingredients/schema.py
import graphene as g
from graphene_django.types import DjangoObjectType
# from graphene_django.filter import DjangoFilterConnectionField

from mba.models import Category, Ingredient

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient

class Query(object):
    ingredient_detail = g.Field(IngredientType,
        id = g.Int(),
    )

    def resolve_ingredient_detail(self, info, **kwagrs):
        _id = kwagrs.get('id')
        return Ingredient.objects.get(id=_id)