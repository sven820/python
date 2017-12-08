# Author:JJ.sven

# p2里面用raw_input()
username = input("name: ")
age = int(input("age: "))
print(type(age))

job = input("job: ")

info = '''
name: %s 
age: %d 
job: %s
''' % (username, age, job)

info2 = '''
name: {name} 
age: {age}
job: {job}
'''.format(name=username, age=age, job=job)

info3 = '''
name: {0} 
age: {1}
job: {2}
'''.format(username, age, job)

print(info3)