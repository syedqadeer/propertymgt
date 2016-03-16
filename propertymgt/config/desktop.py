# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Property Management",
			"color": "green",
			"icon": "icon-building",
			"type": "module",
			"label": _("Property Management")
		},
		{
			"module_name": "Property Billing",
			"color": "blue",
			"icon": "icon-money",
			"type": "module",
			"label": _("Property Billing")
		}
	]
