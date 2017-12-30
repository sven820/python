/**
 * Created by jinxiaofei on 2017/12/26.
 */

/** 一、查找元素
 * 1、直接查找
 *
 *  document.getElementById             根据ID获取一个标签
    document.getElementsByName          根据name属性获取标签集合
    document.getElementsByClassName     根据class属性获取标签集合
    document.getElementsByTagName       根据标签名获取标签集合

 * 2、间接查找
 *
 *  parentNode          // 父节点
    childNodes          // 所有子节点
    firstChild          // 第一个子节点
    lastChild           // 最后一个子节点
    nextSibling         // 下一个兄弟节点
    previousSibling     // 上一个兄弟节点

    parentElement           // 父节点标签元素
    children                // 所有子标签
    firstElementChild       // 第一个子标签元素
    lastElementChild        // 最后一个子标签元素
    nextElementtSibling     // 下一个兄弟标签元素
    previousElementSibling  // 上一个兄弟标签元素
 */
// 直接查找
document.getElementById('id')
document.getElementsByClassName('class_name')
document.getElementsByTagName('tag')
document.getElementsByName('attr_name')

// 间接查找
ele = document.getElementById('id')

/** 文本内容
 */
ele.innerText;
ele.innerHTML;
ele.value; //input, select, textarea;
/** 事件
 *  1 标签中绑定
 *  2 dom操作绑定
 *  3 事件监听
 */
ele.onclick = function () {  };
ele.onfocus = function () {  }; //成为焦点
ele.onblur = function ()  {  }; //失去焦点
ele.onmouseover = function () {}; //鼠标移入
ele.onmouseout = function () {}; //鼠标移出

//false 参数表示冒泡还是捕捉，同一事件可重复添加，都会被执行
// false冒泡 外层先执行事件
// true 捕捉 内层先执行事件
ele.addEventListener('click', function () {}, false)
ele.addEventListener('click', function () {}, false)
/** 操作
 */
//class
ele.className;
ele.classList;
ele.classList.add('');
ele.classList.remove('');
//style
ele.style;
ele.style.fontSize = '18px';
ele.style.backgroundColor = 'red';
//attribute
ele.attributes;
ele.getAttribute('')
ele.removeAttribute('')
ele.setAttribute('')

//创建标签 添加, position:只能是'beforeBegin'、 'afterBegin'、 'beforeEnd'、 'afterEnd'
var eleAdded = '<div class="c1">jfjfjjf</div>';
ele.insertAdjacentHTML('beforeEnd', eleAdded);

var tag = document.createElement('div');
tag.innerText = 'jfjfjjf';
ele.appendChild(tag);
ele.insertBefore(tag);
ele.insertAdjacentElement('afterBegin',tag);

//表单操作
var form = document.createElement('form');
form.submit();

//alert
alert('xxoo');
var res = confirm('ooxx'); //res 表示点了取消还是确定

//当前网址
location.href;
location.href = 'www.baidu.com' ; //跳转，重定向
location.reload(); //reload page

//定时器
var timer = setInterval(function () {

}, 5000);
clearInterval(timer);

//只执行一次
var timer2 = setTimeout(function () {

}, 1000);
clearTimeout(timer2);