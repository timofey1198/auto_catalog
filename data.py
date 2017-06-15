# -*- coding: utf-8 -*-
import sqlite3


conn = sqlite3.connect(main_path + '/data/cars.db')
cursor = conn.cursor()
 
# Создание таблицы

cursor.execute("""CREATE TABLE name
                  (id integer primary key, chat_id integer, status text,
                   link text)
               """)
