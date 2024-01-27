from hl7apy.core import Message,Segment
from hl7apy import parser
hl7_message = Message("ADT_A01")
pid = Segment("PID")
hl7_message.add_segment(pid)
m = parser.parse_message(hl7_message)
# print(m.children)