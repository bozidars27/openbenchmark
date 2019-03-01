<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use CommandHandler;
use ConfigParser;
use ErrorResponse;

class ExperimentController extends Controller
{

    function __construct() {
        $this->config_parser   = new ConfigParser();
        $this->command_handler = new CommandHandler();
    }

    function start() {
        $this->cmd_handler->reserve_nodes();
        $this->cmd_handler->otbox_start();

        sleep($cmd_handler::OV_GUARD_TIME); //A guard time to wait for the nodes to start sending serial data before running OV
        
        $this->cmd_handler->ov_start();

        sleep($cmd_handler::OV_LOG_GUARD_TIME); //A guard time to wait for OV to start writing the log
        
        return $this->cmd_handler->ov_monitor();
    }

    function upload() {
        return response()->json([
            'status' => 'success'
        ]);
    }

    function exp_terminate() {
        return $this->cmd_handler->exp_terminate();
    }


    // Functions for test routes
    function reserve_exp() {
        return $this->cmd_handler->reserve_nodes();
    }

    function start_otbox() {
        return $this->cmd_handler->otbox_start();
    }

    function start_ov() {
        return $this->cmd_handler->ov_start();
    }

    function start_watcher() {
        return $this->cmd_handler->ov_monitor();
    }

    // Scenario data retrieval
    function get_config_data($param, $scenario=null, $testbed=null) {
        if ($param == null) 
            return ErrorResponse::response(422, '`param` is a required argument');
        else if ($param == 'nodes' && ($scenario == null or $testbed == null))
            return ErrorResponse::response(422, 'If `param` is set to `nodes`, `scenario` and `testbed` cannot be null');
        else 
            return response()->json($this->config_parser->get_config_data($param, $scenario, $testbed));
    }
}
