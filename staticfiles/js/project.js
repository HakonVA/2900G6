/* Project specific Javascript goes here. */

function append_url(new_url){

    var curr_page = window.location.href;
    
    var new_page = curr_page + new_url;

    window.location.assign(new_page);
    
}