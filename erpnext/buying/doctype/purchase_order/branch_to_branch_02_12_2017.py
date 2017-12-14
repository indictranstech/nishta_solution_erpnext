# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt
from __future__ import unicode_literals
import frappe

from frappe.utils import flt, cstr, nowdate, nowtime
from erpnext.stock.utils import update_bin
from erpnext.stock.stock_ledger import update_entries_after

def purchase_order_to_sales_order(doc, method):
    cust_details = frappe.db.get_value("Customer", filters={"name":doc.supplier}, fieldname=["name", "company"], as_dict=True)
    sup_details = frappe.db.get_value("Supplier", filters={"name":doc.supplier}, fieldname=["name", "company", "branch_or_head"], as_dict=True)
    ware_details=frappe.db.get_value("Warehouse",filters={"company":cust_details.company,"is_default":1},fieldname=["name","company"],as_dict=True)
    if sup_details.branch_or_head:
        sales_order = frappe.get_doc({
                "doctype":"Sales Order",
                "customer":doc.supplier,
                "mobile":"0",
                "email":"potoso@gmail.com",
                "order_mode":"Branch Transfer",
                "type_of_order":"Branch Transfer",
                "mobile":"0",
                "house_no":"0",
                "street_name":"NSR Road",
                "area":"0",
                "landmark":"0",
                "pincode":"0",
                "deliver_mode":"Door Delivery",
                "deliver_date":"0",
                "deliver__slot":"10 Am To 12 Pm",
                "title":doc.supplier,
                "branch_purchase_order":doc.name,
                "delivery_date":doc.transaction_date,
                "company":cust_details.company,
                })
        for d in doc.get("items"):
            
            sales_order_items = frappe.get_doc({
                "doctype":"Sales Order Item",
                "item_code":d.item_code,
                "item_name":d.item_name,
                "rate":d.rate,
                "qty":d.qty,
                "amount":d.amount,
                "shape":"NA",
                "egg_type":"NA",
                "message_on_cake":"Store Transfer",
                "warehouse":ware_details.name,
                })
            sales_order.append("items", sales_order_items)
        sales_order.save(ignore_permissions=True);


def sales_invoice_to_purchase_receipt(doc, method):
    cust_details = frappe.db.get_value("Customer", filters={"name":doc.customer}, fieldname=["name", "company", "branch_or_head"], as_dict=True)
    sup_details = frappe.db.get_value("Supplier", filters={"name":doc.customer}, fieldname=["name", "company", "branch_or_head"], as_dict=True)
    if cust_details.branch_or_head:
        purchase_receipt = frappe.get_doc({
                "doctype":"Purchase Receipt",
                "supplier":doc.customer,
                "title":doc.customer,
                "head_sales_invoice_no":doc.name,
                "company":sup_details.company,
                })
        default_ware_house = frappe.db.get_value("Warehouse", filters={"company":sup_details.company, "is_default":1}, fieldname=["name", "company"], as_dict=True)
        warehouse = "";
        if default_ware_house:
            warehouse = default_ware_house.name
        for d in doc.get("items"):
            sales_order_no = d.sales_order
            sales_order_details = frappe.db.get_value("Sales Order", filters={"name":sales_order_no}, fieldname=["branch_purchase_order", "company"], as_dict=True)
            purchase_order_no = "";
            if sales_order_details.branch_purchase_order:
                purchase_order_no = sales_order_details.branch_purchase_order;
                purchase_receipt_item = frappe.get_doc({
                "doctype":"Purchase Receipt Item",
                "item_code":d.item_code,
                "item_name":d.item_name,
                "rate":d.rate,
                "qty":d.qty,
                "amount":d.amount,
                "purchase_order":purchase_order_no,
                "warehouse":warehouse
                })
                purchase_receipt.append("items", purchase_receipt_item)
        purchase_receipt.save(ignore_permissions=True);
    # frappe.msgprint(doc.name)
    # frappe.msgprint("tested",raise_exception=True)
