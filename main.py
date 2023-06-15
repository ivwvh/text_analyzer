import re
from pathlib import Path
from typing import NoReturn

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
        self.clean_text()
        self.get_words()

    def open_file(self) -> None | NoReturn:
        try:
            file = open(self.file_path,
                        '+r',
                        encoding=self.text_encoding
                        )
            self.file = file
        except FileNotFoundError:
            raise FileNotFoundError("Файл не найден")

    def get_text(self) -> None:
        self.text = self.file.read()
        self.file.close()

    def check_empty_file(self) -> RuntimeError | None:
        if not self.text:
            raise RuntimeError("Файл пуст")

    def make_lower(self) -> None:
        self.text = self.text.lower()

    def print_text(self) -> None:
        print(self.text)

    def clean_text(self) -> None:
        self.text = [word for word in re.split("[\W]", self.text) if word]

    def get_words(self) -> None:
        self.words = self.text


TextAnalyzer(file_path="./test.txt")
