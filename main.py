import re 
from pathlib import Path
from typing import NoReturn
import pymorphy3
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
        self.get_pos(["NOUN", "VERB"])

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
        self.check_empty_file()
        self.text = self.text.lower()

    def clean_text(self) -> None:
        self.check_empty_file()
        self.text = re.findall(r"[А-Яа-яёЁ]+", self.text)

    def get_pos(self, pos: list = None) -> None:
        self.check_empty_file()
        if not pos:
            raise Exception("Не указана часть речи")
        mngr = pymorphy3.MorphAnalyzer()
        all_words = {mngr.parse(i)[0].normal_form: mngr.parse(i)[0].tag.POS for i in self.text}
        if len(pos) == 1:
            print(f"{pos[0]}: {[i for i in all_words if all_words.get(i) == pos[0]]}")
        else:
            for part in pos:
                print(f"{part}: {[i for i in all_words if all_words.get(i) == part]}")

    def print_text(self) -> None:
        print(self.text)


TextAnalyzer(file_path="./test.txt")
