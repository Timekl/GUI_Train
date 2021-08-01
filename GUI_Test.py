from tkinter import *
import csv


class QuestionGui:
    def __init__(self, father_window):
        self.father_window = father_window
        self.data = list()

    def set_windows(self):
        self.father_window.title("问答游戏")

    def init_window(self):
        pass

    def engineering(self):
        pass

    def read_csv(self):
        with open('GUI_Question_Test.CSV') as f:
            read_data = csv.DictReader(f)
            self.data = [row for row in read_data]

    def show_data(self):
        for row in self.data:
            print(row)


if __name__ == '__main__':
    father_window = Tk()
    qg = QuestionGui(father_window)
    qg.set_windows()
    father_window.mainloop()
# root = Tk()
#
# li = ['C', 'python', 'php', 'html', 'SQL', 'java']
# movie = ['CSS', 'jQuery', 'Bootstrap']
# listb = Listbox(root)  # 创建两个列表组件
# listb2 = Listbox(root)
# for item in li:  # 第一个小部件插入数据
#     listb.insert(0, item)
#
# for item in movie:  # 第二个小部件插入数据
#     listb2.insert(0, item)
#
# listb.pack()  # 将小部件放置到主窗口中
# listb2.pack()
# root.mainloop()  # 进入消息循环
