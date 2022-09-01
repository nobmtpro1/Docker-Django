var urlRequestCart = $("#js-data").data("urlrequestcart");
var urlCheckout = $("#js-data").data("urlcheckout");
var urlCheckOrderStatus = $("#js-data").data("urlcheckorderstatus");
var urlCheckOrderStatusSuccess = $("#js-data").data(
    "urlcheckorderstatussuccess"
);
var debounce = null;

function numberWithDots(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
}

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

        formData.append("cart", JSON.stringify(cart));

        $.ajax({
            url: urlRequestCart,
            data: formData,
            processData: false,
            contentType: false,
            type: "POST",
            success: function (data) {
                console.log(data);
                data?.cart?.items.forEach((item) => {
                    $(`.js-quantity[data-id="${item?.id}"]`).val(
                        item?.quantity
                    );
                });
                $(".js-totalQuantity").html(data?.cart?.totalQuantity);
                $(".js-total").html(numberWithDots(data?.cart?.total));
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

$(document).on("click", ".js-checkout", function (e) {
    var formData = new FormData();

    formData.append(
        "csrfmiddlewaretoken",
        $('[name="csrfmiddlewaretoken"]').val() || ""
    );

    formData.append("name", $('[name="name"]').val() || "");
    formData.append("email", $('[name="email"]').val() || "");
    formData.append("phone", $('[name="phone"]').val() || "");

    var cart = [];
    $(".js-quantity").each(function (i) {
        var item = {};
        item.id = $(this).data("id");
        item.quantity = $(this).val();
        cart.push(item);
    });

    formData.append("cart", JSON.stringify(cart));

    $.ajax({
        url: urlCheckout,
        data: formData,
        processData: false,
        contentType: false,
        type: "POST",
        success: function (data) {
            console.log(data);
            $(".js-popupName").html(data?.order[0]?.fields?.name);
            $(".js-popupPhone").html(data?.order[0]?.fields?.phone);
            $(".js-popupEmail").html(data?.order[0]?.fields?.email);
            $(".js-popupTotal").html(numberWithDots(data?.cart?.total));
            $(".js-popupOrderCode").html("TICKET" + data?.order[0]?.pk);

            var html = `<tr>
                            <td>Đơn hàng</td>
                            <td></td>
                            <td></td>
                        </tr>`;
            data?.cart?.items.forEach((item) => {
                ticket = JSON.parse(item.data)[0];
                html += `
                        <tr>
                            <td>${ticket?.fields?.name}</td>
                            <td>${item?.quantity} vé</td>
                            <td>${numberWithDots(
                                ticket?.fields?.price
                            )} VNĐ</td>
                        </tr>
                `;
            });

            html += `<tr>
                        <td>Tổng cộng</td>
                        <td></td>
                        <td>${numberWithDots(data?.cart?.total)} VNĐ</td>
                    </tr>`;

            $(".js-popupTable").html(html);

            $(".js-popupPayment").addClass("active");
            checkOrderStatus(data?.order[0]);
        },
        error: function (data, textStatus, jqXHR) {
            var errors = data.responseJSON.errors;
            console.log(errors);
            var message = "";

            for (const property in errors) {
                message += errors[property][0] + "\r\n";
            }

            alert(message);
        },
    });
});

function checkOrderStatus(order) {
    setInterval(() => {
        var formData = new FormData();

        formData.append(
            "csrfmiddlewaretoken",
            $('[name="csrfmiddlewaretoken"]').val() || ""
        );
        formData.append("orderId", order?.pk);

        $.ajax({
            url: urlCheckOrderStatus,
            data: formData,
            processData: false,
            contentType: false,
            type: "POST",
            success: function (data) {
                console.log(data);
                window.location.href =
                    urlCheckOrderStatusSuccess +
                    `?name=${order?.fields?.name}&phone=${order?.fields?.phone}&email=${order?.fields?.email}`;
            },
            error: function (data, textStatus, jqXHR) {
                var errors = data.responseJSON.errors;
                console.log(errors);
            },
        });
    }, 3000);
}

$(document).on("click", ".js-popupCancel", function (e) {
    $(".js-popupPayment").removeClass("active");
});
