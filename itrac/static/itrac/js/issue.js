$(function () {
    // SHow the "click to view" icon when mouse over the item-name
    function mouseOverListItem(event) {
        const target = $(event.target);
        target.children(':nth-child(2)').css('display', 'inline');
    }
  
    // Hide the "click to view" icon when mouse leaves the item-name
    function mouseLeaveListItem(event) {
        const target = $(event.target);
        target.children(':nth-child(2)').css('display', 'none');
    }
  
    const issue_details_ajax = (url) => {
        $.ajax({
            url: url,
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#issue-details").html("Loading...")
            },
            success: function (data) {
                $("#issue-details").html(data.html_issue_detail);
                
                //set up the event istener
                $(".js-collapse-toggle").click(function () {
                    console.log("toggle")
                    $(this).find('i').toggleClass('fa-minus-circle fa-plus-circle');
                });
  
                // default to expand
                $(".js-collapse-details").collapse();
            }
        });
    };
  
    const loadIssueDetailPartial = function () {
        url = $(this).attr("data-url");
        issue_details_ajax(url);
    };  
    $(".js_issue_item_title").click(loadIssueDetailPartial);
  
    $('#search-results-list ul li').hover(function(){
         $(this).css('background-color', 'lightblue');
    });
    $('#search-results-list ul li').mouseleave(function(){
         $(this).css('background-color', '');
    });
    $('#search-results-list ul li a').click(function(){
        $('#search-results-list ul li a').css('color', 'black');
        $(this).css('color', 'blue');
    });
  
    $(".js-collapse-toggle").click(function () {
        $(this).find('i').toggleClass('fa-minus-circle fa-plus-circle');
    });
});