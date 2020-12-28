$(".search_select2").select2({
    placeholder: "Buscar",
    minimumInputLength: 3,
    ajax: {
        url: "/api/app_ids/",
        dataType: 'json',
        delay: 1000,
        data: function (term) {
            return {
                q: term['term'],
            };
        },
        processResults: function (data) {
            return {
                results: $.map(data['games'], function (obj) {
                    return {id: obj['appid'], text: obj['name']};
                })
            };
        },
    },
});

$("#currency-input").select2()

$(".search_select2").on('select2:select', function () {
    let app_id = $(this).select2('data')[0]['id']
    let currency = $('#currency-input option:selected').val()
    var posting = $.post('api/game/', {app_id: app_id, currency: currency});

    posting.done(function (data) {
        var get_detail = $.get('detail/'+data['id'])

        get_detail.done(function (data){
            $('div#result').append(data)
        })

        $('.search_select2').find('option').remove()
    });
});
