import hl7apy
from hl7apy import parser
from hl7apy.exceptions import UnsupportedVersion ,ParserError
from pprint import pprint
hl7apy.set_default_version('2.3.1')
hl7apy.get_default_version()
from datetime import datetime
from hl7apy.core import Message
from hl7apy.core import Field,Segment
import json
from hl7apy.parser import parse_field, parse_component
# hl7 segments
# MSH – Message header
# OBR  Observation request
# OBX  Observation result
# PID  Patient identification
created_message = 'hl7'
json_m = {"MSH": {"0": {"name": "MSH_1", "long_name": "FIELD_SEPARATOR", "value": "|"}, "1": {"name": "MSH_2", "long_name": "ENCODING_CHARACTERS", "value": "^~\\&"}, "2": {"name": "MSH_3", "long_name": "SENDING_APPLICATION", "value": "Manufacturer"}, "3": {"name": "MSH_4", "long_name": "SENDING_FACILITY", "value": "analyzer"}, "4": {"name": "MSH_7", "long_name": "DATE_TIME_OF_MESSAGE", "value": "20070423101830"}, "5": {"name": "MSH_9", "long_name": "MESSAGE_TYPE", "value": "ORU^R01"}, "6": {"name": "MSH_10", "long_name": "MESSAGE_CONTROL_ID", "value": "1"}, "7": {"name": "MSH_11", "long_name": "PROCESSING_ID", "value": "P"}, "8": {"name": "MSH_12", "long_name": "VERSION_ID", "value": "2.3.1"}, "9": {"name": "MSH_16", "long_name": "APPLICATION_ACKNOWLEDGMENT_TYPE", "value": "0"}, "10": {"name": "MSH_18", "long_name": "CHARACTER_SET", "value": "ASCII"}}}
def create_hl7_message(hl7_json):
    

    try:
        # dict_message = json.load(hl7_json)
        # print(type(hl7_json))
        m = Message()
        # m2 = Message("ORU_R01")
        # msh_seg = Segment("MSH")
        # m2.add_segment(msh_seg)
        # m2.msh ="MSH|^~\&|Manufacturer|analyzer|||20070423101830||ORU^R01|1|P|2.3.1||||0||ASCII|||"
        # msh = "MSH|^~\&|GHH_ADT||||20080115153000||ORU^R01|0123456789|P|2.5||||AL\r"
        # m2.msh = msh
        # print(m2.validate())
        # print(m2.to_er7())
        # m = Message("OBR")
        print("empty messge",m.__dict__)
        for key in hl7_json.keys():
            print(key)
            seg = Segment(key)
            # m.add_segment(key)
            for child in hl7_json[key].keys():
                # index =list(hl7_json[key]).index(child)
                # name =  f"MS_{index+1}"
                # print('******',name)
                field = Field(hl7_json[key][child]['name'])
                field = parse_field(hl7_json[key][child]['value'], name=hl7_json[key][child]['name'])
                seg.add(field)
                print("child value",hl7_json[key][child]['value'])
                print("child name",hl7_json[key][child]['name'])
                print("segment",seg.to_er7())
            # seg1 = Segment("MSH")
            # seg1 = "MSH|^~\&|Manufacturer|analyzer|||20070423101830||ORU^R01|1|P|2.3.1||||0||ASCII|||"
                # print("seg1", seg1.to_er7())
            m.add_segment(seg)
        print(m.validate())
        print(m.to_er7())
        #     for element in seg.__dict__["children"]:
        #         print(element.name)
        #         dict_message[seg.name][element.long_name] = element.value
        #         # print(element.long_name)
        # print(dict_message)
        # with open("created_message.hl7", "w") as f: 
        #     f.write(created_message)
    except Exception as e:
        print("Error",e)
create_hl7_message(json_m)