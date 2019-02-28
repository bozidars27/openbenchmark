import os

class Utils:
	id_to_eui64   = {}
	eui64_to_id   = {}
	experiment_id = None
	scenario      = None
	date          = ""
	firmware      = ""

	scenario_config  = os.path.join(os.path.dirname(__file__), "scenarios")