import socket

from hl7apy.parser import parse_message



def query(host, port):
    msg = r'''MSH|^~\&|SendingAPP|Sender Facility|Receiving APP|Receiving Facility|20220124014108^S|NO SECURITY|ADT^A08|2022012401410800823|T|2.3|00051||AL|
EVN|A08|20031111163831+0000^S||00102|00002|
PID|1|49120452|7337379446|234166342|Wolfe^Darlene^M||19820530|F||Hispanic|1889 Wattle St^APT215^Hermosa Beach^NY^916518712||(159) 052-1309|(214)555-1212X00019||||401585549515|644-11-8968|
PV1|1|P|^^^00002|R||00019|8866423^Burgess^Gretchen^L|||||||||||||00111|
DG1|0001|I9||NODX||W|||||||||01|6142326^Solomon^Bobby^L|
GT1|0001|3322261701|Gilliam^Kyler^V||5008 SOMEPLACE RD^APT215^FT WORTH^TX^76132-0000|(817)555-1212|(214)555-1212X00019|
IN1|0001|0000008|0000114|UNITED HEALTH  87726|P O BOX 740800^^ATLANTA^GA^30374-0800||(800)842-5724|||||20000401|||P|OYLE^OLIVE^M|00002|19760824|5008 SOMEPLACE RD^APT215^FT WORTH^TX^76132-0000|Y|Y||||||A|||||||||234166342|||||||F|
IN2||234166342|0009999^UNKNOWN||I|'''

    message = parse_message(msg)

    # establish the connection+
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port))
        # send the message
        sock.sendall(message.to_mllp().encode('UTF-8'))
        # receive the answer
        received = sock.recv(1024*1024)
        print("Received response: ")
        print(repr(received))
    finally:
        pass
        # sock.close()


if __name__ == '__main__':
    res = query('localhost', 21110)
