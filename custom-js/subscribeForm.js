$(function() {
  $('.form-control').focus(formFocus);
});

function formFocus() {
  $('#alert-field')
    .removeClass()
    .addClass('hidden');
}

function sendEmail(e) {
  e.preventDefault();

  const POST_URL = 'https://script.google.com/macros/s/AKfycbz-i5wjmsJ-mcaEDs-pSoJRR72fFFbyLLdesOYYx97vQZK0Pn6hvEm91A/exec';

  const postRequest = {
    name: e.target['name-field'].value,
    email: e.target['email-field'].value,
	page: e.target['page-field'].value
  };
  
  if(POST_URL) {
    $.post(POST_URL, JSON.stringify(postRequest))
      .then(res => {
      
        e.target.reset();
        $('#alert-field')
          .removeClass()
          .addClass(`alert alert-${res.code}`)
          .text(res.msg);
      });

    $('#alert-field')
      .removeClass()
      .html('<progress></progress>')
      .removeClass('hidden');
  } else {
    alert('Something went wrong!');
    // alert('You must set the POST_URL variable with your script ID');
  }

}

function changeSubject(e) {
  if(e.target.value === 'Other') {

    $('#subject-select').removeClass('col-xs-12')
      .addClass('col-xs-6');
    $('#hidden-other-subject').removeClass('hidden');
  } else {
    $('#subject-select').removeClass('col-xs-6')
      .addClass('col-xs-12');

    $('#hidden-other-subject').addClass('hidden');
  }
}