from random import randint
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

def update_score(status):
    global score,best_score
    if status:
        score += 1
    else:
        score = 0
    text_score.setText('количество балов:' + str(score))
    if score > best_score:
        best_score_txt = score

def check(users):
    global levl_btn
    print(btns_for_task, users)
    index = len(users) - 1
    print(index + 1,index + 1 < len(btns_for_task))
    if index + 1 <= len(btns_for_task):
        print(btns_for_task[index] == users[index])
        if btns_for_task[index] == users[index]:
            hilight_btn(btns[users[index]] , 'green',500)
            if index + 1 == len(btns_for_task):
                update_score(True)
        else:
            print("error")
            levl_btn = 3
            hilight_btn(btns[users[index]] , 'yellow',500)
            set_btn_enablet(False)
            QTimer.singleShot(1200,lambda: [set_btn_enablet(True),play()])
            update_score(False)
            return
    if index + 1 == len(btns_for_task):
        set_btn_enablet(False)
        QTimer.singleShot(1200,lambda: [set_btn_enablet(True),next_lvl()])

def next_lvl():
    global levl_btn, user_cliced
    user_cliced = []
    print(user_cliced, ' клики пользавателя')
    levl_btn += 1
    play()

def play():
    set_btn_enablet(True)
    btn_play.hide()
    global btns_for_task
    btns_for_task = creat_list_btn(btns_for_task)

    def show_next_btn(index):
        if index < levl_btn:
            num = btns_for_task[index]
            hilight_btn(btns[num],'red',500)
#            btns_for_task.append(num)
            print(btns_for_task)
            QTimer.singleShot(1200,lambda: show_next_btn(index+1))
    show_next_btn(0)

def user_cliced_btn(click_btn):
    num_btn = int(click_btn.text()) - 1
    print(num_btn)
    user_cliced.append(num_btn)
    check(user_cliced)

def creat_list_btn(has_btns):
    new_btns = levl_btn - len(has_btns)
    if new_btns <= 0:
        has_btns = []
        for i in range(levl_btn):
            num = randint(0,5)
            has_btns.append(num)
    else:
        for i in range(new_btns):
            num = randint(0,5)
            has_btns.append(num)
    return has_btns

def set_btn_enablet(enablet):
    for btn in btns:
        btn.setEnabled(enablet)

user_cliced = []
levl_btn = 3

btn1 = QPushButton()
btn1.setText('1')
btn1.setFont(QFont('Times',100))
btn1.setStyleSheet('background-color:rgb(243, 244, 150);')
btn1.clicked.connect(lambda: user_cliced_btn(btn1))

btn2 = QPushButton()
btn2.setText('2')
btn2.setFont(QFont('Times',100))
btn2.setStyleSheet('background-color:rgb(243, 244, 150);')
btn2.clicked.connect(lambda: user_cliced_btn(btn2))

btn3 = QPushButton()
btn3.setText('3')
btn3.setFont(QFont('Times',100))
btn3.setStyleSheet('background-color:rgb(243, 244, 150);')
btn3.clicked.connect(lambda: user_cliced_btn(btn3))

btn4 = QPushButton()
btn4.setText('4')
btn4.setFont(QFont('Times',100))
btn4.setStyleSheet('background-color:rgb(243, 244, 150);')
btn4.clicked.connect(lambda: user_cliced_btn(btn4))

btn5 = QPushButton()
btn5.setText('5')
btn5.setFont(QFont('Times',100))
btn5.setStyleSheet('background-color:rgb(243, 244, 150);')
btn5.clicked.connect(lambda: user_cliced_btn(btn5))

btn6 = QPushButton()
btn6.setText('6')
btn6.setFont(QFont('Times',100))
btn6.setStyleSheet('background-color:rgb(243, 244, 150);')
btn6.clicked.connect(lambda: user_cliced_btn(btn6))

btn_play = QPushButton('Играть!')
btn_play.setFont(QFont('Times',150))
btn_play.setStyleSheet('background-color:rgb(255, 255, 0);')
btn_play.clicked.connect(play)
line_btn_play =  QHBoxLayout()
line_btn_play.addWidget(btn_play)

btns = [btn1,btn2,btn3,btn4,btn5,btn6]
set_btn_enablet(False)
btns_for_task = []


score = 0
text_score = QLabel('количество балов: ' + str(score),alignment=Qt.AlignCenter)#(q,alignment=Qt.AlignCenter)
text_score.setFont(QFont('Times',50))

with open('text.txt','r') as text:
    best_score = text.read()

best_score_txt = QLabel('рекорд:' + str(best_score),alignment=Qt.AlignCenter)#(q,alignment=Qt.AlignCenter)
best_score_txt.setFont(QFont('Times',50))

line_best_score = QHBoxLayout()
line_best_score.addWidget(best_score)

line_text1 = QHBoxLayout()
line_text1.addWidget(text_score)

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
