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

        self.row = 0

        # father_window 的相关参数
        self.sw = self.father_window.winfo_screenwidth()
        self.sh = self.father_window.winfo_screenheight()
        self.ww = self.sw / 4
        self.wh = self.sh / 4
        self.x = (self.sw - self.ww) / 2
        self.y = (self.sh - self.wh) / 2

        self.my_question = Text(self.father_window)
        self.my_question.place(x=0, y=0, width=self.ww / 2, height=self.wh - 30)
        self.my_answer = Text(self.father_window)
        self.my_answer.place(x=self.ww / 2, y=0, width=self.ww / 2, height=self.wh - 30)

    def set_window(self):
        self.father_window.title('问答游戏')
        self.father_window.geometry('%dx%d+%d+%d' % (self.ww, self.wh, self.x, self.y))
        self.init_question()
        self.init_answer('')
        self.init_button()

    def init_button(self):
        const_width = self.ww / 5
        button1 = Button(self.father_window, text='A', command=lambda: self.engineering('A'))
        button2 = Button(self.father_window, text='B', command=lambda: self.engineering('B'))
        button3 = Button(self.father_window, text='C', command=lambda: self.engineering('C'))
        button4 = Button(self.father_window, text='D', command=lambda: self.engineering('D'))
        button5 = Button(self.father_window, text='E', command=lambda: self.engineering('E'))
        button1.place(x=0, y=self.wh - 30, width=const_width, height=30)
        button2.place(x=const_width, y=self.wh - 30, width=const_width, height=30)
        button3.place(x=const_width * 2, y=self.wh - 30, width=const_width, height=30)
        button4.place(x=const_width * 3, y=self.wh - 30, width=const_width, height=30)
        button5.place(x=const_width * 4, y=self.wh - 30, width=const_width, height=30)

    def init_question(self):
        self.my_question.configure(state='normal')
        data = self.data[self.row]
        que = ''
        que = que + 'Question:\n\t' + data['Question'] + '\nOption:'
        for option in ['A', 'B', 'C', 'D', 'E']:
            if data[option] != '':
                que = que + '\n\t' + option + ':' + data[option]
        self.my_question.delete(1.0, END)
        self.my_question.insert(1.0, que)
        self.my_question.configure(state='disable')

    def init_answer(self, ans):
        self.my_answer.configure(state='normal')
        self.my_answer.delete(1.0, END)
        self.my_answer.insert(1.0, ans)
        self.my_answer.configure(state='disable')

    def engineering(self, option):
        data = self.data[self.row]
        option = option + ' next step'
        if data[option] != '':
            next_step = data[option].split(':')
            operation = next_step[0]
            operand = next_step[1]
            if operation == 'jump':
                self.row = int(operand) - 2
                self.init_question()
            elif operation == 'answer':
                self.init_answer('Answer:\n\t' + operand)

    def show_data(self):
        for row in self.data:
            print(row)


if __name__ == '__main__':
    main_window = Tk()
    qg = QuestionGui(main_window)
    qg.set_window()
    main_window.mainloop()
