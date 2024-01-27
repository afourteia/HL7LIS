from hl7apy.core import Message, Segment

def create_ack_message(temp_message_dict, response_type = ""):
    # Create the message with MSH and ACK segments
    message = Message()
    # print(message.to_er7())
    # print(message.children)
    # print(message.msa.to_er7())

    if response_type == "ACK^R01":
        message = Message('ACK')
        # Add segments to the message
        message.add_segment('MSA')
    elif response_type == "QCK^Q02":
        message = Message("QCK")
        # Add segments to the message
        message.add_segment('MSA')
        message.add_segment('ERR')
        message.add_segment('QAK')
        err_segment = Segment('ERR')
        err_segment.err_1 = temp_message_dict["error_code_and_location"]
        message.err = err_segment
        qak_segment = Segment('QAK')
        qak_segment.qak_1 = temp_message_dict["query_tag"]
        qak_segment.qak_2 = temp_message_dict["query_response_status"]
        message.qak = qak_segment

    elif response_type == "DSR^Q03":
        message = Message("DSR")
        # Add segments to the message
        message.add_segment('MSA')
        message.add_segment('ERR')
        message.add_segment('QAK')
        message.add_segment('QRD')
        message.add_segment('QRF')
        err_segment = Segment('ERR')
        err_segment.err_1 = temp_message_dict["error_code_and_location"]
        message.err = err_segment
        qak_segment = Segment('QAK')
        qak_segment.qak_1 = temp_message_dict["query_tag"]
        qak_segment.qak_2 = temp_message_dict["query_response_status"]
        message.qak = qak_segment
        qrd_segment = Segment('QRD')
        message.qrd = qrd_segment
        qrf_segment = Segment('QRF')
        message.qrf = qrf_segment
        
    # Populate the MSH segment
    msh_segment = Segment('MSH')
    msh_segment = parse_segment(message.msh.to_er7())
    msh_segment.msh_3 =     temp_message_dict["sending_application"]
    msh_segment.msh_4 =     temp_message_dict["sending_facility"]
    msh_segment.msh_5 =     temp_message_dict["receiving_application"]
    msh_segment.msh_6 =     temp_message_dict["receiving_facility"]
    msh_segment.msh_9 =     temp_message_dict["message_type"]
    msh_segment.msh_10 =    temp_message_dict["message_control_id"]
    msh_segment.msh_11 =    temp_message_dict["processing_id"]
    message.msh = msh_segment

    

    # Populate the MSA segment
    msa_segment = Segment('MSA')
    # msa_segment = parse_segment(message.msa.to_er7())
    msa_segment.msa_1 = temp_message_dict["acknowledgment_code"]
    msa_segment.msa_2 = temp_message_dict["message_control_id"]
    msa_segment.msa_3 = temp_message_dict["text_message"]
    msa_segment.msa_6 = temp_message_dict["error_condition"]        
    message.msa = msa_segment

    # print(msh_segment.to_er7())
    # print(msa_segment.to_er7())


    
    message.validate()

    # Return the message
    return message