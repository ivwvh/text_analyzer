import re
from pathlib import Path
from typing import NoReturn

import chardet
import pymorphy3
from collections import Counter

import wordcloud
import random
"""

Скачать текст
загрузить TXT файл
Топ 10/20 глаголов\существительных\прилагателных в тексте

"""


class TextAnalyzer:
    def __init__(self,
                 file_path=None,
                 text_encoding=None,
                 pos=None,
                 cloud_width=400,
                 cloud_height=400,
                 cloud_max_words=200,
                 cloud_file_name="cloud",
                 cloud_color=(),
                 most_common_max_words=10
                 ) -> None:
        if not file_path:
            raise Exception("Не указан путь к файлу")
        self.file_path = Path(file_path)
        if not text_encoding:
            rawdata = open(self.file_path, "rb").read()
            self.text_encoding = chardet.detect(rawdata).get("encoding")
        else:
            self.text_encoding = text_encoding
        self.open_file()
        self.get_text()
        self.make_lower()
        self.clean_text()
        self.get_pos(pos)
        self.get_most_common(["VERB"],
                             max_words=most_common_max_words)
        self.generate_cloud(pos,
                            cloud_width,
                            cloud_height,
                            max_words=cloud_max_words,
                            cloud_file_name=cloud_file_name,
                            color=cloud_color)

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
        """TODO: РАЗОБРАТЬСЯ С ГЕНЕРАТОРАМИ"""
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
                       pos=None,
                       width=400,
                       height=400,
                       cloud_file_name="cloud",
                       max_words=200,
                       color=()
                       ) -> None:
        '''TODO: СЛИШКОМ МНОГО ОТВЕТСТВЕННОСТИ'''
        if len(pos) == 1:
            words = [i for i in self.all_words if self.all_words[i] == pos[0]]
            text = " ".join(words)
        else:
            words = []
            for part in pos:
                words.extend([i for i in self.all_words if self.all_words[i] == part])
            text = " ".join(words)
        if not cloud_file_name:
            raise Exception("Не указано название картинки")
        if not color:
            color = tuple(random.randint(0, 255) for i in range(3))
        cloud = wordcloud.WordCloud(width=width,
                                    height=height,
                                    max_words=max_words,
                                    color_func=lambda *args, **kwargs: color).generate(text)
        cloud.to_file(f"./{cloud_file_name}.jpg")

    def get_most_common(self,
                        pos,
                        max_words=10):
        words = [word for word in self.text if self.mngr.parse(word)[0].tag.POS == pos[0]]
        counter = Counter(words)
        print("\n")
        counted = counter.most_common(max_words)
        for tup in counted:
            print(f"Слово: {tup[0]}, количество использований: {tup[1]}")

    def print_result(self, pos) -> None:
        "TODO: КОЛИЧЕСТВО НУЖНЫХ СЛОВ, КУДА СОХРАНЯЕТСЯ КАРТИНКА"
        print(f'Всего слов в тексте: {len(self.text)}')
        print(f'Из них {pos}: {len(self.text)}')
        print(f'Картинка сохранена в: {len(self.text)}')


TextAnalyzer(file_path="./test.txt",
             pos=["NOUN", "VERB"],
             cloud_max_words=1000,
             most_common_max_words=12
             )
