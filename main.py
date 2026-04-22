from random import randint
from time import sleep
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import(
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QApplication,
    QWidget,
)


app = QApplication([])
win = QWidget()
win.setWindowIcon(QIcon('icon.png'))
win.setStyleSheet('background-color:rgb(181, 230, 29);')
win.resize(1000,1000)
win.setWindowTitle('КЛИК-КЛИК')

def hilight_btn(btn,color,duration_ms = 500):
    original_stule = btn.styleSheet()
    btn.setStyleSheet(f'background-color:{color};')
    QTimer.singleShot(duration_ms , lambda: btn.setStyleSheet(original_stule))

def play():
#    btn_play.hide()
    for btn_s in range(levl_btn):
        num = randint(0,5)
        hilight_btn(btns[num],'red',1000)
        btns_for_task.append(num)
#        sleep(1)
        print(btns_for_task)

levl_btn = 3

btn1 = QPushButton()
btn1.setText('1')
btn1.setFont(QFont('Times',100))
btn1.setStyleSheet('background-color:rgb(243, 244, 150);')

btn2 = QPushButton()
btn2.setText('2')
btn2.setFont(QFont('Times',100))
btn2.setStyleSheet('background-color:rgb(243, 244, 150);')

btn3 = QPushButton()
btn3.setText('3')
btn3.setFont(QFont('Times',100))
btn3.setStyleSheet('background-color:rgb(243, 244, 150);')

btn4 = QPushButton()
btn4.setText('4')
btn4.setFont(QFont('Times',100))
btn4.setStyleSheet('background-color:rgb(243, 244, 150);')

btn5 = QPushButton()
btn5.setText('5')
btn5.setFont(QFont('Times',100))
btn5.setStyleSheet('background-color:rgb(243, 244, 150);')

btn6 = QPushButton()
btn6.setText('6')
btn6.setFont(QFont('Times',100))
btn6.setStyleSheet('background-color:rgb(243, 244, 150);')

btn_play = QPushButton('Играть!')
btn_play.setFont(QFont('Times',150))
btn_play.setStyleSheet('background-color:rgb(255, 255, 0);')
btn_play.clicked.connect(play)
line_btn_play =  QHBoxLayout()
line_btn_play.addWidget(btn_play)

btns = [btn1,btn2,btn3,btn4,btn5,btn6]
btns_for_task = []


num1 = 0
text1 = QLabel('количество балов: ' + str(num1),alignment=Qt.AlignCenter)#(q,alignment=Qt.AlignCenter)
text1.setFont(QFont('Times',50))

with open('text.txt','r') as text:
    best_score = text.read()

best_score = QLabel('рекорд:' + str(best_score),alignment=Qt.AlignCenter)#(q,alignment=Qt.AlignCenter)
best_score.setFont(QFont('Times',50))

line_best_score = QHBoxLayout()
line_best_score.addWidget(best_score)

line_text1 = QHBoxLayout()
line_text1.addWidget(text1)

line_123_h = QHBoxLayout()#сдесь 1я 2я 3я кнопка
line_123_h.addWidget(btn1)
line_123_h.addWidget(btn2)
line_123_h.addWidget(btn3)

line_456_h = QHBoxLayout()#сдесь 4я 5я 6я кнопка
line_456_h.addWidget(btn4)
line_456_h.addWidget(btn5)
line_456_h.addWidget(btn6)

main_line = QVBoxLayout()
main_line.addLayout(line_best_score)
main_line.addLayout(line_text1)
main_line.addLayout(line_123_h)
main_line.addLayout(line_btn_play)
main_line.addLayout(line_456_h)


win.setLayout(main_line)

#stop
win.show()
app.exec_()
