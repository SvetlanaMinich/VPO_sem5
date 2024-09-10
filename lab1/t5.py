import os

def task5(dir: str, ext: str):
    """
    Функция для поиска файлов с указанным расширением в заданной папке и её подпапках.
    
    Аргументы:
    dir -- путь к папке, в которой будет производиться поиск.
    ext -- расширение файлов для поиска.
    """
    
    # Проверка, что расширение не содержит пробелов или специальных символов
    for i in ext:
        if not i.isalpha() and not i.isdigit():
            print('ОШИБКА. Расширение не должно содержать пробелов и специальных символов.')
            return
    
    # Если расширение не начинается с точки, добавляем её
    if not ext.startswith('.'):
        ext = '.' + ext
    
    # Проверка, что указанная директория существует
    if not os.path.isdir(dir):
        print(f"ОШИБКА: Указанная папка '{dir}' не существует.")
        return
    
    files_num = 0
    # Рекурсивный обход папки и её подпапок с помощью os.walk
    for root, _, files in os.walk(dir):
        for name in files:
            if name.endswith(ext):
                # Вывод полного пути к каждому найденному файлу с нужным расширением
                print(os.path.join(root, name))
                files_num += 1
                
    if files_num == 0:
        print(f'Файлы с расширением {ext} в папке {dir} не найдены.')


task5(r'C:\sem5\vpo\lab1\t5_dir', 'mp3')