// Prosta funkcja przerzucająca wartość listy rozwijanej do ukrytego formularza.
/*function hidden_input_value_set()
{
  var x = document.getElementById("Genderselector").value;
  document.getElementById("id_gender").value = x;
}

function hidden_input_name_set()
{
  var x = document.getElementById("Genderselector").name;
  document.getElementById("id_gender").name = x;
}*/

$(document).ready(function()
{
  $("button[name='move_plan']").click(function(event)
 {
//  console.log(event);
  var button_triger = $(event.target);
  var sender_id = button_triger.attr('value');
  var closest = button_triger.closest("p").nextAll(".selectables").first().attr('value') //.filter(":selected").attr('value');
  //var closest = button_triger.closest(".select").nextAll().first().filter(":selected").attr('value');
  alert(closest);
  //hidden_input_value_set(closest)
  });
});
