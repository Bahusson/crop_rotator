/* Funkcja ustawiająca język o podanej wartości.
Zasadniczo zmienia ciastko językowe klienta.
Jak będziesz miał czas to to skróć i zrób tak,
żeby nie trzeba się grzebać w kodzie,
jak się ustawi nowy język.*/

// var domain = "127.0.0.1" // Tu zmień domenę z localhost albo podepnij to jakoś lepiej.

function setCookie(cvalue)
{
  document.cookie = "esks_language = " + cvalue + ";domain=" + ";path=/";
  location.reload();
}

$(document).ready(function()
{
  $('#lang_flag_pl').click(function() // Ustaw Język Polski
 {
   setCookie("pl")
  });

  $('#lang_flag_en').click(function() // Ustaw Język Angielski
 {
    setCookie("en")
  });

  $('#lang_flag_de').click(function() // Ustaw Język Niemiecki
 {
   setCookie("de")
  });

  $('#lang_flag_fr').click(function() // Ustaw Język Francuski
 {
   setCookie("fr")
  });

  $('#lang_flag_ru').click(function() // Ustaw Język Rosyjski
 {
    setCookie("ru")
  });

  $('#lang_flag_uk').click(function() // Ustaw Język Ukraiński
 {
   setCookie("uk")
  });

  $('#lang_flag_es').click(function() // Ustaw Język Hiszpański
 {
    setCookie("es")
  });

  $('#lang_flag_hi').click(function() // Ustaw Język Hindi
 {
   setCookie("hi")
  });
});
