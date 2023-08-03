var item_sold_val = ""
var condition_text_val = ""
var exclude_location_text_val = ""
$(document).ready(function () {
    $(".item_location").select2()
    $(".item_condition").select2({
        tags: true,
        tokenSeparators: [',', ' ']
    })
    $(".exclude_location").select2({
        tags: true,
        tokenSeparators: [',', ' ']
    })
    $(".item_buy_format").select2
    console.log('done')
})

$('#btnNavbarSearch').on('click', function () {
    debugger
    if ($('#item_sold').is(':checked')) {
        item_sold_val = $('#item_sold').val()
    }
    $('#datatables').DataTable({
        ajax: {
            url: '/home',
            type: 'POST',
            data: {
                location: $('#location').val(),
                condition: $('#condition').val(),
                buy_format: $('#buy_format').val(),
                min: $('#min').val(),
                max: $('#max').val(),
                item_sold: item_sold_val,
                searchtext: $('#search_input').val(),
            },
            dataType: 'json',
        },
        "language": {
            'loadingRecords': '<img src="static/assets/img/loader.gif">'
        },
        // data:response.data,
        'columns': [
            { data: 'title' },
            { data: 'price' },
            {
                data: 'img', render: function (data) {
                    return '<img src="' + data + '" width="100" height="100">'
                }
            },
            { data: 'condition' },
            { data: 'location' },
        ],

        "bDestroy": true,
    })

})

$('#btn_submit_search').on('click', function () {
    debugger
    var buy_format_text = $('#buy_format :selected').text()
    var condition_text = $('#condition').select2('data')
    var exclude_location = $('#exclude_location').select2('data')
    console.log(exclude_location.text)
    exclude_location.forEach(element => {
        exclude_location_text_val = element.text
        console.log($.trim(exclude_location_text_val))
    })
    condition_text.forEach(element => {
        condition_text_val = element.text
        console.log(condition_text)
    });

    if ($('#item_sold').is(':checked')) {
        var item_sold_val = $('#item_sold').val()
    }
    $.ajax({
        type: 'POST',
        url: '/ebay_scrape_request_history',
        data: {
            location_url_val: $('#location').val(),
            location_text: exclude_location_text_val,
            exclude_location: $('#exclude_location').text(),
            condition_url_val: $('#condition').val(),
            condition_text: condition_text_val,
            buy_format_url_val: $('#buy_format').val(),
            buy_format: buy_format_text,
            min: $('#min').val(),
            max: $('#max').val(),
            item_sold: item_sold_val,
            searchtext: $('#search_input').val(),
        },
        dataType: 'json',
    })
})


