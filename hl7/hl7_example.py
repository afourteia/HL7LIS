import hl7

# Load the HL7 message into a variable
hl7_message = "MSH|^~\\&|SENDING_APPLICATION|SENDING_FACILITY|RECEIVING_APPLICATION|RECEIVING_FACILITY|202212290801||ADT^A01|93457|P|2.5|||||"

# Parse the HL7 message
parsed_message = hl7.parse(hl7_message)
print(parsed_message)
print(hl7_message)
# Access the individual segments of the message
msh_segment = parsed_message[0]
evn_segment = parsed_message[1]
pid_segment = parsed_message[2]

# Access the fields of a segment
sending_application = msh_segment[2]
patient_id = pid_segment[2]