from pathlib import Path

"""

Скачать текст
загрузить TXT файл
Топ 10/20 глаголов\существительных\прилагателных в тексте

"""


class TextAnalyzer:
    def __init__(self, file_path=None, text_encoding="utf-8") -> None:
        self.text_encoding = input("Введите название кодировки: ")
        self.file_path = Path(file_path)
        if not self.text_encoding:
            self.text_encoding = text_encoding
        if not file_path:
            self.file_path = Path(input("Введите путь до файла: "))

        self.get_text()
        self.print_text()

    def get_text(self) -> None:
        self.text = open(self.file_path,
                         '+r',
                         encoding=self.text_encoding).read()

    def print_text(self) -> None:
        print(self.text)


TextAnalyzer()
