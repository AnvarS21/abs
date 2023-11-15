# from models import Product, Category
# import peewee

# Обновление данных
# query = Product.update(price=500).where(Product.title == 'Zara t-shirt')
# print(query)
# query.execute()

# query = Product.update(price=(Product.price + Product.price * 0.5))
# #Увеличиваем всем товарам цену
# query.execute()

##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----
# Удаление данных
# Удаление через запрос
# query = Product.delete().where(Product.id == 32 or Product.id == 31)
# query.execute()

##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----


# Удаление через объект

# product = Product.get(id=26)
# print(product, product.title)
# product.delete_instance()

# query = Category.delete().where(Category.title == 'анвар лох')
# query.execute()
