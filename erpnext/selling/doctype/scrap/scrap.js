// Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Scrap', {
	refresh : function(frm) {

		var Current_User = user;
		frappe.call({
			"method" : "erpnext.selling.doctype.scrap.scrap.day_remove",
			args : {
				doctype : "Scrap",
				"user" : user,

			},
			callback : function(data) {

				frm.doc.warehouse = data.message;
				cur_frm.refresh_field("warehouse");
			}
		})

	},

	item : function(frm) {
		var item = frm.doc.item;
		var warehouse = frm.doc.warehouse;
		frappe.call({
			"method" : "erpnext.selling.doctype.scrap.scrap.stock",
			args : {
				doctype : "Scrap",
				"item" : item,
				"warehouse" : warehouse,

			},
			callback : function(data) {
alert(data.message);
				//frm.doc.warehouse = data.message;
				//cur_frm.refresh_field("warehouse");
			}
		})	
		

	}

});
