# -*- coding: utf-8 -*-
# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

@frappe.whitelist()
def show_current_stock(user=None):
	#===========================================================================
	# login_company = frappe.db.get_value("tabUser", filters={"email":user}, fieldname=['company'], as_dict=True)
	# company = login_company.company;
	#===========================================================================
	
	send_data_bind = []
	user_details = frappe.get_value("User", filters={"name":user}, fieldname=['company', 'username'], as_dict=True)
	user_id = frappe.session.user
	user_deta = frappe.db.get_value("User", filters={"name":user_id}, fieldname=["company"], as_dict=True)
	company = user_deta.company
	select_warehouse = frappe.get_value("Warehouse", filters={"company":company,"is_default":1}, fieldname=['warehouse_name'], as_dict=True)
	default_warehouse = select_warehouse.warehouse_name
	frappe.msgprint(default_warehouse)
	stock_details = frappe.get_list("Stock Ledger Entry", fields=["item_code"], filters={"warehouse":default_warehouse})
		for stock_item_details in stock_details:
			stock_list = {}
	 		stock_list['item_code'] =  stock_item_details.item_code
	 		data.append(stock_list);
	 	    final_send_list = [ {"transaction_data":data}]
        
        return final_send_list
		
	#===========================================================================
	# stock_details = frappe.get_list("Stock Ledger Entry", fields=["item_code"], filters={"warehouse":default_warehouse})
	# 	for stock_item_details in stock_details:
	# 		stock_list = {}
	# 		stock_list['item_code'] =  stock_item_details.item_code
	# 		data1.append(stock_list);
	# 	final_send_list = [ {"transaction_data":data1}]
 #     return final_send_list
 #===========================================================================
	#===========================================================================
	# frappe.msgprint(default_warehouse)
	#===========================================================================
	
		#=======================================================================
		# item_code = stock_items.item_code
		# frappe.msgprint(item_code)
		# data_bind = [item_code]
		# send_data_bind.append(data_bind)
		# frappe.msgprint("test")
	 #    return send_data_bind
	 #=======================================================================
		
	
	#===========================================================================
	# frappe.msgprint(default_warehouse)
	#===========================================================================
	
	#===========================================================================
	# frappe.msgprint(company)
	#===========================================================================
	#===========================================================================
	# return user
	#===========================================================================
	#===========================================================================
	# return frappe.db.sql("select item_code, warehouse,actual_qty from `tabStock Ledger Entry` where `warehouse`=%s",("R Puram - TD"),as_dict=True);
	#===========================================================================
	
	
	
		
	

