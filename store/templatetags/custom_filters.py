from django import template
import locale

locale.setlocale(locale.LC_ALL, 'en_US.utf8')
register = template.Library()

@register.filter()
def currency(value):
    return locale.currency(value, grouping=True)

