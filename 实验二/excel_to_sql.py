import pymysql
import pandas as pd


"""
 函数sql_connect 用于数据库的连接
"""
def sql_connect():

    # 首先 建立数据库连接
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="248613",
        db="python_test",
        charset="utf8"
    )

    return conn

# 获取数据库游标
conn = sql_connect()
cur = conn.cursor()

"""
 函数sql_create 用户创建数据库
"""
def sql_create(sp_cource, sp_teacher, sp_classes, sp_student, sp_score_record, cur, conn):
    
    # 提交
    cur.execute(sp_cource)
    cur.execute(sp_teacher)
    cur.execute(sp_classes)
    cur.execute(sp_student)
    cur.execute(sp_score_record)

    conn.commit()
    print("Create Tables OK")

# 课程 表
sp_cource = """create table sp_course(
    	               c_id varchar(10) not null primary key,
    	               c_name varchar(32) not null
                    );"""

# 教师表格
sp_teacher = """create table sp_teacher(
                        t_id varchar(10) not null primary key,
                        t_name varchar(32) not null,
                        t_pass varchar(32),
                        t_sex varchar(4) not null,
                        t_nation varchar(25) not null,
                        t_pol_stat varchar(10) not null,
                        t_idcard varchar(20) not null,
                        t_address varchar(100) not null,
                        t_edu_bg varchar(15) not null,
                        t_gra_ins varchar(50) not null,
                        t_phone varchar(15) not null,
                        t_course varchar(10),
                        t_pic_path varchar(100)
                    );"""

# 班级类别表
sp_classes = """create table sp_classes(
                        cs_id varchar(10) not null primary key,
                        cs_date int not null,
                        cs_class int not null,
                        cs_adviser varchar(10) not null
                    );"""

# 学生信息表
sp_student = """create table sp_student(
                        s_id int auto_increment primary key,
                        s_name varchar(32) not null,
                        s_pass varchar(32) not null,
                        s_sex varchar(4) not null,
                        s_idcard varchar(20) not null,
                        s_address varchar(100) not null,
                        s_nation varchar(25) not null,
                        s_pol_stat varchar(10) not null,
                        s_school_time varchar(10) not null,
                        s_household varchar(10) not null,
                        s_schoolmethod varchar(10) not null,
                        s_class varchar(10),
                        s_pic_path varchar(100)
                    );"""

# 学生成绩表
sp_score_record = """create table sp_score_record(
                        sr_gradeid varchar(10) not null,
                        sr_stuid int not null,
                        sr_courseid varchar(10) not null,
                        sr_examtime varchar(10) not null,
                        sr_examtype varchar(10) not null,
                        sr_xueqi int not null,
                        sr_score double not null,
                        primary key(sr_stuid)
                    );"""

# 调用函数创建数据库
# sql_create(sp_cource, sp_teacher, sp_classes, sp_student, sp_score_record, cur)


# 接下来开始插入数据
"""
 函数sql_insert 用于向数据库中添加数据，但是这个函数只是手动添加数据
"""
def sql_insert(sp_course_sql, sp_course_data,
               sp_teacher_sql, sp_teacher_data, 
               sp_classes_sql, sp_classes_data, 
               sp_student_sql, sp_student_data, 
               sp_score_record_sql, sp_score_record_data,
               cur, conn):
    # 向表中添加数据
    cur.executemany(sp_course_sql, sp_course_data)
    cur.executemany(sp_teacher_sql, sp_teacher_data)
    cur.executemany(sp_classes_sql, sp_classes_data)
    cur.executemany(sp_student_sql, sp_student_data)
    cur.executemany(sp_score_record_sql, sp_score_record_data)
    conn.commit()
    print("Insert Data Ok!")

sp_course_sql = "insert into sp_course(c_id, c_name) values(%s, %s)"
sp_course_data = [
    ('C10001','语文'),
    ('C10002','数学'),
    ('C10003','英语'),
    ('C10004','物理'),
    ('C10005','化学'),
    ('C10006','生物'),
    ('C10007','地理'),
    ('C10008','政治'),
    ('C10009','历史'),
    ('C10010','音乐')
]

sp_teacher_sql = "insert into sp_teacher(t_id, t_name,t_pass,t_sex,t_nation,t_pol_stat,t_idcard,t_address,t_edu_bg,t_gra_ins, t_phone,t_course,t_pic_path) \
    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
sp_teacher_data = [
    ('T10001','谢中贵', '1', '男', '汉族', '中共党员', \
'340822199108084316', '安徽省合肥市', '本科', '安徽科技学院', '18365073582', 'C10001', 'null'),
    ('T10002','洛天', '1', '男', '汉族', '中共党员', \
'340822199108084317', '安徽省合肥市', '本科', '安徽科技学院', '18365073582', 'C10002', 'null'),
    ('T10003','洛熙', '1', '男', '汉族', '中共党员', \
'340822199108084318', '安徽省合肥市', '本科', '安徽科技学院', '18365073582', 'C10003', 'null'),
    ('T10004','落夕', '1', '女', '汉族', '中共党员', \
'340822199108084319', '安徽省合肥市', '本科', '安徽科技学院', '18365073582', 'C10004', 'null'),
    ('T10005','张三', '1', '男', '汉族', '中共党员', \
'340822199108084320', '安徽省合肥市', '本科', '安徽科技学院', '18365073582', 'C10005', 'null'),
    ('T10006','李四', '1', '男', '汉族', '中共党员', \
'340822199108084321', '安徽省合肥市', '本科', '安徽科技学院', '18365073582', 'C10006', 'null'),
    ('T10007','王五', '1', '男', '汉族', '中共党员', \
'340822199108084322', '安徽省合肥市', '本科', '安徽科技学院', '18365073582', 'C10007', 'null'),
    ('T10008','王世博', '1', '男', '汉族', '中共党员', \
'340822199108084323', '安徽省合肥市', '本科', '安徽科技学院', '18365073582', 'C10008', 'null'),
    ('T10009','刘伯温', '1', '男', '汉族', '中共党员', \
'340822199108084324', '安徽省合肥市', '本科', '安徽科技学院', '18365073582', 'C10009', 'null'),
    ('T10010','赵六', '1', '男', '汉族', '中共党员', \
'340822199108084325', '安徽省合肥市', '本科', '安徽科技学院', '18365073582', 'C10010', 'null')
]

sp_classes_sql = "insert into sp_classes(cs_id,cs_date,cs_class,cs_adviser) values(%s, %s, %s, %s)"
sp_classes_data = [
    ('G10001', 2014, 1, 'T10001'),
    ('G10002', 2013, 1, 'T10001'),
    ('G10003', 2012, 1, 'T10001'),
    ('G10004', 2011, 1, 'T10001'),
    ('G10005', 2014, 2, 'T10001')
]

sp_student_sql = "insert into sp_student(s_id, s_name, s_pass, s_sex, s_idcard, s_address, s_nation, s_pol_stat, s_school_time, s_household, s_schoolmethod, s_class, s_pic_path) \
    values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
sp_student_data = [
    (1, '孙悟空', '1570000000', '男', '340822199108080000',\
'安徽省合肥市', '少数民族', '共青团员', '2014-04-18', '城市', '走读生', 'G10001', 'null'),
    (2, '猪八戒', '1570000001', '男', '340822199108080001',\
'安徽省合肥市', '少数民族', '共青团员', '2014-04-18', '城市', '走读生', 'G10001', 'null'),
    (3, '沙悟净', '1570000002', '男', '340822199108080002',\
'安徽省合肥市', '少数民族', '共青团员', '2014-04-18', '城市', '走读生', 'G10001', 'null'),
    (4, '刘备', '1570000003', '男', '340822199108080003',\
'安徽省合肥市', '少数民族', '共青团员', '2014-04-18', '城市', '走读生', 'G10001', 'null'),
    (5, '关羽', '1570000004', '男', '340822199108080004',\
'安徽省合肥市', '少数民族', '共青团员', '2014-04-18', '城市', '走读生', 'G10001', 'null'),
    (6, '张飞', '1570000005', '男', '340822199108080005',\
'安徽省合肥市', '少数民族', '共青团员', '2014-04-18', '城市', '走读生', 'G10001', 'null'),
    (7, '赵云', '1570000006', '男', '340822199108080006',\
'安徽省合肥市', '少数民族', '共青团员', '2014-04-18', '城市', '走读生', 'G10001', 'null'),
    (8, '曹操', '1570000007', '男', '340822199108080007',\
'安徽省合肥市', '少数民族', '共青团员', '2014-04-18', '城市', '走读生', 'G10001', 'null'),
    (9, '诸葛亮', '1570000008', '男', '340822199108080008',\
'安徽省合肥市', '少数民族', '共青团员', '2014-04-18', '城市', '走读生', 'G10001', 'null'),
    (10, '曹植', '1570000009', '男', '340822199108080009',\
'安徽省合肥市', '少数民族', '共青团员', '2014-04-18', '城市', '走读生', 'G10001', 'null'),
    (11, '曹丕', '1570000010', '男', '340822199108080010',\
'安徽省合肥市', '少数民族', '共青团员', '2014-04-18', '城市', '走读生', 'G10001', 'null'),
    (12, '王云', '1570000011', '男', '340822199108080011',\
'安徽省合肥市', '少数民族', '共青团员', '2014-04-18', '城市', '走读生', 'G10001', 'null'),
    (13, '李渊', '1570000012', '男', '340822199108080012',\
'安徽省合肥市', '少数民族', '共青团员', '2014-04-18', '城市', '走读生', 'G10001', 'null'),
    (14, '李世民', '1570000013', '男', '340822199108080013',\
'安徽省合肥市', '少数民族', '共青团员', '2014-04-18', '城市', '走读生', 'G10001', 'null'),
    (15, '李元吉', '1570000014', '男', '340822199108080014',\
'安徽省合肥市', '少数民族', '共青团员', '2014-04-18', '城市', '走读生', 'G10001', 'null'),
    (16, '李元霸', '1570000015', '男', '340822199108080015',\
'安徽省合肥市', '少数民族', '共青团员', '2014-04-18', '城市', '走读生', 'G10001', 'null'),
    (17, '姜子牙', '1570000016', '男', '340822199108080016',\
'安徽省合肥市', '少数民族', '共青团员', '2014-04-18', '城市', '走读生', 'G10001', 'null'),
    (18, '武吉', '1570000017', '男', '340822199108080017',\
'安徽省合肥市', '少数民族', '共青团员', '2014-04-18', '城市', '走读生', 'G10001', 'null')
]

sp_score_record_sql = "insert into sp_score_record(sr_gradeid, sr_stuid, sr_courseid, sr_examtime, sr_examtype, sr_xueqi, sr_score) \
    values(%s, %s, %s, %s, %s, %s, %s)"
sp_score_record_data = [
    ('G10001', 1, 'C10001', '2014', '线上', 1, 99.0),
    ('G10002', 2, 'C10002', '2014', '线上', 1, 88.0),
    ('G10003', 3, 'C10003', '2014', '线上', 1, 92.0),
    ('G10004', 4, 'C10004', '2014', '线上', 1, 100.0),
    ('G10005', 5, 'C10005', '2014', '线上', 1, 98.0),
]

# 调用函数插入数据
# sql_insert(sp_course_sql, sp_course_data, 
        #    sp_teacher_sql, sp_teacher_data, 
        #    sp_classes_sql, sp_classes_data, 
        #    sp_student_sql, sp_student_data, 
        #    sp_score_record_sql, sp_score_record_data,
        #    cur, conn)


"""
 函数 sql_insert_by_excel() 此函数用于读物excel数据添加进数据库
 @Param: 
   @file_path: 文件相对路径
   @sql: 执行的sql语句
   @cur: 游标
   @conn: MySQL连接
"""
def sql_insert_by_excel(file_path, sql, cur, conn):
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

# 调用函数读取excel文件插入到数据库中
sql_insert_by_excel(r"xlsx\sp_classes.xlsx", sp_classes_sql, cur, conn)
sql_insert_by_excel(r"xlsx\sp_course.xlsx", sp_course_sql, cur, conn)
sql_insert_by_excel(r"xlsx\sp_score_record.xlsx", sp_score_record_sql, cur, conn)
sql_insert_by_excel(r"xlsx\sp_teacher.xlsx", sp_teacher_sql, cur, conn)
sql_insert_by_excel(r"xlsx\sp_student.xlsx", sp_student_sql, cur, conn)

"""
 函数table_truncate()，用于清空表中的数据
 @Param:
   @table_name: 表名
   @cur：游标
   @conn：连接
"""
def table_truncate(table_name, cur, conn):
    sql = f"truncate {table_name};"
    cur.execute(sql)
    conn.commit()
    print("Truncate Table Ok!")

# 调用函数清空表中的数据
# table_truncate("sp_classes", cur, conn)
# table_truncate("sp_course", cur, conn)
# table_truncate("sp_score_record", cur, conn)
# table_truncate("sp_teacher", cur, conn)
# table_truncate("sp_student", cur, conn)

cur.close()
conn.close()