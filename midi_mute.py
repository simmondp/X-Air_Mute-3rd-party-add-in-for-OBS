#
# Project     OBS Mute Script
# @author      Paul Simmonds
#
# @license    GPLv3 - Copyright
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# This script should be located (on a windows machine) in the OBS Scripts directory
# Typically this will be located here:
# C:\Program Files\obs-studio\data\obs-plugins\frontend-tools\scripts
##
# OBS must be configured for the Python install location [Tools][Scripts][Python Settings]
# Use [Browse] and locate: %USERPROFILE%\AppData\Local\Programs\Python\Python36

# X-Air 18 MIDI for CH Mutes
#	Channel = 2
#	CC (control change)
#	CC Number = 0-15 (Ch1 = 0 etc.)
#	Value = 0 (Mute OFF)  or 127 (Mute ON) 

import obspython as obs
import sys
import time
import mido

# ------------------------------------------------------------
portname = "MidiView 1"
debug = False  # default to "True" until overwritten by properties
source_name = ""  # source name to monitor, stored from properties
# ------------------------------------------------------------

def dprint(*input):
	if debug:
		print(*input)

def _handler_frontend_event(event):
    dprint("Hello _handler_frontend_event")
    global cur_scene
    if event == obs.OBS_FRONTEND_EVENT_SCENE_CHANGED:
        # Get the scene name of the current scene
        scene = obs.obs_frontend_get_current_scene()
        cur_scene = obs.obs_source_get_name(scene)
        obs.obs_source_release(scene)
        dprint("The scene selected is --> " + cur_scene)
        _parse_scene_title(cur_scene)


def _parse_scene_title(scene_title):
	dprint("Hello _parse_scene_title")
	if scene_title.find("[") >= 0:
		parse_string = scene_title.split("[")
		dprint("First string split = " + parse_string[1])
		if parse_string[1].find("]") >= 0:
			mic_string = parse_string[1].split("]")
			dprint("Second string split = " + mic_string[0])
			mic_array = mic_string[0].split(",")
			dprint("String array = " + str(mic_array))
			_set_mic_unmute(mic_array)


# We now don't care about Channel assignments as its a 1:1 match on all 16 channels
def _set_mic_unmute(mic_unmute_string_list):
	import array as arr
	mute_array = arr.array('i', [127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127])
	
	try:
		outport = mido.open_output(portname)
		dprint("Connected to MIDI output")
	except:
		dprint("cannot connect to MIDI output")
		exit()
	
	# Now iterate the list
	if not outport.closed:
		dprint("Port is open - lets send some midi!")
		for mic_number in mic_unmute_string_list:
			dprint("Un-mute microphone " + mic_number)
			mic = int(mic_number)
			if mic < 17:
				mute_array[int(mic_number)-1] = 0
			
		# Now send all 16 channels
		for x in range(16):
			msg = mido.Message('control_change', channel=1, control=x, value=mute_array[x])
			outport.send(msg)
			
		#close the MIDI Interface port
		outport.close()
		
	if outport.closed:
		dprint("Yes, the port is closed.")
	
	
#===================================================================================
# OBS Script Functions

def _initialize():
    obs.obs_frontend_add_event_callback(_handler_frontend_event)  # crash if unidentified script
    dprint("frontend_add_event_callback Initialized")


def script_description():
    return "<b>OBS to X-Air 18 Mute Control</b>" + \
            "<hr>" + \
            "Set the microphone channel on the mixing desk as [1,2,3] in the scene name for those channels you want un-muted.</b><br/>" + \
            "Paul Simmonds, ©2020-2024<br/>"


def script_update(settings):
    global debug
    debug = obs.obs_data_get_bool(settings, "debug")  # for printing debug messages


def script_properties():
    props = obs.obs_properties_create()
    # Add testing buttons and debug toggle
    obs.obs_properties_add_bool(props, "debug", "Print Debug Messages")
    return props


def script_load(settings):
    _initialize()
    dprint("OBS Script Loaded")


def script_unload():
    obs.obs_frontend_remove_event_callback(_handler_frontend_event)
    dprint("OBS Mute Indicator Script Unloaded. Goodbye!")
	
	
