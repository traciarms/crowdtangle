/**
 * Created by traciarms on 7/30/16.
 */
// AJAX for posting
function post_api() {
    var url = $('form.api_form').attr('action');

    $.ajax({
        url: url,
        type: "POST", // http method

        // handle a successful response
        success : function(json) {
            console.log('post was a success')
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log('post was not a success')
        }
    });
}

// handle button click
$('#api_form').submit(function( event) {
    event.preventDefault();

    post_api();
});

// AJAX for posting
function post_delete(url) {
    console.log('here in the post_delete method');
    $.ajax({
        url: url,
        type: "POST", // http method

        // handle a successful response
        success : function(json) {
            console.log('post was a success')
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log('post was not a success')
        }

    });
}

// handle delete link click
$('.delete_item').click(function( event){
    event.preventDefault();
    console.log('here in the delete click');
    var url = $('.delete_item').attr('href');
    alert('the url is {}'.format(url));
    
    post_delete(url);

});