$(document).ready(function()
{
  $("button[name='add_element_button']").click(function(event)
 {
  var button_triger = $(event.target);
  var add_key = button_triger.attr('add_key');
  var add_element = button_triger.closest(".master0").find(".slave0").first().children().first().children("option:selected").attr('value');
  $("#add_key").val(add_key);
  $("#add_element").val(add_element);
  $('StepChangeForm').trigger('submit');
  });
});
