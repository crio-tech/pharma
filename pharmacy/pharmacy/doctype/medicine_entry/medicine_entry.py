# -*- coding: utf-8 -*-
# Copyright (c) 2021, crio and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document
import frappe

class MedicineEntry(Document):
	def validte(self):
		print(self.name)
		# for med in self.medicine_entry_list:
		# 	print(med)
			# medicine = frappe.get_doc('Medicine')
	
	def create_batch(self,batch_no,medicine,exp_date):
		batch_doc = frappe.get_doc('Medicine Batch')
		batch_doc.batch_no = batch_no
		batch_doc.medicine = medicine
		batch_doc.exp = exp_date

		batch_doc.save()

	def create_stock(self,medicine,pharma,batch_no,qty,bill):
		if frappe.db.exists('Medicine Stock', ''):
			pass