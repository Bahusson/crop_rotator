/* Funkcja ustawiająca język o podanej wartości.
Zasadniczo zmienia ciastko językowe klienta.
Jak będziesz miał czas to to skróć i zrób tak,
żeby nie trzeba się grzebać w kodzie,
jak się ustawi nowy język.*/

var domain = "plodozmian.agro.pl"
var domain2 = "www.plodozmian.agro.pl"
var domain3 = "127.0.0.1"

function setCookie(cvalue)
{
  document.cookie = "rotator_language = " + cvalue + ";domain=" + domain + ";path=/";
  document.cookie = "rotator_language = " + cvalue + ";domain=" + domain2 + ";path=/";
  document.cookie = "rotator_language = " + cvalue + ";domain=" + domain3 + ";path=/";
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

});
