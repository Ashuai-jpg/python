let num = 0
const delay = 300
const start = Math.round(performance.now()) 


const countDownTMR = setInterval(()=>{
    num++
    if(num > 10) {
        const end = Math.round(performance.now()) 
        console.log(`Speed [map]: ${  end - start} miliseconds`)
        return clearInterval(countDownTMR)
    }
    console.log(num)
},delay)

