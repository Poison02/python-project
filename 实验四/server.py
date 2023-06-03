import socket
import threading
import pandas as pd
import pymysql

SERVER_HOST = '0.0.0.0'  # 监听所有网卡的连接
SERVER_PORT = 8000  # 监听的端口号
BUFFER_SIZE = 1024  # 缓冲区大小

# 数据库连接信息
DB_HOST = '127.0.0.1'
DB_PORT = 3306
DB_USER = 'root'
DB_PASSWORD = '248613'
DB_NAME = 'python_test'


class ClientThread(threading.Thread):
    def __init__(self, client_socket, client_address):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self.client_address = client_address

    def run(self):
        try:
            # 接收客户端请求
            request = self.client_socket.recv(BUFFER_SIZE).decode()
            print("request:", request)
            if request.startswith('upload_file'):
                # 接收文件路径
                # file_path = self.client_socket.recv(BUFFER_SIZE).decode()
                file_path = request.split(' ')[1]
                print("file_path:", file_path)
                db = pymysql.connect(
                    host=DB_HOST, 
                    port=DB_PORT, 
                    user=DB_USER, 
                    password=DB_PASSWORD, 
                    database=DB_NAME
                )
                cursor = db.cursor()
                sql = "insert into test(id, name, age) values(%s, %s, %s)"
                self.excel_to_sql(file_path, db, cursor, sql)
                db.commit()
                # 查询记录条数并发送给客户端
                cursor.execute('SELECT COUNT(*) FROM test')
                count = cursor.fetchone()[0]
                self.client_socket.send(str(count).encode())
                # 关闭数据库连接
                cursor.close()
                db.close()
            else:
                # 转换小写字母为大写字母
                response = request.upper()
                # 发送响应给客户端
                self.client_socket.send(response.encode())
        except Exception as e:
            print(f'Error: {e}')
        finally:
            # 关闭套接字
            self.client_socket.close()
    
    def excel_to_sql(self, file_path, conn, cur, sql):
        # 读取excel文件插入MySQL中
        df = pd.read_excel(file_path)
        lst = []
        for i in range(0, len(df)):
            record = tuple(df.loc[i])
            lst.append(record)
            # 把空值，或者缺失填充
            sql = sql.replace(
                'nan', 'null').replace('None', 'null').replace('none', 'null')

        # 执行插入语句
        cur.executemany(sql, lst)
        # 提交
        conn.commit()
        print("Insert By Excel Data Ok!")


def main():
    # 创建服务器套接字
    # AF_INET表示socket网络层使用IP协议，SOCK_STREAM表示socket传输层使用tcp协议
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定端口
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    # 进行监听
    server_socket.listen(5)
    print(f'Server listening on {SERVER_HOST}:{SERVER_PORT}')
    while True:
        # 接受客户端连接
        client_socket, client_address = server_socket.accept()
        print(client_socket, client_address)
        print(f'Client {client_address[0]}:{client_address[1]} connected')
        # 创建线程处理客户端请求
        client_thread = ClientThread(client_socket, client_address)
        client_thread.start()


if __name__ == '__main__':
    main()
