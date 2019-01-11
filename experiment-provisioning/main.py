import argparse
import ConfigParser
import os
import base64

from otbox_startup import OTBoxStartup
from otbox_flash import OTBoxFlash
from ov_startup import OVStartup
from reservation import Reservation
from ov_log_monitor import OVLogMonitor


configParser = ConfigParser.RawConfigParser()   
configFilePath = os.path.join(os.path.dirname(__file__), 'conf.txt')
configParser.read(configFilePath)

USERNAME = os.environ["user"] if "user" in os.environ else configParser.get('exp-config', 'user')
PRIVATE_SSH = os.environ["private_ssh"] if "private_ssh" in os.environ else ""
HOSTNAME = 'saclay.iot-lab.info'

EXP_DURATION = 30 #Duration in minutes
NODES = "saclay,a8,106+107"

FIRMWARE = os.path.join(os.path.dirname(__file__), 'firmware')
BROKER = configParser.get('exp-config', 'broker')

def add_private_key():
	if PRIVATE_SSH != "":
		private_ssh_file = os.path.join(os.path.expanduser("~"), ".ssh", "id_rsa")

		private_ssh_decoded = base64.b64decode(PRIVATE_SSH)

		with open(private_ssh_file, "w") as f:
			f.write(private_ssh_decoded)


def add_parser_args(parser):
	parser.add_argument('--action', 
        dest       = 'action',
        choices    = ['check', 'reserve', 'terminate', 'otbox', 'otbox-flash', 'ov-start', 'ov-monitor'],
        required   = True,
        action     = 'store'
    )
	parser.add_argument('--testbed', 
        dest       = 'testbed',
        choices    = ['iotlab', 'opentestbed'],
        default    = 'iotlab',
        action     = 'store'
	)
	parser.add_argument('--firmware', 
        dest       = 'firmware',
        default    = '03oos_openwsn_prog',
        action     = 'store'
	)

def get_args():
	parser = argparse.ArgumentParser()
	add_parser_args(parser)
	args = parser.parse_args()

	return {
		'action'  : args.action,
		'testbed' : args.testbed,
		'firmware': args.firmware
	}

def main():
	args = get_args()

	action = args['action']
	testbed = args['testbed']
	firmware = '{0}/{1}'.format(FIRMWARE, args['firmware'])

	add_private_key()

	print 'Script started'
	
	if action == 'check':
		print 'Checking experiment'
		Reservation(USERNAME, HOSTNAME).check_experiment()
	if action == 'reserve':
		print 'Reserving nodes'
		Reservation(USERNAME, HOSTNAME).reserve_experiment(EXP_DURATION, NODES)
	if action == 'terminate':
		print 'Terminating experiment'
		Reservation(USERNAME, HOSTNAME).terminate_experiment()
	elif action == 'otbox':
		print 'Starting OTBox'
		OTBoxStartup(USERNAME, HOSTNAME, testbed).start()
	elif action == 'otbox-flash':
		print 'Flashing OTBox'
		OTBoxFlash(firmware, BROKER, testbed).flash()
	elif action == 'ov-start':
		print 'Starting OV'
		OVStartup().start()
	elif action == 'ov-monitor':
		print 'Starting OV log monitoring'
		OVLogMonitor().start()

if __name__ == '__main__':
	main()

