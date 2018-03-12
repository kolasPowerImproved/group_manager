// ==UserScript==
// @name cisco_auto
// @namespace work
// @match *://*/*
// @grant none
// ==/UserScript==
(function ($) {

    $(".submit-row").append($(document.createElement('button'))

        .addClass('cisco-btn')

        .text('Cisco Disco'));

    var arr = [
        {val: 1, text: 'Cisco'},
        {val: 2, text: 'Edge-Core'},
        {val: 3, text: 'Alcatel'},
        {val: 4, text: 'Dell'},
        {val: 5, text: 'OLT'},
        {val: 6, text: 'Extreme'}
    ];

    $(".submit-row").append($(document.createElement('select'))

        .addClass('comm-selector'));
    $(arr).each(function () {
        $('.comm-selector').append($("<option>").attr('value', this.val).text(this.text));
    });


    $(".submit-row").append($(document.createElement('input'))

        .addClass('cisco-input')

        .val(''));

    $('.cisco-btn').click(function (e) {

        e.preventDefault();
        var comm_selector_value = $('.comm-selector').val()

        if (comm_selector_value === '1')
            $("#id_login").val('Catalyst_')
        else if (comm_selector_value === '2')
            $("#id_login").val('EC_')
        else if (comm_selector_value === '3')
            $("#id_login").val('OmniSwitch_')
        else if (comm_selector_value === '4')
            $("#id_login").val('Dpc_')
        else if (comm_selector_value === '5')
            $("#id_login").val('GP_')
        else if (comm_selector_value === '6')
            $("#id_login").val('Xtreme_');

        $('#id_requester').val(11);


        javascript:DateTimeShortcuts.handleCalendarQuickLink(0, 0);

        javascript:DateTimeShortcuts.handleCalendarQuickLink(1, 0);

        javascript:DateTimeShortcuts.handleClockQuicklink(0, new Date().strftime('%H:%M:%S'));

        if (comm_selector_value === '5')
            $('#id_group').val(38);
        else
            $('#id_group').val(15);

        $('#id_do_not_block').attr('checked', true);

        var id_building = $('#id_building').val()

        if ($('.cisco-input').val() === '11') {
            $('#id_building').val(1726)
        }
        else if ($('.cisco-input').val() === '12')
            $('#id_building').val(3426)
        else if ($('.cisco-input').val() === '14')
            $('#id_building').val(4071)
        else if ($('.cisco-input').val() === '3')
            $('#id_building').val(1711)
        else if ($('.cisco-input').val() === '4')
            $('#id_building').val(1727)
        else if ($('.cisco-input').val() === '5')
            $('#id_building').val(1734)
        else if ($('.cisco-input').val() === '6')
            $('#id_building').val(1724)
        else if ($('.cisco-input').val() === '617')
            $('#id_building').val(3669)
        else if ($('.cisco-input').val() === '7')
            $('#id_building').val(1774)
        else if ($('.cisco-input').val() === '8')
            $('#id_building').val(1763)
        else if ($('.cisco-input').val() === '22')
            $('#id_building').val(4875)
        else if ($('.cisco-input').val() === '23')
            $('#id_building').val(7526)

        location.reload();
        javascript:pick_ip_first();

    })

})(django.jQuery)