/* Javascript for FirstXBlock. */


function SaveIsRead(runtime, element) {

    function updateCount(result) {
        $('.is_read', element).text('('+result.is_read+')');
    }

    var handlerUrl = runtime.handlerUrl(element, 'save_skip_text');

    $('p', element).click(function(eventObject) {
        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify({"is_read": "True"}),
            success: updateCount
        });
    });

    $(function ($) {
        /* Here's where you'd do things on page load. */
    });
}

