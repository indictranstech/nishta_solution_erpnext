from __future__ import unicode_literals
import frappe

from frappe.utils import flt, cstr, nowdate, nowtime
from erpnext.stock.utils import update_bin
from erpnext.stock.stock_ledger import update_entries_after

def company_based_naming_series_create(doc, method):
    test=1
    if test:   
            user = frappe.session.user
            company_details = frappe.db.get_value("User", filters={"name":user}, fieldname=["company", "name"],as_dict=True)
            #frappe.msgprint(company_details)
            #frappe.msgprint(company_details)
            if company_details:
                company_name = company_details.company
                if company_name:
                    map_details = frappe.db.get_value("series mapping", filters={"company":company_name}, fieldname=["name", "company"], as_dict=True)
                    if map_details:
                        map_name = map_details.name
                        doctype_list = doc.doctype
                        serial_det = frappe.db.get_value("child mapping", filters={"doctype_list":doctype_list, "parent":map_name, "type":"Default"}, fieldname=["serial_no", "doctype_list"], as_dict=True)
                        if serial_det:
                            doc.naming_series = serial_det.serial_no
    else:
        pass
