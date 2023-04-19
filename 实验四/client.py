import socket
import threading
import tkinter as tk
from tkinter import filedialog

SERVER_HOST = '127.0.0.1'  # 服务器IP地址
SERVER_PORT = 8000  # 服务器端口号
BUFFER_SIZE = 1024  # 缓冲区大小


class ClientGUI:
    def __init__(self, master):
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # 创建输入框和发送按钮
        self.input_entry = tk.Entry(self.master)
        self.input_entry.pack(side=tk.LEFT, padx=5)
        self.send_button = tk.Button(self.master, text='发送', command=self.send_message)
        self.send_button.pack(side=tk.LEFT)

        # 创建显示框
        self.display_text = tk.Text(self.master)
        self.display_text.pack(side=tk.TOP, padx=5, pady=5)

        # 创建上传按钮
        self.upload_button = tk.Button(self.master, text='上传文件', command=self.upload_file_path)
        self.upload_button.pack(side=tk.LEFT, padx=5)

    def send_message(self):
        # 获取用户输入的字符串
        message = self.input_entry.get()
        if message:
            # 连接服务器
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((SERVER_HOST, SERVER_PORT))
            # 发送数据
            client_socket.send(message.encode())
            # 接收服务器返回的数据
            response = client_socket.recv(BUFFER_SIZE)
            print("response: ", response)
            self.display_text.insert(tk.END, f'Server: {response.decode()}\n')
            # 关闭套接字
            client_socket.close()

    def upload_file_path(self):
        # 弹出文件对话框选择Excel文件
        file_path = filedialog.askopenfilename()
        msg = "upload_file " + file_path
        if msg:
            # 连接服务器
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((SERVER_HOST, SERVER_PORT))
            # 发送文件路径
            client_socket.send(msg.encode())
            # 接收服务器返回的记录条数
            response = client_socket.recv(BUFFER_SIZE)
            print("response:: ", response)
            self.display_text.insert(tk.END, f'Server: {response.decode()}\n')
            # 关闭套接字
            client_socket.close()


# 创建GUI界面
root = tk.Tk()
root.title('客户端')
client_gui = ClientGUI(root)
root.mainloop()
