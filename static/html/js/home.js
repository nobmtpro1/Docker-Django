var urlRequestCart = $("#js-data").data("urlrequestcart");
var debounce = null;

function requestCart() {
    clearInterval(debounce);
    debounce = setTimeout(() => {
        var formData = new FormData();

        formData.append(
            "csrfmiddlewaretoken",
            $('[name="csrfmiddlewaretoken"]').val() || ""
        );

        var cart = [];
        $(".js-quantity").each(function (i) {
            var item = {};
            item.id = $(this).data("id");
            item.quantity = $(this).val();
            cart.push(item);
        });

        formData.append("cart", cart || []);

        $.ajax({
            url: urlRequestCart,
            data: formData,
            processData: false,
            contentType: false,
            type: "POST",
            success: function (data) {
                console.log(data);
            },
            error: function (data, textStatus, jqXHR) {
                var errors = data.responseJSON.errors;
                console.log(errors);
            },
        });
    }, 300);
}

$(document).on("click", ".js-plusQuantity", function () {
    var input = $(this).parent().find(".js-quantity");
    input.val(parseInt(input.val()) + 1);
    requestCart();
});

$(document).on("click", ".js-minusQuantity", function () {
    var input = $(this).parent().find(".js-quantity");
    if (parseInt(input.val()) > 0) {
        input.val(parseInt(input.val()) - 1);
    }
    requestCart();
});

$(document).on("input", ".js-quantity", function (e) {
    if (parseInt($(this).val()) < 0) {
        $(this).val(0);
    } else {
        $(this).val(parseInt($(this).val()) || 0);
    }
    requestCart();
});
