__author__ = "JJ.sven"

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint, Index, Date, String, MetaData, Table
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import mapper
from sqlalchemy import func
from sqlalchemy import or_, and_

'''SQLAchemy ORM 框架 
sqlachemy 无法修改表结构，如果要修改可以使用Alembic | SQLAlchemy-Migrate
1.配置mysql处理库
MySQL-Python
    mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
   
pymysql
    mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
   
MySQL-Connector
    mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
   
cx_Oracle
    oracle+cx_oracle://user:pass@host:port/dbname[?key=value&key=value...]

2. 使用create_engine执行原生sql

3. ORM

4. 常见配置
类型名称	python类型	描述
Integer	int	常规整形，通常为32位
SmallInteger	int	短整形，通常为16位
BigInteger	int或long	精度不受限整形
Float	float	浮点数
Numeric	decimal.Decimal	定点数
String	str	可变长度字符串
Text	str	可变长度字符串，适合大量文本
Unicode	unicode	可变长度Unicode字符串
Boolean	bool	布尔型
Date	datetime.date	日期类型
Time	datetime.time	时间类型
Interval	datetime.timedelta	时间间隔
Enum	str	字符列表
PickleType	任意Python对象	自动Pickle序列化
LargeBinary	str	二进制

常见的SQLALCHEMY列选项
可选参数	描述
primary_key	如果设置为True，则为该列表的主键
unique	如果设置为True，该列不允许相同值
index	如果设置为True，为该列创建索引，查询效率会更高
nullable	如果设置为True，该列允许为空。如果设置为False，该列不允许空值
default	定义该列的默认值


'''

#echo 是否打印日志
'''
处理中文

sqlalchemy设置编码字符集一定要在数据库访问的URL上增加charset=utf8，
否则数据库的连接就不是utf8的编码格式
'''
engine = create_engine("mysql+pymysql://root:jxf1992@localhost/test?charset=utf8", encoding='utf-8', echo=True)

'''原生sql'''
#执行sql, 返回游标
# cur = engine.execute("select * from student")
# print(cur.fetchall())

'''ORM'''
# ORM 基类
Base = declarative_base()


'''创建表方式1 常用'''
class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(32), nullable=False, index=True) #index 索引
    age = Column(Integer, nullable=False)
    birthday = Column(Date, nullable=False)
    sex = Column(Integer, nullable=False)
    class_id = Column(Integer, nullable=False)

'''创建表方式2'''
metadata = MetaData()
class_ = Table(
    'class', metadata,
    Column('class_id', Integer, primary_key=True),
    Column('name', String(32), nullable=False),
    Column('teacher', String(32), nullable=False),
    Column('num', Integer, nullable=False)
)

class Class_(object):
    def __init__(self, class_id, name, teacher, num):
        self.class_id = class_id
        self.name = name
        self.teacher = teacher
        self.num = num

mapper(Class_, class_)

'''外键设置'''

class Teacher(Base):
    __tablename__ = 'teacher'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(32), nullable=False)
    age = Column(Integer, nullable=False)
    man_stu_id = Column(Integer, ForeignKey('student.id')) #外键

    # 关联对象 和表结构无关
    # 被设置对象里可 关联获取或更新当前对象
    '''
        1. 反查
            obj = Session.query(Student).first()
            for i in obj.teacheres: #通过Student对象反查关联的Teacher记录
                print(i)
 
            teacher_obj = Session.query(Teacher).first()
            print(teacher_obj.stu.name)  #在teacher_obj里直接查关联的Student表
            
        2. 创建关联对象
            obj = Session.query(Student).filter().all()[0]
            obj.teacheres = [Teacher(), #添加关联对象
                             Teacher()]
            session.commit()
    '''
    stu = relationship('Student', backref='teacheres')



'''这里开始创建表'''
Base.metadata.create_all(engine)

'''查询'''
Session_cls = sessionmaker(bind=engine)
session = Session_cls()
# filter_by 使用关键字参数，用于精确组合查询，不支持条件>, <, !=
# filter_by()就是把你传参的key,value写成filter的sql格式，再加个and组合起来而已
for s in session.query(Student).filter_by(id=10):
    print('filter_by：', s.name, s)
# filter 可支持条件组合查询, 支持or_, in_算法
for s in session.query(Student).filter(and_(Student.id>=10, Student.name=='lisi')):
    print('query：', s.name, s)
# filter也可多调用来多条件查询
for s in session.query(Student).filter(Student.id>=10).filter(Student.name=='lisi'):
    print('query multi: ', s.name, s)

# 获取所有数据, 不写all也一样
for s in session.query(Student.name, Student.age).all():
    print('query all：', s.name, s)

# 统计分组
print('query group：', session.query(Student.name, func.count(Student.name)).group_by(Student.name).all())

'''修改'''
s = session.query(Student).filter_by(name='jinxiaofei').one()
s.age = 17

# session.rollback() #回滚

'''增加'''
s1 = Student()
s1.name = 'test_insert'
s1.age = 30
s1.birthday='2019-09-09'
s1.sex = 1
s1.class_id = 2
# session.add(s1) # insert
# session.add_all()



'''删'''
session.query(Student).filter_by(name='test_insert').delete()


session.commit()

