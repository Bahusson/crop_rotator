// Prosta funkcja przerzucająca wartość listy rozwijanej do ukrytego formularza.
function genderset()
{
  var x = document.getElementById("Genderselector").value;
  document.getElementById("id_gender").value = x;
}

$(document).ready(function()
{
  $('#send').click(function()
 {
  genderset()
  });
});
