# -*- encoding: utf-8 -*-
{
    "name": "Donation Extension",
    "version": "1.0",
    "author": "Business Tec Systems",
    "category": "Accounting & Finance",
    "description": """
Odoo module extending functionality of OCA Donation by adding notes, document numbering and qweb report with donation confimation letter
     """,
    "website": "http://www.businesstec.net/",
    "license": "AGPL-3",
    "depends": [
        "report",
        "donation"
    ],
    "demo": [],
    "data": [
        "donation_view.xml"
    ],
    #"test": [], 
    #"js": [], 
    #"css": [], 
    #"qweb": [], 
    "installable": True,
    "auto_install": False,
    "active": False
}
