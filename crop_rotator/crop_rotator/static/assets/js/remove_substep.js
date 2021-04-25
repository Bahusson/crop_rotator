$(document).ready(function()
{
  $("button[name='remove_substep_button']").click(function(event)
 {
  var button_triger = $(event.target);
  var remove_key = button_triger.attr('substep_id');
  $("#inter_key").val(remove_key);
  $('StepChangeForm').trigger('submit');
  });
});
