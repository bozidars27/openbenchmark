import os
import json
from scenarios.scenario import Scenario
from utils import Utils


class HomeAutomation(Scenario):

	SCENARIO_IDENTIFIER = 'home-automation'
	CONFIG_FILES        = {
		"main"  : os.path.join(Utils.scenario_config, "home_automation", "_config.json"),
		"iotlab": os.path.join(Utils.scenario_config, "home_automation", "_iotlab_config.json"),
		"wilab" : os.path.join(Utils.scenario_config, "home_automation", "_wilab_config.json"),
	}

	def __init__(self, sut_command_payload):
		super(HomeAutomation, self).__init__(sut_command_payload)
		super(HomeAutomation, self)._read_config(self.CONFIG_FILES)
		self._instantiate_nodes()