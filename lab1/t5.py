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



import unittest
from unittest.mock import patch

class TestTask5(unittest.TestCase):
    @patch('os.path.isdir')
    @patch('os.walk')
    @patch('builtins.print')
    def test_task5_valid(self, mock_print, mock_walk, mock_isdir):
        """Тестирует корректный поиск файлов с заданным расширением."""
        mock_isdir.return_value = True
        mock_walk.return_value = [
            ('/test_dir', [], ['file1.mp3', 'file2.txt']),
            ('/test_dir/subdir', [], ['file3.mp3'])
        ]
        
        task5('/test_dir', 'mp3')
        
        expected_calls = [
            unittest.mock.call(r'/test_dir\file1.mp3'),
            unittest.mock.call(r'/test_dir/subdir\file3.mp3')
        ]
        mock_print.assert_has_calls(expected_calls)

    @patch('os.path.isdir')
    @patch('builtins.print')
    def test_task5_invalid_extension(self, mock_print, mock_isdir):
        """Тестирует случай с некорректным расширением файла."""
        mock_isdir.return_value = True
        
        task5('/test_dir', 'mp3?')
        
        mock_print.assert_called_with('ОШИБКА. Расширение не должно содержать пробелов и специальных символов.')

    @patch('os.path.isdir')
    @patch('builtins.print')
    def test_task5_non_existent_directory(self, mock_print, mock_isdir):
        """Тестирует случай с несуществующей директорией."""
        mock_isdir.return_value = False
        
        task5('/non_existent_dir', 'mp3')
        
        mock_print.assert_called_with("ОШИБКА: Указанная папка '/non_existent_dir' не существует.")

    @patch('os.path.isdir')
    @patch('os.walk')
    @patch('builtins.print')
    def test_task5_no_files_with_extension(self, mock_print, mock_walk, mock_isdir):
        """Тестирует случай, когда файлы с указанным расширением не найдены."""
        mock_isdir.return_value = True
        mock_walk.return_value = [
            ('/test_dir', [], ['file1.txt']),
            ('/test_dir/subdir', [], ['file2.txt'])
        ]
        
        task5('/test_dir', 'mp3')
        
        mock_print.assert_called_with('Файлы с расширением .mp3 в папке /test_dir не найдены.')

if __name__ == '__main__':
    unittest.main()
