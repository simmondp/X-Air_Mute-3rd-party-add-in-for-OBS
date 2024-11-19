# OBS_toX-Air_Mute
Python script for OBS to issue unmute commands to an X-Air 18 when a scene is selected

@author      Paul Simmonds
@license    GPLv3 - Copyright

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details. <http://www.gnu.org/licenses/>.

This script should be located (on a windows machine) in the OBS Scripts directory
Typically this will be located here:
C:\Program Files\obs-studio\data\obs-plugins\frontend-tools\scripts

OBS must be configured for the Python install location [Tools][Scripts][Python Settings]
Use [Browse] and locate: %USERPROFILE%\AppData\Local\Programs\Python\Python36

# X-Air 18 MIDI for CH Mutes
	Channel = 2
	CC (control change)
	CC Number = 0-15 (Ch1 = 0 etc.)
	Value = 0 (Mute OFF)  or 127 (Mute ON) 

Once installed, simply add the comma sepeted chanels inside [ ] to the scene name
for example:
My new scene [1,3,5,15] 
and when selected OBS will unmute chanels 1, 3, 5 and 15, and mute the rest.

# INSTALL NOTES

01. Download the latest Python Version from https://www.python.org/
	** Important, download the "python-3.12.7-amd64"
	** 3.13 does not work with OBS 30.2.3

02. Remove old version of Python (if they exist)

03. Install [python-3.12.7-amd64.exe] the downloaded Python EXE (RunAs Admin)
	[x] Use admin privilages
	[x] Add python.exe to the PATH
	Install in default "%USERPROFILE%\AppData\Local\Programs\Python\Python312"

04. RunAs Admin CMD to get a DOS Window

05. Type "C:" then "%USERPROFILE%\AppData\Local\Programs\Python\Python312"

06. Upgrade to latest version of PIP
	Type "python.exe -m pip install --upgrade pip"

07. Install the Midi library using "python -m pip install mido[ports-rtmidi]"

08. OBS must be configured for the Python install location [Tools][Scripts][Python Settings]
	Set the location to match the install directory
	In this case "%USERPROFILE%\AppData\Local\Programs\Python\Python312"

09. Use the python script (midi_port_test.py) in a CMD window to display the MIDI ports
    detected, and copy the X-Air 18 port name.
    >> Configure/edit the script to use that port

10. Copy the python script (midi_mute.py) into the OBS Scripts directory, typically here:
	"C:\Program Files\obs-studio\data\obs-plugins\frontend-tools\scripts"

11. Restart OBS
