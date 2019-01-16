odoo.define('report_expenses_portal_user.register_expenses', function (require) {
    'use strict';

  require('web.dom_ready');
  var core = require('web.core');

  $('.select2_control').select2({

  });

});

$(function(){
  var name_desc = $('#name_desc'),
  project = $('#x_project_id'),
  product = $('#product_id'),
  date = $('#date'),
  unit_amount = $('#unit_amount'),
  quantity = $('#quantity'),
  reference = $('#reference'),
  voucher_file = $('#voucher_file');

  var total_amount = $('#total_amount');

  $('.partial_amount').change(function(){
    if( unit_amount.val() && quantity.val() && unit_amount.val() >= 0.1 &&  quantity.val() >= 0.1);
      $('#result_total').removeClass("hidden");
      total = unit_amount.val() * quantity.val();
      total = total.toFixed(2);
      total_amount.html(total);
  });

  var fileInput = $('#voucher_file');
  var maxSize = fileInput.data('max-size');

  $(document).on('change', fileInput, function(){
    var sendExpense = $('#btnSendExpense');
    if(fileInput.get(0).files.length){
        var fileSize = fileInput.get(0).files[0].size; // in bytes
        if(fileSize > maxSize){
            sendExpense.addClass("hidden");
            $('#result_custom').removeClass("hidden").html("<h3>This file is too long</h3>");
            $('#voucher_file').removeClass("my-success");
            $('#voucher_file').addClass("my-error");
            return false;
        }else{
            sendExpense.removeClass("hidden");
            $('#voucher_file').removeClass("my-error");
            $('#voucher_file').addClass("my-success");
            $('#result_custom').addClass("hidden");
        }
    }
  });

$('#btnSendExpense').click(function(event){
    event.preventDefault();

    if ($.trim(name_desc.val()) == "") {
      $(name_desc).removeClass("my-success").addClass("my-error");
      $('#errorName').html("Please fill this field");
    }else{
      $(name_desc).removeClass("my-error").addClass("my-success");
    }

    if ($.trim(product.val()) == "") {
      $(product).removeClass("my-success").addClass("my-error");
      $('#errorProduct').html("Please fill this field");
    }else{
      $(product).removeClass("my-error").addClass("my-success");
    }

    if ($.trim(date.val()) == "") {
      $(date).removeClass("my-success").addClass("my-error");
      $('#errorDate').html("Please fill this field");
    }else{
      $(date).removeClass("my-error").addClass("my-success");
    }

    if ($.trim(unit_amount.val()) == "" && unit_amount.val() <= 0.00) {
      $(unit_amount).removeClass("my-success").addClass("my-error");
      $('#errorUnitAmount').html("Please fill this field");
    }else{
      $(unit_amount).removeClass("my-error").addClass("my-success");
    }

    if ($.trim(quantity.val()) == "" && quantity.val() <= 0.00) {
      $(quantity).removeClass("my-success").addClass("my-error");
      $('#errorQuantity').html("Please fill this field");
    }else{
      $(quantity).removeClass("my-error").addClass("my-success");
    }

    name_req = $('#name_desc').hasClass("my-success");
    product_req = $('#product_id').hasClass("my-success");
    date_req = $('#date').hasClass("my-success");
    unit_amount_req = $('#unit_amount').hasClass("my-success");
    quantity_req = $('#quantity').hasClass("my-success");
    project_req = $('#project_id');

    if (name_req && product_req && date_req && unit_amount_req && quantity_req ){
      console.log("Todos los valores correctos");
      $('#formExpense').submit();
    }else{
      console.log("Valores vacios");
      //return false;
    }

  });

});
