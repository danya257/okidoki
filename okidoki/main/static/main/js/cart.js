    $(document).ready(function() {
        $('.add-to-cart-form').on('submit', function(event) {
            event.preventDefault();
            var url = $(this).data('url');
            $.ajax({
              url: url,
              type: 'POST',
              data: $(this).serialize(),
              success: function(response) {
                alert(response.message);
                console.log(url);
              }
            });
          });
        });
