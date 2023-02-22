# coding : utf-8
import os
import win32crypt
import sys
import binascii
#导入QT组件
from PyQt5.QtWidgets import QMainWindow,QApplication,QHeaderView,QAbstractItemView,QTableWidgetItem,QMenu,QMessageBox
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
#导入主界面UI
from rdpui import Ui_Dialog

#任务栏图标，实际上效果很魔幻
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

class ConnDesk:
    def __init__(self,username,password,host) -> None:

        # 临时rdp文件
        self.rdpTemp = "rdp.rdp"

        self.username = username
        self.password = password
        self.host = host
        
    def AddPwd(self):
        try:
            pwdHash = win32crypt.CryptProtectData(self.password.encode('utf-16-le'), u'psw', None, None, None, 0)
            self.password = binascii.hexlify(pwdHash).decode("utf-8")
            # rdp模板文件
            self.model = f'''
screen mode id:i:1 
desktopwidth:i:1920 
desktopheight:i:1080 
session bpp:i:24 
winposstr:s:2,3,188,8,1062,721 
full address:s:{self.host}
compression:i:1 
keyboardhook:i:2 
audiomode:i:0 
redirectdrives:i:0 
redirectprinters:i:0 
redirectcomports:i:0 
redirectsmartcards:i:0 
displayconnectionbar:i:1 
autoreconnection enabled:i:1 
username:s:{self.username}
domain:s:MyDomain 
alternate shell:s: 
shell working directory:s: 
password 51:b:{self.password}
disable wallpaper:i:1 
disable full window drag:i:1 
disable menu anims:i:1 
disable themes:i:0 
disable cursor setting:i:0 
bitmapcachepersistenable:i:1
'''
            rdpTemp = open(self.rdpTemp,"w",encoding="utf-8")
            rdpTemp.write(self.model)
            rdpTemp.close()
            print("写入文件成功")
            return self.password
        except:
            return False
    
    def conn(self):
        cmd = f"mstsc {self.rdpTemp}"
        os.system(cmd)
        

#继承视窗和UI
class MainCode(QMainWindow,Ui_Dialog):

    def __init__(self):
        #初始化
        QMainWindow.__init__(self)
        Ui_Dialog.__init__(self)

        #将UI生成传到self
        self.setupUi(self)
        self.filedb = './ymhost.json'
        # 数据文件
        if os.path.exists(self.filedb):
            print("加载数据")
            self.relodb()

        #禁止修改表格
        # self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        #不显示行名称
        self.tableWidget.verticalHeader().setVisible(False)
        #让表格铺满
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #让选中项变成一行
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 列头双击自动排序
        # self.tableWidget.setSortingEnabled(True)
        
        #绑定表格右键事件
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested[QtCore.QPoint].connect(self.del_table_line)

        #表格数据更新时的事件
        # self.tableWidget.doubleClicked.connect(self.on_click)# 被双击修改时
        self.tableWidget.itemChanged.connect(self.on_update)# 内容已更新时

        #绑定添加按钮的事件
        self.pushButton.clicked.connect(self.add_desk)

    def on_update(self):
        print("有更新")
        if os.path.exists("./ymhost.json"):
            try:
                hostjson = eval(open(self.filedb,"r",encoding="utf-8").read())
            except:
                hostjson = {"0":{}}
            filedata = open(self.filedb,"w",encoding="utf-8")
        else:
            hostjson = {}
            filedata = open(self.filedb,"w",encoding="utf-8")
        # print(hostjson)
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            addline = str(currentQTableWidgetItem.row())
            # print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
            # print(hostjson[currentQTableWidgetItem.row()]["name"])
            # 更新的行
            if currentQTableWidgetItem.column() == 0:
                # print(hostjson[currentQTableWidgetItem.row()]["name"],currentQTableWidgetItem.text())
                hostjson[addline]["name"] = currentQTableWidgetItem.text()
            if currentQTableWidgetItem.column() == 1:
                hostjson[addline]["host"] = currentQTableWidgetItem.text()
            if currentQTableWidgetItem.column() == 2:
                hostjson[addline]["username"] = currentQTableWidgetItem.text()
            if currentQTableWidgetItem.column() == 3:
                hostjson[addline]["password"] = currentQTableWidgetItem.text()
        filedata.write(str(hostjson))
        filedata.close()
        self.tableWidget.update()

    # 重载数据
    def relodb(self,**args):
        if os.path.exists("./ymhost.json"):
            data = open(self.filedb,"r",encoding="utf-8")
            try:
                data = eval(data.read())
                for i in data:
                    i = data[i]
                    # 跳过空数据
                    if len(i) == 0:
                        continue
                    name,host,username,password = i["name"],i["host"],i["username"],i["password"]
                    info = [name,host,username,password]
                    row = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row)
                    for listed in range(len(info)):
                        item = QTableWidgetItem(str(info[listed]))
                        item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                        self.tableWidget.setItem(row,listed,item)
                    self.tableWidget.update()
            except:
                print("加载数据出错了")


    # 修改关闭程序的事件
    def closeEvent(self, event):
        print("保存并退出程序")
        event.accept()

        # 提示框例子
        # result = QtWidgets.QMessageBox.question(self, "将关闭程序", "是否保存修改的数据并关闭程序?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        # if(result == QtWidgets.QMessageBox.Yes):
        #     print("保存退出")
        #     event.accept()
        # else:
        #     print("取消关闭")
        #     event.ignore()

    # 单元格被双击时
    def on_click(self):
        # for currentQTableWidgetItem in self.tableWidget.selectedItems():
        #     print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
        pass

     #右键表格功能
    def del_table_line(self, pos):
        pop_menu = QMenu()
        conn_desk = pop_menu.addAction('连接桌面')
        # edit_desk = pop_menu.addAction('编辑桌面')
        del_desk = pop_menu.addAction('删除桌面')
        # export_desk = pop_menu.addAction('导出桌面')
        
        # 获取右键菜单中当前被点击的是哪一项
        action = pop_menu.exec_(self.tableWidget.mapToGlobal(pos))

        # 选中连接桌面
        if action == conn_desk:
            print("连接桌面")
            # 获取当前选中的行
            row = self.tableWidget.currentRow()
            # 获取当前选中行的主机地址
            host = self.tableWidget.item(row , 1).text()
            username = self.tableWidget.item(row , 2).text()
            password = self.tableWidget.item(row , 3).text()
            new = ConnDesk(username,password,host)
            print("密码：",new.AddPwd())
            # 开启连接
            new.conn()

        # # 选中编辑桌面
        # if action == edit_desk:
        #     print("编辑桌面")

        # 选中删除桌面
        if action == del_desk:
            selected_items = self.tableWidget.selectedItems()
            if len(selected_items) == 0:  # 说明没有选中任何行
                return
            selected_items = [selected_items[i] for i in range(len(selected_items)-1, -1, -7)]
            # 将选定行的行号降序排序，从索引大的行开始删除
            for items in selected_items:
                self.tableWidget.removeRow(self.tableWidget.indexFromItem(items).row())

            # 从数据文件中删除，若列表无数据，则会在上一步结束执行
            hostjson = eval(open(self.filedb,"r",encoding="utf-8").read())
            filedata = open(self.filedb,"w",encoding="utf-8")
            # 要删除的数据对应索引
            rowline = str(self.tableWidget.rowCount())
            hostjson.pop(rowline)
            filedata.write(str(hostjson))
            filedata.close()
            self.tableWidget.update()

        # 选中导出桌面
        # if action == export_desk:
        #     print("导出桌面")
    
    # 添加一条记录
    def add_desk(self):
            if self.radioButton.isChecked():
                self.scrn = "full"
                # print('选中了全屏')
            if self.radioButton_2.isChecked():
                self.scrn = "area"
                # print('选中了窗口化')
            name = self.lineEdit.text()
            host = self.lineEdit_2.text()
            username = self.lineEdit_3.text()
            password = self.lineEdit_4.text()
            if len(name) == 0 or len(host) == 0 or len(username) == 0 or len(password) == 0:
                QMessageBox.information(self, "新增失败", "有不完整的内容",QMessageBox.Yes)
                return
            info = [name,host,username,password]
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            if os.path.exists("./ymhost.json"):
                # print("文件存在")
                try:
                    hostjson = eval(open(self.filedb,"r",encoding="utf-8").read())
                    if len(hostjson) == 0:
                        # print("长度为0")
                        hostjson = {"0":{}}
                except:
                    hostjson = {"0":{}}
                filedata = open(self.filedb,"w",encoding="utf-8")
            else:
                # print("文件不存在")
                hostjson = {"0":{}}
                filedata = open(self.filedb,"w",encoding="utf-8")
            addlen = str(self.tableWidget.rowCount() -1)
            hostjson[addlen] = {}
            for listed in range(len(info)):
                # print("新增内容：",info[listed])
                item = QTableWidgetItem(str(info[listed]))
                item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                self.tableWidget.setItem(row,listed,item)
                if listed == 0:
                    hostjson[addlen]["name"] = info[listed]
                if listed == 1:
                    hostjson[addlen]["host"] = info[listed]
                if listed == 2:
                    hostjson[addlen]["username"] = info[listed]
                if listed == 3:
                    hostjson[addlen]["password"] = info[listed]
            # print(hostjson)
            filedata.write(str(hostjson))
            filedata.close()
            self.tableWidget.update()


if __name__ == "__main__":  
    app = QApplication(sys.argv) 
    window = MainCode()
    window.setWindowIcon(QIcon(":/app.ico"))
    window.show()
    sys.exit(app.exec_())
