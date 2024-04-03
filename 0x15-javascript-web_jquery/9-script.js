$('document').ready(
  $.get(
    'https://hellosalut.stefanbohacek.dev/?lang=fr&format=json',
    function (data, status) {
      $('#hello').append(data.hello);
    })
);
