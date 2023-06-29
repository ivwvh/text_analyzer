import re
from pathlib import Path
from typing import NoReturn

import chardet
import pymorphy3
from collections import Counter

import wordcloud
"""

Скачать текст
загрузить TXT файл
Топ 10/20 глаголов\существительных\прилагателных в тексте

"""


class TextAnalyzer:
    def __init__(self,
                 file_path=None,
                 text_encoding=None,
                 pos: list = None,
                 cloud_pos=[],
                 cloud_width=400,
                 cloud_height=400,
                 cloud_max_words=200,
                 cloud_path="./cloud.jpg") -> None:
        if not file_path:
            raise Exception("Не указан путь к файлу")
        self.file_path = Path(file_path)
        if not text_encoding:
            rawdata = open(self.file_path, "rb").read()  # получаем сырые данные
            self.text_encoding = chardet.detect(rawdata).get("encoding")  # с помощью бибилиотеки chardet пытаемся определить кодировку
        else:
            self.text_encoding = text_encoding
        self.open_file()
        self.get_text()
        self.make_lower()
        self.clean_text()
        self.get_pos(pos)
        self.get_most_common(["VERB"])
        self.generate_cloud(cloud_pos,
                            cloud_width,
                            cloud_height,
                            max_words=cloud_max_words,
                            path=cloud_path)

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
        self.mngr = pymorphy3.MorphAnalyzer()
        normal_forms = [self.mngr.parse(i)[0].normal_form for i in self.text]
        tags = [self.mngr.parse(i)[0].tag.POS for i in self.text]
        self.all_words = {normal_forms[i]: tags[i] for i in range(len(self.text))}
        if len(pos) == 1:
            self.words = [i for i in self.all_words if self.all_words[i] == pos[0]]
            print(f"{pos[0]}: {[i for i in self.all_words if self.all_words[i] == pos[0]]}")
            print(self.words)
        else:
            for part in pos:
                print(f"{part}: {[i for i in self.all_words if self.all_words[i] == part]}")

    def generate_cloud(self,
                       pos: list = None,
                       width: int = 400,
                       height: int = 400,
                       path: str | Path = None,
                       max_words: int = 200) -> None:
        if not pos:
            raise Exception("Не указана часть речи")
        else:
            if len(pos) == 1:
                words = [i for i in self.all_words if self.all_words[i] == pos[0]]
                text = " ".join(words)
            else:
                words = []
                for part in pos:
                    words.extend([i for i in self.all_words if self.all_words[i] == part])
                text = " ".join(words)
        if not path:
            raise Exception("Не указан путь к картинке")
        cloud = wordcloud.WordCloud(width=width,
                                    height=height,
                                    max_words=max_words).generate(text)
        cloud.to_file(path)

    def get_most_common(self, pos):
        words = [word for word in self.text if self.mngr.parse(word)[0].tag.POS == pos[0]]
        counter = Counter(words)
        print("\n")
        counted = counter.most_common(10)
        for tup in counted:
            print(f"Слово: {tup[0]}, количество использований: {tup[1]}")

    def print_text(self) -> None:
        print(self.text)


TextAnalyzer(file_path="./test.txt", pos=["NOUN", "VERB"],
             cloud_pos=['VERB'],
             cloud_max_words=1000)
