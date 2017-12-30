/**
 * Created by jinxiaofei on 2017/12/25.
 */

/** 1、基本函数
 *
 *  JavaScript中函数基本上可以分为一下三类：
 *
 *  注意：对于JavaScript中函数参数，实际参数的个数可能小于形式参数的个数，函数内的特殊值arguments中封装了所有实际参数。
 */

// 普通函数
    function func(arg){
        return true;
    }

// 匿名函数
    var f = function(arg){
        return "tony";
    }
    f('xx')
    setInterval(function () {
        console.log('123')
    }, 5000)

// 自执行函数
    (function(arg){
        console.log(arg);
    })('123')

/** 2、作用域 （重要）
 *
 *  JavaScript中每个函数都有自己的作用域，当出现函数嵌套时，就出现了作用域链。当内层函数使用变量时，会根据作用域链从内到外一层层的循环，如果不存在，则异常。

    切记：所有的作用域在创建函数且未执行时候就已经存在。

    注：声明提前，在JavaScript引擎“预编译”时进行，找到变量var一下，就是申明一下，没赋值的变量的值默认是undefined。

    注：python中是以函数作为作用域,和js一样，也存在作用域链，并且执行前作用域已确定
 */

/** 3、闭包
 *
 *  闭包是指可以包含自由（未绑定到特定对象）变量的代码块。

    「闭包」，是指拥有多个变量和绑定了这些变量的环境的表达式（通常是一个函数），因而这些变量也是该表达式的一部分。

    闭包是个函数，而它「记住了周围发生了什么」。表现为由「一个函数」体中定义了「另个函数」

    由于作用域链只能从内向外找，默认外部无法获取函数内部变量。闭包，在外部获取函数内部的变量
 */

/** 4、面向对象
*   对于下述代码需要注意：

    Foo充当的构造函数
    this代指对象
    创建对象时需要使用 new
*/

function Foo (name,age) {
    this.Name = name;
    this.Age = age;
    this.Func = function(arg){
        return this.Name + arg;
    }
}

var obj = new Foo('alex', 18);
var ret = obj.Func("sb");
console.log(ret);
/**上述代码中每个对象中均保存了一个相同的Func函数，从而浪费内存。使用原型和可以解决该问题：
 * */

function Foo (name,age) {
    this.Name = name;
    this.Age = age;
}
//Foo的原型
Foo.prototype = {
    GetInfo: function(){
        return this.Name + this.Age
    },
    getAge : function(arg){
        return this.Age;
    }
}

/**
 *  备注：this 在对象调用函数时，函数内部也能用this，代指调用者
 *
 *  1 当在标签中绑定事件时候，this为window（全局变量），要想为被点击标签，需要在绑定
 *    事件的时候传入this   <div onClick='func(this)'/>
 */


/**
 *  词法分析解析
 *
 *  1 先分析行参 行参赋值
 *  2 再分析变量 有行参则声明，此时还没赋值，值为undefined
 *  3 最后分析函数 函数优先级高，如果定义了函数，则把函数赋值给变量
 *
 *  所以最后age已经是一个函数了
 *
 *  最后再执行函数t（），
       第一个log age为函数
       之后age被赋值27，所以第二个age是27
       再定义age函数，这一步在运行前分析的时候已经处理过了，并不会再执行age = function age(){}，所以最后一个log还是27
 */
function t(age) {
    console.log(age); //function age()
    var age = 27;
    console.log(age); //27
    function age() {};
    console.log(age); //27
}
t(3)
