/**
 * Created by traciarms on 7/30/16.
 */
// AJAX for posting
function post_api() {
    var csrftoken = $('[name=csrfmiddlewaretoken]').val();

    $.ajax({
        url: '/hit_api/',
        type: "POST", // http method
        data: {'csrfmiddlewaretoken': csrftoken},

        // handle a successful response
        success : function(data) {
            console.log('hit api was a success');
            var rows = $('table.data tr');
            rows.show();
            $("#header").html(data);
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log('post was not a success')
        }
    });
}


// handle button click
$('#api-form').submit(function( event) {
    event.preventDefault();
    post_api();

});

// AJAX for posting
function post_delete(row_id) {
    var csrftoken = $('[name=csrfmiddlewaretoken]').val();
    console.log('here in the post_delete method');
    $.ajax({
        url: "/delete_item/",
        data: {'row_id': row_id,
               'csrfmiddlewaretoken': csrftoken},
        type: "POST", // http method

        // handle a successful response
        success : function(json) {
            var table_row = $('#table-row-'+row_id);
            table_row.hide();
            console.log('delete was a success')
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log('post was not a success')
        }

    });
}

// handle delete link click
$('.delete_item').click(function(event){
    event.preventDefault();
    var row_id = $(this).attr('id');

    post_delete(row_id);

});