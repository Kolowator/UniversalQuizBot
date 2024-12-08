import json

quiz_data = [
    {
        'question': 'Что такое Python?',
        'options': ['Язык программирования', 'Тип данных', 'Музыкальный инструмент', 'Змея на английском'],
        'correct_option': 0
    },
    {
        'question': 'Какой тип данных используется для хранения целых чисел?',
        'options': ['int', 'float', 'str', 'natural'],
        'correct_option': 0
    },
    {
        'question': 'Для вывода сообщений на экран консоли используется функция:',
        'options': ['input()', 'int()', 'print()', 'string()'],
        'correct_option': 2
    },
    {
        'question': 'Для преобразования данных в число используется функция:',
        'options': ['input()', 'int()', 'print()', 'string()'],
        'correct_option': 1
    },
    {
        'question': 'Для преобразования данных в текст используется функция:',
        'options': ['input()', 'int()', 'print()', 'string()'],
        'correct_option': 3
    },
    {
        'question': 'Какой из значков используется для возведения в степень?',
        'options': ['*', '^', '^^', '**'],
        'correct_option': 3
    },
    {
        'question': 'Какой тип данных хранит вещественные (нецелые) числа?',
        'options': ['int', 'float', 'str', 'natural'],
        'correct_option': 1
    },
    {
        'question': 'Как обозначается оператор присваивания в Python?',
        'options': ['=', '==', '=!'],
        'correct_option': 0
    },
    {
        'question': 'С помощью какой команды подключаются модули в Python?',
        'options': ['input', 'open', 'include', 'open'],
        'correct_option': 0
    },
    {
        'question': 'С помощью какого ключевого слова объявляются функции в Python?',
        'options': ['del', 'main', 'function', 'def'],
        'correct_option': 3
    },
    
    # Добавьте другие вопросы
]

filename = 'quiz_data.json'

with open(filename, 'w', encoding='utf-8') as file:
    # Преобразуем данные в строку JSON и записываем в файл
    json.dump(quiz_data, file, ensure_ascii=False, indent=4)