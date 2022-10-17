
let captionsList = document.querySelectorAll('.caption-item');
let unitsList = document.querySelectorAll('.unit');

captionsList.forEach(function (item, index) {
  item.addEventListener('mouseover', function () {
     unitsList[index].classList.add('hovered');
  });
  
  item.addEventListener('mouseout', function () {
     unitsList[index].classList.remove('hovered');
  });
});


$('.report-add__work-plus').click(function(e){

   e.preventDefault();

   // $(".report-add__work-wrapper").children('.report-add__work-item').clone().append("<a class='remove-append' href='#'>Удалить</a>").appendTo(".report-add__work-clone");
   $(".report-add__work-wrapper").children('.report-add__work-item').clone().appendTo(".report-add__work-clone");


   // $(".report-add__work-wrapper").children('.report-add__work-item').clone().appendTo(".report-add__work-clone");
   

   var summ = 0;
   $('.work-time').each(function(){
      
      summ += parseFloat($(this).val());
      $('.sub_total').val(summ);


  });
})




$(".report-add__work-clone").on("click", function(event){


      var t =$(this).children('.report-add__work-item').children('.remove-append').text()

      console.log(t)

   
});

$('.remove-append').on('click', function(e){
   e.preventDefault();
   $(this).parent('.report-add__work-item').remove()



})


$('.report-add__rek-plus').click(function(e){

   e.preventDefault();

   
   $(".report-add__rek-wrapper").children('.report-add__rek-item').clone().appendTo(".report-add__rek-clone");



})


$('.report-add__file-plus').click(function(e){

   e.preventDefault();

   
   $(".report-add__file-wrapper").children('.report-add__file-item').clone().appendTo(".report-add__file-clone");

})



jQuery(".work-time").keyup(function () {

   var summ = 0;
   $('.work-time').each(function(){
      
      summ += parseFloat($(this).val());
      $('.sub_total').val(summ);


  });
})


$('.report-add__work-summ').click(function(e){

   e.preventDefault();

   
   
   var summ = 0;
   $('.work-time').each(function(){
      
      summ += parseFloat($(this).val());
      $('.sub_total').val(summ);


  });
})


function Print(){
   $(".tableToPrint td, .tableToPrint th").each(function(){ $(this).css("width",  $(this).width() + "px")  });
   $(".tableToPrint tr").wrap("<div class='avoidBreak'></div>");
   window.print();
}