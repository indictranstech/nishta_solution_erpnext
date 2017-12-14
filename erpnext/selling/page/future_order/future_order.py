# -*- coding: utf-8 -*-
# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import datetime

@frappe.whitelist()
def show_order_details(sel_date=None):
	if not sel_date:
		date = frappe.utils.data.today();
		add_date = frappe.utils.data.add_days(date, 1);
	else:
		sel_date = datetime.datetime.strptime(sel_date, "%d-%m-%Y").strftime("%Y-%m-%d")
		add_date = sel_date
	return frappe.db.sql("select name,customer,mobile,deliver_mode,type_of_order,`customer_delivery_time` as customer_delivery_time ,order_status, pickup_store,deliver_date,advance_paid,grand_total from `tabSales Order` where type_of_order!='Branch Transfer' and status!='Cancelled' and date(`deliver_date`)=%s ",(add_date),as_dict=True);

