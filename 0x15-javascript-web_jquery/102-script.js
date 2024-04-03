$('document').ready(
  function () {
    function fetchData () {
      $.get(
        'https://www.fourtonfish.com/hellosalut/hello/',
        $.param({
          lang: $('#language_code').val()
        }),
        function (data, status) {
          $('#hello').html(data.hello);
        }
      );
    }

    $('#btn_translate').click(function () {
      fetchData();
    });

    $('#language_code').on('keypress', function (e) {
      if (e.which == 13) {
        e.preventDefault();
        fetchData();
      }
    });
  });
