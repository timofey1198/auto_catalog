# -*- coding: utf-8 -*-
import sqlite3
from os.path import dirname, realpath


main_path = dirname(realpath(__name__))
 
# Создание таблицы
'''
cursor.execute("""CREATE TABLE cars
                  (id integer primary key, firm text, model text, 
                   engine_type text, engine_volume integer, 
                   engine_power integer, engine_moment integer, 
                   engine_fuel_consumption_dealer float, 
                   engine_fuel_consumption_user float, 
                   engine_fuel_consumption_avg float, price integer, 
                   user_defined_expense integer, to_0_length integer,
                   to_0_price, to_1_length integer, to_1_price, 
                   to_2_length integer, to_2_price, 
                   to_3_length integer, to_3_price, 
                   to_4_length integer, to_4_price, 
                   to_5_length integer, to_5_price, 
                   transport_tax integer)
               """)
'''


def car_info_to_html(car_dict):
    if car_dict['price'] == None:
        car_dict['price'] = 'Цена не указана'
    if car_dict['engine_type'] == None:
        car_dict['engine_type'] = 'Тип не указан'
    if car_dict['engine_volume'] == None:
        car_dict['engine_volume'] = 'Объем не указан'
    if car_dict['engine_power'] == None:
        car_dict['engine_power'] = 'Мощность не указана'
    avg_price = '-'
    html = """
    <a href="/cars?car={car_id}">
        <div class="news link_block">
            
                <h2>{firm}&nbsp{model} {price}/{price_per_year}</h2><br>
                Тип двигателя: {engine_type}<br>
                Объем двигателя: {engine_volume}<br>
                Мощность двигателя: {engine_power}<br>
            
        </div>
        </a>
        """.format(car_id = car_dict['id'],
                   firm = car_dict['firm'], model = car_dict['model'],
                   price = car_dict['price'], price_per_year = avg_price,
                   engine_type = car_dict['engine_type'],
                   engine_volume = car_dict['engine_volume'],
                   engine_power = car_dict['engine_power'])
    return html


def lists_cars_to_dicts(lists_cars):
    headers = ['id', 'firm', 'model', 'engine_type', 'engine_volume', 
               'engine_power', 'engine_moment', 
               'engine_fuel_consumption_dealer', 
               'engine_fuel_consumption_user', 
               'engine_fuel_consumption_avg', 'price', 
               'user_defined_expense',
               'to_0_length', 'to_0_price',
               'to_1_length', 'to_1_price', 
               'to_2_length', 'to_2_price', 
               'to_3_length', 'to_3_price', 
               'to_4_length', 'to_4_price', 
               'to_5_length', 'to_5_price', 
               'transport_tax']
    dicts_cars = []
    for list_car in lists_cars:
        dict_car = {}
        i = 0
        for key in headers:
            dict_car[key] = list_car[i]
            i = i + 1
        dicts_cars.append(dict_car)
    return dicts_cars


def get_cars():
    """
    get_cars()
    """
    conn = sqlite3.connect(main_path + '/data/cars.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cars')
    return lists_cars_to_dicts(cursor.fetchall())


def get_cars_by_interval(start_num, end_num):
    """
    get_cars_by_interval(start_num, end_num)
        start_num: integer number, the start of the interval
        end_num: integer number, the end of the interval
    """
    
    if type(start_num) != int or type(end_num) != int:
        raise TypeError('Тип аргументов не соответствует спецификации')
    if start_num > end_num:
        raise ValueError(
            'Значение начала промежутка больше, чем значение конца')
    if start_num < 1:
        start_num = 1
    
    conn = sqlite3.connect(main_path + '/data/cars.db')
    cursor = conn.cursor()
    cursor.execute('SELECT count(*) FROM cars')
    number_of_cars = cursor.fetchall()[0][0]
    
    if start_num > number_of_cars:
        return {}
    if end_num > number_of_cars:
        end_num = number_of_cars
    
    cursor.execute("""
                   SELECT * FROM cars
                   WHERE id >= ? AND id <= ?""",
                    [start_num, end_num]
                   )
    return lists_cars_to_dicts(cursor.fetchall())


def add_changings(model, field, value):
    conn = sqlite3.connect(main_path + '/data/cars.db')
    cursor = conn.cursor()
    #Доделать


def is_exist_car(firm, model):
    conn = sqlite3.connect(main_path + '/data/cars.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT count(*) FROM cars
        WHERE firm=? AND model=?
        """, [firm, model])
    return bool(cursor.fetchall()[0][0])


def get_main_info(car_id):
    conn = sqlite3.connect(main_path + '/data/cars.db')
    cursor = conn.cursor()
    cursor.execute('SELECT firm,model FROM cars WHERE id=?',
                   [car_id])
    answer = cursor.fetchall()
    if len(answer) > 0:
        return answer[0]
    else:
        return (None, None)


def new_car(firm, model, price, engine_type, engine_volume,
             engine_power, engine_moment,
             engine_fuel_consumption_dealer, transport_tax,
             user_defined_expense):
    """
    new_car
    """
    
    # Тут добавить проверку данных
    
    if is_exist_car(firm, model):
        raise ValueError('Машина такой фирмы и модели уже существует')
    
    conn = sqlite3.connect(main_path + '/data/cars.db')
    cursor = conn.cursor()
    cursor.execute("""
                   INSERT INTO cars (firm, model, price, engine_type,
                                     engine_volume, engine_power, engine_moment,
                                     engine_fuel_consumption_dealer, 
                                     transport_tax, user_defined_expense
                                     ) 
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                   """, [firm, model, price, engine_type, engine_volume, 
                        engine_power, engine_moment,
                        engine_fuel_consumption_dealer, transport_tax,
                        user_defined_expense]
                   )
    conn.commit()


'''
cursor.execute("""CREATE TABLE options
                  (id integer primary key, model text, 
                  
                  )
               """)
'''

# Написать readme.txt

if __name__ == '__main__':
    #new_car('test', 't_0')
    #conn = sqlite3.connect(main_path + '/data/cars.db')
    #cursor = conn.cursor()
    #cursor.execute("""
                   #SELECT * FROM cars
                   #""")
    #print(cursor.fetchall())
    #print(is_exist_car('test', 't_1'))
    print(get_main_info(-1))