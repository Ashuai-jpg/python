let num = 0
const countDownTMR = setInterval(()=>{
    num++
    console.log(num)
    if(num > 10) return clearInterval(countDownTMR)
},300)