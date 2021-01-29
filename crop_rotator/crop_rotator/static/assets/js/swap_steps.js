$(document).ready(function()
{
  $("button[name='move_plan']").click(function(event)
 {
  var button_triger = $(event.target);
  var sender_id = button_triger.attr('value');
  var receiver_order = button_triger.closest("p").nextAll(".selectables").first().children("option:selected").attr('value')
  var receiver_id = button_triger.closest("p").nextAll(".selectables").first().children("option:selected").attr('name')
  $("#id_sender_step").val(sender_id);
  $("#id_receiver_step").val(receiver_id);
  $("#id_receiver_step_order").val(receiver_order);
  $('#SwitchStepsForm').trigger('submit');
  });
});
