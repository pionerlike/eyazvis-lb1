import tkinter
import collector
import processor
from tkinter import scrolledtext


class Window():
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Система поиска словосочетаний")

        self.path_text = tkinter.Label(
            text="Введите путь к файлу"
        )

        self.path_text.grid(
            row=0,
            column=0,
            sticky="nw",
            pady=(20, 5),
            padx=20
        )

        self.path_entry = tkinter.Entry(
            width=40
        )

        self.path_entry.grid(
            row=0,
            column=1,
            sticky="ne",
            pady=(20, 5),
            padx=20
        )

        self.search_box_text = tkinter.Label(
            text="Введите слово"
        )

        self.search_box_text.grid(
            row=1,
            column=0,
            sticky="nw",
            pady=5,
            padx=20
        )

        self.search_box_entry = tkinter.Entry(
            width=40
        )

        self.search_box_entry.grid(
            row=1,
            column=1,
            sticky="ne",
            pady=5,
            padx=20
        )

        self.result_box = scrolledtext.ScrolledText(
            width=120
        )

        self.result_box.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="news",
            pady=10,
            padx=20
        )

        self.search_button = tkinter.Button(
            text="Найти",
            width=30,
            command=self.search
        )

        self.search_button.grid(
            row=3,
            column=0,
            sticky="sw",
            pady=10,
            padx=20
        )

        self.save_button = tkinter.Button(
            text="Сохранить",
            width=30,
            command=self.save
        )

        self.save_button.grid(
            row=3,
            column=1,
            sticky="se",
            pady=10,
            padx=20
        )

        self.window.mainloop()

    def search(self):
        try:
            path = self.path_entry.get()
            pdf = collector.PDF(f"{path}")
            phrases = processor.Phrases(str(pdf))
            symbols = self.search_box_entry.get()
            result = phrases.find(f"{symbols}")
            self.result_box.insert(tkinter.INSERT, result)
        except FileNotFoundError:
            self.result_box.insert(tkinter.INSERT, (
                    "Неправильно введен путь к файлу." + "\n" +
                    "Попробуйте скопировать полный путь к файлу с помощью проводника." + "\n" +
                    "Если программа находится внутри папки, которая расположена " + "\n" +
                    "вместе с нужным файлом добавьте в начале пути '../'." + "\n" +
                    "В качестве разделителя пути используйте символ '/'." + "\n" +
                    "Не забудьте указать расширение, и проверить регистр символов." + "\n" +
                    "Если внутри программы не работают горячие клавиши" + "\n" +
                    "смените раскладку клавиатуры на англ."
            ))

    def save(self):
        with open("Отчет.txt", mode='w', encoding="utf-8") as file:
            text = self.result_box.get("1.0", tkinter.END)
            file.write(text)
