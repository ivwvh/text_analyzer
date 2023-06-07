
"""

Скачать текст
загрузить TXT файл
Топ 10/20 глаголов\существительных\прилагателных в тексте

"""


class TextAnalyzer:
    def __init__(self) -> None:
        self.text = open("./test.txt", '+r', encoding="utf-8").read()
        print(self.text)


TextAnalyzer()
