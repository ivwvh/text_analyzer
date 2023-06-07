from encoding_checker import check_encoding
"""

Скачать текст
загрузить TXT файл
Топ 10/20 глаголов\существительных\прилагателных в тексте

"""


class TextAnalyzer:
    def __init__(self) -> None:
        self.text_encoding = input("Введите название кодировки: ")
        if check_encoding(self.text_encoding):
            self.text = None
            self.get_text()
            self.print_text()
        else:
            print("Кодировки не существует")
    
    def get_text(self) -> None:
        self.text = open("./test.txt", '+r', encoding=self.text_encoding).read()
    
    def print_text(self):
        print(self.text)

TextAnalyzer()
