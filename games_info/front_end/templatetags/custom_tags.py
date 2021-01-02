from django import template
from django.utils.safestring import mark_safe

register = template.Library()


def render_price(value):
    if value['is_free']:
        return 'Free to Play'
    else:
        if int(value['discount_percent']) == 0:
            return value['final_formatted']
        else:
            text = f'<span class="percent_discount">{value["discount_percent"]}% </span>' \
                   f'<span class="risked_initial"><s>{value["initial_formatted"]}</s></span>' \
                   f'<span class="final_formatted">{value["final_formatted"]}</span>'
            return mark_safe(text)


register.filter('render_price', render_price)
