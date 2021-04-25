$(document).ready(function()
{
  $("button[name='remove_element_button']").click(function(event)
 {
  var button_triger = $(event.target);
  var remove_key = button_triger.attr('remove_key');
  var remove_element = button_triger.attr('remove_element');
  $("#inter_key").val(remove_key);
  $("#inter_element").val(remove_element);
  $('StepChangeForm').trigger('submit');
  });
});
