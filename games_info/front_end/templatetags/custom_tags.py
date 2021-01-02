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


def render_languages(value):
    languages = value.split(',')
    text = ''
    fa_audio = ' <i class="fas fa-volume-up"></i>'
    for language in languages:
        text += f'<li class="list-group-item language-item"><p class="text-center language-item">' \
                f'{language.capitalize().replace("<strong>*</strong>", fa_audio)}' \
                f'</p></li>'

    return mark_safe(text)


register.filter('render_price', render_price)
register.filter('render_languages', render_languages)
