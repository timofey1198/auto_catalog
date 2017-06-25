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


def get_cars():
    """
    get_cars()
    """
    pass


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
    
    #Доделать


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


def new_car(firm, model, price, engine_type, engine_volume,
             engine_power, engine_moment,
             engine_fuel_consumption_dealer, transport_tax):
    """
    new_car
    """
    
    if is_exist_car(firm, model):
        raise ValueError('Машина такой фирмы и модели уже существует')
    
    conn = sqlite3.connect(main_path + '/data/cars.db')
    cursor = conn.cursor()
    cursor.execute("""
                   INSERT INTO cars (firm, model, price, engine_type,
                                     engine_volume, engine_power, engine_moment,
                                     engine_fuel_consumption_dealer, 
                                     transport_tax
                                     ) 
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                   """, [firm, model, price, engine_type, engine_volume, 
                        engine_power, engine_moment,
                        engine_fuel_consumption_dealer, transport_tax]
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
    conn = sqlite3.connect(main_path + '/data/cars.db')
    cursor = conn.cursor()
    cursor.execute("""
                   SELECT * FROM cars
                   """)
    print(cursor.fetchall())
    print(is_exist_car('test', 't_1'))