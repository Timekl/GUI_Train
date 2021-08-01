from tkinter import *
import csv


def read_csv():
    with open('GUI_Question_Test.CSV') as f:
        init_data = csv.DictReader(f)
        data = [row for row in init_data]
    return data


class QuestionGui:
    def __init__(self, father_window):
        self.father_window = father_window
        self.data = read_csv()

        # father_window 的相关参数
        self.sw = self.father_window.winfo_screenwidth()
        self.sh = self.father_window.winfo_screenheight()
        self.ww = self.sw / 4
        self.wh = self.sh / 4
        self.x = (self.sw - self.ww) / 2
        self.y = (self.sh - self.wh) / 2

    def set_window(self):
        self.father_window.title('问答游戏')
        self.father_window.geometry('%dx%d+%d+%d' % (self.ww, self.wh, self.x, self.y))
        my_text = Text(self.father_window)
        my_text.insert(1.0, 'asd')
        my_text.configure(state='disable')
        my_text.place(x=0, y=0, width=100, height=100)
        self.init_button()

    def init_button(self):
        const_width = self.ww / 5
        button1 = Button(self.father_window, text='A', command=self.engineering('A'))
        button2 = Button(self.father_window, text='B', command=self.engineering('B'))
        button3 = Button(self.father_window, text='C', command=self.engineering('C'))
        button4 = Button(self.father_window, text='D', command=self.engineering('D'))
        button5 = Button(self.father_window, text='E', command=self.engineering('E'))
        button1.place(x=0, y=self.wh - 30, width=const_width, height=30)
        button2.place(x=const_width, y=self.wh - 30, width=const_width, height=30)
        button3.place(x=const_width * 2, y=self.wh - 30, width=const_width, height=30)
        button4.place(x=const_width * 3, y=self.wh - 30, width=const_width, height=30)
        button5.place(x=const_width * 4, y=self.wh - 30, width=const_width, height=30)

    def init_question(self, row):
        pass

    def init_answer(self, ans):
        pass

    def engineering(self, option):
        pass

    def show_data(self):
        for row in self.data:
            print(row)


if __name__ == '__main__':
    main_window = Tk()
    qg = QuestionGui(main_window)
    qg.set_window()
    main_window.mainloop()
