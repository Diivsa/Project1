import sqlite3
import tkinter as tk
from tkinter import ttk

# Создаем подключение к БД
conn = sqlite3.connect('employees.db')
c = conn.cursor()

# Создаем таблицу, если ее не существует
c.execute('''
          CREATE TABLE IF NOT EXISTS employees 
          (id INTEGER PRIMARY KEY AUTOINCREMENT, 
          name TEXT, 
          phone TEXT, 
          email TEXT, 
          salary REAL)
          ''')
conn.commit()

# Функция для добавления нового сотрудника в БД
def add_employee(name, phone, email, salary):
    c.execute('''INSERT INTO employees (name, phone, email, salary) VALUES (?, ?, ?, ?)''', (name, phone, email, salary))
    conn.commit()

# Функция для изменения информации о сотруднике в БД
def update_employee(id, name, phone, email, salary):
    c.execute('''UPDATE employees SET name=?, phone=?, email=?, salary=? WHERE id=?''', (name, phone, email, salary, id))
    conn.commit()

# Функция для удаления сотрудника из БД
def delete_employee(id):
    c.execute('''DELETE FROM employees WHERE id=?''', (id,))
    conn.commit()

# Функция для поиска сотрудника по ФИО
def search_employee(name):
    c.execute('''SELECT * FROM employees WHERE name LIKE ?''', ('%' + name + '%',))
    return c.fetchall()

# Графический интерфейс с использованием tkinter
root = tk.Tk()
root.title('Список сотрудников компании')

# Определение функций интерфейса (добавление, изменение, удаление, поиск)
# ...

# Создание виджета Treeview для вывода записей из БД
tree = ttk.Treeview(root, columns=('ID', 'Name', 'Phone', 'Email', 'Salary'), show='headings')
tree.heading('ID', text='ID')
tree.heading('Name', text='Name')
tree.heading('Phone', text='Phone')
tree.heading('Email', text='Email')
tree.heading('Salary', text='Salary')
tree.pack()

# Запуск графического интерфейса
root.mainloop()

# Закрытие соединения с БД
conn.close()