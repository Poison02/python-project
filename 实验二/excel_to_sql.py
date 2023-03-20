import pymysql
import pandas as pd

# 首先 建立数据库连接
conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="248613",
    db="python_test",
    charset="utf8"
)

# # 获取数据库游标
cur = conn.cursor()

# # 创建第一个表格 课程表
# sp_cource = """create table sp_course(
# 	               c_id varchar(10) not null primary key,
# 	               c_name varchar(32) not null,
# 	               delflag boolean default false
#                 );"""

# # 教师表格
# sp_teacher = """create table sp_teacher(
#                     t_id varchar(10) not null primary key,
#                     t_name varchar(32) not null,
#                     t_pass varchar(32),
#                     t_sex varchar(4) not null,
#                     t_nation varchar(25) not null,
#                     t_pol_stat varchar(10) not null,
#                     t_idcard varchar(20) not null,
#                     t_address varchar(100) not null,
#                     t_job_time date not null,
#                     t_edu_bg varchar(15) not null,
#                     t_gra_ins varchar(50) not null,
#                     t_phone varchar(15) not null,
#                     t_course varchar(10),
#                     t_pic_path varchar(100),
#                     delflag boolean default false,
#                     foreign key(t_course) references sp_course(c_id)
#                 );"""

# # 班级类别表
# sp_classes = """create table sp_classes(
#                     cs_id varchar(10) not null primary key,
#                     cs_date int not null,
#                     cs_class int not null,
#                     cs_adviser varchar(10) not null,
#                     delflag boolean default false,
#                     foreign key(cs_adviser) references sp_teacher(t_id)
#                 );"""

# # 学生信息表
# sp_student = """create table sp_student(
#                     s_id int auto_increment primary key,
#                     s_name varchar(32) not null,
#                     s_pass varchar(32) not null,
#                     s_sex varchar(4) not null,
#                     s_idcard varchar(20) not null,
#                     s_address varchar(100) not null,
#                     s_nation varchar(25) not null,
#                     s_pol_stat varchar(10) not null,
#                     s_school_time varchar(10) not null,
#                     s_household varchar(10) not null,
#                     s_schoolmethod varchar(10) not null,
#                     s_class varchar(10),
#                     s_pic_path varchar(100),
#                     delflag boolean default false,
#                     foreign key(s_class) references sp_classes(cs_id)
#                 );"""

# # 学生成绩表
# sp_score_record = """create table sp_score_record(
#                         sr_gradeid varchar(10) not null,
#                         sr_stuid int not null,
#                         sr_courseid varchar(10) not null,
#                         sr_examtime varchar(10) not null,
#                         sr_examtype varchar(10) not null,
#                         sr_xueqi int not null,
#                         sr_score double not null,
#                         primary key(sr_stuid, sr_courseid, sr_examtime),
#                         foreign key(sr_gradeid) references sp_classes(cs_id),
#                         foreign key(sr_stuid) references sp_student(s_id),
#                         foreign key(sr_courseid) references sp_course(c_id)
#                     );"""

# # 提交
# cur.execute(sp_cource)
# cur.execute(sp_teacher)
# cur.execute(sp_classes)
# cur.execute(sp_student)
# cur.execute(sp_score_record)

# conn.commit()
# print("Create OK")

# 接下来开始插入数据
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
sp_teacher_sql = "insert into sp_teacher(t_id, t_name,t_pass,t_sex,t_nation,t_pol_stat,t_idcard,t_address,t_job_time,t_edu_bg,t_gra_inst_phone,t_course,t_pic_path,delflag) \
    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
sp_teacher_data = [
    ('T10001','谢中贵', '1', '男', '汉族', '中共党员', \
'340822199108084316', '安徽省合肥市', '2014-04-18', '本科', '安徽科技学院', '18365073582', 'C10001', 'null', 'false'),
    ('T10002','洛天', '1', '男', '汉族', '中共党员', \
'340822199108084317', '安徽省合肥市', '2014-04-18', '本科', '安徽科技学院', '18365073582', 'C10002', 'null', 'false'),
    ('T10003','洛熙', '1', '男', '汉族', '中共党员', \
'340822199108084318', '安徽省合肥市', '2014-04-18', '本科', '安徽科技学院', '18365073582', 'C10003', 'null', 'false'),
    ('T10004','落夕', '1', '女', '汉族', '中共党员', \
'340822199108084319', '安徽省合肥市', '2014-04-18', '本科', '安徽科技学院', '18365073582', 'C10004', 'null', 'false'),
    ('T10005','张三', '1', '男', '汉族', '中共党员', \
'340822199108084320', '安徽省合肥市', '2014-04-18', '本科', '安徽科技学院', '18365073582', 'C10005', 'null', 'false'),
    ('T10006','李四', '1', '男', '汉族', '中共党员', \
'340822199108084321', '安徽省合肥市', '2014-04-18', '本科', '安徽科技学院', '18365073582', 'C10006', 'null', 'false'),
    ('T10007','王五', '1', '男', '汉族', '中共党员', \
'340822199108084322', '安徽省合肥市', '2014-04-18', '本科', '安徽科技学院', '18365073582', 'C10007', 'null', 'false'),
    ('T10008','王世博', '1', '男', '汉族', '中共党员', \
'340822199108084323', '安徽省合肥市', '2014-04-18', '本科', '安徽科技学院', '18365073582', 'C10008', 'null', 'false'),
    ('T10009','刘伯温', '1', '男', '汉族', '中共党员', \
'340822199108084324', '安徽省合肥市', '2014-04-18', '本科', '安徽科技学院', '18365073582', 'C10009', 'null', 'false'),
    ('T10010','赵六', '1', '男', '汉族', '中共党员', \
'340822199108084325', '安徽省合肥市', '2014-04-18', '本科', '安徽科技学院', '18365073582', 'C10010', 'null', 'false')
]

sp_classes_sql = "insert into sp_classes(cs_id,cs_date,cs_class,cs_adviser,delflag) values(%s, %s, %s, %s, %s)"
sp_classes_data = [
    ('G10001', 2014, 1, 'T10001','false'),
    ('G10002', 2013, 1, 'T10001','false'),
    ('G10003', 2012, 1, 'T10001','false'),
    ('G10004', 2011, 1, 'T10001','false'),
    ('G10005', 2014, 2, 'T10001','false')
]
sp_student_data = [
    "insert into sp_student values(1, '孙悟空', '1570000000', '男', '340822199108080000',\
'安徽省合肥市', '少数民族', '共青团员', '2014-04-18', '城市', '走读生', 'G10001', null,false);"
    "insert into sp_student values(2, '猪八戒', '1570000001', '男', '340822199108080001',\
'安徽省合肥市', '少数民族', '共青团员', '2014-04-18', '城市', '走读生', 'G10001', null,false);"
    "insert into sp_student values(3, '沙悟净', '1570000002', '男', '340822199108080002',\
'安徽省合肥市', '少数民族', '共青团员', '2014-04-18', '城市', '走读生', 'G10001', null,false);"
    "insert into sp_student values(4, '刘备', '1570000003', '男', '340822199108080003',\
'安徽省合肥市', '少数民族', '共青团员', '2014-04-18', '城市', '走读生', 'G10001', null,false);"
    "insert into sp_student values(5, '关羽', '1570000004', '男', '340822199108080004',\
'安徽省合肥市', '少数民族', '共青团员', '2014-04-18', '城市', '走读生', 'G10001', null,false);"
    "insert into sp_student values(6, '张飞', '1570000005', '男', '340822199108080005',\
'安徽省合肥市', '少数民族', '共青团员', '2014-04-18', '城市', '走读生', 'G10001', null,false);"
    "insert into sp_student values(7, '赵云', '1570000006', '男', '340822199108080006',\
'安徽省合肥市', '少数民族', '共青团员', '2014-04-18', '城市', '走读生', 'G10001', null,false);"
    "insert into sp_student values(8, '曹操', '1570000007', '男', '340822199108080007',\
'安徽省合肥市', '少数民族', '共青团员', '2014-04-18', '城市', '走读生', 'G10001', null,false);"
    "insert into sp_student values(9, '诸葛亮', '1570000008', '男', '340822199108080008',\
'安徽省合肥市', '少数民族', '共青团员', '2014-04-18', '城市', '走读生', 'G10001', null,false);"
    "insert into sp_student values(10, '曹植', '1570000009', '男', '340822199108080009',\
'安徽省合肥市', '少数民族', '共青团员', '2014-04-18', '城市', '走读生', 'G10001', null,false);"
    "insert into sp_student values(11, '曹丕', '1570000010', '男', '340822199108080010',\
'安徽省合肥市', '少数民族', '共青团员', '2014-04-18', '城市', '走读生', 'G10001', null,false);"
    "insert into sp_student values(12, '王云', '1570000011', '男', '340822199108080011',\
'安徽省合肥市', '少数民族', '共青团员', '2014-04-18', '城市', '走读生', 'G10001', null,false);"
    "insert into sp_student values(13, '李渊', '1570000012', '男', '340822199108080012',\
'安徽省合肥市', '少数民族', '共青团员', '2014-04-18', '城市', '走读生', 'G10001', null,false);"
    "insert into sp_student values(14, '李世民', '1570000013', '男', '340822199108080013',\
'安徽省合肥市', '少数民族', '共青团员', '2014-04-18', '城市', '走读生', 'G10001', null,false);"
    "insert into sp_student values(15, '李元吉', '1570000014', '男', '340822199108080014',\
'安徽省合肥市', '少数民族', '共青团员', '2014-04-18', '城市', '走读生', 'G10001', null,false);"
    "insert into sp_student values(16, '李元霸', '1570000015', '男', '340822199108080015',\
'安徽省合肥市', '少数民族', '共青团员', '2014-04-18', '城市', '走读生', 'G10001', null,false);"
    "insert into sp_student values(17, '姜子牙', '1570000016', '男', '340822199108080016',\
'安徽省合肥市', '少数民族', '共青团员', '2014-04-18', '城市', '走读生', 'G10001', null,false);"
    "insert into sp_student values(18, '武吉', '1570000017', '男', '340822199108080017',\
'安徽省合肥市', '少数民族', '共青团员', '2014-04-18', '城市', '走读生', 'G10001', null,false);"
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

# 向成绩表中添加数据
# cur.executemany(sp_score_record_sql, sp_score_record_data)
# conn.commit()
# print("OKOKOK")

# 读取excel文件插入MySQL中
df = pd.read_excel("sp_score_record.xlsx")
lst = []
for i in range(0, len(df)):
    record = tuple(df.loc[i])
    lst.append(record)
    # 把空值，或者缺失填充
    sp_score_record_sql = sp_score_record_sql.replace('nan', 'null').replace('None', 'null').replace('none', 'null')

# 执行插入语句
cur.executemany(sp_score_record_sql, lst)
# 提交
conn.commit()
print("OK")

cur.close()
conn.close()
