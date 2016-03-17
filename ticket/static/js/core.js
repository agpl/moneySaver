/**
 * Created by Adam Gontarek on 2016-03-11.
 */

$(document).ready(function () {
    $(document).on('change', '.cost, .itemsNumber', function(){
        var parent = $(this).parents('tr'),
            cost = parseFloat(parent.find('.cost').val()),
            number = parseFloat(parent.find('.itemsNumber').val()),
            singleCost = parseFloat(cost/number);

        parent.find('.singleCost').val(singleCost.toFixed(2));

    });
})