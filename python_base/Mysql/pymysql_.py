__author__ = "JJ.sven"

import pymysql

conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       passwd='jxf1992',
                       db='test')
# cursor = conn.cursor() #默认获取是元祖类型
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor) #设置获取结果为字典

'''查询数据
注：在fetch数据时按照顺序进行，可以使用cursor.scroll(num,mode)来移动游标位置，如：

cursor.scroll(1,mode='relative')  # 相对当前位置移动
cursor.scroll(2,mode='absolute') # 相对绝对位置移动
'''
cursor.execute("select * from student")
# 获取一/n/all条
# print(cursor.fetchone())
# print(cursor.fetchmany(10))
print(cursor.fetchall())
print(cursor.rowcount)

'''修改数据'''
'''修改一条'''
# effect_row = cursor.execute("update student set age=18 where name='jinxiaofei'")
# print(effect_row)
'''修改多条'''
datas = [
    ('test', 20, '1992-08-08', 1, 1),
    ('test', 20, '1992-08-08', 1, 1),
    ('test', 20, '1992-08-08', 1, 1)
]
# effect_row = cursor.executemany("insert into student (name,age,birthday,sex,class_id) values (%s,%s,%s,%s,%s)", datas)
# print(effect_row)
# 获取创建数据的自增id, 执行insert后才有
# print('lastrowid: ',cursor.lastrowid)

# print(cursor.execute("delete from student where name='test' AND age=20"))



conn.commit()
cursor.close()
conn.close()