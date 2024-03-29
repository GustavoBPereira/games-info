# ALL_CURRENCIES = (
#     ('us', 'U.S.Dollar'), ('eu', 'Euro'), ('ar', 'Argentine Peso'), ('au', 'Australian Dollar'),
#     ('br', 'Brazilian Real'), ('uk', 'British Pound'), ('ca', 'Canadian Dollar'), ('cl', 'Chilean Peso'),
#     ('cn', 'Chinese Yuan'), ('az', 'CIS - U.S.Dollar'), ('co', 'Colombian Peso'), ('cr', 'Costa Rican Colon'),
#     ('hk', 'Hong Kong Dollar'), ('in', 'Indian Rupee'), ('id', 'Indonesian Rupiah'), ('il', 'Israeli New Shekel'),
#     ('jp', 'Japanese Yen'), ('kz', 'Kazakhstani Tenge'), ('kw', 'Kuwaiti Dinar'), ('my', 'Malaysian Ringgit'),
#     ('mx', 'Mexican Peso'), ('nz', 'New Zealand Dollar'), ('no', 'Norwegian Krone'), ('pe', 'Peruvian Sol'),
#     ('ph', 'Philippine Peso'), ('pl', 'Polish Zloty'), ('qa', 'Qatari Riyal'), ('ru', 'Russian Ruble'),
#     ('sa', 'Saudi Riyal'), ('sg', 'Singapore Dollar'), ('za', 'South African Rand'), ('pk', 'South Asia - USD'),
#     ('kr', 'South Korean Won'), ('ch', 'Swiss Franc'), ('tw', 'Taiwan Dollar'), ('th', 'Thai Baht'),
#     ('tr', 'Turkish Lira'), ('ae', 'U.A.E.Dirham'), ('ua', 'Ukrainian Hryvnia'), ('uy', 'Uruguayan Peso'),
#     ('vn', 'Vietnamese Dong')
# )


accepted_currency = {
    'br': {'language': 'brazilian', 'name': 'Brazilian Real', 'code': 'BRL'},
    'us': {'language': 'english', 'name': 'U.S.Dollar', 'code': 'USD'},
    'uk': {'language': 'english', 'name': 'British Pound', 'code': 'GBP'},
    'ar': {'language': 'spanish', 'name': 'Argentine Peso', 'code': 'ARS'},
}

headers = {
    'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
        ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}
