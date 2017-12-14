frappe.pages['current-stock'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Current Stock',
		single_column: true
	});
	
	
	page.main.append(frappe.render_template('current_stock', {
		data : ""
	}));
	var Current_User = user;
	
	frappe.call({
		method : "erpnext.stock.page.current_stock.current_stock.show_current_stock",
		args : {
			
			"user" : user,
		},
		callback : function(data) {
			
                    $(".body_val").html("");
                    page.main.append(frappe.render_template('current_stock', {
                    	data: stock_data
                       
                    }));
                   
		}
		
	});
	
	
	
	
}