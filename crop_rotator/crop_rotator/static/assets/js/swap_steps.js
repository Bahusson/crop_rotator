// Prosta funkcja przerzucająca wartość listy rozwijanej do ukrytego formularza.
function hidden_input_value_set()
{
  var x = document.getElementById("Genderselector").value;
  document.getElementById("id_gender").value = x;
}

function hidden_input_name_set()
{
  var x = document.getElementById("Genderselector").name;
  document.getElementById("id_gender").name = x;
}

$(document).ready(function()
{
  $("button[name='move_plan']").click(function()
 {
  var button_triger2 = $(event.target);
  var closest = button_triger2.closest(".p").nextAll("select[name='step_selection']").first().filter(":selected"); // .selected()?
  hidden_input_value_set(closest)
  });
});
