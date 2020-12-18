// Prosta funkcja przerzucająca wartość listy rozwijanej do ukrytego formularza.
function actionset(appname, filtername)
{
  var x = document.getElementById(appname).value;
  document.getElementById(filtername).value = x;
}

$(document).ready(function()
{
  $('#send').click(function()
 {
  actionset("app_view0", "view_filter0")
  actionset("app_view1", "view_filter1")
  actionset("app_view2", "view_filter2")
  });
});
