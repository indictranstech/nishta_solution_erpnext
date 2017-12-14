# -*- coding: utf-8 -*-
# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class SaleClose(Document):
	pass

@frappe.whitelist()
def day_close(user=None,today=None):
	user_details = frappe.get_value("User", filters={"name":user}, fieldname=['company', 'username'], as_dict=True)
	user_id = frappe.session.user
	user_deta = frappe.db.get_value("User", filters={"name":user_id}, fieldname=["company"], as_dict=True)
	company = user_deta.company
	sale_close_data = frappe.get_list("Sales Invoice Payment", fields=["mode_of_payment", "amount"], filters={"date":today})
	total_amount=0;
	total_card_amount=0;
	for sale_close_data1 in sale_close_data:
		mode_of_payment =  sale_close_data1.mode_of_payment
		if mode_of_payment == "Cash":
			amount =  sale_close_data1.amount
			total_amount=amount+total_amount
		if mode_of_payment == "Credit Card":
			card_amount =  sale_close_data1.amount
			total_card_amount=card_amount+total_card_amount	
			
	list_amount=frappe.db.sql("""select sum(amount) as amount,mode_of_payment from `tabSales Invoice Payment` where date(date)=%s and owner=%s group by mode_of_payment""",(today,user_id),as_dict=True)
	send_list={}		
	for list_amount_val in list_amount:
		mode_of_payment=list_amount_val.mode_of_payment;
		amount=list_amount_val.amount;
		send_list[mode_of_payment]=amount
	return [send_list]
	