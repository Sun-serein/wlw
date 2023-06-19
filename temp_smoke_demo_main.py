from PyQt5.Qt import *
from Ui_untitled import Ui_Form
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtChart import QChart, QLineSeries,QValueAxis
import math
import smoke
import jinggai
import pymysql

def savetomysql(data):
        db = pymysql.connect(host='localhost', user='root', password='wmx580231', db='py')
        cursor = db.cursor()
        sql = "INSERT INTO wlw VALUES ('%s')"%(data)
        try:
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            print("成功提交数据库")
        except:
        # 如果发生错误则回滚
            print("数据提交错误")
            db.rollback()
    # 关闭数据库连接
        db.close()

def savetomysql1(temp,x,y,z,state):
        db = pymysql.connect(host='localhost', user='root', password='wmx580231', db='py')
        cursor = db.cursor()
        sql = "INSERT INTO jg VALUES ('%s','%s','%s','%s','%s')"%(temp,x,y,z,state)
        try:
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            print("成功提交数据库")
        except:
        # 如果发生错误则回滚
            print("数据提交错误")
            db.rollback()
    # 关闭数据库连接
        db.close()       



class Window(QWidget, Ui_Form):

    def __init__(self):         #用于初始化类,定义了 __init__() 方法后，类的实例化操作会自动调用该方法。
        super().__init__()
        self.setup_ui()
        self.pushButton.clicked.connect(self.currentSmokeValue)
        self.pushButton_2.clicked.connect(self.currentjinggaiValue)
    def setup_ui(self):
        self.setupUi(self)
        self.setdate()
        self.currentSmokeValue()
        self.currentjinggaiValue()

    def select_mysql_data():
        db = pymysql.connect(host='localhost', user='root', password='wmx580231', db='py')
        cursor = db.cursor()
        sql = "SELECT * FROM wlw"
        try:
            cursor.execute(sql)
            # 提交到数据库执行
            result = cursor.fetchall()

            # 将查询结果存储到数组中
            data = []
            for row in result:
                data.append(row)

            # 关闭数据库连接
            db.close()

            # 返回查询结果
            return data
            
        
        except Exception as e:
            # 如果发生错误则回滚
            print("数据库查询错误:", e)
            db.rollback()
    data=select_mysql_data()
    print(data)

    def setdate(self):
        chart = QChart()
        chart.setTitle("烟雾浓度数据变化曲线")
        self.graphicsView.setChart(chart)
        seri = QLineSeries()
        seri.setName("烟雾浓度")
        chart.addSeries(seri)
        data  = select_mysql_data()
        t=len(data)
        for i in range(len(data)):
            y = []
            y.add(data(i))
            seri.append(t,y[i])
            t += 1
        ax = QValueAxis()
        ax.setRange(0,10)
        ax.setTitleText("x")
        ay = QValueAxis()
        ay.setRange(0,200)
        ay.setTitleText("y")
        chart.setAxisX(ax,seri)
        chart.setAxisY(ay,seri)

    def currentSmokeValue (self):
        value = smoke.getvalue()
        self.lcdNumber.display(value[0])
        self.label_3.setText(value[1])
        if value[0]>70:
            QMessageBox.warning(self, "报警", "烟雾浓度异常,请报警!!!", QMessageBox.Ok)
            self.label_12.setText("烟雾浓度异常,请报警")
        else:
            self.label_12.setText("")
        a = value[0]
        savetomysql(a)
        
    def currentjinggaiValue (self):
        value = jinggai.getvalue()
        self.lcdNumber_2.display(value[0])
        self.lcdNumber_3.display(value[1])
        self.lcdNumber_4.display(value[2])
        self.lcdNumber_5.display(value[3])
        self.label_9.setText(str(value[4]))
        if value[0]>60 and value[3]>1000:
            QMessageBox.warning(self, "报警", "井盖温度异常,位置异常,请立即报警!!!", QMessageBox.Ok)
            self.label_13.setText("井盖温度异常,位置异常,请立即报警!!!")
        elif value[0]>60:
            QMessageBox.warning(self, "报警", "井盖温度异常,请立即报警!!", QMessageBox.Ok)
            self.label_13.setText("井盖温度异常,请立即报警!!")
        elif value[3]>1000:
            QMessageBox.warning(self, "报警", "井盖位置异常,请立即报警!!", QMessageBox.Ok)
            self.label_13.setText("井盖位置异常,请立即报警!!")
        elif value[0]<60 or value[3]<1000:
            self.label_13.setText("")
        a=value[0]
        b=value[1]
        c=value[2]
        d=value[3]
        e=value[4]
        savetomysql1(a,b,c,d,e)

    
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv) #管理图形用户界面应用程序的控制流和主要设置
    mywindow1 = Window()
    mywindow1.show()
    sys.exit(app.exec_())#app.exec_()的作用是运行主循环，必须调用此函数才能开始事件处理，调用该方法进入程序的主循环直到调用exit（）结束。
   
