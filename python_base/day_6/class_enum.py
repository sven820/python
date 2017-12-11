__author__ = "JJ.sven"

from enum import Enum, unique

Month = Enum('Month', ('Jan',
                               'Feb',
                               'Mar',
                               'Apr',
                               'May',
                               'Jun',
                               'Jul',
                               'Aug',
                               'Sep',
                               'Oct',
                               'Nov',
                               'Dec'))

print(Month.Jan.value)
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

@unique
class Weekday(Enum):

    Sun = 0
    Mon = 1
    Tur = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print(Weekday.Sun.value)

'''==========sep words=========='''