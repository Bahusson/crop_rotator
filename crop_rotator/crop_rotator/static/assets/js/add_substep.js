$(document).ready(function()
{
  $("button[name='add_substep_button']").click(function(event)
 {
  var button_triger = $(event.target);
  var remove_key = button_triger.attr('inter_key');
  $("#inter_key").val(remove_key);
  $('StepChangeForm').trigger('submit');
  });
});
