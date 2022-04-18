import numpy as np
import PyPDF2
import re


class PDF:
    def __init__(self, path):
        self.__file = PyPDF2.PdfFileReader(
            open(path, "rb"),
            strict=False
        )
        self.text = np.array([])
        self.__collect_text()

    def __collect_text(self):
        for i in range(self.__file.getNumPages()):
            self.text = np.append(
                self.text,
                [self.__file.getPage(i).extractText()]
            )

    def __str__(self):
        text = ""
        for element in self.text:
            text += str(element)
        return text
