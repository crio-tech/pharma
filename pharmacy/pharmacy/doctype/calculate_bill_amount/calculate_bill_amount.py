# -*- coding: utf-8 -*-
# Copyright (c) 2020, crio and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document
import frappe
from six import string_types
import json
from frappe.utils import nowdate, getdate
import datetime


class CalculateBillAmount(Document):
	pass


@frappe.whitelist()
def get_bills(doc):
	if isinstance(doc, string_types):
		doc = frappe._dict(json.loads(doc))
	bill_list = frappe.db.get_list('Bill',{'pharma':doc.pharma, 'bill_date': ['between',[doc.from_date, doc.to_date]], 'bill_status': 'unpaid'},['name', 'bill_date', 'amount', 'bill_status'],order_by="bill_date")
	return bill_list
