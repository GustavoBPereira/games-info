from django import forms


class SearchGameForm(forms.Form):
    CHOICES = choices = (
        ('us', 'U.S.Dollar'), ('eu', 'Euro'), ('ar', 'Argentine Peso'), ('au', 'Australian Dollar'),
        ('br', 'Brazilian Real'), ('uk', 'British Pound'), ('ca', 'Canadian Dollar'), ('cl', 'Chilean Peso'),
        ('cn', 'Chinese Yuan'), ('az', 'CIS - U.S.Dollar'), ('co', 'Colombian Peso'), ('cr', 'Costa Rican Colon'),
        ('hk', 'Hong Kong Dollar'), ('in', 'Indian Rupee'), ('id', 'Indonesian Rupiah'), ('il', 'Israeli New Shekel'),
        ('jp', 'Japanese Yen'), ('kz', 'Kazakhstani Tenge'), ('kw', 'Kuwaiti Dinar'), ('my', 'Malaysian Ringgit'),
        ('mx', 'Mexican Peso'), ('nz', 'New Zealand Dollar'), ('no', 'Norwegian Krone'), ('pe', 'Peruvian Sol'),
        ('ph', 'Philippine Peso'), ('pl', 'Polish Zloty'), ('qa', 'Qatari Riyal'), ('ru', 'Russian Ruble'),
        ('sa', 'Saudi Riyal'), ('sg', 'Singapore Dollar'), ('za', 'South African Rand'), ('pk', 'South Asia - USD'),
        ('kr', 'South Korean Won'), ('ch', 'Swiss Franc'), ('tw', 'Taiwan Dollar'), ('th', 'Thai Baht'),
        ('tr', 'Turkish Lira'), ('ae', 'U.A.E.Dirham'), ('ua', 'Ukrainian Hryvnia'), ('uy', 'Uruguayan Peso'),
        ('vn', 'Vietnamese Dong')
    )

    game_search = forms.CharField(max_length=64)
    currency = forms.ChoiceField(choices=CHOICES)
    game_search.widget.attrs.update(
        {'class': 'form-control', 'id': 'search-input', 'aria-label': 'Game Name', 'autocomplete': 'off'}
    )
    currency.widget.attrs.update(
        {'class': 'form-control', 'id': 'currency-input'}
    )
