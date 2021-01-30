// Te dwie poniższe funkcje razem powodują, że guziki "zamieniają się miejscami"
function toggleshort(name, value)
{
 var x = document.getElementsByName(name)[value];
 if (x.style.display === 'none') {
    x.style.display = 'block';
 }
 else {
    x.style.display = 'none';
}
}

function toggleshort2(name, value)
{
 var x = document.getElementsByName(name)[value].style;
 if (x.display == 'none' || x.display == '') {
    x.display = 'block';
 }
 else {
    x.display = 'none';
}
}


$(document).ready(function()
{
 $("button[name='safety_valve']").click(function() // Udostępnij przycisk usunięcia
  {
    var value = $(event.target).val();
    toggleshort2("ButtonHiddenDiv", value);
    toggleshort("safety_valve", value);

});

$("button[name='dont_delete']").click(function() // Udostępnij przycisk usunięcia
 {
   var value = $(event.target).val();
   toggleshort2("ButtonHiddenDiv", value);
   toggleshort("safety_valve", value);
});

$("button[name='safety_valve_event']").click(function() // Udostępnij przycisk usunięcia
 {
   var value = $(event.target).val();
   toggleshort2("EventButtonHiddenDiv", value);
   toggleshort("safety_valve_event", value);
});

$("button[name='dont_delete_event']").click(function() // Udostępnij przycisk usunięcia
 {
   var value = $(event.target).val();
   toggleshort2("EventButtonHiddenDiv", value);
   toggleshort("safety_valve_event", value);
});
});
