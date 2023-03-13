// console.log("hello word");
// let a = 10
// function outer(){
//     let b = 20
//     function inner(){
//         let c = 30
//         console.log(a, b, c);
//     }

//     inner()
// }

// outer()
// outer()

function outer() {
    let counter = 0
    function innter() {
        counter++
        console.log(counter)
    }
    innter()
}
outer()
outer()

// demo code for JavaScript Closure 
function outer() {
    let counter = 0
    function innter() {
        counter++
        console.log(counter)
    }
    return innter
}
let fn = outer()
fn()
fn()




// const h1  = document.querySelector('h1')
// const btn1 = document.getElementById('btn1')
// function test (){
//     let btn1Col = "red"
//     const changeCol = ()=>{
//         btn1Col = (btn1Col == "red") ? "green" : "red"
//         btn1.style.backgroundColor = btn1Col
//     }
//     return changeCol
// }

// let btn1Col = "red"
// function test (){
//     btn1Col = (btn1Col == "red") ? "green" : "red"
//     btn1.style.backgroundColor = btn1Col
//     console.log(btn1Col);
//  }

// btn1.addEventListener("click" ,test)

