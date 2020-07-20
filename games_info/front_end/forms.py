from django import forms


class SearchGameForm(forms.Form):
    game_search = forms.CharField(max_length=64)

    game_search.widget.attrs.update(
        {'class': 'form-control', 'id': 'search-input', 'aria-label': 'Game Name', 'autocomplete': 'off'}
    )
