$(document).ready(function () {
    console.log('done')
    $('#datatables').DataTable({
        ajax: {
            url: '/get_ebay_request_history',
            dataSrc: ''
        },
        columns: [
            { data: 'request_name' },
            { data: 'location_text_name' },
            { data: 'exclude_location' },
            { data: 'condition_text_name' },
            { data: 'buy_format_text_name' },
            { data: 'min_price' },
            { data: 'max_price' },
            { data: 'sold_item' },
        ]
    });
})