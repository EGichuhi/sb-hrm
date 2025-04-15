from frappe import _

def get_data():
    return [
        {
            "module_name": "HR",
            "color": "#3498db",
            "icon": "octicon octicon-organization",
            "type": "module",
            "label": _("HR"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Employee",
                    "label": _("Employee"),
                    "description": _("Manage employee records."),
                },
                {
                    "type": "doctype",
                    "name": "Attendance",
                    "label": _("Attendance"),
                    "description": _("Track employee attendance."),
                },
                {
                    "type": "doctype",
                    "name": "Leave Application",
                    "label": _("Leave Application"),
                    "description": _("Manage leave applications."),
                },
                {
					"type": "doctype",
					"name": "Payroll",
					"label": _("Payroll"),
					"description": _("Manage payroll and salary."),
				},
				{
					"type": "doctype",
					"name": "Performance Review",
					"label": _("Performance Review"),
					"description": _("Conduct performance reviews."),
				},
                {
					"type": "doctype",
					"name": "Recruitment",
					"label": _("Recruitment"),
					"description": _("Manage recruitment process."),
				},
                {
					"type": "doctype",
					"name": "HR dashboard",
					"label": _("HR Dashboard"),
					"description": _("View HR metrics and analytics."),
				},
                
            ],
        }
    ]
