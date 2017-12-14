# -*- coding: utf-8 -*-
# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Scrap(Document):
	pass

@frappe.whitelist()
def day_remove(user=None):
	user_details = frappe.get_value("User", filters={"name":user}, fieldname=['company', 'username'], as_dict=True)
	user_id = frappe.session.user
	user_deta = frappe.db.get_value("User", filters={"name":user_id}, fieldname=["company"], as_dict=True)
	company = user_deta.company
	select_warehouse = frappe.get_value("Warehouse", filters={"company":company,"is_default":1}, fieldname=['warehouse_name'], as_dict=True)
	default_warehouse = select_warehouse.warehouse_name
	return default_warehouse

@frappe.whitelist()
def stock(item=None,warehouse=None):
	return item