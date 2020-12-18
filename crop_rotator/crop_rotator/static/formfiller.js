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
