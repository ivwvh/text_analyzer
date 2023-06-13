from pathlib import Path
from typing import NoReturn
from string import punctuation

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
        self.get_words()
        self.clean_text()

    def open_file(self) -> None | NoReturn:
        try:
            file = open(self.file_path,
                      '+r',
                      encoding=self.text_encoding)
            self.file = file
        except FileNotFoundError:
            raise Exception("Файл не найден")

    def get_text(self) -> None:
        self.text = self.file.read()

    def check_empty_file(self) -> RuntimeError | None:
        if not self.text:
            raise RuntimeError("Файл пуст")

    def make_lower(self) -> None:
        self.text = self.text.lower()

    def print_text(self) -> None:
        print(self.text)

    def get_words(self) -> None:
        self.words = self.text.split()

    def clean_text(self) -> None:
        for i in range(len(self.words)):
            for symbol in self.words[i]:
                if symbol in punctuation:
                    punct = symbol
                    self.words[i] = self.words[i].replace(punct, "")
        for i in range(self.words.count("")):
            self.words.remove("")
        print(self.words)


TextAnalyzer(file_path="./test.txt")
