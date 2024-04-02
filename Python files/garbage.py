class CheckSkills(QWidget, Skill_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.test.clicked.connect(self.open_test)

    def open_test(self):
        self.test = Test()
        self.close()
        self.test.show()


class Test(QWidget, Test_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.count = 1
        with open('../Questions.txt', encoding='utf-8') as q:
            self.questions = q.read().split('\n')
        self.next_quest.clicked.connect(self.change_question)
        self.show_quest.clicked.connect(self.show_question)
        self.end_test.clicked.connect(self.end_questions)

    def change_question(self):
        with sqlite3.connect('../Elements and stuff/Elements_db') as con:
            self.label.setText(self.questions[self.count])
            if self.first_ans.isChecked() is False and self.second_ans.isChecked() is False:
                self.label.setText('Нужно ответить на вопрос')
            elif self.first_ans.isChecked() is True:
                con.cursor().execute(f'''UPDATE Data SET Ваш_ответ = "Да" WHERE Номер_вопроса = {self.count}''')
                self.count += 1
            elif self.second_ans.isChecked() is True:
                con.cursor().execute(f'''UPDATE Data SET Ваш_ответ = "Нет" WHERE Номер_вопроса = {self.count}''')
                self.count += 1

    def show_question(self):
        self.label.setText(self.questions[self.count - 1])

    def end_questions(self):
        if self.count == 11:
            self.res = Results()
            self.close()
            self.res.show()
        else:
            self.label.setText('Нужно ответить на все вопросы')


class Results(QWidget, Result_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fill_answers()

    def fill_answers(self):
        with sqlite3.connect('../Elements and stuff/Elements_db') as con:
            fields = con.cursor().execute('''SELECT Ваш_ответ, Правильный_ответ, Пояснение FROM Data''').fetchall()
            self.result.setColumnCount(3)
            self.result.setRowCount(10)
            self.result.setHorizontalHeaderLabels(['Ваш_ответ', 'Правильный_ответ', '                        '
                                                                                    '                Пояснение'
                                                                                    '                                '
                                                                                    '                           '])
            self.result.resizeColumnsToContents()
            for i in range(3):
                for j in range(10):
                    item = QTableWidgetItem(fields[j][i])
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                    self.result.setItem(j, i, item)
            for j in range(10):
                if fields[j][0] != fields[j][1]:
                    self.result.item(j, 0).setBackground(QColor(255, 0, 0))
                    self.result.item(j, 1).setBackground(QColor(255, 0, 0))
                    self.result.item(j, 2).setBackground(QColor(255, 0, 0))
                else:
                    self.result.item(j, 0).setBackground(QColor(0, 127, 0))
                    self.result.item(j, 1).setBackground(QColor(0, 127, 0))
                    self.result.item(j, 2).setBackground(QColor(0, 127, 0))