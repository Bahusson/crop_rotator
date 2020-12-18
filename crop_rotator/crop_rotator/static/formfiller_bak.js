// Prosta funkcja przerzucająca wartość listy rozwijanej do ukrytego formularza.
function formfill(elname, elid)
{
  var x = document.getElementById(elname).value;
  document.getElementById(elid).value = x;
}


function formcheckfill(elname, elid)
{
  if (document.getElementById(elname).checked === false) {
    x = "0" ;}
  else {
    x = "1" ;}
  document.getElementById(elid).value = x;
}

$(document).ready(function()
{
  $('#send').click(function()
 {
  formfill("sh_choice1", "id_sh_choice1")
  formfill("sh_choice2", "id_sh_choice2")
  formfill("sh_choice3", "id_sh_choice3")
  formfill("if_room_change", "id_if_room_change")
  formfill("duration", "id_duration")
  formfill("faculty", "id_faculty")
  formfill("degree", "id_degree")
  formfill("semester", "id_semester")
  formfill("spouse_cohabitant", "id_spouse_cohabitant")
  formfill("special_case_docs", "id_special_case_docs")
  formfill("international_placement", "id_international_placement")
  formcheckfill("mailinglist", "id_mailinglist")
  formcheckfill("dataprocessing", "id_dataprocessing")
  });
});
