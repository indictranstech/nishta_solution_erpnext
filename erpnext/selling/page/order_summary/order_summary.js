frappe.pages['order-summary'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent : wrapper,
		title : 'Order Summary',
		single_column : true
	});
	page.main.append(frappe.render_template('order_summary', {
		data : ""
	}));
	page.$sel_date = wrapper.page.add_field({
		fieldname : "sel_date",
		fieldtype : "Date",
		label : __("Date"),
		"default": frappe.datetime.get_today()
	}).$input.change(function() {
		print_order();
	});

	print_order();
	function print_order() {
		sel_date = ""
		if (page.$sel_date.val()!="") {
			sel_date = page.$sel_date.val()
		}
		//alert(sel_date)
		frappe
				.call({
					method : 'erpnext.selling.page.order_summary.order_summary.print_order',
					args : {
						sel_date:sel_date	
					},
					callback : function(data) {
						$(".page_div").html("");
						page.main.append(frappe.render_template(
								'order_summary', {
									data : data['message']
								}));
					}

				});

	}

}
