// const product = document.getElementsByClassName('product')
// const moreText = document.getElementsByClassName('moreText')
// const point = document.getElementsByClassName("point")
// const textButton = document.getElementsByClassName("textButton")

// for (let i = 0; i < textButton.length; i++) {
//    textButton[i].addEventListener("click", () => {

//       if (point[i].style.display === "none") {
//          moreText[i].style.display = "none"
//          point[i].style.display = "inline"
//          textButton[i].innerHTML = "more"

//       } else {
//          moreText[i].style.display = "inline"
//          point[i].style.display = "none"
//          textButton[i].innerHTML = "show less"
//       }
//    })
// }


$(document).ready(function(){
    var maxLength = 50;
    $(".show-read-more").each(function(){
        var myStr = $(this).text();
        if($.trim(myStr).length > maxLength){
            var newStr = myStr.substring(0, maxLength);
            var removedStr = myStr.substring(maxLength, $.trim(myStr).length);
            $(this).empty().html(newStr);
            $(this).append(' ...');
            // $(this).append('<span class="more-text">' + removedStr + '</span>');
        }
    });
    
   //  $(".read-more").click(function(){
   //       $(".show-read-more").append(' <a href="javascript:void(0);" class="read-less">read less...</a>');
   //      $(this).siblings(".more-text").contents().unwrap();
   //      $(this).remove();
        
   //  });

   //  $(".read-less").click(function(){
   //    $(".show-read-more").
   // });
});


var ratings = null;
function setRatingVar(elem){
   ratings = document.querySelector(`#${elem.parentElement.getAttribute('id')}`);
   ratings.querySelectorAll('.fa').forEach(rate => {
      rate.addEventListener('click', function () {
         ratings.querySelector('input.rating-value').value = this.getAttribute('data-rating');
         return SetRatingStar();
      });
   });
}

var SetRatingStar = function () {
   if(ratings.length > 0){
      return ratings.forEach(rating => {
         return rating.querySelectorAll('.fa').forEach(rate => {
            if (parseInt(rating.querySelector('input.rating-value').value) >= parseInt(rate.getAttribute('data-rating'))) {
               rate.classList.remove('fa-star-o');
               return rate.classList.add('fa-star');
            } else {
               rate.classList.remove('fa-star');
               return rate.classList.add('fa-star-o');
            }
         });
      });
   }else{
      return ratings.querySelectorAll('.fa').forEach(rate => {
         if (parseInt(ratings.querySelector('input.rating-value').value) >= parseInt(rate.getAttribute('data-rating'))) {
            rate.classList.remove('fa-star-o');
            return rate.classList.add('fa-star');
         } else {
            rate.classList.remove('fa-star');
            return rate.classList.add('fa-star-o');
         }
      });
   }
};

   


document.addEventListener("DOMContentLoaded", function (e) {
   
   ratings = document.querySelectorAll('.rating');   
   SetRatingStar();
});

