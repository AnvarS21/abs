import peewee
import random
from models import Category, Product

def add_cotegory(name):
    try:
        name = name.lower().strip()
        data = Category(title=name)
        data.save()
        print(f'Сохранили категорию {name}!')
    except (peewee.IntegrityError, peewee.IntegrityError):
        print(f'Такая категория как {name} уже существует!')

# add_cotegory('    Платья')
# add_cotegory('Джинсы')
# add_cotegory('Футболки')
# add_cotegory('Свитеры')
# add_cotegory('Обувь')

def add_product(name, price, category_name):
    try:
        category_id = Category.get(title=category_name.lower().strip())
    except peewee.DoesNotExist:
        category_id = None

    if category_id:
        data = Product(title=name, price=price, category_id=category_id)
        data.save()
        print(f'Сохранили товар {name}!')
    else:
        print(f'Категории {category_name} не сущетсвует!')

# add_product('Zara t-shirt', 300, 'футболки')
# add_product('Supreme t-shirt', 200, 'футболки')
# add_product('Polo t-shirt', 400, 'футболки')
# add_product('Aygen 58', 1000, 'платья')
# add_product('Platye 48', 1100, 'платья')
# add_product('Lewys', 500, 'джинсы')
# add_product('Nike Air Jordan', 1500, 'обувь')
# add_product('Polo', 700, 'свитеры')
# add_product('Polo', 700, 'брюки')


##---------------##---------------##---------------##---------------##---------------##---------------##---------------
# Добавление новых данных

add_cotegory('cars')
add_cotegory('telephons')


# with open('files/cars.txt', 'r') as file:
#     ls = file.readlines()
#     for x in ls:
#         name = x.strip()
#         price = random.randint(5000, 20000)
#         add_product(name, price, 'cars')

with open('files/telefon.txt', 'r') as file:
    ls = file.readlines()
    for x in ls:
        name = 'анвар лох'
        price = random.randint(200, 1300)
        add_product(name, price, 'telephons')


