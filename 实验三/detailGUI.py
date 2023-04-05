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
        self.geometry("680x400+200+20")
        self.resizable(0, 0)  # 不能改变窗体大小
        self.flag = flag  # 接收从主窗口传过来的flag来控制自己窗口的控件状态
        self.current_student_list = current_student  # 接收从主窗口床过来的学生信息
        self.temp_list = []
        # 加载控件
        self.setup_UI()

    # 加载学生详细信息
    def load_student_detail(self):
        if len(self.current_student_list) == 0 and self.flag == 1:
            messagebox.showinfo("系统消息","没有任何数据需要展示!")
        else:
            self.var_sno.set(self.current_student_list[0][1])  # 学号
            self.var_name.set(self.current_student_list[0][2])  # 姓名
            if "男" in self.current_student_list[0][2]:  # 性别
                self.var_gender.set(1)
            else:
                self.var_gender.set(0)
            self.var_age.set(self.current_student_list[0][5])  # 出生日期
            self.var_mobile.set(self.current_student_list[0][6])  # 电话
            self.var_email.set(self.current_student_list[0][7])  # 邮箱
            self.var_home.set(self.current_student_list[0][8])  # 地址
            self.var_academy.set(self.current_student_list[0][3])  # 专业

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
        # 性别
        self.Label_gender = Label(self.Pane_detail, text="性别:").place(x=480, y=10)
        self.var_gender = IntVar()
        self.Radio_man = Radiobutton(self.Pane_detail, text="男", variable=self.var_gender, value=1,
                                     style="TRadiobutton")
        self.Radio_man.place(x=540, y=10)
        self.Radio_woman = Radiobutton(self.Pane_detail, text="女", variable=self.var_gender, value=0,
                                       style="TRadiobutton")
        self.Radio_woman.place(x=600, y=10)
        # 第二排:出生日期
        self.Label_age = Label(self.Pane_detail, text="出生日期:", style="TLabel")
        self.Label_age.place(x=10, y=60)
        self.var_age = StringVar()
        self.Entry_age = Entry(self.Pane_detail, textvariable=self.var_age, style="TEntry")
        self.Entry_age.place(x=110, y=65)
        # 第三排:手机号码
        self.Label_mobile = Label(self.Pane_detail, text="电话号码:", style="TLabel")
        self.Label_mobile.place(x=10, y=110)
        self.var_mobile = StringVar()
        self.Entry_mobile = Entry(self.Pane_detail, textvariable=self.var_mobile, style="TEntry")
        self.Entry_mobile.place(x=110, y=115)
        # 邮箱地址
        self.Label_email = Label(self.Pane_detail, text="邮箱地址:", style="TLabel")
        self.Label_email.place(x=280, y=110)
        self.var_email = StringVar()
        self.Entry_email = Entry(self.Pane_detail, textvariable=self.var_email, width=35)
        self.Entry_email.place(x=400, y=115)

        # 第四排:家庭住址
        self.Label_home = Label(self.Pane_detail, text="家庭住址:", style="TLabel")
        self.Label_home.place(x=10, y=160)
        self.var_home = StringVar()
        self.Entry_home = Entry(self.Pane_detail, textvariable=self.var_home, width=60)
        self.Entry_home.place(x=110, y=165)
        # 专业
        self.Label_academy = Label(self.Pane_detail, text="专业:", style="TLabel")
        self.Label_academy.place(x=320, y=210)
        self.var_academy = StringVar()
        self.Entry_academy = Entry(self.Pane_detail, textvariable=self.var_academy, width=25)
        self.Entry_academy.place(x=400, y=215)

        # 放置两个按钮
        self.Button_save = Button(self, text="保存", style="TButton", command=lambda: self.commit())
        self.Button_save.place(x=350, y=350)

        # 初始化界面数据及控件状态
        self.load_student_detail()
        self.load_windows_flag()

    #
    def load_windows_flag(self):
        if self.flag == 1:
            self.Button_save.place_forget()
            self.Entry_sno["state"] = DISABLED
            self.Entry_name["state"] = DISABLED
            self.Radio_man["state"] = DISABLED
            self.Radio_woman["state"] = DISABLED
            self.Entry_age["state"] = DISABLED
            self.Entry_mobile["state"] = DISABLED
            self.Entry_email["state"] = DISABLED
            self.Entry_home["state"] = DISABLED
            self.Entry_academy["state"] = DISABLED
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
                        if len(self.Entry_sno.get()) == 0 or len(self.Entry_name.get()) == 0 \
                                or len(self.Entry_mobile.get()) == 0 or len(self.Entry_academy.get()) == 0 :
                            messagebox.showinfo("系统消息", "学号、姓名、电话号码、专业都不能为空！")
                        else:
                            self.get_input()
                            sql = "insert into student(sno, name, academy, gender, birthday, mobile, email, address) values (%s,%s,%s,%s,%s,%s,%s,%s)"
                            self.connect_database(sql, (self.temp_list[0],
                                                        self.temp_list[1],
                                                        self.temp_list[7],
                                                        self.temp_list[2],
                                                        self.temp_list[3],
                                                        self.temp_list[4],
                                                        self.temp_list[5],
                                                        self.temp_list[6]))
                            messagebox.showinfo("系统消息", "学生信息添加成功")
                            break_flag = messagebox.askyesno("提示", "继续添加学生？")
                            if break_flag:
                                self.Entry_sno.delete(0, "end")
                                self.Entry_name.delete(0, "end")
                                # self.var_gender.delete(0,"end")
                                self.Entry_age.delete(0, "end")
                                self.Entry_mobile.delete(0, "end")
                                self.Entry_email.delete(0, "end")
                                self.Entry_home.delete(0, "end")
                                self.Entry_academy.delete(0, "end")
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
                if len(self.Entry_sno.get()) == 0 or len(self.Entry_name.get()) == 0 \
                        or len(self.Entry_mobile.get()) == 0 \
                        or len(self.Entry_academy.get()) == 0:
                    messagebox.showinfo("系统消息",
                                        "学号、姓名、电话号码、专业都不能为空！")
                else:
                    self.get_input()
                    sql = "update student set " \
                          "name=%s,gender=%s,birthday=%s,mobile=%s,email=%s,address=%s,academy=%s " \
                          "where sno=%s"
                    self.connect_database(sql, (self.temp_list[1],
                                                self.temp_list[2],
                                                self.temp_list[3],
                                                self.temp_list[4],
                                                self.temp_list[5],
                                                self.temp_list[6],
                                                self.temp_list[7],
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
        if self.var_gender.get() == 1:
            self.temp_list.append("男")
        else:
            self.temp_list.append("女")
        self.temp_list.append(self.Entry_age.get().strip())
        self.temp_list.append(self.Entry_mobile.get().strip())
        self.temp_list.append(self.Entry_email.get().strip())
        self.temp_list.append(self.Entry_home.get().strip())
        self.temp_list.append(self.Entry_academy.get().strip())
        print("测试", self.temp_list)
