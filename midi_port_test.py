#
# Project     Midi Port Test Script v2
# Addition of Windows error message to assist debug
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

import sys
import time
import mido
import ctypes

#=========================================================================
#List the Midi port names
mystr=""
print('------ OUTPUT ------')
for port in mido.get_output_names():
  mystr+=port
  mystr+="\r\n"
  print(port)
print('-------------------------')
ctypes.windll.user32.MessageBoxW(0, mystr, u"MIDI References Found", 0)
	
#End
