from pathlib import Path
from sys import exit
"""

Скачать текст
загрузить TXT файл
Топ 10/20 глаголов\существительных\прилагателных в тексте

"""


class TextAnalyzer:
    def __init__(self, file_path=None, text_encoding="utf-8") -> None:
        if not file_path:
            print("Не указан путь к файлу")
            exit()
        self.file_path = Path(file_path)
        self.text_encoding = text_encoding

        self.open_file()
        self.get_text()
        self.print_text()

    def open_file(self) -> None:
        self.text = open(self.file_path,
                         '+r',
                         encoding=self.text_encoding)

    def get_text(self):
        self.text = self.text.read()

    def print_text(self) -> None:
        print(self.text)


TextAnalyzer(file_path="./test.txt")
