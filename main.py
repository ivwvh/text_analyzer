
"""

Скачать текст
загрузить TXT файл
Топ 10/20 глаголов\существительных\прилагателных в тексте

"""

text = open("./test.txt", '+r', encoding="utf-8").read()


class TextAnalyzer:
    def __init__(self, text: str) -> None:
        self.text = text

    def print_text(self) -> None:
        print(self.text)


TextAnalyzer(text).print_text()
