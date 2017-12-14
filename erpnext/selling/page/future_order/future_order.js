frappe.pages['future-order'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent : wrapper,
		title : 'Pre Order List',
		single_column : true
	});
	
	page.main.append(frappe.render_template('future_order', {
		data : ""
	}));
	page.$sel_date = wrapper.page.add_field({
		fieldname : "sel_date",
		fieldtype : "Date",
		label : __("Date"),
		"default" : frappe.datetime.get_today()

	}).$input.change(function() {
		report();
	});

	report();
	function report() {
		sel_date = ""
		if (page.$sel_date.val() != "") {
			sel_date = page.$sel_date.val()
		}
		frappe
				.call({
					method : 'erpnext.selling.page.future_order.future_order.show_order_details',
					args : {
						sel_date : sel_date
					},
					callback : function(data) {
						$(".body_val").html("");
						page.main.append(frappe.render_template('future_order',
								{
									data : data['message']
								}));

					}

				});

	}

}