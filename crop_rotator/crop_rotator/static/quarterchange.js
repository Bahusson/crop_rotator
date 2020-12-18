// Prosta funkcja przerzucająca wartość listy rozwijanej do ukrytego formularza.
function quarterset()
{
  var x = document.getElementById("Quarterselector").value;
  document.getElementById("id_quarter").value = x;
}

$(document).ready(function()
{
  $('#send').click(function()
 {
  quarterset()
  });
});
