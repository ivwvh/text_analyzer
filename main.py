"""

Скачать текст
загрузить TXT файл
Топ 10/20 глаголов\существительных\прилагателных в тексте

"""


class TextAnalyzer:
    def __init__(self) -> None:
        self.text_encoding = input("Введите название кодировки: ")
        if not self.text_encoding:
            self.text_encoding = "utf_8"
            self.text = None
            self.get_text()
            self.print_text()
        else:
            self.text = None
            self.get_text()
            self.print_text()

    def get_text(self) -> None:
        self.text = open("./test.txt", '+r', encoding=self.text_encoding).read()
    
    def print_text(self):
        print(self.text)


TextAnalyzer()
