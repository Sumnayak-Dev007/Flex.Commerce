$(function() {
    // $('.increment_btn').on('click', function (e) {
    //     console.log("button clicked :D");
    //     e.preventDefault();
        
    //     // Find the closest product_val and decrement the qty-input value
    //     var inc_value = $(this).closest('.product_val').find('.qty_input').val();
    //     var value = parseInt(inc_value, 10);
        
    //     value = isNaN(value) ? 0 : value;  // Ensure value is a number
    //     if (value < 10) {  // Allow decrement until the value is 1
    //         value++;
    //         $(this).closest('.product_val').find('.qty_input').val(value);
    //     }
    // });
    

    // $('.decrement_btn').on('click', function (e) {
    //     console.log("button clicked :D");
    //     e.preventDefault();
        
    //     // Find the closest product_val and decrement the qty-input value
    //     var dec_value = $(this).closest('.product_val').find('.qty_input').val();
    //     var value = parseInt(dec_value, 10);
        
    //     value = isNaN(value) ? 0 : value;  // Ensure value is a number
    //     if (value > 1) {  // Allow decrement until the value is 1
    //         value--;
    //         $(this).closest('.product_val').find('.qty_input').val(value);
    //     }
    // });
    

    $('.addToCartBtn').on("click", function (e) {
        e.preventDefault();
    
        var product_id = $(this).closest('.prod_data').find('.prod_id').val();
        var product_qty = $(this).closest('.prod_data').find('.qty_input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
    
        if (product_id && product_qty) {
            $.ajax({
                type: "POST",
                url: "/add-to-cart/",
                data: {
                    'product_id': product_id,
                    'product_qty': product_qty,
                    csrfmiddlewaretoken: token
                },
                success: function (response) {
                    alertify.success(response.status);
                },
                error: function (error) {
                    console.error("Error adding to cart:", error);
                    alertify.error("Failed to add to cart");
                }
            });
        } else {
            alert("Invalid product data.");
        }
    });

    $('.changeQty').on("click", function (e) {
        e.preventDefault();
        console.log("Changing qantity")
        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var product_qty = $(this).closest('.product_data').find('.qty_input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
    
        if (product_id && product_qty) {
            $.ajax({
                type: "POST",
                url: "/update-cart/",
                data: {
                    'product_id': product_id,
                    'product_qty': product_qty,
                    csrfmiddlewaretoken: token
                },
                success: function (response) {
                    // alertify.success(response.status);
                },
                error: function (error) {
                    console.error("Error adding to cart:", error);
                    alertify.error("Failed to add to cart");
                }
            });
        } else {
            alert("Invalid product data.");
        }
    });

    
    $('.delete-cart-item').click(function (e) { 
        e.preventDefault();
        var product_id = $(this).closest('.del_prod').find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        console.log("Product ID:", product_id);
        $.ajax({
            type: "POST",
            url: "/delete-cart-item/",
            data: {
                'product_id': product_id,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                alertify.success(response.status);
                location.reload();
                
            }
        });
        
    });

    $('.addToWishlist').on("click", function (e) {
        e.preventDefault();
        console.log("Button clicked!");
        var product_id = $(this).closest('.addto').find('.prodid').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            type: "POST",
            url: "/add-to-wishlist/",
            data: {
                'product_id': product_id,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                alertify.success(response.status);
            },
            error: function (xhr, status, error) {
                console.error("Error: ", error);
            }
        });
    });
    
    $('.del-wish').on("click",(function (e) { 
        e.preventDefault();
        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        console.log("I am clicked :D")

        $.ajax({
            type: "POST",
            url: "/del-wish/",
            data: {
                'product_id':product_id,
                csrfmiddlewaretoken:token
            },
            success: function (response) {
                alertify.success(response.status)
                location.reload();
            }
        });
    }));
    
    jqck
});
