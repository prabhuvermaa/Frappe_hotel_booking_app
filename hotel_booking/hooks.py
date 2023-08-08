from . import __version__ as app_version

app_name = "hotel_booking"
app_title = "Hotel Booking"
app_publisher = "Prabhu Verma"
app_description = "A Custom appliaction created for make Hotel booking seamless."
app_email = "prabhuvermaaa@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/hotel_booking/css/hotel_booking.css"
# app_include_js = "/assets/hotel_booking/js/hotel_booking.js"

# include js, css files in header of web template
# web_include_css = "/assets/hotel_booking/css/hotel_booking.css"
# web_include_js = "/assets/hotel_booking/js/hotel_booking.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "hotel_booking/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "hotel_booking.utils.jinja_methods",
#	"filters": "hotel_booking.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "hotel_booking.install.before_install"
# after_install = "hotel_booking.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "hotel_booking.uninstall.before_uninstall"
# after_uninstall = "hotel_booking.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "hotel_booking.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"hotel_booking.tasks.all"
#	],
#	"daily": [
#		"hotel_booking.tasks.daily"
#	],
#	"hourly": [
#		"hotel_booking.tasks.hourly"
#	],
#	"weekly": [
#		"hotel_booking.tasks.weekly"
#	],
#	"monthly": [
#		"hotel_booking.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "hotel_booking.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "hotel_booking.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "hotel_booking.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["hotel_booking.utils.before_request"]
# after_request = ["hotel_booking.utils.after_request"]

# Job Events
# ----------
# before_job = ["hotel_booking.utils.before_job"]
# after_job = ["hotel_booking.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"hotel_booking.auth.validate"
# ]
