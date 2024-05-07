import csv
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import random


def database_1(name):
    # Добавляем расширение файла
    name += '.csv'

    # Считываем базу данных
    filename = open(name, 'r')

    # Читаем файл как список словарей
    file = csv.DictReader(filename)

    # Записываем данные
    for col in file:
        list_1_dict = {}
        list_1_dict['Регион'] = col['Название']
        list_1_dict['Товар'] = col['Продукт']
        price_array_dict = {}
        for i in range(2001, 2024):
            price_array_dict[str(i)] = col[str(i)]
        list_1_dict['Цена'] = price_array_dict
        list_1.append(list_1_dict)


def database_2(name):
    # Добавляем расширение файла
    opening = name + '.csv'

    # Считываем базу данных
    filename = open(opening, 'r')

    # Читаем файл как список словарей
    file = csv.DictReader(filename)

    # Записываем данные
    for col in file:
        list_2_dict = {}
        list_2_dict['Регион'] = col['Название']
        price_array_dict = {}
        for i in range(2001, 2024):
            price_array_dict[str(i)] = col[str(i)]
        list_2_dict[name] = price_array_dict
        list_2.append(list_2_dict)


def database_3(name):
    # Добавляем расширение файла
    opening = name + '.csv'

    # Считываем базу данных
    filename = open(opening, 'r')

    # Читаем файл как список словарей
    file = csv.DictReader(filename)

    # Записываем данные
    for col in file:
        list_3_dict = {}
        list_3_dict['Регион'] = col['Название']
        price_array_dict = {}
        for i in range(2001, 2024):
            price_array_dict[str(i)] = col[str(i)]
        list_3_dict[name] = price_array_dict
        list_3.append(list_3_dict)


def graphics(region, year):
    # Списки данных для графиков
    info_1 = []
    info_2 = []
    info_3 = []
    info_4 = []

    # Выбор подходящих пользавателю данных о зарплатах
    for col in list_2:
        if col['Регион'] == region:
            info_1 = col['Средняя зарплата']
        if col['Средняя зарплата'][year] == '':
            info_2.append(0)
        else:
            info_2.append(float(col['Средняя зарплата'][year]))

    # Выбор подходящих пользавателю данных о стоимости питания
    for col in list_3:
        if col['Регион'] == region:
            info_3 = col['Стоимость питания']
        if col['Стоимость питания'][year] == '':
            info_4.append(0)
        else:
            info_4.append(float(col['Стоимость питания'][year].replace(',', '.')))

    # Преобразуем данные для первого графика
    x_1 = list(info_1.keys())
    y_1 = list(info_1.values())
    for i in range(len(x_1)):
        x_1[i] = float(x_1[i])
        y_1[i] = float(y_1[i])

    # Преобразуем данные для второго графика
    x_2 = []
    y_2 = info_2
    for i in range(len(info_2)):
        x_2.append(i + 1)

    # Преобразуем данные для третьего графика
    x_3 = list(info_3.keys())
    y_3 = list(info_3.values())
    for i in range(len(x_3)):
        x_3[i] = float(x_3[i])
        y_3[i] = float(y_3[i].replace(',', '.'))

    # Преобразуем данные для четвёртого графика
    x_4 = []
    y_4 = info_4
    for i in range(len(info_4)):
        x_4.append(i + 1)

    # Графики
    plt.figure('Графики')

    # Первый график
    plt.subplot(2, 2, 1)
    plt.plot(x_1, y_1, color='#ee00ff')
    plt.title("Зарплата " + region)
    plt.xlabel('Год')
    plt.ylabel('Зарплата')

    # Второй график
    plt.subplot(2, 2, 2)
    plt.bar(x_2, y_2, color='#22ff00')  # Построение второго графика
    plt.title('Зарплата по регионам в ' + year + ' году')
    plt.xlabel('Регион')
    plt.ylabel('Зарплата')

    # Третий график
    plt.subplot(2, 2, 3)
    plt.scatter(x_3, y_3, color='#ff0066')  # Строим график
    plt.title("Стоимость продуктов " + region)
    plt.xlabel('Год')
    plt.ylabel('Стоимость продуктов')

    # Четвёртый график
    plt.subplot(2, 2, 4)
    plt.bar(x_4, y_4, color='blue')  # Построение второго графика
    plt.title('Стоимость минимального набора продуктов')
    plt.xlabel('Регион')
    plt.ylabel('Стоимость продуктов')

    # Выодим график на экран
    plt.show()


def graphic_product(a):
    name = random.randint(0, 352)
    # Данные для первого графика
    x_1 = []
    y_1 = [0] * 23
    for i in range(23):
        x_1.append(2001 + i)
    for col in list_1:
        if col['Товар'] == list_1[name]['Товар']:
            for el in range(23):
                if col['Цена'][str(2001 + el)] != '':
                    y_1[el] += float(col['Цена'][str(2001 + el)].replace(',', '.'))
    for i in range(23):
        y_1[i] /= 23

    # Данные для второго графика
    x_2 = []
    y_2 = []
    i = 1
    for col in list_1:
        if col['Товар'] == list_1[name]['Товар']:
            x_2.append(i)
            i = i + 1
            if col['Цена']['2010'] != '':
                y_2.append(float(col['Цена']['2010'].replace(',', '.')))
            else:
                y_2.append(0)

    # Строим первый график
    plt.figure('Графики')
    plt.subplot(1, 2, 1)
    plt.plot(x_1, y_1, color='#ee00ff')  # Строим график
    plt.title("Средняя цена товара по России")
    plt.xlabel('Год')
    plt.ylabel('Цена')

    # Строим второй график
    plt.subplot(1, 2, 2)
    plt.bar(x_2, y_2, color='#22ff00')  # Построение второго графика
    plt.title('Средняя цена продукта по регионам')
    plt.xlabel('Регион')
    plt.ylabel('Цена')

    # Выводим окно с графиками
    plt.show()


def reference(window):
    # Создание сообщения в справке
    message = ''
    for i in range(len(list_2)):
        message += str(i + 1) + '-' + list_2[i]['Регион'] + ' '

    # Новое окно - справка
    new_window = Toplevel(window)
    new_window.title("Справка")

    # Вывод текста
    message = StringVar(value=message)
    listbox = Listbox(new_window, listvariable=message, height=20, width=50)
    listbox.pack(side=LEFT, fill=BOTH, expand=1)

    # Прокрутка
    scrollbar = ttk.Scrollbar(new_window, orient="vertical", command=listbox.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    listbox["yscrollcommand"] = scrollbar.set


def menu(window):
    # Создание меню и подменю окна
    main_menu = Menu()
    file_menu = Menu()
    settings_menu = Menu()
    settings_menu_1 = Menu()
    settings_menu_2 = Menu()
    settings_menu_3 = Menu()
    settings_menu_4 = Menu()
    settings_menu_5 = Menu()
    settings_menu_6 = Menu()
    settings_menu_7 = Menu()
    settings_menu_8 = Menu()
    settings_menu_9 = Menu()
    settings_menu_10 = Menu()
    settings_menu_11 = Menu()
    settings_menu_12 = Menu()
    settings_menu_13 = Menu()
    settings_menu_14 = Menu()
    settings = Menu()

    # Сортировка товаров по подменю
    for el in range(21):
        settings_menu.add_command(label=list_1[el]['Товар'],
                                  command=lambda: graphic_product(list_1[el]['Товар']))
    for el in range(21, 36):
        settings_menu_1.add_command(label=list_1[el]['Товар'],
                                    command=lambda: graphic_product(list_1[el]['Товар']))
    for el in range(36, 58):
        settings_menu_2.add_command(label=list_1[el]['Товар'],
                                    command=lambda: graphic_product(list_1[el]['Товар']))
    for el in range(58, 65):
        settings_menu_3.add_command(label=list_1[el]['Товар'],
                                    command=lambda: graphic_product(list_1[el]['Товар']))
    for el in range(66, 80):
        settings_menu_4.add_command(label=list_1[el]['Товар'],
                                    command=lambda: graphic_product(list_1[el]['Товар']))
    for el in range(80, 85):
        settings_menu_5.add_command(label=list_1[el]['Товар'],
                                    command=lambda: graphic_product(list_1[el]['Товар']))
    for el in range(85, 89):
        settings_menu_6.add_command(label=list_1[el]['Товар'],
                                    command=lambda: graphic_product(list_1[el]['Товар']))
    for el in range(89, 106):
        settings_menu_7.add_command(label=list_1[el]['Товар'],
                                    command=lambda: graphic_product(list_1[el]['Товар']))
    for el in range(106, 124):
        settings_menu_3.add_command(label=list_1[el]['Товар'],
                                    command=lambda: graphic_product(list_1[el]['Товар']))
    for el in range(124, 136):
        settings_menu_5.add_command(label=list_1[el]['Товар'],
                                    command=lambda: graphic_product(list_1[el]['Товар']))
    settings_menu_2.add_command(label=list_1[136]['Товар'],
                                command=lambda: graphic_product(list_1[136]['Товар']))
    for el in range(137, 144):
        settings_menu_8.add_command(label=list_1[el]['Товар'],
                                    command=lambda: graphic_product(list_1[el]['Товар']))
    for el in range(144, 151):
        settings_menu_9.add_command(label=list_1[el]['Товар'],
                                    command=lambda: graphic_product(list_1[el]['Товар']))
    for el in range(151, 161):
        settings_menu_10.add_command(label=list_1[el]['Товар'],
                                     command=lambda: graphic_product(list_1[el]['Товар']))
    for el in range(161, 179):
        settings_menu_11.add_command(label=list_1[el]['Товар'],
                                     command=lambda: graphic_product(list_1[el]['Товар']))
    for el in range(179, 189):
        settings_menu_12.add_command(label=list_1[el]['Товар'],
                                     command=lambda: graphic_product(list_1[el]['Товар']))
    settings_menu_11.add_command(label=list_1[189]['Товар'],
                                 command=lambda: graphic_product(list_1[189]['Товар']))
    settings_menu_11.add_command(label=list_1[190]['Товар'],
                                 command=lambda: graphic_product(list_1[190]['Товар']))
    for el in range(191, 200):
        settings_menu_12.add_command(label=list_1[el]['Товар'],
                                     command=lambda: graphic_product(list_1[el]['Товар']))
    for el in range(200, 206):
        settings_menu_9.add_command(label=list_1[el]['Товар'],
                                    command=lambda: graphic_product(list_1[el]['Товар']))
    for el in range(207, 209):
        settings_menu_10.add_command(label=list_1[el]['Товар'],
                                     command=lambda: graphic_product(list_1[el]['Товар']))
    for el in range(209, 211):
        settings_menu_11.add_command(label=list_1[el]['Товар'],
                                     command=lambda: graphic_product(list_1[el]['Товар']))
    settings_menu_12.add_command(label=list_1[211]['Товар'],
                                 command=lambda: graphic_product(list_1[211]['Товар']))
    settings_menu_10.add_command(label=list_1[212]['Товар'],
                                 command=lambda: graphic_product(list_1[212]['Товар']))
    for el in range(213, 215):
        settings_menu_12.add_command(label=list_1[el]['Товар'],
                                     command=lambda: graphic_product(list_1[el]['Товар']))
    settings_menu_10.add_command(label=list_1[215]['Товар'],
                                 command=lambda: graphic_product(list_1[el]['Товар']))
    settings_menu_11.add_command(label=list_1[216]['Товар'],
                                 command=lambda: graphic_product(list_1[el]['Товар']))
    for el in range(255, 271):
        settings_menu_13.add_command(label=list_1[el]['Товар'],
                                     command=lambda: graphic_product(list_1[el]['Товар']))
    for el in range(290, 325):
        settings_menu_14.add_command(label=list_1[el]['Товар'],
                                     command=lambda: graphic_product(list_1[el]['Товар']))

    # Сортировка товаров по меню
    settings.add_cascade(label="Мужская",
                         menu=settings_menu_10)
    settings.add_cascade(label="Женская",
                         menu=settings_menu_11)
    settings.add_cascade(label="Детская",
                         menu=settings_menu_12)

    # Сортировка товаров по меню
    file_menu.add_cascade(label="Мясо", menu=settings_menu)
    file_menu.add_cascade(label="Рыба", menu=settings_menu_1)
    file_menu.add_cascade(label="Молочная продукция", menu=settings_menu_2)
    file_menu.add_cascade(label="Овощи и фрукты", menu=settings_menu_3)
    file_menu.add_cascade(label=list_1[65]['Товар'],
                          command=lambda: graphic_product(list_1[65]['Товар']))
    file_menu.add_cascade(label="Сладости", menu=settings_menu_4)
    file_menu.add_cascade(label="Напитки", menu=settings_menu_5)
    file_menu.add_cascade(label="Специи", menu=settings_menu_6)
    file_menu.add_cascade(label="Злаки и хлеб", menu=settings_menu_7)
    file_menu.add_cascade(label="Общественное питание", menu=settings_menu_8)
    file_menu.add_cascade(label="Ткани", menu=settings_menu_9)
    file_menu.add_cascade(label="Одежда", menu=settings)
    file_menu.add_cascade(label="Гигиена", menu=settings_menu_13)
    file_menu.add_cascade(label="Мебель", menu=settings_menu_14)

    file_menu.add_separator()
    file_menu.add_command(label="Выход")

    # Вывод меню
    main_menu.add_cascade(label="Товары", menu=file_menu)
    main_menu.add_cascade(label="Справка", command=lambda: reference(window))

    return main_menu


def interface():
    # Первоначальная настройка окна
    window = ThemedTk(theme="Kroc")
    window.title('Исследование уровня доходов и характера расходов в регионах России')
    window['bg'] = '#dc90f5'
    window.geometry('1000x600')
    window.option_add("*tearOff", FALSE)

    # Область выделенная под ввод и управление показа
    frame = Frame(
        window,
        padx=10,
        pady=10,
        bg='#ffb700'
    )
    frame.pack(expand=True)

    # Поле ввода региона
    write_region = Label(
        frame,
        bg='#ffb700',
        text="Введите регион:   "
    )
    write_region.grid(row=3, column=1)
    user_region = Entry(
        frame,
    )
    user_region.grid(row=3, column=2, pady=5)

    # Поле ввода года
    write_year = Label(
        frame,
        bg='#ffb700',
        text="Введите год:  ",
    )
    write_year.grid(row=4, column=1)
    user_year = Entry(
        frame,
    )
    user_year.grid(row=4, column=2, pady=5)

    # Кнопка показа статистики
    button = ttk.Button(
        frame,
        text='Показать статистику',
        command=lambda: graphics(user_region.get(),
                                 user_year.get())
    )
    button.grid(row=5, column=2)

    # Картинка
    canvas = Canvas(bg='#dc90f5',
                    width=974,
                    height=500)
    canvas.pack(anchor=CENTER)
    image = PhotoImage(file="region.png")
    canvas.create_image(10, 10,
                        anchor=NW,
                        image=image)

    # Создание меню
    window.config(menu=menu(window))

    # Показ окна
    window.mainloop()


# Вводим список для записи информации из баз данных
list_1 = []
list_2 = []
list_3 = []

# Записываем первую базу данных
database_1("Товары_1")
database_1("Товары_2")

# Записываем вторую базу данных
database_2('Средняя зарплата')
database_3('Стоимость питания')

# Вывод окна приложения
interface()
