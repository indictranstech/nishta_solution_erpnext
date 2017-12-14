# -*- coding: utf-8 -*-
# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import datetime

@frappe.whitelist()
def print_order(sel_date=None):
	if not sel_date:
		date = frappe.utils.data.today();
		add_date=frappe.utils.data.add_days(date,1);
	else:
		sel_date=datetime.datetime.strptime(sel_date, "%d-%m-%Y").strftime("%Y-%m-%d")
		add_date=sel_date
	basic = {}
	items = {}
	send_data = []
	order_ids = frappe.db.sql("select name  from `tabSales Order` where type_of_order!='Branch Transfer' and status!='Cancelled' and date(`deliver_date`)=%s ", (add_date), as_dict=True);
	for order_ids_val in order_ids:
		items_list = []
		
		ordered_items = frappe.get_list("Sales Order Item", filters={"parent":order_ids_val.name}, fields=["*"])
		count_items=0
		for ordered_items_val in ordered_items:
			items = {
			"item_name":ordered_items_val.item_code,
			"qty":ordered_items_val.qty,
			"shape":ordered_items_val.shape,
			"egg_type":ordered_items_val.egg_type,
			"message":ordered_items_val.message_on_cake,
			}
			count_items=count_items+1
			items_list.append(items)
		basic = {
			"order_id":order_ids_val.name,
			"delivery_time":order_ids_val.customer_delivery_time,
			"note":order_ids_val.notw,
			"count_items":count_items
		}
		send_list = {"basic":basic, "items":items_list}
		send_data.append(send_list)
	return send_data;
