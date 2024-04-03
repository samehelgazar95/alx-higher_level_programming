$(
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json',
    function (data, status) {
      $(data.results).each(function (index, ele) {
        li = $('<li></li>').append(ele.title);
        $('#list_movies').append(li);
      });
    })
);
