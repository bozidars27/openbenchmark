<?php
	
namespace App\Classes\ExperimentController;

class ConfigParser {

	private $scenario_config;
	
	function get_config_data($param, $scenario, $testbed) {
		return $this->_invoke_python_interface($param, $scenario, $testbed);
	}

	private function _invoke_python_interface($param, $scenario, $testbed) {
		$python_interface_path = base_path() . "/../scenario-config/interface.py";

		$command = "python $python_interface_path --param=$param";
		$command .= $param == 'nodes' ? " --scenario=$scenario --testbed=$testbed" : "";

		return json_decode(shell_exec($command));
	}
}