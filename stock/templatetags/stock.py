
from django import template

register = template.Library()


@register.filter
def is_category_shown(products, current_index):
    try:
        return (
            products[int(current_index) - 1].category_id !=
            products[current_index].category_id
        )
    except (IndexError, AssertionError, ValueError):
        return True
