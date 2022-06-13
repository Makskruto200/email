$(function() {
    
 
    $("#text").text(localStorage.getItem("op"))
    $("body").css("background", localStorage.getItem("fon"))
    $("body").css("backgroundSize","cover")
        
       
    
    $("#fon").click(function() {
    
        $("#submenu").slideToggle(500);
    });
    

$(".mun").click(function() {
        localStorage.setItem("fon",$(this).css("background"));
        $("body").css("background",$(this).css("background"))
        $("body").css("backgroundSize","cover")
        
      
        
    });
    $("#_").click(function() {
        
        $("#text_input").slideToggle(500);
    });
    
    
 });
    input=document.getElementById("text_input")
    input.oninput = function() {
        localStorage.setItem("op",input.value);
       $(function() {$("#text").text(input.value)})
  };
