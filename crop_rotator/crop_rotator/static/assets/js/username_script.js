$(document).ready(function()
{
  $("#send").click(function(event)
 {
  var button_triger = $(event.target);
  var username = button_triger.val();
  $("#id_username").val(username);
  });
});
