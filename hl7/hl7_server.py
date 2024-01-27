import hl7apy
from hl7apy import parser
from hl7apy.exceptions import UnsupportedVersion
from pprint import pprint
hl7apy.set_default_version('2.3.1')
hl7apy.get_default_version()
import socket
from datetime import datetime
import json
import uuid
# hl7 segments
# MSH – Message header
# OBR  Observation request
# OBX  Observation result
# PID  Patient identification
hl7_message = "MSH|^~\\&|SENDING_APPLICATION2|SENDING_FACILITY|RECEIVING_APPLICATION|RECEIVING_FACILITY|202212290801||ADT^A01|93457|P|2.5|||||"

m = parser.parse_message(hl7_message,find_groups=False)
dict_message = {}
try:
    print("Trying to parse the message with the specific parser")
    m = parser.parse_message(hl7_message,find_groups=False)
    print(m.children)
    for seg in m.children:
        print(seg.name)
        dict_message[seg.name] ={}
        print(dict_message)
        # print(seg.__dict__)
        for element in seg.__dict__["children"]:
            dict_message[seg.name][element.long_name] = element.value
            # print(element.long_name)
            print(dict_message)

        
    # print(m.msh.msh_9.value)
    # print(m.msh.msh_3.value)
    # print(type(m.msh.msh_9.__dict__['element_list'][3]))
    # print(m.msh.msh_9.__dict__['element_list'][3].__dict__.values())
    # print(m.msh.msh_9.__dict__['element_list'][3])
    


except UnsupportedVersion:
    print("Unsupported version, trying to parse the message with the generic parser")
    m = parser.parse_message(hl7_message,find_groups=False)
    
    