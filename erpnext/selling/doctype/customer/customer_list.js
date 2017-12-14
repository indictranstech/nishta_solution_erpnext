frappe.listview_settings['Customer'] = {
	add_fields: ["customer_name", "territory", "customer_group", "customer_type", "image"],
	
	
	
		
	
	
	
	
	
	
};

frappe.ui.form.on("Customer", "refresh", function(frm){
	alert("ok");
    frm.add_custom_button("Link", function(){
			var myWin = window.open('https://google.com');
	});
});

