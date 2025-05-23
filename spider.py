# Form implementation generated from reading ui file '.\spider.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from time import sleep
from config import DATABASE_NAME, DATABASE_HOST, DATABASE_PASSWORD, DATABASE_USER, DEFUALT_LINKS, API_ID, API_HASH, MESSAGE_LIMIT, DELAY
from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import FloodWaitError, UserAlreadyParticipantError, InviteHashExpiredError, InviteRequestSentError, ChatInvalidError
from telethon import functions
from telethon.tl.functions.channels import GetFullChannelRequest
from bs4 import BeautifulSoup
import requests
import os
import keyboard
import mysql.connector
import re
import csv





class Ui_MainWindow(object):

    def update_acc(self):
        try:
            with mysql.connector.connect(user=DATABASE_USER, password=DATABASE_PASSWORD, database=DATABASE_NAME, host=DATABASE_HOST) as connections:
                with connections.cursor() as cursor:
                    sql = "SELECT number FROM accs"
                    cursor.execute(sql)
                    for i in cursor:
                        self.mamad.append(i[0])
                        self.zahra.append(i[0])
                    connections.commit()
        except:
            pass

    def update_groups_list(self):
        try:
            with mysql.connector.connect(user=DATABASE_USER, password=DATABASE_PASSWORD, database=DATABASE_NAME, host=DATABASE_HOST) as connections:
                with connections.cursor() as cursor:
                    sql = "SELECT title FROM groups ORDER BY tartib"
                    cursor.execute(sql)
                    for i in cursor:
                        self.haman.append(i[0])
                        self.mahdieh.append(i[0])
                    connections.commit()
        except:
            pass

    def setupUi(self, MainWindow):
        self.mamad = []
        self.zahra = []
        self.haman = []
        self.mahdieh = []

        self.update_acc()
        self.update_groups_list()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(972, 728)
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addacount = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addacount.setGeometry(QtCore.QRect(10, 10, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Sakkal Majalla")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.addacount.setFont(font)
        self.addacount.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.addacount.setMouseTracking(False)
        self.addacount.setTabletTracking(False)
        self.addacount.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.addacount.setAcceptDrops(False)
        self.addacount.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.addacount.setAutoFillBackground(False)
        self.addacount.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.addacount.setCheckable(False)
        self.addacount.setChecked(False)
        self.addacount.setAutoRepeat(False)
        self.addacount.setAutoExclusive(False)
        self.addacount.setAutoDefault(False)
        self.addacount.setDefault(True)
        self.addacount.setFlat(False)
        self.addacount.setObjectName("addacount")
        self.readgroup = QtWidgets.QPushButton(parent=self.centralwidget)
        self.readgroup.setGeometry(QtCore.QRect(150, 10, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Sakkal Majalla")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.readgroup.setFont(font)
        self.readgroup.setDefault(True)
        self.readgroup.setObjectName("readgroup")
        self.lists = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.lists.setGeometry(QtCore.QRect(10, 80, 541, 381))
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
        self.selectallzero = QtWidgets.QPushButton(parent=self.tab)
        self.selectallzero.setGeometry(QtCore.QRect(20, 10, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.selectallzero.setFont(font)
        self.selectallzero.setDefault(True)
        self.selectallzero.setObjectName("selectallzero")
        self.deselectallzero = QtWidgets.QPushButton(parent=self.tab)
        self.deselectallzero.setGeometry(QtCore.QRect(130, 10, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.deselectallzero.setFont(font)
        self.deselectallzero.setDefault(True)
        self.deselectallzero.setObjectName("deselectallzero")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.tab)
        self.scrollArea.setGeometry(QtCore.QRect(10, 40, 331, 311))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 329, 309))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout1 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout1.setObjectName("verticalLayout1")
        if self.mamad:
            for i, v in enumerate(self.mamad):
                self.mamad[i] = QtWidgets.QCheckBox(parent=self.scrollAreaWidgetContents)
                self.mamad[i].setGeometry(QtCore.QRect(10, 10 + (i * 30), 311, 20))
                self.mamad[i].setObjectName(v)
                self.verticalLayout1.addWidget(self.mamad[i])
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.lists.addTab(self.tab, "")
        self.ListGroups = QtWidgets.QWidget()
        self.ListGroups.setObjectName("ListGroups")
        self.scrollArea_3 = QtWidgets.QScrollArea(parent=self.ListGroups)
        self.scrollArea_3.setGeometry(QtCore.QRect(10, 40, 331, 311))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")

        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 329, 309))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout.setObjectName("verticalLayout")
        if self.haman:
            for i, v in enumerate(self.haman):
                self.haman[i] = QtWidgets.QCheckBox(parent=self.scrollAreaWidgetContents_3)
                self.haman[i].setGeometry(QtCore.QRect(10, 10 + (i * 30), 311, 20))
                self.haman[i].setObjectName(v)
                self.verticalLayout.addWidget(self.haman[i])
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.scrollArea_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.selectallone = QtWidgets.QPushButton(parent=self.ListGroups)
        self.selectallone.setGeometry(QtCore.QRect(20, 10, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.selectallone.setFont(font)
        self.selectallone.setObjectName("selectallone")
        self.deselectallone = QtWidgets.QPushButton(parent=self.ListGroups)
        self.deselectallone.setGeometry(QtCore.QRect(130, 10, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.deselectallone.setFont(font)
        self.deselectallone.setAutoDefault(False)
        self.deselectallone.setDefault(False)
        self.deselectallone.setFlat(False)
        self.deselectallone.setObjectName("deselectallone")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.ListGroups)
        self.lineEdit_2.setGeometry(QtCore.QRect(332, 10, 191, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.ListGroups)
        self.pushButton_9.setGeometry(QtCore.QRect(230, 10, 93, 28))
        self.pushButton_9.setObjectName("pushButton_9")
        self.lists.addTab(self.ListGroups, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.matnersalli = QtWidgets.QPlainTextEdit(parent=self.tab_2)
        self.matnersalli.setGeometry(QtCore.QRect(0, 0, 481, 351))
        self.matnersalli.setObjectName("matnersalli")
        self.lists.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.tab_3)
        self.lineEdit.setGeometry(QtCore.QRect(80, 60, 421, 41))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.tab_3)
        self.pushButton_8.setGeometry(QtCore.QRect(190, 150, 221, 51))
        self.pushButton_8.setObjectName("pushButton_8")
        self.lists.addTab(self.tab_3, "")
        self.startsend = QtWidgets.QPushButton(parent=self.centralwidget)
        self.startsend.setGeometry(QtCore.QRect(290, 10, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Sakkal Majalla")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.startsend.setFont(font)
        self.startsend.setDefault(True)
        self.startsend.setObjectName("startsend")
        self.readdatabase = QtWidgets.QPushButton(parent=self.centralwidget)
        self.readdatabase.setGeometry(QtCore.QRect(430, 10, 121, 51))
        self.readdatabase.setFont(font)
        self.readdatabase.setDefault(True)
        self.readdatabase.setObjectName("readdatabase")


        self.textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 470, 951, 192))
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
        self.lists.setCurrentIndex(0)
        self.addacount.clicked.connect(self.add_acc_btn) # type: ignore
        self.readgroup.clicked.connect(self.readgroup_btn) # type: ignore
        self.startsend.clicked.connect(self.stat_send_btn) # type: ignore
        self.readdatabase.clicked.connect(self.read_database)
        self.deselectallone.clicked.connect(self.deselect_all_one_btn) # type: ignore
        self.deselectallzero.clicked.connect(self.deselect_all_zero_btn) # type: ignore
        self.selectallone.clicked.connect(self.select_all_one_btn) # type: ignore
        self.selectallzero.clicked.connect(self.select_all_zero_btn) # type: ignore
        self.pushButton_8.clicked.connect(self.manualinsert)
        self.pushButton_9.clicked.connect(self.select_all_one_btnx)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def manualinsert(self):
        text = self.lineEdit.text()
        self.handel_insert("man input", "man input", "man input", text, "group", "man input", "man input")
        self.textBrowser.append(f"با موفقیت وارد دیتا بیس گردید{text}")

    def read_database(self):
        self.textBrowser.setText("در حال به وجود آوردن فایل خروجی لطفا منتظر بمانید")
        with mysql.connector.connect(user=DATABASE_USER, password=DATABASE_PASSWORD, host=DATABASE_HOST,
                                         database=DATABASE_NAME) as connection:
            with connection.cursor() as cursor:
                sql = f"SELECT * FROM groups"
                cursor.execute(sql)
                header = ['link', 'title', 'description', 'sub']
                with open("database.csv", "w", encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(header)
                    app.processEvents()
                    for i in cursor:
                        app.processEvents()
                        data = [i[1], i[3], i[5], f"{i[4]}"]
                        writer.writerow(data)

                connection.commit()
        self.textBrowser.append("خروجی با موفقیت انجام شده و در فایل database.csv دخیره گردید")


    def check_link(self, link):
        if "t.me" in link:
            tmp = link.split("/")
            if len(tmp) == 5 and tmp[3] == 'joinchat':
                return (3, tmp[4])
            else:
                try:
                    tmp1 = tmp[3]
                    if tmp1[0] == "+":
                        return (2, tmp1[1:])
                    else:
                        return (1, tmp1)
                except:
                    return (5, 5)

        else:
            return (5, 5)




    def check_temp(self, temp_link):
        try:
            with mysql.connector.connect(user=DATABASE_USER, password=DATABASE_PASSWORD, host=DATABASE_HOST,
                                         database=DATABASE_NAME) as connection:
                with connection.cursor() as cursor:
                    sql = f"INSERT INTO tmp (link) VALUES ('{temp_link}')"
                    cursor.execute(sql)
                    connection.commit()

            return True

        except:
            return False

    def insertdate(self, id, title, hash, link, type, sub, des):
        try:
            with mysql.connector.connect(user=DATABASE_USER, password=DATABASE_PASSWORD, host=DATABASE_HOST,
                                         database=DATABASE_NAME) as connection:
                with connection.cursor() as cursor:
                    sql = f"INSERT INTO {type} (id, link, hash, title, sub, des) VALUES ('{id}', '{link}', '{hash}', '{title}', '{sub}', '{des}')"
                    self.textBrowser.append(sql)
                    cursor.execute(sql)
                    connection.commit()

            return True

        except:
            return False



    def add_acc_btn(self):
        os.system("start cmd")
        sleep(1.5)
        keyboard.write("python addacount.py")
        keyboard.press_and_release("Enter")


    def give_acc_for_reading(self):
        if not self.mamad:
            return "not mamad"
        for i, v in enumerate(self.mamad):
            if self.mamad[i].isChecked():
                return self.mamad[i].text()

        return False

    def handel_insert(self, id, title, hash, link, type, sub, des):
        if type == 'channel':
            if self.insertdate(id, title, hash, link, "channels", sub, des):
                pass
            else:
                self.textBrowser.append("link tekrari")
        elif type == "group":
            if self.insertdate(id, title, hash, link, "groups", sub, des):
                pass
            else:
                self.textBrowser.append("link tekrari")
        else:
            if self.insertdate(id, title, hash, link, "mega", sub, des):
                pass
            else:
                self.textBrowser.append("link tekrari")
    def readgroup_btn(self):
        test = self.give_acc_for_reading()
        if test == "not mamad":
            self.textBrowser.setText("لطفا ابتدا یک اکانت اضافه نمایید")
        elif test == False:
            self.textBrowser.setText("لطفا یک اکانت برای استخراج گروه ها انتخاب نمایید")
        else:
            self.textBrowser.setText("")
            self.textBrowser.append("در حال اتصال به تلگرام")
            client = TelegramClient(test, api_hash=API_HASH, api_id=API_ID)
            client.start()
            self.textBrowser.append("اتصال به تلگرام با موفقیت انجام شد")

            def main_work(link):
                tmp = self.check_link(link)
                if tmp[0] == 1:
                    try:
                        ent = client.get_entity(tmp[1])
                        ch_full = client(GetFullChannelRequest(channel=ent))
                        des = ch_full.full_chat.about
                        if not des:
                            des = "no des"

                        sub = ch_full.full_chat.participants_count
                        if not sub:
                            sub = "no sub"
                        if ent.broadcast:
                            self.handel_insert(ent.id, ent.title, ent.access_hash, link, "channel", sub, des)
                        elif ent.megagroup:
                            self.handel_insert(ent.id, ent.title, ent.access_hash, link, "group", sub, des)
                        else:
                            self.handel_insert(ent.id, ent.title, ent.access_hash, link, "mega", sub, des)
                    except:
                        pass
                else:
                    try:
                        r = requests.get(link).text

                        soup = BeautifulSoup(r, features="html.parser")
                        try:
                            vvv = str(soup.find_all('a', class_="tgme_action_button_new shine")[0])
                            name = soup.find_all('span')[0].text
                            subg = str(soup.find_all("div", class_="tgme_page_extra")[0].text)
                            try:
                                nnn = str(soup.find_all("div", class_="tgme_page_description")[0].text)
                            except:
                                nnn = "no descriptions"
                            if "Channel" in vvv:
                                self.insertdate("not", name, "not", link, "channels", subg, nnn)
                            else:
                                self.insertdate("not", name, "not", link, "groups", subg, nnn)
                        except:
                            self.textBrowser.append("این لینک نا معتبر است")
                    except:
                        pass








                # else:
                #     try:
                #         result = client(functions.messages.ImportChatInviteRequest(
                #             hash=tmp[1]
                #         ))
                #         ent = client.get_entity(link)
                #     except FloodWaitError as error:
                #         errorr = int(str(error).split(" ")[3]) + 4
                #         self.textBrowser.append(f"sleep for {errorr} secoond")
                #         sleep(errorr)
                #         result = client(functions.messages.ImportChatInviteRequest(
                #             hash=tmp[1]
                #         ))
                #         ent = client.get_entity(link)
                #     except UserAlreadyParticipantError:
                #         ent = client.get_entity(link)

                    # if ent.broadcast:
                    #     self.handel_insert(ent.id, ent.title, ent.access_hash, link, "channel")
                    # elif ent.megagroup:
                    #     self.handel_insert(ent.id, ent.title, ent.access_hash, link, "group")
                    # else:
                    #     self.handel_insert(ent.id, ent.title, ent.access_hash, link, "mega")
            for link in DEFUALT_LINKS:
                tmp = self.check_link(link)
                app.processEvents()
                if tmp:
                    if tmp[0] == 1:
                        ent = client.get_entity(tmp[1])
                        result = client(functions.channels.JoinChannelRequest(
                            channel=ent
                        ))
                        self.textBrowser.append(f"در حال خواندن {MESSAGE_LIMIT}پیام از کانال {ent.title}")
                        messages = client.get_messages(ent, limit=MESSAGE_LIMIT)
                        self.textBrowser.append(f"خواندن پیام ها از کانال {ent.title}با موفقیت انجام شد")
                        for message in messages:
                            app.processEvents()
                            x = message.message
                            if x:
                                links = re.findall(r'https?://\S+', x)
                                if links:
                                    t = links[0]
                                    if self.check_temp(t):
                                        main_work(t)
                                        self.textBrowser.append(f"done with {t}")
                                    else:
                                        self.textBrowser.append("in link tekrari ast")
                    else:
                        try:
                            result = client(functions.messages.ImportChatInviteRequest(
                                hash=tmp[1]
                            ))
                            ent = client.get_entity(link)
                        except FloodWaitError as error:
                            errorr = int(str(error).split(" ")[3]) + 4
                            self.textBrowser.append(f"sleep for {errorr} secoond")
                            sleep(errorr)
                            result = client(functions.messages.ImportChatInviteRequest(
                                hash=tmp[1]
                            ))
                            ent = client.get_entity(link)
                        except UserAlreadyParticipantError:
                            ent = client.get_entity(link)
                        self.textBrowser.append(f"در حال خواندن {MESSAGE_LIMIT}پیام از کانال {ent.title}")
                        messages = client.get_messages(ent, limit=MESSAGE_LIMIT)
                        self.textBrowser.append(f"خواندن پیام ها از کانال {ent.title}با موفقیت انجام شد")
                        for message in messages:
                            app.processEvents()
                            x = message.message
                            if x:
                                links = re.findall(r'https?://\S+', x)
                                if links:
                                    t = links[0]
                                    if self.check_temp(t):
                                        main_work(t)
                                        self.textBrowser.append(f"done with {t}")
                                    else:
                                        self.textBrowser.append("in link tekrari ast")
            self.textBrowser.append("عملیات با موفقیت به پایان رسید")



    def reading_group_cheked(self):
        if not self.haman:
            return "not haman"
        tmp = []
        for i , v in enumerate(self.haman):
            if self.haman[i].isChecked():
                app.processEvents()
                tmp.append(self.haman[i].text())
        if tmp:
            return tmp
        else:
            return False

    def give_acc_for_reading1(self):
        if not self.mamad:
            return "not mamad"
        tmp = []
        for i, v in enumerate(self.mamad):
            if self.mamad[i].isChecked():
                tmp.append(self.mamad[i].text())

        if tmp:
            return tmp
        else:
            return False





    def stat_send_btn(self):
        test = self.reading_group_cheked()
        if test == "not haman":
            self.textBrowser.setText("لطفا ابتدا گروه استخراج کنید اضافه نمایید")
        elif test == False:
            self.textBrowser.setText("لطفا حد اقل یک گروه را انتخاب نمایید")
        else:
            test1 = self.give_acc_for_reading1()
            if test1 == "not mamad":
                self.textBrowser.setText("لطفا ابتدا یک اکانت اضافه نمایید")
            elif test1 == False:
                self.textBrowser.setText("لطفا یک اکانت برای استخراج گروه ها انتخاب نمایید")
            else:
                self.textBrowser.setText("")
                self.textBrowser.append("در حال اتصال به تلگرام")
                #TODO
                matn_payam = self.matnersalli.toPlainText()
                acount_number = 0
                acc_ban = 0
                done_coredct = False
                client = TelegramClient(test1[acount_number], api_hash=API_HASH, api_id=API_ID)
                client.start()
                self.textBrowser.append("اتصال به تلگرام با موفقیت انجام شد")
                app.processEvents()
                vbvb = len(test)
                o = 0
                while o < vbvb:
                    group = test[o]
                    app.processEvents()
                    with mysql.connector.connect(user=DATABASE_USER, password=DATABASE_PASSWORD, database=DATABASE_NAME,
                                                 host=DATABASE_HOST) as connections:
                        with connections.cursor() as cursor:
                            sql = f"SELECT link FROM groups WHERE title = '{group}'"
                            cursor.execute(sql)
                            link = [i for i in cursor][0][0]
                            #TODO
                            tmp = self.check_link(link)
                            if tmp[0] == 5:
                                o += 1
                                self.textBrowser.append("لینک ورودی معتبر نمیباشد")
                                continue
                            try:
                                ent = client.get_entity(link)
                            except:
                                try:
                                    client(functions.messages.ImportChatInviteRequest(hash=tmp[1]))
                                    ent = client.get_entity(link)
                                except InviteHashExpiredError:
                                    self.textBrowser.append("گروه مورد نظر منقضی شده است")
                                    o += 1
                                    continue
                                except FloodWaitError as error:
                                    errorr = int(str(error).split(" ")[3]) + 4
                                    self.textBrowser.append(f"مدت زمان محدودیت زمانی اکانت {test1[acount_number]}{errorr}ثانیه می باشد")
                                    self.textBrowser.append(f"اکانت {test1[acount_number]} متوقف شد شروع اتصال به اکانت بعدی")
                                    # if acc_ban == len(test1):
                                    #     done_coredct = True
                                    #     break
                                    if False:
                                        pass
                                    else:
                                        if acount_number + 1 == len(test1):
                                            acount_number = 0
                                        else:
                                            acount_number += 1
                                    client.disconnect()
                                    self.textBrowser.append(f"در حال اتصال به تلگرام با اکانت {test1[acount_number]}")
                                    client = TelegramClient(test1[acount_number], api_hash=API_HASH, api_id=API_ID)
                                    client.start()
                                    self.textBrowser.append("اتصال به تلگرام با موفقیت انجام شد")
                                    continue
                                    # try:
                                    #     result = client(functions.messages.ImportChatInviteRequest(
                                    #         hash=tmp[1]
                                    #     ))
                                    #     ent = client.get_entity(link)
                                    # except InviteHashExpiredError:
                                    #     self.textBrowser.append("گروه مورد نظر منقضی شده است")
                                    #     o += 1
                                    #     continue
                                    # except FloodWaitError:
                                    #     acc_ban += 1
                                    #     continue
                                    # except UserAlreadyParticipantError:
                                    #     ent = client.get_entity(link)
                                except UserAlreadyParticipantError:
                                    ent = client.get_entity(link)
                                except InviteRequestSentError:
                                    self.textBrowser.append("درخواست عضویت ارسال شد برای ارسال به این گروه باید منتظر تایید ادمین بمانید")
                                    o += 1
                                    continue
                                except ValueError:
                                    o += 1
                                    continue
                                except ChatInvalidError:
                                    o+= 1
                                    continue
                            try:
                                client.send_message(ent, matn_payam)
                                self.textBrowser.append(f"ارسال چیام به {test1[acount_number]}با اکانت {group}با موفقیت انجام شد")
                                o += 1
                            except:
                                o += 1
                                app.processEvents()
                                continue
                            app.processEvents()
                            #TODO
                            connections.commit()
                if done_coredct:
                    self.textBrowser.append("عملیات به دلیل مسدودی موقت تمامی اکانت ها متوقف گردید لطفا بعد دوباره تلاش کنید")
                else:
                    self.textBrowser.append("ارسال پیام مورد نظر شما به لیست گروه های انتخاب شده با موفقیت انجام گردید امیدوارم موفق باشید")




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addacount.setText(_translate("MainWindow", "افزودن اکانت"))
        self.readgroup.setText(_translate("MainWindow", "خواندن گروه ها"))
        self.selectallzero.setText(_translate("MainWindow", "انتخاب همه"))
        self.deselectallzero.setText(_translate("MainWindow", "لغو انتخاب"))
        if self.zahra:
            for i, v in enumerate(self.mamad):
                self.mamad[i].setText(_translate("MainWindow", self.zahra[i]))
        self.lists.setTabText(self.lists.indexOf(self.tab), _translate("MainWindow", "لیست اکانت ها"))
        if self.mahdieh:
            for i, v in enumerate(self.haman):
                self.haman[i].setText(_translate("MainWindow", self.mahdieh[i]))
        self.selectallone.setText(_translate("MainWindow", "انتخاب همه"))
        self.deselectallone.setText(_translate("MainWindow", "لغو انتخاب"))
        self.lists.setTabText(self.lists.indexOf(self.ListGroups), _translate("MainWindow", "لیست گروه ها"))
        self.matnersalli.setPlainText(_translate("MainWindow", "test jhbhuvhuvh"))
        self.lists.setTabText(self.lists.indexOf(self.tab_2), _translate("MainWindow", "متن پیام"))
        self.startsend.setText(_translate("MainWindow", "شروع ارسال"))
        self.readdatabase.setText(_translate("MainWindow", "خروجی از دیتا بیس"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "لینک مورد نظر خود را وارد کنید"))
        self.pushButton_8.setText(_translate("MainWindow", "اضافه کردن لینک"))
        self.lists.setTabText(self.lists.indexOf(self.tab_3), _translate("MainWindow", "اضافه کردن دستی"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", f"1-{len(self.haman)}"))
        self.pushButton_9.setText(_translate("MainWindow", "انتخاب کردن"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
