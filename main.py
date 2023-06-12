from pathlib import Path

"""

Скачать текст
загрузить TXT файл
Топ 10/20 глаголов\существительных\прилагателных в тексте

"""


class TextAnalyzer:
    def __init__(self, file_path=None, text_encoding="utf-8") -> None:
        if not file_path:
            raise Exception("Не указан путь к файлу")
        self.file_path = Path(file_path)
        self.text_encoding = text_encoding

        self.open_file()
        self.get_text()
        self.make_lower()
        self.print_text()

    def open_file(self) -> None:
        try:
            self.text = open(self.file_path,
                             '+r',
                             encoding=self.text_encoding)
        except FileNotFoundError:
            raise Exception("Файл не найден")

    def get_text(self) -> str:
        self.text = self.text.read()
        if not len(self.text):
            raise Exception("Файл пуст")

    def make_lower(self) -> str:
        self.text = self.text.lower()

    def print_text(self) -> None:
        print(self.text)


TextAnalyzer(file_path="./test.txt")
