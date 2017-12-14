frappe.pages['pre-order-graph'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent : wrapper,
		title : 'Today Delivery Orders/Spot Orders',
		single_column : true
	});
//	page.main.append(frappe.render_template('pre_order_graph', {
//		data : ""
//	}));
	report();
	function report() {
		frappe
				.call({
					method : 'erpnext.selling.page.pre_order_graph.pre_order_graph.show_order_details',
					callback : function(data) {
						$(".body_val").html("");
						page.main.append(frappe.render_template(
								'pre_order_graph', {
									data : data['message']
								}));

					}

				});

	}
	
	

}
//future-order