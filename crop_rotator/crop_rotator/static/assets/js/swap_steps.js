// Prosta funkcja przerzucająca wartość listy rozwijanej do ukrytego formularza.
function hidden_input_value_set()
{
  var x = document.getElementById("Genderselector").value;
  document.getElementById("id_gender").value = x;
}

$(document).ready(function()
{
  $("button[name='move_plan']").click(function()
 {
  var button_triger2 = $(event.target);
  var closest = button_triger2.closest(".p").nextAll(".selection").first().filter(":selected"); // .selected()?
  hidden_input_value_set(closest)
  });
});
