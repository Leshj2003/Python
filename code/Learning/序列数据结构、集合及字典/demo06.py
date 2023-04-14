# -*-  coding = utf-8 -*-
# @Time : 2023/4/14 20:31
# @Author : LHJ青梦
# @File : demo06.py
# @Software: PyCharm

'''
文件“schoolCode.csv”和“MajorCode.csv”中的数据是每个学院的编号和专业的编号，“studentList.csv”文件中有若干学生信息，学生出现的顺序是他在班级中排名顺序，每行中的数据用逗号分隔，各数据依顺代表：

学生姓名,学生性别,学院,专业名称,行政班（专业加班级号，例如经济1901）,入学年级。

假如本科的学生层次编号为012，请为“studentList.csv”中的数据增加学号，学号创建规则是：

学生层次+入学年份后两位+学院代码+专业代码+班级号+班中排名。

：012171985170110 表示本科生、2017年入学、文法学院、 编辑出版专业、1701班、排名为10的同学

输入格式说明

第一行输入学生姓名

第二行输入班级

输出格式说明

第一行输出  该学生的学号、学生姓名、学生性别、学院、专业名称、行政班、入学年级信息，各项之间空格分隔

其后分行输出该班级所有同学的学号、学生姓名、学生性别、学院、专业名称、行政班、入学年级信息，各项之间空格分隔
'''


def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:          # 只读模式打开文件
        file_to_list = [line.strip().split(',') for line in file]          # 文件全部内容读取出来放入列表中，每个元素为一行字符串
    return file_to_list                                                    # 以列表形式返回文件中的数据


def student_id(ls_student, ls_school, ls_major):                  # 生成学号并插入到lsStudent中
    dic_school = {x[0]: x[1] for x in ls_school}                  # 构建学院字典
    dic_major = {x[0]: x[1] for x in ls_major}                    # 构建专业字典
    detail = []
    for student in ls_student:                                    # 生成学号
        student_number = '012'
        student_number = student_number + student[5][2:] + dic_school[student[2]] + dic_major[student[3]] + student[4][-4:]
        # student[5][2:] 入学年份后2位，student[2]是学院，dic_school[student[2]] 是学院编号，
        # student[3]是专业，  dic_major[student[3]]是专业编号，student[4]是专业班级，如'新闻类1703'，
        # student[4][-4:]取班级编号后2位
        student_number = student_number + '{0:0>2}'.format([x[0] for x in ls_student if student[4] == x[4]].index(student[0]) + 1)
        # 查询学生在自己班级中的排序拼接到学号上
        detail.append([student_number] + student)                # 将学号和其他信息加入到列表中
    return detail                                                # 返回加了学号的学生信息


def student_info(stu_name, ls_student):
    student_detail = [info for info in ls_student if info[1] == stu_name][0]  # 列表中仅有一个元素，取出这个元素
    return student_detail                                                     # 返回学生的详细信息


def classmate(stu_class, ls_student):
    classmate_of_student = [info for info in ls_student if info[5] == stu_class]
    return classmate_of_student                                 # 返回同班同学的信息列表


if __name__ == '__main__':
    stuName = input()                                                  # 输入学生姓名
    stuClass = input()                                                 # 输入班级
    student_list = read_file('studentList.csv')[1:]                        # 获得学生信息列表
    school_code = read_file('schoolCode.csv')                          # 获得学院信息列表
    major_code = read_file('MajorCode.csv')                            # 获得专业信息列表
    studentDetail = student_id(student_list, school_code, major_code)  # 调用函数计算ID并插入到列表中
    print(*student_info(stuName, studentDetail))                       # 输出学生信息
    ls_classmate = classmate(stuClass, studentDetail)                  # 返回同班同学信息列表
    for classmate in ls_classmate:                                     # 逐个输出同学信息
        print(*classmate)