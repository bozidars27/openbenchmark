import os
import json
from scenarios.scenario import Scenario
from utils import Utils


class BuildingAutomation(Scenario):

	SCENARIO_IDENTIFIER = 'building-automation'
	CONFIG_FILES        = {
		"main"  : os.path.join(Utils.scenario_config, "building_automation", "_config.json"),
		"iotlab": os.path.join(Utils.scenario_config, "building_automation", "_iotlab_config.json"),
		"wilab" : os.path.join(Utils.scenario_config, "building_automation", "_wilab_config.json"),
	}

	def __init__(self, sut_command):
		super(BuildingAutomation, self).__init__(sut_command)
		super(BuildingAutomation, self)._read_config(self.CONFIG_FILES)
		self._instantiate_nodes()