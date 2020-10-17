from django import template

register = template.Library()


@register.filter(name='count')
def count(queryset):
    return len(queryset)