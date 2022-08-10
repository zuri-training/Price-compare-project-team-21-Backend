const product = document.getElementsByClassName('product')
const moreText = document.getElementsByClassName('moreText')
const point = document.getElementsByClassName("point")
const textButton = document.getElementsByClassName("textButton")

for (let i =0; i <textButton.length; i++){
    textButton[i].addEventListener("click", ()=>{

         if (point[i].style.display === "none" ){
            moreText[i].style.display = "none"
            point[i].style.display= "inline"
            textButton[i].innerHTML = "more"

         }else{
            moreText[i].style.display = "inline"
            point[i].style.display ="none"
            textButton[i].innerHTML  = "show less"
         }
    })
}

