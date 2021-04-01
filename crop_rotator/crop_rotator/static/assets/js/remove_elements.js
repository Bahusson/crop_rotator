$(document).ready(function()
{
  $("button[name='remove_element_button']").click(function(event)
 {
  var button_triger = $(event.target);
  var remove_key = button_triger.attr('remove_key');
  var remove_element = button_triger.attr('remove_element');
  $("#remove_key").val(remove_key);
  $("#remove_element").val(remove_element);
  $('StepChangeForm').trigger('submit');
  });
});
