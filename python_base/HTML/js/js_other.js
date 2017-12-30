/**
 * Created by jinxiaofei on 2017/12/25.
 */

/** 1、控制打印
 */
console.log('log string')

/** 2、定时器
 *
 *  setInterval(func, ms)
 */
function func(arg) {
    alert('javascript')
}
setInterval('alert(123)', 2000)
setInterval(func, 2000, 'arg')
