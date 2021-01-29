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
  var receiver_order = button_triger.closest("p").nextAll(".selectables").first().children("option:selected").attr('value')
  var receiver_id = button_triger.closest("p").nextAll(".selectables").first().children("option:selected").attr('name')
  alert(receiver_id);
  //hidden_input_value_set(closest)
  });
});
