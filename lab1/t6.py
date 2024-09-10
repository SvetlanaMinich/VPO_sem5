import requests
from urllib.parse import urlparse
import os

def task6(url: str, save_dir_path: str):
    """
    Функция для скачивания файла с указанного URL и сохранения его в указанную директорию.

    Аргументы:
    url -- URL для скачивания файла.
    save_dir_path -- Путь к папке, в которой будет сохранён файл.
    """

    # Проверяем корректность URL, разбирая его на компоненты
    try:
        parse_res = urlparse(url=url)  # Разбираем URL на компоненты
        if not parse_res.scheme or not parse_res.netloc:  # Проверяем наличие схемы (http/https) и хоста
            print("ОШИБКА. Некорректный URL.")
            return
    except Exception:
        print(f"ОШИБКА. Невозможно обработать URL.")
        return

    # Проверяем, существует ли указанная папка для сохранения файла
    if not os.path.isdir(save_dir_path):  # Проверяем, что директория существует
        print(f"ОШИБКА. Указанная папка '{save_dir_path}' не существует.")
        return

    # Извлекаем имя файла из URL
    file_name = os.path.basename(parse_res.path)  # Извлекаем имя файла из пути в URL
    if not file_name:  # Если не удается извлечь имя файла, выводим ошибку
        print("ОШИБКА. Невозможно извлечь имя файла из URL.")
        return

    # Формируем полный путь для сохранения файла
    file_path = os.path.join(save_dir_path, file_name)  # Полный путь для сохранения файла

    # Попытка загрузки файла с URL
    try:
        # Скачиваем файл по частям, чтобы не загружать его целиком в память
        response = requests.get(url, stream=True)  # Запрос на загрузку файла с URL
        response.raise_for_status()  # Проверяем статус ответа. Если ошибка, вызываем исключение
    except Exception:
        print(f"ОШИБКА. Не удалось скачать файл.")  # Если возникла ошибка при загрузке, выводим сообщение
        return

    # Сохранение файла на локальный диск
    try:
        with open(file_path, 'wb') as file:  # Открываем файл для записи в бинарном режиме
            for chunk in response.iter_content(chunk_size=8192):  # Загружаем файл по частям (8КБ за раз)
                file.write(chunk)  # Записываем каждую часть в файл
        print(f"Файл успешно сохранён в: {file_path}")  # Сообщение о успешном сохранении файла
    except Exception:
        print(f"ОШИБКА. Не удалось сохранить файл.")  # Если не удалось сохранить файл, выводим сообщение об ошибке
        return


# task6('https://filesampleshub.com/download/document/txt/sample1.txt', 
#       r'C:\sem5\vpo\lab1\t5_dir')

import unittest
from unittest.mock import patch, MagicMock

class TestTask6(unittest.TestCase):
    @patch('requests.get')
    @patch('os.path.isdir')
    @patch('builtins.print')
    def test_task6_success(self, mock_print, mock_isdir, mock_get):
        """Тестирует успешное скачивание и сохранение файла."""
        mock_isdir.return_value = True
        mock_get.return_value = MagicMock(status_code=200, iter_content=MagicMock(return_value=[b'content']))
        
        with patch('builtins.open', unittest.mock.mock_open()) as mock_open:
            task6('https://example.com/file.txt', r'C:\sem5\vpo\lab1\t5_dir')
            mock_open.assert_called_once_with(r'C:\sem5\vpo\lab1\t5_dir\file.txt', 'wb')
            mock_print.assert_called_once_with("Файл успешно сохранён в: C:\\sem5\\vpo\\lab1\\t5_dir\\file.txt")

    @patch('requests.get')
    @patch('os.path.isdir')
    @patch('builtins.print')
    def test_task6_invalid_url(self, mock_print, mock_isdir, mock_get):
        """Тестирует обработку некорректного URL."""
        mock_isdir.return_value = True
        task6('://example.com/file.txt', r'C:\sem5\vpo\lab1\t5_dir')
        mock_print.assert_called_once_with("ОШИБКА. Некорректный URL.")
    
    @patch('requests.get')
    @patch('os.path.isdir')
    @patch('builtins.print')
    def test_task6_non_existent_directory(self, mock_print, mock_isdir, mock_get):
        """Тестирует обработку несуществующей директории."""
        mock_isdir.return_value = False
        task6('https://example.com/file.txt', '/non_existent_dir')
        mock_print.assert_called_once_with("ОШИБКА. Указанная папка '/non_existent_dir' не существует.")
    
    @patch('requests.get')
    @patch('os.path.isdir')
    @patch('builtins.print')
    def test_task6_no_file_name_in_url(self, mock_print, mock_isdir, mock_get):
        """Тестирует URL без имени файла."""
        mock_isdir.return_value = True
        task6('https://example.com/', r'C:\sem5\vpo\lab1\t5_dir')
        mock_print.assert_called_once_with("ОШИБКА. Невозможно извлечь имя файла из URL.")
    
    @patch('requests.get')
    @patch('os.path.isdir')
    @patch('builtins.print')
    def test_task6_download_failure(self, mock_print, mock_isdir, mock_get):
        """Тестирует обработку ошибки при загрузке файла."""
        mock_isdir.return_value = True
        mock_get.side_effect = requests.exceptions.RequestException
        task6('https://example.com/file.txt', r'C:\sem5\vpo\lab1\t5_dir')
        mock_print.assert_called_once_with("ОШИБКА. Не удалось скачать файл.")

if __name__ == '__main__':
    unittest.main()