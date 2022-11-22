import sys,os
import time
import pickle
from datetime import datetime
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyperclip as pc
import qrcode
from PIL import ImageQt
import csv



#------------TAB--------------#
class LoginPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Login')
        self.setGeometry(600, 300, 250, 210)
        self.center()
        #------------------ enter program key --------------------------#
        self.programkeylabel = QLabel('ProgramKey:', self)
        self.programkeylabel.move(25, 10)
        self.programkeyedit = QLineEdit(self)
        self.programkeyedit.move(115, 10)
        #---------------- enter Account ---------------------------#
        self.Accountlabel = QLabel('Account:', self)
        self.Accountlabel.move(25, 60)
        self.Accountedit = QLineEdit(self)
        self.Accountedit.move(115, 60)
        #---------------- enter private key ---------------------------#
        self.PrivateKeylabel = QLabel('PrivateKey:', self)
        self.PrivateKeylabel.move(25, 110)
        self.PrivateKeyedit = QLineEdit(self)
        self.PrivateKeyedit.setEchoMode(QLineEdit.Password)
        self.PrivateKeyedit.move(115, 110)
        #------------------- login button -----------------------------#
        self.loginbutton = QPushButton('Login',self)
        self.loginbutton.move(130, 160)
        #------------------- register button --------------------------#
        self.registerbutton = QPushButton('Register',self)
        self.registerbutton.move(20, 160)
    def center(self):
        #計算螢幕長和寬
        screen=QDesktopWidget().screenGeometry()
        #gui介面長和寬
        size=self.geometry()
        #計算中點並移動
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)
    def clear(self):
        self.programkeyedit.clear()
        self.Accountedit.clear()
        self.PrivateKeyedit.clear()   

class ErrorPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('RememberKey')
        self.setGeometry(600, 300, 250, 150)
        self.center()
        self.relogin = QPushButton('retry',self)
        self.relogin.move(75,80)
    def wait(self):
        count = 9
        for i in range(10):
            self.Errorlabel = QLabel('Key Error ...wait..'+ str(count - i), self)
            self.Errorlabel.move(65, 50)
            self.Errorlabel.resize(130,25)
            self.Errorlabel.show()
            self.relogin.hide()
            QApplication.processEvents()
            time.sleep(1)
            if i <9:
                self.Errorlabel.clear()
        self.relogin.show()
    def center(self):
        #計算螢幕長和寬
        screen=QDesktopWidget().screenGeometry()
        #gui介面長和寬
        size=self.geometry()
        #計算中點並移動
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)
    def clear(self):
        self.Errorlabel.clear()

class RegisterPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Register')
        self.setGeometry(600, 300, 258, 200)
        self.center()
        #-------------------Set Account ----------------------#
        self.SetAccountlabel = QLabel('Set Account:', self)
        self.SetAccountlabel.move(25, 10)
        self.SetAccountedit = QLineEdit(self)
        self.SetAccountedit.move(130, 10)
        #-------------------Set private key ----------------------#
        self.SetPrivateKeylabel = QLabel('Set PrivateKey:', self)
        self.SetPrivateKeylabel.move(25, 60)
        self.SetPrivateKeyedit = QLineEdit(self)
        self.SetPrivateKeyedit.setEchoMode(QLineEdit.Password)
        self.SetPrivateKeyedit.move(130, 60)  
        #-------------------Confirm private key ----------------------#
        self.ConfirmPrivateKeylabel = QLabel('Confirm PrivateKey:', self)
        self.ConfirmPrivateKeylabel.move(25, 110)
        self.ConfirmPrivateKeyedit = QLineEdit(self)
        self.ConfirmPrivateKeyedit.setEchoMode(QLineEdit.Password)
        self.ConfirmPrivateKeyedit.move(130, 110)       
        #-------------------Create account ----------------------#
        self.registerbutton = QPushButton('Create',self)
        self.registerbutton.move(130, 160)
        #--------------------relogin -----------------------------#
        self.relogin = QPushButton('return',self)
        self.relogin.move(10,160)  
    def center(self):
        #計算螢幕長和寬
        screen=QDesktopWidget().screenGeometry()
        #gui介面長和寬
        size=self.geometry()
        #計算中點並移動
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)      
    def clear(self):
        self.SetAccountedit.clear()
        self.SetPrivateKeyedit.clear()

class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.keyword = ''
        self.setWindowTitle('RememberKey')
        self.setGeometry(500, 200, 500, 550)
        self.center()
        #------export button------------------#
        self.Exportbutton = QPushButton('Export',self)
        self.Exportbutton.move(380,110)
        #------import button------------------#
        self.Importbutton = QPushButton('Import',self)
        self.Importbutton.move(280,110)
        #---------add button------------------#
        self.ADDbutton = QPushButton('Add',self)
        self.ADDbutton.move(380,140)
        #---------Delete button---------------#
        self.Deletebutton = QPushButton('Delete',self)
        self.Deletebutton.move(380,170)
        #--------Search button --------------#
        self.Searchbutton = QPushButton('Search',self)
        self.Searchbutton.move(130,115)
        #------- RefreshAccountlist button --------------#
        self.RefreshAccountlistbutton = QPushButton('Refresh',self)
        self.RefreshAccountlistbutton.move(130,145)
        #------- Ｓignout button -------------#  
        self.Signoutbutton = QPushButton('Sign out',self)
        self.Signoutbutton.move(380,200)
        #--------Search edit-------------------#
        self.Searchedit = QLineEdit(self)
        self.Searchedit.move(30,125)
        #--------Select Account Label -----------#
        self.SelectAccountlabel = QLabel('Select Account :', self)
        self.SelectAccountlabel.move(30,160)
        #------- AccountName Label ---------#
        self.AccountNamelabel = QLabel('Account Name :',self)
        self.AccountNamelabel.move(30,220)
        #------- AccountText Label ---------#
        self.AccountTextlabel = QLabel('Account :',self)
        self.AccountTextlabel.move(30,250)
        #------- AccountCopy button --------#
        self.AccountCopybutton = QPushButton('Copy',self)
        self.AccountCopybutton.move(300,250)
        #------- AccountCopyQRcode button --------#
        self.AccountCopyQRcodebutton = QPushButton('QRcode',self)
        self.AccountCopyQRcodebutton.move(390,250)
        #------- KeyText label ---------------------#
        self.KeyTextlabel = QLabel('Key :',self)
        self.KeyTextlabel.move(30,280)
        #------- KeyCopy button---------------------#
        self.KeyCopybutton = QPushButton('Copy',self)
        self.KeyCopybutton.move(300,280)
        #-------KeyCopy QRcode button----------------#
        self.KeyCopyQRcodebutton = QPushButton('QRcode',self)
        self.KeyCopyQRcodebutton.move(390,280)   
        #-------PhoneText label----------------------#
        self.PhoneTextlabel =QLabel('Phone :',self)
        self.PhoneTextlabel.move(30,310)  
        #-------PhoneCopy button ---------------------#
        self.PhoneCopybutton = QPushButton('Copy',self)
        self.PhoneCopybutton.move(300,310)
        #-------PhoneCopy QRcode button -------------#
        self.PhoneCopyQRcodebutton = QPushButton('QRcode',self)
        self.PhoneCopyQRcodebutton.move(390,310)   
        #-------IDText label----------------------#
        self.IDTextlabel =QLabel('ID :',self)
        self.IDTextlabel.move(30,340)  
        #-------IDCopy button ---------------------#
        self.IDCopybutton = QPushButton('Copy',self)
        self.IDCopybutton.move(300,340)
        #-------IDCopy QRcode button -------------#
        self.IDCopyQRcodebutton = QPushButton('QRcode',self)
        self.IDCopyQRcodebutton.move(390,340)   
        #------- NoteText label --------------------#
        self.NoteTextlabel = QLabel('Note :',self)
        self.NoteTextlabel.move(30,375)
        #--------Select Account comboBox button---------#
        self.Accountcomboxbutton = QPushButton('select',self)
        self.Accountcomboxbutton.move(220,192)
        #--------Select Group comboBox button---------#
        self.Groupcomboxbutton = QPushButton('select',self)
        self.Groupcomboxbutton.move(220,80)
        #------------Group label-----------------------#
        self.Grouplabel = QLabel('Group: ',self)
        self.Grouplabel.move(30,60)
        #--------create Group button ------------------#
        self.CreateGroupbutton = QPushButton('createGroup',self)
        self.CreateGroupbutton.move(380,80)

    def RefreshGroup(self):
        # #--------Select Group comboBox---------#
        self.Groupcombobox = QComboBox(self)
        self.GroupList = self.UpdateGrouplist()
        self.Groupcombobox.addItems(self.GroupList)
        self.Groupcombobox.resize(200,35)
        self.Groupcombobox.move(30, 80)
        self.Groupcombobox.show()
    def Refresh(self):
        global Wlogin
        global data
        global WHomePage
        #---------Account Label----------------#
        self.mylabel = QLabel(Wlogin.Accountedit.text(), self)
        self.mylabel.move(27, 10)
        self.mylabel.setStyleSheet("background-color: lightgreen") 
        self.mylabel.setFont(QFont('Arial', 30))
        self.mylabel.setStyleSheet("border: 1px solid black;")
        self.mylabel.setAlignment(Qt.AlignCenter)
        self.mylabel.resize(450,50)
        self.mylabel.show()
        #--------Select Account comboBox---------#
        self.Accountcombobox = QComboBox(self)
        self.AccountList = self.UpdateAccountList()
        self.Accountcombobox.addItems(self.AccountList)
        self.Accountcombobox.resize(200,35)
        self.Accountcombobox.move(30, 190)
        self.Accountcombobox.show()
    def CreateRefreshtable(self,HasList):
        global WHomePage,data
        if HasList == False:
            #------- ShowAccount Name Label------#
            self.ShowAccountNamelabel = QLabel('',self)
            self.ShowAccountNamelabel.move(130,225)
            self.ShowAccountNamelabel.resize(200,20)
            self.ShowAccountNamelabel.show()
            #------- ShowAccount Label ---------#
            self.ShowAccountlabel = QLabel('',self)
            self.ShowAccountlabel.move(100,255)
            self.ShowAccountlabel.resize(200,20)
            self.ShowAccountlabel.setStyleSheet("background-color: white") 
            self.ShowAccountlabel.show()        
            #------- ShowKey label ---------------------#
            self.ShowKeylabel = QLabel('',self)
            self.ShowKeylabel.move(100,285)
            self.ShowKeylabel.resize(200,20)
            self.ShowKeylabel.setStyleSheet("background-color: white") 
            self.ShowKeylabel.show()
            #------- ShowPhoen label ---------------------#
            self.ShowPhoenlabel = QLabel('',self)
            self.ShowPhoenlabel.move(100,315)
            self.ShowPhoenlabel.resize(200,20)
            self.ShowPhoenlabel.setStyleSheet("background-color: white") 
            self.ShowPhoenlabel.show()
            #------- ShowID label ---------------------#
            self.ShowIDlabel = QLabel('',self)
            self.ShowIDlabel.move(100,345)
            self.ShowIDlabel.resize(200,20)
            self.ShowIDlabel.setStyleSheet("background-color: white") 
            self.ShowIDlabel.show()
            #------- ShowNoteText label --------------------#
            self.ShowNotelabel = QLabel('',self)
            self.ShowNotelabel.resize(430,130)
            self.ShowNotelabel.setStyleSheet("background-color: white") 
            self.ShowNotelabel.move(30,410)
            self.ShowNotelabel.setWordWrap(True)
            self.ShowNotelabel.show()
        else:
            #------- ShowAccount Name Label------#
            self.ShowAccountNamelabel = QLabel(WHomePage.Accountcombobox.currentText(),self)
            self.ShowAccountNamelabel.move(130,225)
            self.ShowAccountNamelabel.resize(200,20)
            self.ShowAccountNamelabel.show()
            #------- ShowAccount Label ---------#
            self.ShowAccountlabel = QLabel(data[WHomePage.Groupcombobox.currentText()][WHomePage.Accountcombobox.currentText()]['Account'],self)
            self.ShowAccountlabel.move(100,255)
            self.ShowAccountlabel.resize(200,20)
            self.ShowAccountlabel.setStyleSheet("background-color: white") 
            self.ShowAccountlabel.show()        
            #------- ShowKey label ---------------------#
            self.ShowKeylabel = QLabel(data[WHomePage.Groupcombobox.currentText()][WHomePage.Accountcombobox.currentText()]['Key'],self)
            self.ShowKeylabel.move(100,285)
            self.ShowKeylabel.resize(200,20)
            self.ShowKeylabel.setStyleSheet("background-color: white") 
            self.ShowKeylabel.show()
            #------- ShowPhoen label ---------------------#
            self.ShowPhoenlabel = QLabel(data[WHomePage.Groupcombobox.currentText()][WHomePage.Accountcombobox.currentText()]['Phone'],self)
            self.ShowPhoenlabel.move(100,315)
            self.ShowPhoenlabel.resize(200,20)
            self.ShowPhoenlabel.setStyleSheet("background-color: white") 
            self.ShowPhoenlabel.show()
            #------- ShowID label ---------------------#
            self.ShowIDlabel = QLabel(data[WHomePage.Groupcombobox.currentText()][WHomePage.Accountcombobox.currentText()]['ID'],self)
            self.ShowIDlabel.move(100,345)
            self.ShowIDlabel.resize(200,20)
            self.ShowIDlabel.setStyleSheet("background-color: white") 
            self.ShowIDlabel.show()
            #------- ShowNoteText label --------------------#
            self.ShowNotelabel = QLabel(data[WHomePage.Groupcombobox.currentText()][WHomePage.Accountcombobox.currentText()]['Note'],self)
            self.ShowNotelabel.resize(430,130)
            self.ShowNotelabel.setStyleSheet("background-color: white") 
            self.ShowNotelabel.move(30,410)
            self.ShowNotelabel.setWordWrap(True)
            self.ShowNotelabel.show() 
    def refreshtable(self):
        if self.AccountList == []:
            self.CreateRefreshtable(HasList = False)
        if self.AccountList!=[]:
            self.CreateRefreshtable(HasList = True )
    def clear(self):
        self.ShowAccountNamelabel.clear()
        self.ShowAccountlabel.clear()
        self.ShowKeylabel.clear()
        self.ShowNotelabel.clear()
        self.ShowPhoenlabel.clear()
        self.ShowIDlabel.clear()
    def clearmylabel(self):
        self.mylabel.clear()
    def clearSelectbox(self):
        self.Accountcombobox.hide()
    def clearGroupcombobox(self):
        self.Groupcombobox.hide()
    def UpdateGrouplist(self):
        global data 
        Grouplist  =[]
        for item in data :
            if item != 'ProgramAccount':
                Grouplist.append(item)
        return Grouplist
    def UpdateAccountList(self):
        global data
        global WHomePage
        AccountList = []
        if WHomePage.Groupcombobox.currentText()!='':
            if self.keyword =='':
                for item in data[WHomePage.Groupcombobox.currentText()]:
                    AccountList.append(item)  
                return AccountList
            else :
                for item in data[WHomePage.Groupcombobox.currentText()]:
                    if self.keyword in item :
                        AccountList.append(item)
                return AccountList  
        else:
            return AccountList
    def center(self):
        #計算螢幕長和寬
        screen=QDesktopWidget().screenGeometry()
        #gui介面長和寬
        size=self.geometry()
        #計算中點並移動
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)
class AddPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('ADD Account')
        self.setGeometry(500, 200, 350, 500)
        self.center()
        #------- Account Name Label ----------#
        self.AccountNamelabel = QLabel('Account Name:', self)
        self.AccountNamelabel.move(27, 10)
        self.AccountNameedit = QLineEdit(self)
        self.AccountNameedit.resize(200,25)
        self.AccountNameedit.move(127,10)
        #------- ADD account Label ----------#
        self.AddAccountlabel = QLabel('Add Account :', self)
        self.AddAccountlabel.move(27, 45)
        self.AddAccountedit = QLineEdit(self)
        self.AddAccountedit.resize(200,25)
        self.AddAccountedit.move(127,45)
        #------- Account Key Label ---------#
        self.AccountKeylabel = QLabel('Set Key:', self)
        self.AccountKeylabel.move(27, 80)
        self.AccountKeyedit = QLineEdit(self)
        self.AccountKeyedit.resize(200,25)
        self.AccountKeyedit.move(127,80)
        #-------Account Phone label---------#
        self.AccountPhonelabel = QLabel('Set Phone :', self)
        self.AccountPhonelabel.move(27, 115)
        self.AccountPhoneedit = QLineEdit(self)
        self.AccountPhoneedit.resize(200,25)
        self.AccountPhoneedit.move(127,115)
        #-------Account ID label---------#
        self.AccountIDlabel = QLabel('Set ID :', self)
        self.AccountIDlabel.move(27, 150)
        self.AccountIDedit = QLineEdit(self)
        self.AccountIDedit.resize(200,25)
        self.AccountIDedit.move(127,150)
        #-------Account Note Label ----------------#
        self.AccountNotelabel = QLabel('Note:', self)
        self.AccountNotelabel.move(27, 200)
        self.AccountNoteedit = QPlainTextEdit(self)
        self.AccountNoteedit.resize(300,200)
        self.AccountNoteedit.move(27,240)
        #------Save Account button-------------------------#
        self.SaveAccountButton = QPushButton('Save',self)
        self.SaveAccountButton.move(230,460)
        #------ return button ----------------------#
        self.returnbutton = QPushButton('Return', self)
        self.returnbutton.move(27,460) 
    def center(self):
        #計算螢幕長和寬
        screen=QDesktopWidget().screenGeometry()
        #gui介面長和寬
        size=self.geometry()
        #計算中點並移動
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)
    def clear(self):
        self.AccountNameedit.clear()
        self.AddAccountedit.clear()
        self.AccountKeyedit.clear()
        self.AccountPhoneedit.clear()
        self.AccountIDedit.clear()
        self.AccountNoteedit.clear()

class DeletePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        global WHomePage
        self.setWindowTitle('Delete Page')
        self.setGeometry(550, 250, 300, 200)
        self.OKbutton = QPushButton('OK',self)
        self.OKbutton.move(40,160) 
        self.returnbutton = QPushButton('return',self)
        self.returnbutton.move(140,160)  
        self.center()     
    def refreshDeletePage(self):
        stri = 'If you want to delete account 「 '+ WHomePage.Accountcombobox.currentText()+' 」, please enter the account name again.'
        self.deleteAccountlabel = QLabel(stri,self)
        self.deleteAccountlabel.move(15,30)
        self.deleteAccountlabel.resize(260,50)
        self.deleteAccountlabel.setWordWrap(True)
        self.deleteedit = QLineEdit(self)
        self.deleteedit.move(15,90)
        self.deleteedit.resize(260,30)
    def clear(self):
        self.deleteAccountlabel.clear()
        self.deleteedit.clear()
    def center(self):
        #計算螢幕長和寬
        screen=QDesktopWidget().screenGeometry()
        #gui介面長和寬
        size=self.geometry()
        #計算中點並移動
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)

class QRcodePage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('my window')
        self.setGeometry(50, 50, 200, 150)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.mylabel = QLabel('this is an image', self)
        layout.addWidget(self.mylabel)
    def showImage(self,img):
        self.myqimage = img
        self.mylabel.setPixmap(QPixmap.fromImage(self.myqimage))

class CreateGroupPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('CreateGroup')
        self.setGeometry(550, 250, 300, 200)
        self.center()
        self.OKbutton = QPushButton('OK',self)
        self.OKbutton.move(50,160) 
        self.returnbutton = QPushButton('return',self)
        self.returnbutton.move(150,160)  
        self.center() 
        #----------Create Group label---------#
        self.CreateGrouplabel = QLabel('Set Group Name :',self)
        self.CreateGrouplabel.move(90,20)   
        #----------Create Group edit---------#
        self.CreateGroupEdit = QLineEdit(self)
        self.CreateGroupEdit.move(50,60)
        self.CreateGroupEdit.resize(200,30)
    def clear(self):
        self.CreateGroupEdit.clear()
    def center(self):
        #計算螢幕長和寬
        screen=QDesktopWidget().screenGeometry()
        #gui介面長和寬
        size=self.geometry()
        #計算中點並移動
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)
class DeleteGroupPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('DeleteGroup')
        self.setGeometry(500, 200, 500, 550)
        self.center()
    def center(self):
        #計算螢幕長和寬
        screen=QDesktopWidget().screenGeometry()
        #gui介面長和寬
        size=self.geometry()
        #計算中點並移動
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)
#-----------function-----------#
def encode(data):
    for item in data:
        predata =''
        for itm in data[item]:
            for it in data[item][itm]:
                for i in range(len(data[item][itm][it])):
                    predata = predata + chr((ord(data[item][itm][it][i])+60))
                data[item][itm][it]=predata
                predata = ''
    return data


def decode(data):
    for item in data:
        predata =''
        for itm in data[item]:
            for it in data[item][itm]:
                for i in range(len(data[item][itm][it])):
                    predata = predata + chr((ord(data[item][itm][it][i])-60))
                data[item][itm][it]=predata
                predata = ''
    return data


def RefreshData():
    Wlogin
    with open(appPath+'/'+Wlogin.Accountedit.text()+'.json', 'rb') as fp:
        global data
        data = pickle.load(fp)
        data = decode(data)
        fp.close()
def AddAccount(AccountName,Account,Key,Phone,ID,Note):
    global data
    global WHomePage
    if AccountName != '' and WHomePage.Groupcombobox.currentText():
        data[WHomePage.Groupcombobox.currentText()][AccountName]= {'Account':Account,'Key':Key,'Phone':Phone,'ID':ID,'Note':Note}
    else:
        QMessageBox.information(None,'create fail','Please enter the Account Name')
def CreateGroup(group):
    global data
    data[group]={}
def SaveData():
    Wlogin
    with open(appPath+'/'+Wlogin.Accountedit.text()+'.json', 'wb') as fp:
        global data
        data = encode(data)
        pickle.dump(data,fp)
        fp.close()

#----------Action-------------#
def compare():
    if os.path.isfile(appPath+'/'+Wlogin.Accountedit.text()+'.json')== True:
        global data
        global WHomePage
        RefreshData()
        if data['ProgramAccount']['Group']['Key']==Wlogin.PrivateKeyedit.text() and Wlogin.programkeyedit.text()== programkey:
            WHomePage.RefreshGroup()
            WHomePage.Refresh()
            WHomePage.refreshtable()
            WHomePage.show()
            Wlogin.hide()
        else:
            Wlogin.hide()
            WErrorPage.show()
            WErrorPage.wait()
    else:
        Wlogin.hide()
        WErrorPage.show() 
        WErrorPage.wait()  
def ErrorToLogin():
    Wlogin.clear()
    Wlogin.show()
    WErrorPage.clear()
    WErrorPage.hide()   
def RegisterCreate():
    if WRegisterPage.SetPrivateKeyedit.text()!='' and WRegisterPage.SetAccountedit.text()!='' and WRegisterPage.ConfirmPrivateKeyedit.text()!='':
        if os.path.isfile(appPath+'/'+WRegisterPage.SetAccountedit.text()+'.json')== True:
            QMessageBox.information(None, 'Create Fail', 'Create Fail!\nThe account has exist.')
        elif WRegisterPage.SetPrivateKeyedit.text()!=WRegisterPage.ConfirmPrivateKeyedit.text():
            QMessageBox.information(None, 'Create Fail', 'Create Fail!\nConfirm PrivateKey not same as PrivateKey.')
        else:
            QMessageBox.information(None, 'Create successfully!', 'Create successfully!\nPrivate Key will not showing anymore,Please remember it.')
            with open(appPath+'/'+WRegisterPage.SetAccountedit.text()+'.json', 'wb') as fp:
                data ={'ProgramAccount':{'Group':{'Account':'','Key':'','Phone':'','ID':'','Note':''}}}
                data['ProgramAccount']['Group']['Account'] = WRegisterPage.SetAccountedit.text()
                data['ProgramAccount']['Group']['Key'] = WRegisterPage.SetPrivateKeyedit.text()
                data['ProgramAccount']['Group']['Note'] = WRegisterPage.SetAccountedit.text() + WRegisterPage.SetPrivateKeyedit.text()
                data = encode(data)
                pickle.dump(data, fp)
                fp.close()
            Wlogin.clear()
            Wlogin.show()
            WRegisterPage.hide()
    else:
        QMessageBox.information(None, 'Create Fail', 'Please enter the Account and Private Key.')  
def ToRegisterPage():
    global WRegisterPage
    WRegisterPage.clear()
    WRegisterPage.show()
    Wlogin.hide()
def RegisterToLogin():
    global Wlogin
    Wlogin.clear()
    Wlogin.show()
    WRegisterPage.hide()
def HomeToAdd():
    global WAddPage
    WAddPage.clear()
    WAddPage.show()
    WHomePage.hide()
def AddToHome():
    WAddPage.hide()
    WHomePage.show()
def AddPageSave():
    global data
    global WHomePage
    AddAccount(WAddPage.AccountNameedit.text(), WAddPage.AddAccountedit.text(), WAddPage.AccountKeyedit.text(),WAddPage.AccountPhoneedit.text(),WAddPage.AccountIDedit.text(), WAddPage.AccountNoteedit.toPlainText())
    SaveData()
    RefreshData()
    WHomePage.clearmylabel()
    WHomePage.clearSelectbox()
    WHomePage.Refresh()
    WAddPage.hide()
    WHomePage.show()
def SelectAccount():
    global WHomePage
    WHomePage.clear()
    WHomePage.refreshtable()
def DeleteAccount():
    global WHomePage
    if WHomePage.AccountList!=[]:
        WHomePage.hide()
        WDeletePage.refreshDeletePage()
        WDeletePage.show()
    else:
        QMessageBox.information(None,'Delete fail','Nothing to delete.')
def DeleteToHome():
    WDeletePage.hide()
    WDeletePage.clear()
    WHomePage.show()
def CheckToDelete():
    global WHomePage
    global data
    if WDeletePage.deleteedit.text()==WHomePage.Accountcombobox.currentText():
        QMessageBox.information(None,'delete','Delete Successfully!')
        del data[WHomePage.Groupcombobox.currentText()][WHomePage.Accountcombobox.currentText()]
        SaveData()
        RefreshData()
        WHomePage.clearmylabel()
        WHomePage.clearSelectbox()
        WHomePage.Refresh()
        WHomePage.clear()
        WHomePage.refreshtable()
        WDeletePage.clear()
        WDeletePage.hide()
        WHomePage.show()
    else:
        QMessageBox.information(None,'delete','Delete Fail,Please check the Account name.')
def Signout():
    global Wlogin,WHomePage
    WHomePage.hide()
    WHomePage.clearGroupcombobox()
    WHomePage.clearSelectbox()
    WHomePage.clearmylabel()
    WHomePage.clear()
    Wlogin.clear()
    Wlogin.show()
    #copy function#
def CopyAccount():
    if WHomePage.AccountList!=[]:
        pc.copy(data[WHomePage.Groupcombobox.currentText()][WHomePage.Accountcombobox.currentText()]['Account'])
def CopyKey():
    if WHomePage.AccountList!=[]:
        pc.copy(data[WHomePage.Groupcombobox.currentText()][WHomePage.Accountcombobox.currentText()]['Key'])
def CopyPhone():
    if WHomePage.AccountList!=[]:
        pc.copy(data[WHomePage.Groupcombobox.currentText()][WHomePage.Accountcombobox.currentText()]['Phone'])
def CopyID():
    if WHomePage.AccountList!=[]:
        pc.copy(data[WHomePage.Groupcombobox.currentText()][WHomePage.Accountcombobox.currentText()]['ID'])
def CopyAccountByQRcode():
    if WHomePage.AccountList!=[]:
        qr = qrcode.QRCode()
        qr.add_data(data[WHomePage.Groupcombobox.currentText()][WHomePage.Accountcombobox.currentText()]['Account'])
        qr.make()
        img = qr.make_image()
        img = ImageQt.ImageQt(img)
        WshowQRcode.showImage(img)
        WshowQRcode.show()      
def CopyKeyByQRcode():
    if WHomePage.AccountList!=[]:
        qr = qrcode.QRCode()
        qr.add_data(data[WHomePage.Groupcombobox.currentText()][WHomePage.Accountcombobox.currentText()]['Key'])
        qr.make()
        img = qr.make_image()
        img = ImageQt.ImageQt(img)
        WshowQRcode.showImage(img)
        WshowQRcode.show()
def CopyPhoneByQRcode():
    if WHomePage.AccountList!=[]:
        qr = qrcode.QRCode()
        qr.add_data(data[WHomePage.Groupcombobox.currentText()][WHomePage.Accountcombobox.currentText()]['Phone'])
        qr.make()
        img = qr.make_image()
        img = ImageQt.ImageQt(img)
        WshowQRcode.showImage(img)
        WshowQRcode.show()    
def CopyIDByQRcode():
    if WHomePage.AccountList!=[]:
        qr = qrcode.QRCode()
        qr.add_data(data[WHomePage.Groupcombobox.currentText()][WHomePage.Accountcombobox.currentText()]['ID'])
        qr.make()
        img = qr.make_image()
        img = ImageQt.ImageQt(img)
        WshowQRcode.showImage(img)
        WshowQRcode.show()    
    #----------#
def SearchAccount():
    global WHomePage
    WHomePage.keyword =  WHomePage.Searchedit.text()
    WHomePage.clearSelectbox()
    WHomePage.clearmylabel()
    WHomePage.Refresh()
def RefreshAccountList():
    global WHomePage
    WHomePage.keyword = ''
    WHomePage.clearSelectbox()
    WHomePage.clearmylabel()
    WHomePage.Refresh()
def HomeToCreateGroup():
    WHomePage.hide()
    WCreateGroupPage.show()
def CreateGroupToHome():
    WCreateGroupPage.hide()
    WCreateGroupPage.clear()
    WHomePage.show()
def CheckCreateGroup():
    global WCreateGroupPage
    if WCreateGroupPage.CreateGroupEdit.text()!='':
        CreateGroup(WCreateGroupPage.CreateGroupEdit.text())
        SaveData()
        RefreshData()
        WHomePage.clearmylabel()
        WHomePage.clearSelectbox()
        WHomePage.clearGroupcombobox()
        WHomePage.RefreshGroup()
        WHomePage.Refresh()
        WCreateGroupPage.hide()
        WHomePage.show()
    else:
        QMessageBox.information(None,'Create fail','please enter Group name.')
def SelectGroup():
    global WHomePage
    WHomePage.clear()
    WHomePage.clearSelectbox()
    WHomePage.clearmylabel()
    WHomePage.Refresh()
def ExportData():
    if os.path.isfile(appPath+'/output.csv')== True:
        reply = QMessageBox.information(None, 'Export', 'The file has exist, do you want to replace?',
            QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            os.remove(appPath+'/output.csv')
        else:
            QMessageBox.information(None,'Export','Export Failed.')
            return
    try:
        with open('output.csv', 'a') as f:
            writer = csv.writer(f)
            for item in data:
                if item != 'ProgramAccount':
                    writer.writerow([item,'AccountName','Account','Key','Phone','ID','Note'])
                    for itm in data[item]:
                        writer.writerow([None,itm,data[item][itm]['Account'],data[item][itm]['Key'],data[item][itm]['Phone'],data[item][itm]['ID'],data[item][itm]['Note']])
                    writer.writerow([''])
            f.close()
        QMessageBox.information(None,'Export','Export Successfully!')
    except:
        QMessageBox.information(None,'Export','Export Failed.')
def ImportData():
    try:
        global data
        with open('output.csv',newline='') as file:
            re = csv.reader(file)
            for row in re:
                if row[0]!='':
                    group = row[0]
                    data[group]={}
                if row[0]==''and len(row)>2:
                    data[group][row[1]]={'Account':row[2],'Key':row[3],'Phone':row[4],'ID':row[5],'Note':row[6]}
        SaveData()
        RefreshData()
        WHomePage.clearmylabel()
        WHomePage.clearSelectbox()
        WHomePage.clearGroupcombobox()
        WHomePage.RefreshGroup()
        WHomePage.Refresh()
        QMessageBox.information(None,'Import','Import Successful!!')
        print(data)
    except:
        QMessageBox.information(None,'Import','Import Failed.')
#----------listener-------------#
def start():
    #- login page -#
    Wlogin.show()
    Wlogin.loginbutton.clicked.connect(compare)
    Wlogin.registerbutton.clicked.connect(ToRegisterPage)
    #- Error Page -#
    WErrorPage.relogin.clicked.connect(ErrorToLogin)
    #- Register Page -#
    WRegisterPage.registerbutton.clicked.connect(RegisterCreate)
    WRegisterPage.relogin.clicked.connect(RegisterToLogin)
    #- Home Page -#
    WHomePage.CreateGroupbutton.clicked.connect(HomeToCreateGroup)
    WHomePage.Groupcomboxbutton.clicked.connect(SelectGroup)
    WHomePage.Exportbutton.clicked.connect(ExportData)
    WHomePage.Importbutton.clicked.connect(ImportData)
    WHomePage.ADDbutton.clicked.connect(HomeToAdd)
    WHomePage.Accountcomboxbutton.clicked.connect(SelectAccount)
    WHomePage.Deletebutton.clicked.connect(DeleteAccount)
    WHomePage.Signoutbutton.clicked.connect(Signout)
    WHomePage.AccountCopybutton.clicked.connect(CopyAccount)
    WHomePage.KeyCopybutton.clicked.connect(CopyKey)
    WHomePage.PhoneCopybutton.clicked.connect(CopyPhone)
    WHomePage.IDCopybutton.clicked.connect(CopyID)
    WHomePage.Searchbutton.clicked.connect(SearchAccount)
    WHomePage.RefreshAccountlistbutton.clicked.connect(RefreshAccountList)
    WHomePage.AccountCopyQRcodebutton.clicked.connect(CopyAccountByQRcode)
    WHomePage.KeyCopyQRcodebutton.clicked.connect(CopyKeyByQRcode)
    WHomePage.PhoneCopyQRcodebutton.clicked.connect(CopyPhoneByQRcode)
    WHomePage.IDCopyQRcodebutton.clicked.connect(CopyIDByQRcode)
    #- Add Page -#
    WAddPage.returnbutton.clicked.connect(AddToHome)
    WAddPage.SaveAccountButton.clicked.connect(AddPageSave)
    #-DeletePage-#
    WDeletePage.returnbutton.clicked.connect(DeleteToHome)
    WDeletePage.OKbutton.clicked.connect(CheckToDelete)
    #-CreateGroupPage-#
    WCreateGroupPage.returnbutton.clicked.connect(CreateGroupToHome)
    WCreateGroupPage.OKbutton.clicked.connect(CheckCreateGroup)
#------ Setting -----------------#
data = {}
appPath = os.getcwd()
programkey = datetime.now().strftime("%Y%m%d")
app = QApplication(sys.argv)
Wlogin = LoginPage()
WHomePage = HomePage()
WErrorPage = ErrorPage()
WRegisterPage = RegisterPage()
WAddPage = AddPage()
WDeletePage = DeletePage()
WshowQRcode = QRcodePage()
WCreateGroupPage = CreateGroupPage()

start()
sys.exit(app.exec_())