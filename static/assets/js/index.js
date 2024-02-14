function load_count_dartil_day_sall() { 
    let data = {
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
    };
    $.ajax({
        url: "count_day_sall_dartil",
        type: "POST",
        data: data,
        success: function(response) {
            $('.load_count_dartil_day_sall').text(response.status)
        },
        error: function(jqXHR, textStatus, errorThrown) {
            // Handle errors appropriately
            console.log("خطا در دریافت اطلاعات");
        }
        });
};//end load_count_month_sall
function load_count_snappshop_day_sall() { 
    let data = {
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
    };
    $.ajax({
        url: "count_day_sall_snappshop",
        type: "POST",
        data: data,
        success: function(response) {
            $('.load_count_snappshop_day_sall').text(response.status)
        },
        error: function(jqXHR, textStatus, errorThrown) {
            // Handle errors appropriately
            console.log("خطا در دریافت اطلاعات");
        }
        });
};//end load_count_month_sall

function load_count_monthly_sales_snappshop() { 
    let data = {
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
    };
    $.ajax({
        url: "count_monthly_sales_snappshop",
        type: "POST",
        data: data,
        success: function(response) {
            $('.load_count_monthly_sales_snappshop').text(response.status)
        },
        error: function(jqXHR, textStatus, errorThrown) {
            // Handle errors appropriately
            console.log("خطا در دریافت اطلاعات");
        }
        });
};//end load_count_month_sall
function load_count_monthly_sales_dartil() { 
    let data = {
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
    };
    $.ajax({
        url: "count_monthly_sales_dartil",
        type: "POST",
        data: data,
        success: function(response) {
            $('.load_count_monthly_sales_dartil').text(response.status)
        },
        error: function(jqXHR, textStatus, errorThrown) {
            // Handle errors appropriately
            console.log("خطا در دریافت اطلاعات");
        }
        });
};//end load_count_month_sall

load_count_dartil_day_sall()
load_count_snappshop_day_sall()
load_count_monthly_sales_snappshop()
load_count_monthly_sales_dartil()