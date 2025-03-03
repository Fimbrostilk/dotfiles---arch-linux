import psutil
import os

def find_a_process(name = 'wf-recorder'):
	for process in psutil.process_iter(attrs = ['name']):
		if process.info['name'] == name:
			return True
	return False

if find_a_process():
	os.system('pkill -INT wf-recorder')
else:
	os.system('wf-recorder -a -y -f /home/angel/Videos/wf-recorder/recording.mkv')
