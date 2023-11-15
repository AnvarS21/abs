import peewee
from models import Product, Category

def get_all_categories():
    return Category.select()

def get_all_products():
    return Product.select()


# categories = get_all_categories()
# print('Категории в БД: ')
# for x in categories:
#     print(x)
#     print(x.title.title())
#     print(x.created_at.strftime('%Y-%m-%d -> %H:%M:%S'))
#     print()

# product = get_all_products()
# print('Все товары в БД: ')
# sum_price = 0
# for x in product:
#     print(f'{x.title} -> {x.price} -> {x.category_id.title}')
#     print()
#     sum_price += x.price
# print(f'AVG price: {sum_price / len(product)}$')


# products = get_all_products()
# category = int(input('Введите категорию (6-платьяб 7-джинсыб 8-футболкиб 9-свитерыб 10-обувь): '))
# for x in products:
#     if x.category_id.category_id == category:
#         print(x.title, x.price, x.category_id.title)

# categoty_name = input('Введите название категории: ').lower().strip()

# try:
#     category = Category.get(title=categoty_name)
#     print(category, category.title)
# except peewee.DoesNotExist:
#     print('Такой категории нет!')

# else:
#     for product in category.products:  #related name
#         print(f'Title: {product.title}, Price: {product.price}, category: {product.category_id.title}')


