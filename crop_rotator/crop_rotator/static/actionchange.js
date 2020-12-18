// Prosta funkcja przerzucająca wartość listy rozwijanej do ukrytego formularza.
function actionset()
{
  var x = document.getElementById("party_view").value;
  document.getElementById("view_filter").value = x;
}

$(document).ready(function()
{
  $('#send').click(function()
 {
  actionset()
  });
});
