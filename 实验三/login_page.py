from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import datetime

import mainGUI
import pymysql
import os


class LoginWindow(Tk):
    """创建登录窗体的GUI界面以及登录的方法"""

    # 构造函数，在对象被创建后就自动运行
    def __init__(self):
        super().__init__()  # 先执行tk这个类的初始化
        self.title("学生信息管理系统")
        self.geometry("300x300")
        self.resizable(0, 0)  # 窗体大小不允许变，两个参数分别代表x轴和y轴

        # 这三个参数都是为了传入下一个界面
        self.user = ""
        self.pwd = ""
        self.state = 1

        # 加载窗体
        self.setup_UI()
        self.user_list = []  # 存储用户信息

    def setup_UI(self):
        # ttk中控件使用style对象设定
        self.Style01 = Style()
        self.Style01.configure("user.TLabel", font=("华文黑体", 20, "bold"), foreground="black")
        self.Style01.configure("TEntry", font=("华文黑体", 20, "bold"))
        self.Style01.configure("TButton", font=("华文黑体", 20, "bold"), foreground="black", bg='red')
        self.Label_user = Label(self, text="用户名:", style="user.TLabel")
        self.Label_user.pack(padx=10, pady=10)
        self.Entry_user = Entry(self, width=12)
        self.Entry_user.pack(padx=10, pady=10)
        # 创建一个Label标签 + Entry   --- 密码
        self.Label_password = Label(self, text="密码:", style="user.TLabel")
        self.Label_password.pack(padx=10, pady=10)
        self.Entry_password = Entry(self, width=12, show="*")
        self.Entry_password.pack(padx=10, pady=10)
        # 创建一个按钮    --- 登录
        self.Button_login = Button(self, text="登录", width=4, command=lambda: self.login())
        self.Button_login.pack(padx=20, pady=10)

    def load_main(self):
        # 关闭当前窗体
        #
        self.destroy()
        # 加载新窗体
        if __name__ == '__main__':
            main_Window = mainGUI.MainWindow(self.user, self.get_now_time(), self.pwd, self.state)
            main_Window.mainloop()

    def login(self):
        # 获取用户的用户名和密码
        user = self.Entry_user.get()
        password = self.Entry_password.get()
        db = pymysql.connect(
            host="localhost",
            user="root",
            password="248613",
            database="python_test"
        )
        cursor = db.cursor()
        sql = "select * from user where user_name=%s"
        cursor.execute(sql, user)
        # 将得到的管理员数据存放在列表中
        self.user_list = cursor.fetchall()
        print(self.user_list)
        cursor.close()
        db.close()
        if len(self.user_list) != 0:
            if 0 == self.user_list[0][2]:
                messagebox.showinfo("系统消息", "账号已禁用，请联系管理员")
            else:
                if password != str(self.user_list[0][1].strip().lower()):
                    messagebox.showinfo("系统消息", "输入密码错误")
                else:
                    messagebox.showinfo("系统消息", "登录成功！")
                    self.user = self.user_list[0][0]
                    self.pwd = self.user_list[0][1]
                    self.state = self.user_list[0][2]
                    self.load_main()
        else:
            messagebox.showinfo("系统消息", '输入用户名不存在')

    def get_now_time(self):
        today = datetime.datetime.today()
        return ("%04d-%02d-%02d %02d:%02d:%02d" % (
            today.year, today.month, today.day, today.hour, today.minute, today.second))


if __name__ == '__main__':
    this_login = LoginWindow()
    print(this_login.get_now_time())
    this_login.mainloop()
