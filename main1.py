import sys

from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QInputDialog
from PyQt5 import QtCore

from matplotlib import rcParams

rcParams['font.family'] = 'fantasy'
rcParams['font.fantasy'] = 'Times New Roman'
rcParams['axes.titlepad'] = 30  # Задать на графиках отступ от заголовка (optional)
rcParams['axes.labelpad'] = 20   # Задать гра графиках отступ от подписей к осям (optional)


from math import sqrt

def click(click_event):
    global prev
    prev = click_event


def distance(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def point_line_distance(point, start, end):
    if start == end:
        return distance(point, start)
    else:
        n = abs(
            (end[0] - start[0]) * (start[1] - point[1]) -
            (start[0] - point[0]) * (end[1] - start[1])
        )
        d = sqrt(
            (end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2
        )
        return n / d


def rdp(points, epsilon):
    dmax = 0.0
    index = 0
    for i in range(1, len(points) - 1):
        d = point_line_distance(points[i], points[0], points[-1])
        if d > dmax:
            index = i
            dmax = d

    if dmax >= epsilon:
        results = rdp(points[:index + 1], epsilon)[:-1] + rdp(points[index:], epsilon)
    else:
        results = [points[0], points[-1]]

    return results

class Alghorithm(QMainWindow):
    x = []
    y = []
    list_koord = []

    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        loadUi("Algorithm_RDP.ui", self)

        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 140, 991, 991))

        self.MplWidget.canvas.mpl_connect("button_press_event", self.on_press)

        self.MplWidget.canvas.axes.clear()  # Очистка содержимого фигуры
        self.MplWidget.canvas.axes.plot(Alghorithm.x, Alghorithm.y)

        self.MplWidget.canvas.axes.set_xlabel('х', fontsize=16, color='black')  # Подпись по оси X
        self.MplWidget.canvas.axes.set_ylabel('y', fontsize=16, color='black')  # Подпись по оси y
        self.MplWidget.canvas.axes.grid(True, color=[0, 0, 0], lw=0.5)  # Решетка, черный цвет, ширина линии
        self.MplWidget.canvas.axes.set_title('График', fontsize=20, color='black')  # Заголовок гистограммы (optional)
        self.MplWidget.canvas.axes.set_xlim(0, 10)
        self.MplWidget.canvas.axes.set_ylim(0, 10)
        self.MplWidget.canvas.draw()

        self.pushButton.clicked.connect(self.NewPoint)

        self.Button_clear.clicked.connect(self.Clear)

        self.Button_generate.clicked.connect(self.RDP_start)

        self.Button_save.clicked.connect(self.Save)

    def Save(self):
        inputDialog = QInputDialog(None)
        inputDialog.setInputMode(QInputDialog.TextInput)
        inputDialog.setWindowTitle('Input')
        inputDialog.setLabelText('Введмте имя файла')
        inputDialog.setStyleSheet("QInputDialog {background-color: rgb(184, 209, 255);}")
        ok = inputDialog.exec_()
        Name = inputDialog.textValue()
        if ok:
            canvas = self.MplWidget.canvas
            canvas.print_figure("C:/Users/Aleksej/Pictures/RDP_"+str(Name)+"str.png")



    def on_press(self, event):

        if event.x >= 123 and event.x <= 860 and event.y >= 100 and event.y <= 730:
            Alghorithm.x.append(event.xdata)
            Alghorithm.y.append(event.ydata)
            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.axes.plot(Alghorithm.x, Alghorithm.y, 'b-')
            self.MplWidget.canvas.axes.set_xlabel('х', fontsize=16, color='black')  # Подпись по оси X
            self.MplWidget.canvas.axes.set_ylabel('y', fontsize=16, color='black')  # Подпись по оси y
            self.MplWidget.canvas.axes.grid(True, color=[0, 0, 0], lw=0.5)  # Решетка, черный цвет, ширина линии
            self.MplWidget.canvas.axes.set_title('График', fontsize=20, color='black')  # Заголовок гистограммы (optional)
            self.MplWidget.canvas.axes.legend('Исходная_кривая' , loc = 'upper left')
            if  self.line_x.text() == "" and self.line_y.text() == "":
                self.MplWidget.canvas.axes.set_xlim(0, 10)
                self.MplWidget.canvas.axes.set_ylim(0, 10)
            else:
                self.MplWidget.canvas.axes.set_xlim(0, float(self.line_x.text()))
                self.MplWidget.canvas.axes.set_ylim(0, float(self.line_y.text()))

            self.MplWidget.canvas.draw()

    def NewPoint(self):
        try:

            self.MplWidget.canvas.axes.set_xlim(0, float(self.line_x.text()))
            self.MplWidget.canvas.axes.set_ylim(0, float(self.line_y.text()))
            self.MplWidget.canvas.draw()
        except ValueError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка ввода области")
            msg.setInformativeText('Вы ввели область координат в неверном формате! Вводите целые или десятичые числа. (например 1 или 1.1)')
            msg.setWindowTitle("Ошибка")
            msg.exec_()

    def Clear(self):
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.draw()
        Alghorithm.x.clear()
        Alghorithm.y.clear()
        Alghorithm.list_koord.clear()

    def RDP_start(self):
        try:
            xx=[]
            x1 = []
            y1 = []
            for i in range(0,len(Alghorithm.x)):
                xx.append([Alghorithm.x[i],Alghorithm.y[i]])
            res = list(rdp(xx, float(self.line_e.text())))
            for j in range(0, len(res)):
                x1.append(res[j][0])
                y1.append(res[j][1])
            print(x1,y1)
            self.MplWidget.canvas.axes.clear()  # Очистка содержимого фигуры
            self.MplWidget.canvas.axes.plot(Alghorithm.x, Alghorithm.y,'-.', color = 'gray')
            self.MplWidget.canvas.axes.plot(x1, y1, 'bo-')
            self.MplWidget.canvas.axes.set_xlabel('х', fontsize=16, color='black')  # Подпись по оси X
            self.MplWidget.canvas.axes.set_ylabel('y', fontsize=16, color='black')  # Подпись по оси y
            self.MplWidget.canvas.axes.grid(True, color=[0, 0, 0], lw=0.5)  # Решетка, черный цвет, ширина линии
            self.MplWidget.canvas.axes.set_title('График', fontsize=20, color='black')  # Заголовок гистограммы (optional)
            self.MplWidget.canvas.axes.legend(('Исходная кривая', 'Упрощенная кривая по алоритму Рамера-Дугласа-Пекера'), loc='upper left')
            self.MplWidget.canvas.draw()  # Выполнение (рисование графика)
        except ValueError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Введен неверный формат переменной Epsilon!")
            msg.setInformativeText('Введите в Epsilon цеолое или десятичное число (1 или 1.5)!')
            msg.setWindowTitle("Ошибка")
            msg.exec_()
        except IndexError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка данных кривой")
            msg.setInformativeText('Сначала постройте исходную кривую')
            msg.setWindowTitle("Ошибка")
            msg.exec_()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = Alghorithm()
    MainWindow.resize(1000, 1200)
    MainWindow.show()
    sys.exit(app.exec_())