from hl7apy.parser import parse_message
from hl7apy.mllp import AbstractHandler,AbstractErrorHandler
from hl7apy.core import Message
from hl7apy.mllp import UnsupportedMessageType,InvalidHL7Message
from hl7apy.mllp import MLLPServer

class PDQHandler(AbstractHandler):
    def reply(self):
        msg = parse_message(self.incoming_message)
        # do something with the message

        res = Message('RSP_K21')
        # populate the message
        return res.to_mllp()

class ErrorHandler(AbstractErrorHandler):
    def reply(self):
        if isinstance(self.exc, UnsupportedMessageType):
            err_code, err_msg = 101, 'Unsupported message'
        elif isinstance(self.exc, InvalidHL7Message):
            err_code, err_msg = 102, 'Incoming message is not an HL7 valid message'
        else:
            print('err')
            err_code, err_msg = 100, 'Unknown error occurred'
            # return your custom response for general errors    
        parsed_message = parse_message(self.incoming_message)

        m = Message("ACK")
        m.MSH.MSH_9 = "ACK^ACK"
        m.MSA.MSA_1 = "AR"
        m.MSA.MSA_2 = parsed_message.MSH.MSH_10
        m.ERR.ERR_1 = "%s" % err_code
        m.ERR.ERR_2 = "%s" % err_msg
        return m.to_mllp()

        
class ORUHandler(AbstractHandler):
    def reply(self):
        msg = parse_message(self.incoming_message)
        # do something with the message

        res = Message('ACK^R01')
        # populate the message
        return res.to_mllp()
    
    

handlers = {
    "ORU^R01":(ORUHandler),
    'QBP^Q22^QBP_Q21': (PDQHandler,), # value is a tuple
    'ERR': (ErrorHandler,)
}

server = MLLPServer('localhost', 2575, handlers)
print(server)
server.serve_forever()