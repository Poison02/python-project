from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import ScoresDetailGUI
import login_page
import pymysql
import os
import sys

import mainGUI


class MainWindow(Tk):

    def __init__(self, login_user, login_time, psw, state):
        super().__init__()
        self.title("成绩查询界面")
        self.geometry("850x560+100+20")
        self.resizable(0, 0)
        self["bg"] = "white"
        # 从登录界面传过来的管理员登录名和登录时间
        self.current_user = login_user
        self.current_time = login_time
        self.current_psw = psw
        self.current_state = state
        # 加载页面UI
        self.setup_UI()

        # 读取学生信息
        self.all_student_list = []  # 使用一个list来存放读取的学生信息
        self.load_file_student_info()

        # 在treeview中加载学生信息
        self.load_treeview(self.all_student_list)

        # 定义一个存储查询结果的列表
        self.query_result_list = []

        self.current_student_list = []

    def setup_UI(self):
        # 设定Style
        self.Style01 = Style()
        self.Style01.configure("left.TPanedwindow", background="white")
        self.Style01.configure("right.TPanedwindow", background="white")
        self.Style01.configure("TButton", width=10, font=("华文黑体", 15, "bold"), background="white")

        # 左右两遍创建两个容器
        self.Pane_left = PanedWindow(width=200, height=541, style="left.TPanedwindow")
        self.Pane_left.place(x=645, y=10)
        self.Pane_right = PanedWindow(width=630, height=540, style="right.TPanedwindow")
        self.Pane_right.place(x=5, y=10)

        # 添加右边按钮
        # self.Button_image = PhotoImage(file="."+os.sep+"images"+os.sep+"tianjia.png")
        self.Button_add = Button(self.Pane_left, text="添加", style="TButton", command=lambda: self.add_studnet())
        self.Button_add.place(x=40, y=20)
        self.Button_update = Button(self.Pane_left, text="修改", style="TButton", command=lambda: self.update_student())
        self.Button_update.place(x=40, y=100)
        self.Button_delete = Button(self.Pane_left, text="删除", style="TButton", command=lambda: self.delete_student())
        self.Button_delete.place(x=40, y=180)
        self.Button_showall = Button(self.Pane_left, text="刷新", style="TButton",
                                     command=lambda: self.load_all_student())
        self.Button_showall.place(x=40, y=260)
        self.Button_showall = Button(self.Pane_left,text="信息查询",style="TButton",command=lambda:self.load_Main())
        self.Button_showall.place(x=40,y=340)

        # 左边：查询，TreeView
        # self.Pane_right = PanedWindow(width=725,height=540,style="right.TPanedwindow")
        # self.Pane_right.place(x=170,y=94)
        # LabelFrame
        self.LabelFrame_query = LabelFrame(self.Pane_right, text="学生成绩查询", width=602, height=70)
        self.LabelFrame_query.place(x=10, y=10)

        # 添加控件
        # 学号
        self.Label_sno = Label(self.LabelFrame_query, text="学号：", style=None)
        self.Label_sno.place(x=5, y=13)
        self.Entry_sno = Entry(self.LabelFrame_query, width=8, style=None)
        self.Entry_sno.place(x=60, y=15)

        # 姓名
        self.Label_name = Label(self.LabelFrame_query, text="姓名：", style=None)
        self.Label_name.place(x=125, y=13)
        self.Entry_name = Entry(self.LabelFrame_query, width=8, style=None)
        self.Entry_name.place(x=180, y=15)

        # 查询按钮
        self.Button_query = Button(self.LabelFrame_query, text="查询", width=4, command=lambda: self.get_query_result())
        self.Button_query.place(x=530, y=8)

        # 添加TreeView控件
        self.Tree = Treeview(self.Pane_right,
                             columns=("sno", "names", "academy", "score_c", "score_python", "score_java"),
                             show="headings", height=21)

        # 设置每一个列的宽度和对齐方式
        self.Tree.column("sno", width=100, anchor="center")
        self.Tree.column("names", width=80, anchor="center")
        self.Tree.column("academy", width=120, anchor="center")
        self.Tree.column("score_c", width=100, anchor="center")
        self.Tree.column("score_python", width=100, anchor="center")
        self.Tree.column("score_java", width=100, anchor="center")

        # 设置每个列的标题
        self.Tree.heading("sno", text="学号")
        self.Tree.heading("names", text="姓名")
        self.Tree.heading("academy", text="专业")
        self.Tree.heading("score_c", text="c语言程序设计")
        self.Tree.heading("score_python", text="python程序设计")
        self.Tree.heading("score_java", text="java程序设计")

        self.Tree.place(x=10, y=80)
        # 为tree绑定双击事件，双击后显示点击学生的详细信息
        self.Tree.bind("<Double-1>", self.view_student)

    # 读取文件/数据库中学生的信息
    def load_file_student_info(self):
        # 使用数据库读取信息
        config = {
            "host": "localhost",
            "user": "root",
            "password": "248613",
            "database": "python_test"
        }
        db = pymysql.connect(**config)
        cursor = db.cursor()
        sql = "select * from score"
        cursor.execute(sql)
        self.all_student_list = list(cursor.fetchall())
        print("使用函数查找的所有学生：", len(list(self.all_student_list)))
        cursor.close()
        db.close()

    def load_treeview(self, current_list: list):
        # 判断是否有数据：
        if len(current_list) == 0:
            messagebox.showinfo("系统消息", "没有数据加载")
        else:
            for index in range(len(current_list)):
                self.Tree.insert("", index, values=(current_list[index][0], current_list[index][1],
                                                    current_list[index][2], current_list[index][3],
                                                    current_list[index][4], current_list[index][5]))

    def get_query_result(self):
        # 准备查询条件：获取学号
        query_condition = [self.Entry_sno.get(), self.Entry_name.get(), ]
        if len(query_condition[0]) == 0 and len(query_condition[1]) == 0:
            messagebox.showinfo("系统消息", "请输入要查找的内容！")
        else:
            for item in self.all_student_list:
                if query_condition[0] in str(item[1]) and query_condition[1] in item[2]:
                    self.query_result_list.append(item)
            for i in self.Tree.get_children():
                self.Tree.delete(i)
            self.load_treeview(self.query_result_list)
            self.query_result_list.clear()

    def load_all_student(self):
        for i in self.Tree.get_children():
            self.Tree.delete(i)
        # 点击显示全部按钮后输入框清空
        self.Entry_sno.delete(0, "end")
        self.Entry_name.delete(0, "end")
        # 查找所有学生信息
        self.load_file_student_info()
        # 加载所有的学生信息到TreeView中
        self.load_treeview(self.all_student_list)

    def load_detail_window(self, flag):
        detail_window = ScoresDetailGUI.DetailWindow(flag, self.current_student_list)
        # 等待detail_window被destroy，然后继续执行以下代码
        self.wait_window(detail_window)
        # tree中刷新信息
        self.load_all_student()

    def add_studnet(self):
        flag = 2
        self.current_student_list = []
        self.load_detail_window(flag)

    def update_student(self):
        flag = 3
        try:
            item = self.Tree.selection()[0]
            print(item)
            Temp_student_list = self.Tree.item(item, "values")
            # 遍历获得完整学生明细信息
            for item in self.all_student_list:
                if item[0] == int(Temp_student_list[0]):
                    self.current_student_list = item
            self.load_detail_window(flag)
        except:
            messagebox.showinfo("系统消息", "请选择左侧需要修改的学生!")

    def view_student(self, event):
        flag = 1
        # 获取Tree表格双击某一行的数据，selection()如果没有指定参数，则表明以列表形式返回所有的item
        # 获取双击某一行的项目标识符
        item = self.Tree.selection()[0]
        print(item)
        # 这个Tree表格中的数据，只是显示了部分数据，为了显示明细窗体，我们需要加载文件中的读取出来的完整信息
        Temp_student_list = self.Tree.item(item, "values")  # 通过item方法，获取改列的所有元素，以元组的形式返回
        print(Temp_student_list)
        print("查看详情的所有学生", len(self.all_student_list))
        # 遍历获得完整学生明细信息
        for item in self.all_student_list:
            if item[0] == int(Temp_student_list[0]):
                self.current_student_list = item
                # print(self.current_student_list)
        self.load_detail_window(flag)

    def delete_student(self):
        try:
            item = self.Tree.selection()[0]
            Temp_student_list = self.Tree.item(item, "values")
            config = {
                "host": "localhost",
                "user": "root",
                "password": "248613",
                "database": "python_test"
            }
            db = pymysql.connect(**config)
            cursor = db.cursor()
            sql = "delete from score where sno=%s"
            cursor.execute(sql, Temp_student_list[1])
            num = messagebox.askokcancel("提示", "确定要删除学生：%s吗？" % Temp_student_list[1])
            if num:
                db.commit()
                messagebox.showinfo("系统消息", "学生%s已经被删除！" % Temp_student_list[1])
            else:
                messagebox.showinfo("系统消息", "您取消了删除学生%s" % Temp_student_list[1])
            cursor.close()
            db.close()
            self.load_all_student()
        except:
            messagebox.showinfo("系统消息", "请选择右侧需要删除的学生!")


    def load_Main(self):
        self.destroy()
        main_Window = mainGUI.MainWindow(self.current_user, self.current_time, self.current_psw, self.current_state)
        main_Window.mainloop()