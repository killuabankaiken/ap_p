import tkinter as tk
from mysql.connector import connect
import tkinter.ttk as ttk
connection = connect(host = 'localhost', username='root', password='433272as', database='myshop')
c = connection.cursor()
c.execute("SELECT * FROM products")
result = c.fetchall()

app = tk.Tk()
app.title("Список товаров")

tv = ttk.Treeview(app)
tv.pack()

tv['columns'] = ('Название', 'Описание', 'Количество', 'Цена')

tv.column('#0', width=0, stretch=tk.NO)
tv.column('Название', anchor=tk.CENTER, width=200)
tv.column('Описание', anchor=tk.CENTER, width=200)
tv.column('Количество', anchor=tk.CENTER, width=100)
tv.column('Цена', anchor=tk.CENTER, width=100)

tv.heading('#0', text='', anchor=tk.CENTER)
tv.heading('Название', text='Название', anchor=tk.CENTER)
tv.heading('Описание', text='Описание', anchor=tk.CENTER)
tv.heading('Количество', text='Количество', anchor=tk.CENTER)
tv.heading('Цена', text='Цена', anchor=tk.CENTER)

for row in result:
    tv.insert('', 'end', text='', values=row)


def add_product():
    name = entry_name.get()
    description = entry_description.get()
    quantity = entry_quantity.get()
    price = entry_price.get()

    query = "INSERT INTO products (name, description, quantity, price) VALUES (%s, %s, %s, %s)"
    values = (name, description, quantity, price)
    c.execute(query, values)
    connection.commit()

    tv.insert('', 'end', text='', values=(name, description, quantity, price))

    entry_name.delete(0, tk.END)
    entry_description.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    entry_price.delete(0, tk.END)

frame_add = tk.Frame(app)
frame_add.pack(pady=10)

label_name = tk.Label(frame_add, text='Название:')
label_name.grid(row=0, column=0)
entry_name = tk.Entry(frame_add)
entry_name.grid(row=0, column=1)

label_description = tk.Label(frame_add, text='Описание:')
label_description.grid(row=1, column=0)
entry_description = tk.Entry(frame_add)
entry_description.grid(row=1, column=1)

label_quantity = tk.Label(frame_add, text='Количество:')
label_quantity.grid(row=2, column=0)
entry_quantity = tk.Entry(frame_add)
entry_quantity.grid(row=2, column=1)

label_price = tk.Label(frame_add, text='Цена:')
label_price.grid(row=3, column=0)
entry_price = tk.Entry(frame_add)
entry_price.grid(row=3, column=1)

button_add = tk.Button(frame_add, text='Добавить товар', command=add_product)
button_add.grid(row=4, columnspan=2)
app.mainloop()
