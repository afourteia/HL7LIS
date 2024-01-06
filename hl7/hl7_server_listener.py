import socket
from datetime import datetime
import json
import uuid
import hl7_parser
import hl7_handler
from hl7apy.core import Message
# listener 
with open('./config.json') as configFile:
    config = json.load(configFile)
    
    
LOCAL_HOST = config['LocalHost']
LOCAL_PORT = config['LocalPort']
REMOTE_IP = config['RemoteHost']
REMOTE_PORT = int(config['RemotePort'])
TcpTimeoutSecs = int(config['TcpTimeoutSeconds'])
HEADER = bytes.fromhex(config['Header'])
TRAILER = bytes.fromhex(config['Trailer'])
SEGMENT_TERMINATOR = bytes.fromhex(config['SegmentTerminator']).decode()
MSG_CODE = config['Message']['MessageCode']
TRIGGER_EVENT = config['Message']['TriggerEvent']
PROCESSING_ID = config['Message']['ProcessingID']
SENDR_APP = config['Message']['SendingApplication']
SENDR_FAC = config['Message']['SendingFacility']
RECV_APP = config['Message']['ReceivingApplication']
RECV_FAC = config['Message']['ReceivingFacility']
PAT_UR = config['Message']['PatientUR']
PAT_NAME = config['Message']['PatientName']
current_datetime = datetime.now().isoformat().replace('-','').replace('T','').replace(':','')[:14]

class Ack:
    def __init__(self, msg_str: str):
        self.senderApp = msg_str.split('|')[4]
        self.senderFac = msg_str.split('|')[5]
        self.RecvApp = msg_str.split('|')[2]
        self.RecvFac = msg_str.split('|')[3]
        self.triggerEvent = msg_str.split('|')[8].split('^')[1]
        self.msgControlId = msg_str.split('|')[9]
        self.processingId = msg_str.split('|')[10]
        self.hL7Version = msg_str.split('|')[11]
    def get_string(self):
        return f"\
MSH|^~\&|{self.senderApp}|{self.senderFac}|{self.RecvApp}|{self.RecvFac}|{current_datetime}||ACK^{self.triggerEvent}\
|{uuid.uuid4().hex}|{self.processingId}|{self.hL7Version}|||AL|NE{SEGMENT_TERMINATOR}MSA|AA|{self.msgControlId}"


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

def main():
    print("MLLP server (s) or client (c)?")
    listen()
        
def listen():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #local_port = input("...Port to listen on: ")
        # s.settimeout(TcpTimeoutSecs)
        # local_ip = "127.0.0.1"
        local_ip = "127.0.0.1"
        # local_ip = "169.254.36.125"
        
        # local_ip = "192.168.0.119"
        # local_ip = "0.0.0.0"
        print("......listening for connections on", local_ip, ":",LOCAL_PORT)
        msg_str = "" # initialize message string     
        try:
            # Bind the socket to the port
            s.bind((local_ip, int(LOCAL_PORT)))
            # Listen for incoming connections
            s.listen(1)
            # Accept the connection
            client_socket, addr = s.accept()
            client_socket.settimeout(TcpTimeoutSecs)
            print("......connection accepted from", addr)
            print(colored(30, 255, 20, datetime.now()))

            # Receive data from the client
            # msg_str = "" # initialize message string      

            while True:
                data = client_socket.recv(16384)
                if data != "":
                    msg_str += data.decode('utf-8')
                if len(data) < 16384:
                    break
        except Exception as e:
            print("......connection failed. Reason:", e)
            s.close()
            listen

        # Remove Header, Trailer and Segment Terminator from the message and print it
        print("...received message:\n")    
        msg_str = msg_str.replace(HEADER.decode(), '').replace(TRAILER.decode(), '')
        print('msg_str')
        print(msg_str)
        with open('msg_str.txt', 'w') as f:
            f.write(msg_str)
        response_payload = Message()
        if msg_str != "":
            message_dict_S, message_dict_R, response_payload = hl7_handler.process_hl7_message(msg_str, remove_none = False)
            # response_payload = hl7_handler.process_hl7_message(msg_str)
            print('response_payload')
            print(type(response_payload))
            # print('response_payload',response_payload.to_er7())
            print('end of response_payload')
            
            # hl7_parser.parce_hl7_message(msg_str)
            for x in msg_str.split(SEGMENT_TERMINATOR):
                print("x",x)

        # Generate and send ACK message back to the client
        try:
            # ack = Ack(msg_str).get_string()
            client_socket.sendall(HEADER + bytearray(response_payload.to_er7(), 'utf8') + TRAILER)
            # client_socket.sendall(HEADER + bytearray(ack, 'utf8') + TRAILER)

            print('\n\n...ACK message sent back to the client:')
            # for x in ack.split(SEGMENT_TERMINATOR):
            #     print(x)
        except Exception as e:
            print(colored(230, 20, 30, "Error while sending the acknowledgement message back to the sender."))
            print(e)
        finally:
            s.close()
            print()
            print('...connection closed. Listening for a new connection...')
            print()
            listen()
if __name__ == '__main__':
    main()