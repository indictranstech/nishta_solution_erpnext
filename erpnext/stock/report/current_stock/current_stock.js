// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors and contributors
// For license information, please see license.txt













function call_warehouse()
{
	
var Current_User = user;
	
frappe.call({
	method : "erpnext.stock.report.current_stock.current_stock.show_current_stock",
	args : {
		
		"user" : user,
	},
	callback : function(data) {
		
             //  var pass_warehouse=data.message;
               
                //frm.doc.Warehouse = pass_warehouse;
				//cur_frm.refresh_field("Warehouse");
              // alert(pass_warehouse)
		       //return  pass_warehouse;
		 
	}
	
});
	
	
}


frappe.query_reports["Current Stock"] = {
	"filters": [
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"width": "80",
			"reqd": 1,
			"default": frappe.sys_defaults.year_start_date,
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"width": "80",
			"reqd": 1,
			"default": frappe.datetime.get_today()
		},
		{
			"fieldname": "item_group",
			"label": __("Item Group"),
			"fieldtype": "Link",
			"width": "80",
			"options": "Item Group"
		},
		{
			"fieldname": "item_code",
			"label": __("Item"),
			"fieldtype": "Link",
			"width": "80",
			"options": "Item"
		},
		{
			"fieldname": "warehouse",
			"label": __("Warehouse"),
			"fieldtype": "Link",
			"width": "80",
			"options": "Warehouse"
			//"default": call_warehouse()
		},
	]
}
