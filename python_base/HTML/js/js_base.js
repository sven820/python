/**
 * Created by jinxiaofei on 2017/12/25.
 */


// 这种申明默认为全局变量

/**
 * JavaScript 中的数据类型分为原始类型和对象类型：

原始类型
数字
字符串
布尔值
对象类型
数组
“字典”
...
特别的，数字、布尔值、null、undefined、字符串是不可变。
 */

name = 'jxf'
// 定义局部变量
var age = 18
console.log(name)

/**
 *  数字类型 Number
 *
 *  JavaScript中不区分整数值和浮点数值，JavaScript中所有数字均用浮点数值表示。

转换：

parseInt(..)    将某值转换成数字，不成功则NaN
parseFloat(..) 将某值转换成浮点数，不成功则NaN
特殊值：

 NaN，非数字。可使用 isNaN(num) 来判断。
Infinity，无穷大。可使用 isFinite(num) 来判断。


 */

// 将字符串转成数据类型
print(parseInt('10'))
print(parseInt('10.098'))
// math模块包装对数字的处理的相关方法
// 对一个数上舍入。
print(Math.ceil(10.7))
// 对一个数下舍入。
print(Math.floor(10.7))
// 舍入最接近的整数
print(Math.round())
// 随机数
print(Math.random())
// other：max(); min(), abs() ...

/**
 * 字符串 String
 *
 * 字符串是由字符组成的数组，但在JavaScript中字符串是不可变的：
 * 可以访问字符串任意位置的文本，但是JavaScript并未提供修改已知字符串内容的方法。
 *
 * 常见功能：
 *  obj.length                           长度

    obj.trim()                           移除空白
    obj.trimLeft()
    obj.trimRight)
    obj.charAt(n)                        返回字符串中的第n个字符
    obj.concat(value, ...)               拼接
    obj.indexOf(substring,start)         子序列位置
    obj.lastIndexOf(substring,start)     子序列位置
    obj.substring(from, to)              根据索引获取子序列
    obj.slice(start, end)                切片
    obj.toLowerCase()                    大写
    obj.toUpperCase()                    小写
    obj.split(delimiter, limit)          分割
    obj.search(regexp)                   从头开始匹配，返回匹配成功的第一个位置(g无效)
    obj.match(regexp)                    全局搜索，如果正则中有g表示找到全部，否则只找到第一个。
    obj.replace(regexp, replacement)     替换，正则中有g则替换所有，否则只替换第一个匹配项，
                                         $数字：匹配的第n个组内容；
                                         $&：当前匹配的内容；
                                         $`：位于匹配子串左侧的文本；
                                         $'：位于匹配子串右侧的文本
                                         $$：直接量$符号
 */

/**
 * 布尔类型 Boolean
 *
 * 布尔类型仅包含真假，与Python不同的是其首字母小写。
 *
 *  ==      比较值相等
    !=       不等于
    ===   比较值和类型相等
    !===  不等于
    ||        或
    &&      且
 */


/** 数组
 *
 * 常见功能
 *
 *  obj.length          数组的大小

    obj.push(ele)       尾部追加元素
    obj.pop()           尾部获取一个元素
    obj.unshift(ele)    头部插入元素
    obj.shift()         头部移除元素
    obj.splice(start, deleteCount, value, ...)  插入、删除或替换数组的元素
                        obj.splice(n,0,val) 指定位置插入元素
                        obj.splice(n,1,val) 指定位置替换元素
                        obj.splice(n,1)     指定位置删除元素
    obj.slice( )        切片
    obj.reverse( )      反转
    obj.join(sep)       将数组元素连接起来以构建一个字符串
    obj.concat(val,..)  连接数组
    obj.sort( )         对数组元素进行排序

 */

/** 字典
 *
 *  js 字典其实属于对象类型
 */

/**
 * 序列化
 *
 *  JSON.stringify(obj)   序列化
    JSON.parse(str)        反序列化
 */


/** 转义
 *
 *  decodeURI( )                   URl中未转义的字符
    decodeURIComponent( )   URI组件中的未转义字符
    encodeURI( )                   URI中的转义字符
    encodeURIComponent( )   转义URI组件中的字符  会转义url中的分割符
    escape( )                       对字符串转义
    unescape( )                     给转义字符串解码
    URIError                        由URl的编码和解码方法抛出

 通过js保存cooki时，需要将数据经过转义后保存
 */

/** eval （就是python中eval和exec的集合）
 *  JavaScript中的eval是Python中eval和exec的合集，既可以编译代码也可以获取返回值。

    eval()
    EvalError   执行字符串中的JavaScript代码

 注：python: val = eval(表达式）； exec（执行代码）=》无返回结果
 */

/** 正则
 *
 * 1、定义正则表达式

    /.../  用于定义正则表达式
    /.../g 表示全局匹配
    /.../i 表示不区分大小写
    /.../m 表示多行匹配
    JS正则匹配时本身就是支持多行，此处多行匹配只是影响正则表达式^和$，m模式也会使用^$来匹配换行的内容)

 定义正则表达式也可以  reg= new RegExp()

 * 匹配 JavaScript中支持正则表达式，其主要提供了两个功能：
 *
 *  1 test(string)     检查字符串中是否和正则匹配
 *      n = 'uui99sdf'
        reg = /\d+/
        reg.test(n)  ---> true
 # 只要正则在字符串中存在就匹配，如果想要开头和结尾匹配的话，就需要在正则前后加 ^和$

 *  2 exec(string)    获取正则表达式匹配的内容，如果未匹配，值为null，否则，获取匹配成功的数组。
 *      获取正则表达式匹配的内容，如果未匹配，值为null，否则，获取匹配成功的数组。

        非全局模式
            获取匹配结果数组，注意：第一个元素是第一个匹配的结果，后面元素是正则子匹配（正则内容分组匹配）
            var pattern = /\bJava\w*\b/;
            var text = "JavaScript is more fun than Java or JavaBeans!";
            result = pattern.exec(text)

            var pattern = /\b(Java)\w*\b/;
            var text = "JavaScript is more fun than Java or JavaBeans!";
            result = pattern.exec(text)

        全局模式
            需要反复调用exec方法，来一个一个获取结果，直到匹配获取结果为null表示获取完毕
            var pattern = /\bJava\w*\b/g;
            var text = "JavaScript is more fun than Java or JavaBeans!";
            result = pattern.exec(text)

            var pattern = /\b(Java)\w*\b/g;
            var text = "JavaScript is more fun than Java or JavaBeans!";
            result = pattern.exec(text)

 *  3 字符串中相关方法
 *      obj.search(regexp)                   获取索引位置，搜索整个字符串，返回匹配成功的第一个位置(g模式无效)
        obj.match(regexp)                    获取匹配内容，搜索整个字符串，获取找到第一个匹配内容，如果正则是g模式找到全部
        obj.replace(regexp, replacement)     替换匹配替换，正则中有g则替换所有，否则只替换第一个匹配项，
                                                $数字：匹配的第n个组内容；
                                                  $&：当前匹配的内容；
                                                  $`：位于匹配子串左侧的文本；
                                                  $'：位于匹配子串右侧的文本
                                                  $$：直接量$符号
 */
var pattern = /^Java\w*/gm;
var text = "JavaScript is more fun than \nJavaEE or JavaBeans!";
result = pattern.exec(text)
var reg = new RegExp('^Java\w*')

/** 时间处理
 *
 * JavaScript中提供了时间相关的操作，时间操作中分为两种时间：

    时间统一时间
    本地时间（东8区）
    更多操作参见：http://www.shouce.ren/api/javascript/main.html
 */
var date = new Date();
date.getDay();
date.setHours(10);

/** 异常处理
 *
 *  try {
        //这段代码从上往下运行，其中任何一个语句抛出异常该代码块就结束运行
    }
    catch (e) {
        // 如果try代码块中抛出了异常，catch代码块中的代码就会被执行。
        //e是一个局部变量，用来指向Error对象或者其他抛出的对象
    }
    finally {
         //无论try中代码是否有异常抛出（甚至是try代码块中有return语句），finally代码块中始终会被执行。
    }
 注：主动跑出异常 throw Error('xxxx')
 */




