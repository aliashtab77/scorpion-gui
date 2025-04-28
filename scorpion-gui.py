from PyQt6 import QtCore, QtGui, QtWidgets
from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import FloodWaitError
from telethon.tl.functions.contacts import  ImportContactsRequest
from telethon.tl.types import InputPhoneContact
from config import DATABASE_NAME, DATABASE_HOST, DATABASE_PASSWORD, DATABASE_USER, API_ID, API_HASH
import mysql.connector
from time import sleep
class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
        self.aks = ""
        self.accs = []
        self.accs_name = []
        with mysql.connector.connect(user=DATABASE_USER, host=DATABASE_HOST, password=DATABASE_PASSWORD, database=DATABASE_NAME) as connection:
            with connection.cursor() as cursor:
                sql = f"SELECT number FROM accs"
                cursor.execute(sql)
                for i in cursor:
                    account = i[0]
                    self.accs.append(account)
                    self.accs_name.append(account)
            connection.commit()
        self.locs = []
        self.locs_name = []
        self.spl = []
        self.linee = []
        with mysql.connector.connect(user=DATABASE_USER, host=DATABASE_HOST, password=DATABASE_PASSWORD, database=DATABASE_NAME) as connection:
            with connection.cursor() as cursor:
                sql = f"SHOW TABLES"
                cursor.execute(sql)
                for i in cursor:
                    name = i[0]
                    if name == "accs" or name[-2:] == "_g":
                        continue
                    else:
                        self.locs.append(name)
                        self.locs_name.append(name)
                        self.spl.append(name)
                        self.linee.append(name)
            connection.commit()


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(972, 728)
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lists = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.lists.setGeometry(QtCore.QRect(10, 20, 941, 441))
        font = QtGui.QFont()
        font.setFamily("Sakkal Majalla")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.lists.setFont(font)
        self.lists.setMouseTracking(False)
        self.lists.setTabletTracking(False)
        self.lists.setAcceptDrops(False)
        self.lists.setAutoFillBackground(False)
        self.lists.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.lists.setTabShape(QtWidgets.QTabWidget.TabShape.Triangular)
        self.lists.setDocumentMode(False)
        self.lists.setTabsClosable(False)
        self.lists.setTabBarAutoHide(False)
        self.lists.setObjectName("lists")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 10, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setDefault(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(130, 10, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setDefault(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.tab)
        self.scrollArea.setGeometry(QtCore.QRect(10, 40, 561, 331))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 538, 329))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        for i, v in enumerate(self.accs):
            self.accs[i] = QtWidgets.QCheckBox(parent=self.scrollAreaWidgetContents)
            self.accs[i].setGeometry(QtCore.QRect(10, 10 + (i * 30), 311, 20))
            self.accs[i].setObjectName(v)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.lists.addTab(self.tab, "")
        self.ListGroups = QtWidgets.QWidget()
        self.ListGroups.setObjectName("ListGroups")
        self.scrollArea_3 = QtWidgets.QScrollArea(parent=self.ListGroups)
        self.scrollArea_3.setGeometry(QtCore.QRect(0, 40, 681, 331))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 679, 329))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        for i, v in enumerate(self.locs):
            self.spl[i] = QtWidgets.QSplitter(parent=self.scrollAreaWidgetContents_3)
            self.spl[i].setGeometry(QtCore.QRect(10, 10 + (i * 30), 266, 34))
            self.spl[i].setOrientation(QtCore.Qt.Orientation.Horizontal)
            self.spl[i].setObjectName(f"splitter_{i}")
            self.locs[i] = QtWidgets.QCheckBox(parent=self.spl[i])
            self.locs[i].setObjectName(v)
            self.linee[i] = QtWidgets.QLineEdit(parent=self.spl[i])
            self.linee[i].setText("")
            self.linee[i].setObjectName(f"lineEdit_{v}")


        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.ListGroups)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 10, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.ListGroups)
        self.pushButton_6.setGeometry(QtCore.QRect(130, 10, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setAutoDefault(False)
        self.pushButton_6.setDefault(False)
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.lists.addTab(self.ListGroups, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=self.tab_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 481, 151))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(parent=self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(20, 180, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser_2 = QtWidgets.QTextBrowser(parent=self.tab_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(130, 170, 256, 51))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 260, 261, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lists.addTab(self.tab_2, "")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 460, 951, 192))
        self.textBrowser.setAcceptRichText(True)
        self.textBrowser.setSearchPaths([])
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 972, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.lists.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_3.clicked.connect(self.select_all_accs)
        self.pushButton_4.clicked.connect(self.deselect_all_accs)
        self.pushButton_5.clicked.connect(self.select_all_locs)
        self.pushButton_6.clicked.connect(self.deselect_all_locs)
        self.pushButton.clicked.connect(self.give_picture)
        self.pushButton_2.clicked.connect(self.start_start)

    def give_picture(self):
        self.file_dialog = QtWidgets.QFileDialog()
        self.file_dialog.setWindowTitle("Select a file")
        self.file_dialog.setNameFilter("All Files (*)")
        if self.file_dialog.exec():
            file_path = self.file_dialog.selectedFiles()[0]
            self.aks = file_path
            self.textBrowser_2.setText(file_path)
        else:
            self.aks = ""
            self.textBrowser_2.setText("")

    def start_start(self):
        acounts = []
        locations = []
        locations_limit = {}

        for i , v in enumerate(self.accs):
            app.processEvents()
            if self.accs[i].isChecked():
                acounts.append(self.accs[i].text())
        if not acounts:
            self.textBrowser.setText("هیچ اکانتی انتخاب نشده است")
        else:
            self.textBrowser.setText("")
            for i, v in enumerate(self.locs):
                app.processEvents()
                if self.locs[i].isChecked():
                    locations.append(self.locs[i].text())
                    locations_limit[self.locs[i].text()] = self.linee[i].text()
            if not locations:
                self.textBrowser.setText("هیچ مکانی انتخاب نشده است")
            else:
                self.textBrowser.setText("")
                self.textBrowser.append("در حال ساخت جدول tmp")
                with mysql.connector.connect(password=DATABASE_PASSWORD, user=DATABASE_USER, host=DATABASE_HOST, database=DATABASE_NAME) as connection:
                    with connection.cursor() as cursor:
                        sql = f"CREATE TABLE IF NOT EXISTS tmp (`id` VARCHAR(255) NOT NULL , `username` VARCHAR(255) NOT NULL , `phone` VARCHAR(255) NOT NULL , UNIQUE (`id`)) ENGINE = InnoDB;"
                        cursor.execute(sql)
                    connection.commit()
                self.textBrowser.append("آماده سازی برای شروع انتقال افراد انتخاب شده به جدول tmp در 5 ثانیه آینده")
                for i in range(1, 6):
                    app.processEvents()
                    self.textBrowser.append(f"{i}...")
                    sleep(1)
                self.textBrowser.setText("")
                for i in locations:
                    app.processEvents()
                    m, n = locations_limit[i].split("-")
                    m, n = int(m), int(n)
                    offset = m - 1
                    limit = (n - m) + 1
                    tmp_table = []
                    with mysql.connector.connect(password=DATABASE_PASSWORD, user=DATABASE_USER, host=DATABASE_HOST,
                                                 database=DATABASE_NAME) as connection:
                        with connection.cursor() as cursor:
                            sql = f"SELECT id, username, phone FROM {i} LIMIT {limit} OFFSET {offset}"
                            cursor.execute(sql)
                            self.textBrowser.append(f"در حال انتقال کاربران از {i} به جدول tmp")
                            for row in cursor:
                                app.processEvents()
                                id, username, phone = row
                                tmp_table.append({"id": id, "username": username, "phone": phone})
                        connection.commit()
                    for j in tmp_table:
                        id, username, phone = j["id"], j["username"], j["phone"]
                        try:
                            with mysql.connector.connect(password=DATABASE_PASSWORD, user=DATABASE_USER,
                                                         host=DATABASE_HOST,
                                                         database=DATABASE_NAME) as connection:
                                with connection.cursor() as cursor:
                                    sql = f"INSERT INTO tmp (id, username, phone ) VALUES ('{id}', '{username}', '{phone}')"
                                    cursor.execute(sql)
                                connection.commit()
                            self.textBrowser.append(f"{id},{username},{phone}    done")
                            app.processEvents()
                        except:
                            self.textBrowser.append(f"{id},{username},{phone}    tekrariii ast")
                            app.processEvents()
                            pass
                user_number = 0
                with mysql.connector.connect(password=DATABASE_PASSWORD, user=DATABASE_USER,
                                             host=DATABASE_HOST,
                                             database=DATABASE_NAME) as connection:
                    with connection.cursor() as cursor:
                        sql = f"SELECT count(*) FROM tmp"
                        cursor.execute(sql)
                        user_number = cursor.fetchone()[0]
                    connection.commit()
                accs_len = len(acounts)
                o = 0
                oo = 0
                if self.aks:
                    self.textBrowser.setText("ارسال پیام همراه با عکس انجام خواهد شد")
                    client = TelegramClient(acounts[o], api_hash=API_HASH, api_id=API_ID)
                    client.start()
                    while oo < user_number:
                        app.processEvents()
                        id_number = ""
                        phone_number = ""
                        user_name = ""
                        self.textBrowser.append(f"{oo} from {user_number}")
                        with mysql.connector.connect(password=DATABASE_PASSWORD, user=DATABASE_USER,
                                                     host=DATABASE_HOST,
                                                     database=DATABASE_NAME) as connection:
                            with connection.cursor() as cursor:
                                sql = f"SELECT id,username, phone FROM tmp LIMIT 1"
                                cursor.execute(sql)
                                id_number, user_name, phone_number = cursor.fetchone()
                            connection.commit()
                        app.processEvents()
                        if phone_number != "None":
                            contact = InputPhoneContact(client_id=0, phone=f"+{phone_number}", first_name="hello", last_name="fe")
                            result = client(ImportContactsRequest([contact]))
                            try:
                                ent = client.get_entity(f"+{phone_number}")
                                try:
                                    client.send_file(ent, self.aks, caption=self.plainTextEdit.toPlainText())
                                    oo += 1
                                    self.textBrowser.append(f"ارسال به {phone_number} با موفقیت انجام شد")
                                    app.processEvents()
                                    with mysql.connector.connect(password=DATABASE_PASSWORD, user=DATABASE_USER,
                                                                 host=DATABASE_HOST,
                                                                 database=DATABASE_NAME) as connection:
                                        with connection.cursor() as cursor:
                                            sql = f"DELETE FROM tmp WHERE id='{id_number}'"
                                            cursor.execute(sql)
                                        connection.commit()
                                except FloodWaitError:
                                    client.disconnect()
                                    self.textBrowser.append(f"accont {acounts[o]} has limited")
                                    o += 1
                                    if o == accs_len:
                                        o = 0
                                    self.textBrowser.append(f"try to connect with {acounts[0]}")
                                    client = TelegramClient(acounts[o], api_hash=API_HASH, api_id=API_ID)
                                    client.start()
                                    continue
                            except ValueError:
                                with mysql.connector.connect(password=DATABASE_PASSWORD, user=DATABASE_USER,
                                                             host=DATABASE_HOST,
                                                             database=DATABASE_NAME) as connection:
                                    with connection.cursor() as cursor:
                                        sql = f"DELETE FROM tmp WHERE id='{id_number}'"
                                        cursor.execute(sql)
                                    connection.commit()
                                oo += 1

                        elif user_name != "None":
                            try:
                                ent = client.get_entity(f"@{user_name}")
                                try:
                                    client.send_file(ent, self.aks, caption=self.plainTextEdit.toPlainText())
                                    oo += 1
                                    self.textBrowser.append(f"ارسال به {username} با موفقیت انجام شد")
                                    app.processEvents()
                                    with mysql.connector.connect(password=DATABASE_PASSWORD, user=DATABASE_USER,
                                                                 host=DATABASE_HOST,
                                                                 database=DATABASE_NAME) as connection:
                                        with connection.cursor() as cursor:
                                            sql = f"DELETE FROM tmp WHERE id='{id_number}'"
                                            cursor.execute(sql)
                                        connection.commit()
                                except FloodWaitError:
                                    client.disconnect()
                                    self.textBrowser.append(f"accont {acounts[o]} has limited")
                                    o += 1
                                    if o == accs_len:
                                        o = 0
                                    self.textBrowser.append(f"try to connect with {acounts[0]}")
                                    client = TelegramClient(acounts[o], api_hash=API_HASH, api_id=API_ID)
                                    client.start()
                                    continue
                            except ValueError:
                                with mysql.connector.connect(password=DATABASE_PASSWORD, user=DATABASE_USER,
                                                             host=DATABASE_HOST,
                                                             database=DATABASE_NAME) as connection:
                                    with connection.cursor() as cursor:
                                        sql = f"DELETE FROM tmp WHERE id='{id_number}'"
                                        cursor.execute(sql)
                                    connection.commit()
                                oo += 1

                        else:
                            self.textBrowser.append(f"کاربر با آیدی {id_number}فاقد شماره تلفن و نام کاربری می باشد")
                            app.processEvents()
                            with mysql.connector.connect(password=DATABASE_PASSWORD, user=DATABASE_USER,
                                                         host=DATABASE_HOST,
                                                         database=DATABASE_NAME) as connection:
                                with connection.cursor() as cursor:
                                    sql = f"DELETE FROM tmp WHERE id='{id_number}'"
                                    cursor.execute(sql)
                                connection.commit()
                            oo += 1

                    self.textBrowser.setText("عملیات با موفقیت با اتمام رسید")
                else:
                    self.textBrowser.setText("ارسال پیام بدون عکس انجام خواهد شد")
                    client = TelegramClient(acounts[o], api_hash=API_HASH, api_id=API_ID)
                    client.start()
                    while oo < user_number:
                        app.processEvents()
                        id_number = ""
                        phone_number = ""
                        user_name = ""
                        self.textBrowser.append(f"{oo} from {user_number}")
                        with mysql.connector.connect(password=DATABASE_PASSWORD, user=DATABASE_USER,
                                                     host=DATABASE_HOST,
                                                     database=DATABASE_NAME) as connection:
                            with connection.cursor() as cursor:
                                sql = f"SELECT id,username, phone FROM tmp LIMIT 1"
                                cursor.execute(sql)
                                id_number, user_name, phone_number = cursor.fetchone()
                            connection.commit()
                        app.processEvents()
                        if phone_number != "None":
                            contact = InputPhoneContact(client_id=0, phone=f"+{phone_number}", first_name="hello", last_name="fe")
                            result = client(ImportContactsRequest([contact]))
                            try:
                                ent = client.get_entity(f"+{phone_number}")
                                try:
                                    client.send_message(ent, self.plainTextEdit.toPlainText())
                                    oo += 1
                                    self.textBrowser.append(f"ارسال به {phone_number} با موفقیت انجام شد")
                                    app.processEvents()
                                    with mysql.connector.connect(password=DATABASE_PASSWORD, user=DATABASE_USER,
                                                                 host=DATABASE_HOST,
                                                                 database=DATABASE_NAME) as connection:
                                        with connection.cursor() as cursor:
                                            sql = f"DELETE FROM tmp WHERE id='{id_number}'"
                                            cursor.execute(sql)
                                        connection.commit()
                                except FloodWaitError:
                                    client.disconnect()
                                    self.textBrowser.append(f"accont {acounts[o]} has limited")
                                    o += 1
                                    if o == accs_len:
                                        o = 0
                                    self.textBrowser.append(f"try to connect with {acounts[0]}")
                                    client = TelegramClient(acounts[o], api_hash=API_HASH, api_id=API_ID)
                                    client.start()
                                    continue
                            except ValueError:
                                with mysql.connector.connect(password=DATABASE_PASSWORD, user=DATABASE_USER,
                                                             host=DATABASE_HOST,
                                                             database=DATABASE_NAME) as connection:
                                    with connection.cursor() as cursor:
                                        sql = f"DELETE FROM tmp WHERE id='{id_number}'"
                                        cursor.execute(sql)
                                    connection.commit()
                                oo += 1

                        elif user_name != "None":
                            try:
                                ent = client.get_entity(f"@{user_name}")
                                try:
                                    client.send_message(ent, self.plainTextEdit.toPlainText())
                                    oo += 1
                                    self.textBrowser.append(f"ارسال به {username} با موفقیت انجام شد")
                                    app.processEvents()
                                    with mysql.connector.connect(password=DATABASE_PASSWORD, user=DATABASE_USER,
                                                                 host=DATABASE_HOST,
                                                                 database=DATABASE_NAME) as connection:
                                        with connection.cursor() as cursor:
                                            sql = f"DELETE FROM tmp WHERE id='{id_number}'"
                                            cursor.execute(sql)
                                        connection.commit()
                                except FloodWaitError:
                                    client.disconnect()
                                    self.textBrowser.append(f"accont {acounts[o]} has limited")
                                    o += 1
                                    if o == accs_len:
                                        o = 0
                                    self.textBrowser.append(f"try to connect with {acounts[0]}")
                                    client = TelegramClient(acounts[o], api_hash=API_HASH, api_id=API_ID)
                                    client.start()
                                    continue
                            except ValueError:
                                with mysql.connector.connect(password=DATABASE_PASSWORD, user=DATABASE_USER,
                                                             host=DATABASE_HOST,
                                                             database=DATABASE_NAME) as connection:
                                    with connection.cursor() as cursor:
                                        sql = f"DELETE FROM tmp WHERE id='{id_number}'"
                                        cursor.execute(sql)
                                    connection.commit()
                                oo += 1

                        else:
                            self.textBrowser.append(f"کاربر با آیدی {id_number}فاقد شماره تلفن و نام کاربری می باشد")
                            app.processEvents()
                            with mysql.connector.connect(password=DATABASE_PASSWORD, user=DATABASE_USER,
                                                         host=DATABASE_HOST,
                                                         database=DATABASE_NAME) as connection:
                                with connection.cursor() as cursor:
                                    sql = f"DELETE FROM tmp WHERE id='{id_number}'"
                                    cursor.execute(sql)
                                connection.commit()
                            oo += 1

                    self.textBrowser.setText("عملیات با موفقیت با اتمام رسید")







    def select_all_locs(self):
        for i, v in enumerate(self.locs):
            self.locs[i].setChecked(True)

    def deselect_all_locs(self):
        for i, v in enumerate(self.locs):
            self.locs[i].setChecked(False)

    def select_all_accs(self):
        for i, v in enumerate(self.accs):
            self.accs[i].setChecked(True)

    def deselect_all_accs(self):
        for i, v in enumerate(self.accs):
            self.accs[i].setChecked(False)

    def give_number_of_table(self, table_name):
        tmp = 0
        with mysql.connector.connect(user=DATABASE_USER, host=DATABASE_HOST, password=DATABASE_PASSWORD, database=DATABASE_NAME) as connection:
            with connection.cursor() as cursor:
                sql = f"SELECT COUNT(*) FROM {table_name}"
                cursor.execute(sql)
                tmp = cursor.fetchone()[0]
            connection.commit()
        return tmp
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "انتخاب همه"))
        self.pushButton_4.setText(_translate("MainWindow", "لغو انتخاب"))
        for i, v in enumerate(self.accs_name):
            self.accs[i].setText(_translate("MainWindow", v))
        self.lists.setTabText(self.lists.indexOf(self.tab), _translate("MainWindow", "لیست اکانت ها"))
        for i, v in enumerate(self.locs_name):
            self.locs[i].setText(_translate("MainWindow", v))
            self.linee[i].setText(_translate("MainWindow", f"1-{self.give_number_of_table(v)}"))

        self.pushButton_5.setText(_translate("MainWindow", "انتخاب همه"))
        self.pushButton_6.setText(_translate("MainWindow", "لغو انتخاب"))
        self.lists.setTabText(self.lists.indexOf(self.ListGroups), _translate("MainWindow", "لیست شهر ها"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "test jhbhuvhuvh"))
        self.pushButton.setText(_translate("MainWindow", "عکس"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sakkal Majalla\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "شروع ارسال"))
        self.lists.setTabText(self.lists.indexOf(self.tab_2), _translate("MainWindow", "متن پیام"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
