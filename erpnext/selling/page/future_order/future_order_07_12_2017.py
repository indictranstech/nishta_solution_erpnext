# -*- coding: utf-8 -*-
# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

@frappe.whitelist()
def show_order_details():
	date=frappe.utils.data.today();
	return frappe.db.sql("select name,customer,mobile,deliver_mode,type_of_order,`customer_delivery_time` as customer_delivery_time , pickup_store,deliver_date from `tabSales Order` where type_of_order!='Branch Transfer' and status!='Cancelled' and date(`deliver_date`)>%s ",(date),as_dict=True);

