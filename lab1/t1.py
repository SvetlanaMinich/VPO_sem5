import random
import unittest

# Функция task1 возвращает строку, которая включает в себя
# сообщение "Hello, World!", затем "Andhiagain!", и восклицательные знаки,
# количество которых случайно выбирается в диапазоне от 5 до 50.
def task1() -> str:
    # Добавляем строку 'Hello, World!' и переходим на новую строку
    res_str = 'Hello, world!\n'  
    
    # Добавляем строку 'Andhiagain!' и снова переходим на новую строку
    res_str += 'Andhiagain!\n'  
    
    # Генерируем случайное количество восклицательных знаков (от 5 до 50)
    # и добавляем к результату
    res_str += '!' * random.randint(5, 50)  
    
    # Выводим результат в консоль
    print(res_str)
    
    # Возвращаем финальную строку
    return res_str  


# Тестовый класс для функции task1
class TestTask1(unittest.TestCase):
    def test_task1(self):
        # Вызываем функцию task1 и сохраняем результат в переменную result
        result = task1()  
        
        result_str = result.split('\n')
        self.assertEqual(len(result_str), 3)
        self.assertEqual(result_str[0], 'Hello, world!') 
        self.assertEqual(result_str[1], 'Andhiagain!')
        
        sign_count = 0
        for i in result_str[2]:
            self.assertTrue(i=='!')
            sign_count += 1
        self.assertTrue(sign_count<=50 and sign_count>=5)                


# Запуск тестов
if __name__ == '__main__':
    unittest.main()
