PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

price_list = PRICE_LIST.split()
items = price_list[::2]
str_prices = price_list[1::2]

prices = [int(price.replace('р', '')) for price in str_prices]

price_dict = dict(zip(items, prices))
print(price_dict)
