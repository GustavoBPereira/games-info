from django import forms

from games_info.crawler import accepted_currency


class SearchGameForm(forms.Form):
    CHOICES = [(currency, accepted_currency[currency]['name']) for currency in accepted_currency]

    game_search = forms.CharField(max_length=64)
    currency = forms.ChoiceField(choices=CHOICES)
    game_search.widget.attrs.update(
        {'class': 'form-control', 'id': 'search-input', 'aria-label': 'Game Name', 'autocomplete': 'off'}
    )
    currency.widget.attrs.update(
        {'class': 'form-control', 'id': 'currency-input'}
    )
