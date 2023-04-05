# 学生窗体GUI基本布局

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import pymysql
import os


class DetailWindow(Toplevel):
    def __init__(self, flag, current_student):
        super().__init__()
        self.title("学生明细信息")
        self.geometry("680x200+200+20")
        self.resizable(0, 0)  # 不能改变窗体大小
        self.flag = flag  # 接收从主窗口传过来的flag来控制自己窗口的控件状态
        self.current_student_list = current_student  # 接收从主窗口床过来的学生信息
        self.temp_list = []
        # 加载控件
        self.setup_UI()

    def load_student_detail(self):
        if len(self.current_student_list) == 0:
            # messagebox.showinfo("系统消息","没有任何数据需要展示!")
            pass
        else:
            self.var_sno.set(self.current_student_list[1])  # 学号
            self.var_name.set(self.current_student_list[2])  # 姓名
            self.var_age.set(self.current_student_list[3])  # 专业
            self.var_id.set(self.current_student_list[4])  # c语言成绩
            self.var_mobile.set(self.current_student_list[5])  # python成绩
            self.var_email.set(self.current_student_list[6])  # java成绩

    def setup_UI(self):
        # detail_UI(self)
        # 设置style
        self.Style02 = Style()
        self.Style02.configure("TPanedwindow")
        self.Style02.configure("title.TLabel", font=("微软雅黑", 10, "bold"))
        self.Style02.configure("TLabel", font=("微软雅黑", 14, "bold"))
        self.Style02.configure("TButton", font=("微软雅黑", 16, "bold"), foreground="navy", width=10)
        self.Style02.configure("TEntry", font=("微软雅黑", 16, "bold"), width=10)
        self.Style02.configure("large.TEntry", font=("微软雅黑", 16, "bold"), width=30)
        self.Style02.configure("TRadiobutton", font=("微软雅黑", 14, "bold"))
        #
        # 加载上面的banner
        self.Login_image = PhotoImage(file="." + os.sep + "images" + os.sep + "shouye.png")
        self.Lable_image = Label(self, image=self.Login_image)
        self.Lable_image.pack()

        # 添加一个title
        self.var_title = StringVar()
        self.Label_title = Label(self, text="==明细窗体==", style="title.TLabel")
        self.Label_title.place(x=500, y=40)

        # 加载一个pane
        self.Pane_detail = PanedWindow(self, width=690, height=450, style="TPanedwindow")
        self.Pane_detail.place(x=5, y=0)

        # 添加属性
        # 第一排:学号
        self.Label_sno = Label(self.Pane_detail, text="学号:")
        self.Label_sno.place(x=10, y=10)
        self.var_sno = StringVar()
        self.Entry_sno = Entry(self.Pane_detail, textvariable=self.var_sno, style="TEntry")
        self.Entry_sno.place(x=62, y=15)
        # 姓名
        self.Label_name = Label(self.Pane_detail, text="姓名:", style="TLabel")
        self.Label_name.place(x=240, y=10)
        self.var_name = StringVar()
        self.Entry_name = Entry(self.Pane_detail, textvariable=self.var_name, style="TEntry")
        self.Entry_name.place(x=300, y=15)

        # 第二排:出生日期
        self.Label_age = Label(self.Pane_detail, text="专业:", style="TLabel")
        self.Label_age.place(x=10, y=60)
        self.var_age = StringVar()
        self.Entry_age = Entry(self.Pane_detail, textvariable=self.var_age, style="TEntry")
        self.Entry_age.place(x=110, y=65)
        # 身份证号码
        self.Label_id = Label(self.Pane_detail, text="c语言成绩:", style="TLabel")
        self.Label_id.place(x=280, y=60)
        self.var_id = StringVar()
        self.Entry_id = Entry(self.Pane_detail, textvariable=self.var_id, width=35)
        self.Entry_id.place(x=400, y=65)
        # 第三排:手机号码
        self.Label_mobile = Label(self.Pane_detail, text="python成绩:", style="TLabel")
        self.Label_mobile.place(x=10, y=110)
        self.var_mobile = StringVar()
        self.Entry_mobile = Entry(self.Pane_detail, textvariable=self.var_mobile, style="TEntry")
        self.Entry_mobile.place(x=110, y=115)
        # 邮箱地址
        self.Label_email = Label(self.Pane_detail, text="java成绩:", style="TLabel")
        self.Label_email.place(x=280, y=110)
        self.var_email = StringVar()
        self.Entry_email = Entry(self.Pane_detail, textvariable=self.var_email, width=35)
        self.Entry_email.place(x=400, y=115)

        # 放置两个按钮
        self.Button_save = Button(self, text="保存", style="TButton", command=lambda: self.commit())
        self.Button_save.place(x=350, y=160)

        # 初始化界面数据及控件状态
        self.load_student_detail()
        self.load_windows_flag()

    def load_windows_flag(self):
        if self.flag == 1:
            self.Button_save.place_forget()
            self.Entry_sno["state"] = DISABLED
            self.Entry_name["state"] = DISABLED
            self.Entry_age["state"] = DISABLED
            self.Entry_id["state"] = DISABLED
            self.Entry_mobile["state"] = DISABLED
            self.Entry_email["state"] = DISABLED
        elif self.flag == 2:
            self.Label_title.configure(text="==新建学生明细==")
        elif self.flag == 3:
            self.Label_title.configure(text="==修改学生明细==")
            self.Entry_sno["state"] = DISABLED

    def commit(self):
        if self.flag == 1:
            pass
        else:
            # 添加学生信息
            if self.flag == 2:
                break_flag = 1
                try:
                    while break_flag:
                        self.get_input()
                        if len(self.Entry_sno.get()) == 0 or len(self.Entry_name.get()) == 0:
                            messagebox.showinfo("系统消息",
                                                "学号、姓名不能为空！")
                        else:
                            self.get_input()
                            print("測試", self.temp_list)
                            sql = "insert into score(sno, name, academy, score_c, score_python, score_java) values(%s,%s,%s,%s,%s,%s)"
                            self.connect_database(sql, (self.temp_list[0],
                                                        self.temp_list[1],
                                                        self.temp_list[2],
                                                        self.temp_list[3],
                                                        self.temp_list[4],
                                                        self.temp_list[5]))
                            messagebox.showinfo("系统消息", "学生信息添加成功")
                            break_flag = messagebox.askyesno("提示", "继续添加学生？")
                            if break_flag:
                                self.Entry_sno.delete(0, "end")
                                self.Entry_name.delete(0, "end")
                                self.Entry_id.delete(0, "end")
                                self.Entry_mobile.delete(0, "end")
                                self.Entry_email.delete(0, "end")

                    # 保存后销毁此窗口
                    self.destroy()
                except pymysql.err.OperationalError as e:
                    messagebox.showerror("错误", e)
                except pymysql.err.DataError as e:
                    messagebox.showerror("错误", e)

                # 修改学生信息
            elif self.flag == 3:
                self.get_input()
                print(self.temp_list)
                if len(self.Entry_sno.get()) == 0 or len(self.Entry_name.get()) == 0:
                    messagebox.showinfo("系统消息",
                                        "学号、姓名不能为空！")
                else:
                    self.get_input()
                    sql = "update score set name=%s,academy=%s,score_c=%s,score_python=%s,score_java=%s  where " \
                          "sno = %s "
                    self.connect_database(sql, (self.temp_list[1],
                                                self.temp_list[2],
                                                self.temp_list[3],
                                                self.temp_list[4],
                                                self.temp_list[5],
                                                self.temp_list[0]))
                    messagebox.showinfo("系统消息", "学生信息修改成功！")
                    # 保存后销毁此窗口
                    self.destroy()

    def connect_database(self, sql, *value):
        config = {
            "host": "localhost",
            "user": "root",
            "password": "248613",
            "database": "python_test"
        }
        db = pymysql.connect(**config)
        cursor = db.cursor()
        cursor.execute(sql, *value)

        db.commit()
        # self.find_all=cursor.fetchall()
        cursor.close()
        db.close()

    def get_input(self):
        # 获取输入框信息保存到list中
        self.temp_list = []

        self.temp_list.append(int(self.Entry_sno.get()))
        self.temp_list.append(self.Entry_name.get().strip())
        self.temp_list.append(self.Entry_age.get().strip())
        self.temp_list.append(self.Entry_id.get().strip())
        self.temp_list.append(self.Entry_mobile.get().strip())
        self.temp_list.append(self.Entry_email.get().strip())
