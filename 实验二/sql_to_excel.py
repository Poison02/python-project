import pandas as pd
from sqlalchemy import create_engine


engine = create_engine("mysql+pymysql://root:248613@localhost:3306/python_test")

# 导出学生信息表
sp_student = "select * from sp_student;"
# 导出教师信息表
sp_teacher = "select * from sp_teacher;"
# 导出班级信息表
sp_classes = "select * from sp_classes;"
# 导出课程表
sp_course = "select * from sp_course;"
# 导出学生成绩表
sp_score_record = "select * from sp_score_record;"

# 将表写入excel
sp_student_data = pd.read_sql(sp_student, engine)
sp_student_data.to_excel("./xlsx/sp_student.xlsx", index=None)
# 将表写入excel
sp_teacher_data = pd.read_sql(sp_teacher, engine)
sp_teacher_data.to_excel("./xlsx/sp_teacher.xlsx", index=None)
# 将表写入excel
sp_classes_data = pd.read_sql(sp_classes, engine)
sp_classes_data.to_excel("./xlsx/sp_classes.xlsx", index=None)
# 将表写入excel
sp_course_data = pd.read_sql(sp_course, engine)
sp_course_data.to_excel("./xlsx/sp_course.xlsx", index=None)
# 将表写入excel
sp_score_record_data = pd.read_sql(sp_score_record, engine)
sp_score_record_data.to_excel("./xlsx/sp_score_record.xlsx", index=None)

print("success")