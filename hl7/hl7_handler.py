import hl7apy
from hl7apy import parser
from hl7apy.exceptions import UnsupportedVersion ,ParserError
from pprint import pprint
hl7apy.set_default_version('2.3.1')
hl7apy.get_default_version()
from datetime import datetime
import json
from hl7apy.core import Message, Segment
from hl7apy.parser import parse_message
from hl7apy.core import Message
from hl7apy.parser import parse_segment

# hl7 segments
# MSH – Message header
# OBR  Observation request
# OBX  Observation result
# PID  Patient identification
FIELD_COUNT_MSH = 20
FIELD_COUNT_PID = 30
FIELD_COUNT_MSA = 6
FIELD_COUNT_ERR = 4
FIELD_COUNT_OBR = 45
FIELD_COUNT_OBX = 17
FIELD_COUNT_QRD = 12
FIELD_COUNT_QRF = 9
FIELD_COUNT_QAK = 2
FIELD_COUNT_DSP = 5
FIELD_COUNT_DSC = 1
hl7_message = "MSH|^~\\&|SENDING_APPLICATION2|SENDING_FACILITY|RECEIVING_APPLICATION|RECEIVING_FACILITY|202212290801||ADT^A01|93457|P|2.5|||||"

# general parser
def parce_hl7_message(hl7_message):
    
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
                index =list(seg.__dict__["children"]).index(element)
                print(element.name)
                # dict_message[seg.name][element.long_name] = element.value
                seg_element_dict = {}
                seg_element_dict['name'] = element.name
                seg_element_dict['long_name'] = element.long_name
                seg_element_dict['value'] = element.value
                dict_message[seg.name][index+1] = seg_element_dict
                # print(element.long_name)
        print(dict_message)
        with open("parsed_message.json", "w") as outfile: 
            json.dump(dict_message, outfile)
        return hl7_message
        # print(m.msh.msh_9.value)
        # print(m.msh.msh_3.value)
        # print(type(m.msh.msh_9.__dict__['element_list'][3]))
        # print(m.msh.msh_9.__dict__['element_list'][3].__dict__.values())
        # print(m.msh.msh_9.__dict__['element_list'][3])
    except ParserError:
        print("ParserError Invalid message")
    except UnsupportedVersion:
        print("Unsupported version, trying to parse the message with the generic parser")
    
# custom parsers
def parse_msh_segment(msh):
    segment_MSH = {
        "field_separator": msh.msh_1.value if msh.msh_1.value else None,
        "encoding_characters": msh.msh_2.value if msh.msh_2.value else None,
        "sending_application": msh.msh_3.value if msh.msh_3.value else None,
        "sending_facility": msh.msh_4.value if msh.msh_4.value else None,
        "receiving_application": msh.msh_5.value if msh.msh_5.value else None,
        "receiving_facility": msh.msh_6.value if msh.msh_6.value else None,
        # "datetime": datetime.datetime.strptime(msh.msh_7.value, "%Y%m%d%H%M%S%f") if msh.msh_7.value else None,
        "security": msh.msh_8.value if msh.msh_8.value else None,
        "message_type": msh.msh_9.value if msh.msh_9.value else None,
        "message_control_id": msh.msh_10.value if msh.msh_10.value else None,
        "processing_id": msh.msh_11.value if msh.msh_11.value else None,
        "version_id": msh.msh_12.value if msh.msh_12.value else None,
        "sequence_number": msh.msh_13.value if msh.msh_13.value else None,
        "continuation_pointer": msh.msh_14.value if msh.msh_14.value else None,
        "accept_acknowledgment_type": msh.msh_15.value if msh.msh_15.value else None,
        "application_acknowledgment_type": msh.msh_16.value if msh.msh_16.value else None,
        "country_code": msh.msh_17.value if msh.msh_17.value else None,
        "character_set": msh.msh_18.value if msh.msh_18.value else None,
        "principal_language_of_message": msh.msh_19.value if msh.msh_19.value else None,
        "alternate_character_set_handling_scheme": msh.msh_20.value if msh.msh_20.value else None
    }
    return segment_MSH




def parse_pid_segment(pid):
    segment_PID = {
        "set_id_pid": pid.pid_1.value if pid.pid_1.value else None,
        "patient_id": pid.pid_2.value if pid.pid_2.value else None,
        "patient_identifier_list": pid.pid_3.value if pid.pid_3.value else None,
        "alternate_patient_id_pid": pid.pid_4.value if pid.pid_4.value else None,
        "patient_name": pid.pid_5.value if pid.pid_5.value else None,
        "mother_maiden_name": pid.pid_6.value if pid.pid_6.value else None,
        "datetime_of_birth": pid.pid_7.value if pid.pid_7.value else None,
        "sex": pid.pid_8.value if pid.pid_8.value else None,
        "patient_alias": pid.pid_9.value if pid.pid_9.value else None,
        "race": pid.pid_10.value if pid.pid_10.value else None,
        "patient_address": pid.pid_11.value if pid.pid_11.value else None,
        "county_code": pid.pid_12.value if pid.pid_12.value else None,
        "phone_number_home": pid.pid_13.value if pid.pid_13.value else None,
        "phone_number_business": pid.pid_14.value if pid.pid_14.value else None,
        "primary_language": pid.pid_15.value if pid.pid_15.value else None,
        "marital_status": pid.pid_16.value if pid.pid_16.value else None,
        "religion": pid.pid_17.value if pid.pid_17.value else None,
        "patient_account_number": pid.pid_18.value if pid.pid_18.value else None,
        "ssn_number_patient": pid.pid_19.value if pid.pid_19.value else None,
        "drivers_license_number_patient": pid.pid_20.value if pid.pid_20.value else None,
        "mothers_identifier": pid.pid_21.value if pid.pid_21.value else None,
        "ethnic_group": pid.pid_22.value if pid.pid_22.value else None,
        "birth_place": pid.pid_23.value if pid.pid_23.value else None,
        "multiple_birth_indicator": pid.pid_24.value if pid.pid_24.value else None,
        "birth_order": pid.pid_25.value if pid.pid_25.value else None,
        "citizenship": pid.pid_26.value if pid.pid_26.value else None,
        "veterans_military_status": pid.pid_27.value if pid.pid_27.value else None,
        "nationality": pid.pid_28.value if pid.pid_28.value else None,
        "patient_death_date_and_time": pid.pid_29.value if pid.pid_29.value else None,
        "patient_death_indicator": pid.pid_30.value if pid.pid_30.value else None
    }
    return segment_PID


def parse_msa_segment(msa):
    segment_MSA = {
        "acknowledgment_code": msa.msa_1.value if msa.msa_1.value else None,
        "message_control_id": msa.msa_2.value if msa.msa_2.value else None,
        "text_message": msa.msa_3.value if msa.msa_3.value else None,
        "expected_sequence_number": msa.msa_4.value if msa.msa_4.value else None,
        "delayed_acknowledgment_type": msa.msa_5.value if msa.msa_5.value else None,
        "error_condition": msa.msa_6.value if msa.msa_6.value else None
    }
    return segment_MSA


def parse_obr_segment(obr):
    segment_OBR = {
        "set_id_obr": obr.obr_1.value if obr.obr_1.value else None,
        "placer_order_number": obr.obr_2.value if obr.obr_2.value else None,
        "filler_order_number": obr.obr_3.value if obr.obr_3.value else None,
        "universal_service_id": obr.obr_4.value if obr.obr_4.value else None,
        "priority": obr.obr_5.value if obr.obr_5.value else None,
        "requested_date_time": obr.obr_6.value if obr.obr_6.value else None,
        "observation_date_time": obr.obr_7.value if obr.obr_7.value else None,
        "observation_end_date_time": obr.obr_8.value if obr.obr_8.value else None,
        "collection_volume": obr.obr_9.value if obr.obr_9.value else None,
        "collector_identifier": obr.obr_10.value if obr.obr_10.value else None,
        "specimen_action_code": obr.obr_11.value if obr.obr_11.value else None,
        "danger_code": obr.obr_12.value if obr.obr_12.value else None,
        "relevant_clinical_info": obr.obr_13.value if obr.obr_13.value else None,
        "specimen_received_date_time": obr.obr_14.value if obr.obr_14.value else None,
        "specimen_source": obr.obr_15.value if obr.obr_15.value else None,
        "ordering_provider": obr.obr_16.value if obr.obr_16.value else None,
        "order_callback_phone_number": obr.obr_17.value if obr.obr_17.value else None,
        "placer_field_1": obr.obr_18.value if obr.obr_18.value else None,
        "placer_field_2": obr.obr_19.value if obr.obr_19.value else None,
        "filler_field_1": obr.obr_20.value if obr.obr_20.value else None,
        "filler_field_2": obr.obr_21.value if obr.obr_21.value else None,
        "result_rpt_status_change_date_time": obr.obr_22.value if obr.obr_22.value else None,
        "charge_to_practice": obr.obr_23.value if obr.obr_23.value else None,
        "diagnostic_serv_sect_id": obr.obr_24.value if obr.obr_24.value else None,
        "result_status": obr.obr_25.value if obr.obr_25.value else None,
        "parent_result": obr.obr_26.value if obr.obr_26.value else None,
        "quantity_timing": obr.obr_27.value if obr.obr_27.value else None,
        "result_copies_to": obr.obr_28.value if obr.obr_28.value else None,
        "parent": obr.obr_29.value if obr.obr_29.value else None,
        "transportation_mode": obr.obr_30.value if obr.obr_30.value else None,
        "reason_for_study": obr.obr_31.value if obr.obr_31.value else None,
        "principal_result_interpreter": obr.obr_32.value if obr.obr_32.value else None,
        "assistant_result_interpreter": obr.obr_33.value if obr.obr_33.value else None,
        "technician": obr.obr_34.value if obr.obr_34.value else None,
        "transcriptionist": obr.obr_35.value if obr.obr_35.value else None,
        "scheduled_date_time": obr.obr_36.value if obr.obr_36.value else None,
        "number_of_sample_containers": obr.obr_37.value if obr.obr_37.value else None,
        "transport_logistics_of_collected_sample": obr.obr_38.value if obr.obr_38.value else None,
        "collector_comment": obr.obr_39.value if obr.obr_39.value else None,
        "transport_arrangement_responsibility": obr.obr_40.value if obr.obr_40.value else None,
        "transport_arranged": obr.obr_41.value if obr.obr_41.value else None,
        "escort_required": obr.obr_42.value if obr.obr_42.value else None,
        "planned_patient_transport_comment": obr.obr_43.value if obr.obr_43.value else None,
        "ordering_facility_name": obr.obr_44.value if obr.obr_44.value else None,
        "ordering_facility_address": obr.obr_45.value if obr.obr_45.value else None,
        # "ordering_facility_phone_number": obr.obr_46.value if obr.obr_46.value else None,
        # "ordering_provider_address": obr.obr_47.value if obr.obr_47.value else None
    }
    return segment_OBR


def parse_obx_segments(obx_segments):
    segment_OBXs = []
    if not obx_segments:
        print("No OBX segments found in the HL7 message.")
    else:
        for obx in obx_segments:
            segment_OBX = {
                "set_id_obx": obx.obx_1.value if obx.obx_1.value else None,
                "value_type": obx.obx_2.value if obx.obx_2.value else None,
                "observation_identifier": obx.obx_3.value if obx.obx_3.value else None,
                "observation_sub_id": obx.obx_4.value if obx.obx_4.value else None,
                "observation_value": obx.obx_5.value if obx.obx_5.value else None,
                "units": obx.obx_6.value if obx.obx_6.value else None,
                "references_range": obx.obx_7.value if obx.obx_7.value else None,
                "abnormal_flags": obx.obx_8.value if obx.obx_8.value else None,
                "probability": obx.obx_9.value if obx.obx_9.value else None,
                "nature_of_abnormal_test": obx.obx_10.value if obx.obx_10.value else None,
                "observe_result_status": obx.obx_11.value if obx.obx_11.value else None,
                "date_last_observe_normal_values": obx.obx_12.value if obx.obx_12.value else None,
                "user_defined_access_checks": obx.obx_13.value if obx.obx_13.value else None,
                "date_time_of_the_observation": obx.obx_14.value if obx.obx_14.value else None,
                "producer_id": obx.obx_15.value if obx.obx_15.value else None,
                "responsible_observer": obx.obx_16.value if obx.obx_16.value else None,
                "observation_method": obx.obx_17.value if obx.obx_17.value else None
            }
            segment_OBXs.append(segment_OBX)

    return segment_OBXs



def parse_qrd_segment(qrd):
    segment_QRD = {
        "query_date_time": qrd.qrd_1.value if qrd.qrd_1.value else None,
        "query_format_code": qrd.qrd_2.value if qrd.qrd_2.value else None,
        "query_priority": qrd.qrd_3.value if qrd.qrd_3.value else None,
        "query_id": qrd.qrd_4.value if qrd.qrd_4.value else None,
        "deferred_response_type": qrd.qrd_5.value if qrd.qrd_5.value else None,
        "deferred_response_date_time": qrd.qrd_6.value if qrd.qrd_6.value else None,
        "quantity_limited_request": qrd.qrd_7.value if qrd.qrd_7.value else None,
        "who_subject_filter": qrd.qrd_8.value if qrd.qrd_8.value else None,
        "what_subject_filter": qrd.qrd_9.value if qrd.qrd_9.value else None,
        "what_department_data_code": qrd.qrd_10.value if qrd.qrd_10.value else None,
        "what_data_code_value_qual": qrd.qrd_11.value if qrd.qrd_11.value else None,
        "query_results_level": qrd.qrd_12.value if qrd.qrd_12.value else None
    }
    return segment_QRD



def parse_qrf_segment(qrf):
    segment_QRF = {
        "where_subject_filter": qrf.qrf_1.value if qrf.qrf_1.value else None,
        "when_data_start_datetime": qrf.qrf_2.value if qrf.qrf_2.value else None,
        "when_data_end_datetime": qrf.qrf_3.value if qrf.qrf_3.value else None,
        "what_user_qualifier": qrf.qrf_4.value if qrf.qrf_4.value else None,
        "other_qry_subject_filter": qrf.qrf_5.value if qrf.qrf_5.value else None,
        "which_datetime_qualifier": qrf.qrf_6.value if qrf.qrf_6.value else None,
        "which_datetime_status_qualifier": qrf.qrf_7.value if qrf.qrf_7.value else None,
        "datetime_selection_qualifier": qrf.qrf_8.value if qrf.qrf_8.value else None,
        "when_quantity_timing_qualifier": qrf.qrf_9.value if qrf.qrf_9.value else None
    }
    return segment_QRF

def parse_err_segment(err):
    segment_ERR = {
        "error_code_and_location": err.err_1.value if err.err_1.value else None
    }
    return segment_ERR


def parse_qak_segment(qak):
    segment_QAK = {
        "query_tag": qak.qak_1.value if qak.qak_1.value else None,
        "query_response_status": qak.qak_2.value if qak.qak_2.value else None
    }
    return segment_QAK



def parse_dsp_segment(dsp):
    segment_DSP = {}
    for i in range(1, len(dsp)):
        sequence_number = int(dsp[i].dsp_2.value)
        property_value = dsp[i].dsp_4.value if dsp[i].dsp_4.value else None

        if sequence_number == 1:
            segment_DSP["admission_number"] = property_value
        elif sequence_number == 2:
            segment_DSP["bed_number"] = property_value
        elif sequence_number == 3:
            segment_DSP["patient_name"] = property_value
        elif sequence_number == 4:
            segment_DSP["date_of_birth"] = property_value
        elif sequence_number == 5:
            segment_DSP["sex"] = property_value
        elif sequence_number == 6:
            segment_DSP["patient_alias"] = property_value
        elif sequence_number == 7:
            segment_DSP["race"] = property_value
        elif sequence_number == 8:
            segment_DSP["patient_address"] = property_value
        elif sequence_number == 9:
            segment_DSP["county_code"] = property_value
        elif sequence_number == 10:
            segment_DSP["home_phone_number"] = property_value
        elif sequence_number == 11:
            segment_DSP["business_phone_number"] = property_value
        elif sequence_number == 12:
            segment_DSP["primary_language"] = property_value
        elif sequence_number == 13:
            segment_DSP["marital_status"] = property_value
        elif sequence_number == 14:
            segment_DSP["religion"] = property_value
        elif sequence_number == 15:
            segment_DSP["patient_account_number"] = property_value
        elif sequence_number == 16:
            segment_DSP["social_security_number"] = property_value
        elif sequence_number == 17:
            segment_DSP["driver_license_number"] = property_value
        elif sequence_number == 18:
            segment_DSP["ethnic_group"] = property_value
        elif sequence_number == 19:
            segment_DSP["birth_place"] = property_value
        elif sequence_number == 20:
            segment_DSP["nationality"] = property_value
        elif sequence_number == 21:
            segment_DSP["bar_code"] = property_value
        elif sequence_number == 22:
            segment_DSP["sample_id"] = property_value
        elif sequence_number == 23:
            segment_DSP["sample_time"] = property_value
        elif sequence_number == 24:
            segment_DSP["stat_or_not"] = property_value
        elif sequence_number == 25:
            segment_DSP["collection_volume"] = property_value
        elif sequence_number == 26:
            segment_DSP["sample_type"] = property_value
        elif sequence_number == 27:
            segment_DSP["fetch_doctor"] = property_value
        elif sequence_number == 28:
            segment_DSP["fetch_department"] = property_value
        elif sequence_number >= 29:
            test_id, test_name, unit, normal_range = property_value.split("^")
            segment_DSP[f"test_{i-28}"] = {
                "test_id": test_id,
                "test_name": test_name,
                "unit": unit,
                "normal_range": normal_range
            }
    return segment_DSP


def parse_dsc_segment(dsc):
    segment_DSC = {
        "continuation_pointer": dsc.dsc_1.value if dsc.dsc_1.value else None
    }
    return segment_DSC




# def process_hl7_message(hl7_message, remove_none = False):
#     message_payload = parse_message(hl7_message.replace("\n", "\r"), find_groups=False)
#     message_type = message_payload.msh.msh_9.value
#     print(message_type)
#     message_dict_R = {}
#     message_dict_S = {}
#     response_payload = Message()
#     if message_type == "ORU^R01":
#         print("ORU^R01 message type detected.")
#         message_dict_R = unpack_oru_r01(message_payload, remove_none)
#         keys_to_copy = ['message_control_id', 'sending_application', 'sending_facility']
#         message_dict_S = {k: v for k, v in message_dict_R['MSH'].items() if k in keys_to_copy}
#         message_dict_S["receiving_application"] = message_dict_S.pop("sending_application")
#         message_dict_S["receiving_facility"] = message_dict_S.pop("sending_facility")
#         message_dict_S = combine_dicts(ack_r01_dict, message_dict_S)
#         message_dict_S = combine_dicts(default_message_dict, message_dict_S)
#         if remove_none:
#             message_dict_S = {k: v for k, v in message_dict_S.items() if v is not None}
#         response_payload = create_ack_message(message_dict_S, "ACK^R01") 
#     elif message_type == "QRY^Q02":
#         print("QRY^Q02 message type detected.")
#         message_dict_R = unpack_qry_q02(message_payload, remove_none)
#         keys_to_copy = ['message_control_id', 'sending_application', 'sending_facility']
#         message_dict_S = {k: v for k, v in message_dict_R['MSH'].items() if k in keys_to_copy}
#         message_dict_S["receiving_application"] = message_dict_S.pop("sending_application")
#         message_dict_S["receiving_facility"] = message_dict_S.pop("sending_facility")
#         message_dict_S["error_code_and_location"] = "0"
#         message_dict_S["query_tag"] = "SR"
#         message_dict_S["query_response_status"] = "NF" # OK: success, NF: no data found, AE: error
#         message_dict_S = combine_dicts(ack_r01_dict, message_dict_S)
#         message_dict_S = combine_dicts(default_message_dict, message_dict_S)
#         if remove_none:
#             message_dict_S = {k: v for k, v in message_dict_S.items() if v is not None}
#         response_payload = create_ack_message(message_dict_S, "QCK^Q02")
#     else:
#         print("Message type not supported.")
#     print(message_dict_R)
#     print('------------------')
#     print(message_dict_S)
#     print('------------------')
#     # print("receiving")
#     # print(message_payload.to_er7().replace("\r", "\n"))
#     # print("sending")
#     # print(ack_r01_payload.to_er7().replace("\r", "\n")
#     return message_dict_S, message_dict_R, response_payload

default_message_dict = {
    "sending_application": "Dalil App",
    "sending_facility": "Dalil Comp",
    "receiving_application": None,
    "receiving_facility": None,    
    "processing_id": "P",
    "character_set": "ASCII",    
    "country_code": None,
    "principal_language_of_message": None,
    "alternate_character_set_handling_scheme": None,
    "accept_acknowledgment_type": None,
}
ack_r01_dict = {
    "message_type": "ACK^RO1",
    "message_control_id": "1",
    "application_acknowledgment_type": 0, # 0: sample result, 1: calibration result, 2: QC result
    "acknowledgment_code": "AA",    # AA: accept, AE: error, AR: refuse
    "text_message": "Message accepted",
    "error_condition": "0" # codes available in PDF
}

def combine_dicts(dict1, dict2):
    combined_dict = {**dict1, **dict2}
    return combined_dict

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
    msh_segment.msh_3 =     temp_message_dict["sending_application"] if temp_message_dict["sending_application"] else ""
    msh_segment.msh_4 =     temp_message_dict["sending_facility"] if temp_message_dict["sending_facility"] else ""
    msh_segment.msh_5 =     temp_message_dict["receiving_application"] if temp_message_dict["receiving_application"] else ""
    msh_segment.msh_6 =     temp_message_dict["receiving_facility"] if temp_message_dict["receiving_facility"] else ""
    msh_segment.msh_9 =     temp_message_dict["message_type"] if temp_message_dict["message_type"] else ""
    msh_segment.msh_10 =    temp_message_dict["message_control_id"] if temp_message_dict["message_control_id"] else ""
    msh_segment.msh_11 =    temp_message_dict["processing_id"] if temp_message_dict["processing_id"] else ""
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



def remove_none_values(d):
    """
    Recursively remove keys with value of None from dictionary
    """
    if isinstance(d, dict):
        return {k: remove_none_values(v) for k, v in d.items() if v is not None}
    elif isinstance(d, list):
        return [remove_none_values(v) for v in d if v is not None]
    else:
        return d

def unpack_oru_r01(m_payload, remove_none=False):
    #unpack hl7 message
    segment_MSH = parse_msh_segment(m_payload.msh)
    segment_PID = parse_pid_segment(m_payload.pid)
    segment_OBR = parse_obr_segment(m_payload.obr)
    segment_OBXs = parse_obx_segments(m_payload.obx)
    combined_dict = {
        "MSH": segment_MSH,
        "PID": segment_PID,
        "OBR": segment_OBR,
        "OBXs": segment_OBXs
    }
    if remove_none:
        print("removing keys with none values")
        combined_dict = remove_none_values(combined_dict)
    return combined_dict

def unpack_qry_q02(m_payload, remove_none=False):
    #unpack hl7 message
    segment_MSH = parse_msh_segment(m_payload.msh)
    segment_QRD = parse_qrd_segment(m_payload.qrd)
    segment_QRF = parse_qrf_segment(m_payload.qrf)
    combined_dict = {
        "MSH": segment_MSH,
        "QRD": segment_QRD,
        "QRF": segment_QRF
    }
    if remove_none:
        print("removing keys with none values")
        combined_dict = remove_none_values(combined_dict)
    return combined_dict

def unpack_other(m_payload, remove_none=False):
    parce_hl7_message(m_payload)
    #unpack hl7 message
    print('unpack_other')
    # print(m_payload.to_er7())
    
    # segment_MSH = parse_msh_segment(m_payload.msh)
    # print(m_payload.msh.to_er7())
    # combined_dict = {
    #     "MSH": segment_MSH,
    # }
    # if remove_none:
    #     combined_dict = remove_none_values(combined_dict)
    # return combined_dict

def process_hl7_message(hl7_message, remove_none = False):
    message_payload = parse_message(hl7_message.replace("\n", "\r"), find_groups=False)
    message_type = message_payload.msh.msh_9.value
    print(message_type)
    message_dict_R = {}
    message_dict_S = {}
    response_payload = Message()
    if message_type == "ORU^R01":
        print("ORU^R01 message type detected.")
        message_dict_R = unpack_oru_r01(message_payload, remove_none)
        keys_to_copy = ['message_control_id', 'sending_application', 'sending_facility']
        message_dict_S = {k: v for k, v in message_dict_R['MSH'].items() if k in keys_to_copy}
        message_dict_S["receiving_application"] = message_dict_S.pop("sending_application")
        message_dict_S["receiving_facility"] = message_dict_S.pop("sending_facility")
        # message_dict_S.pop("message_type")
        message_dict_S = combine_dicts(ack_r01_dict, message_dict_S)
        message_dict_S = combine_dicts(default_message_dict, message_dict_S)
        if remove_none:
            message_dict_S = {k: v for k, v in message_dict_S.items() if v is not None}
        response_payload = create_ack_message(message_dict_S, "ACK^R01")
    elif message_type == "QRY^Q02":
        print("QRY^Q02 message type detected.")
        message_dict_R = unpack_qry_q02(message_payload, remove_none)
        keys_to_copy = ['message_control_id', 'sending_application', 'sending_facility']
        message_dict_S = {k: v for k, v in message_dict_R['MSH'].items() if k in keys_to_copy}
        message_dict_S["receiving_application"] = message_dict_S.pop("sending_application")
        message_dict_S["receiving_facility"] = message_dict_S.pop("sending_facility")
        message_dict_S["error_code_and_location"] = "0"
        message_dict_S["query_tag"] = "SR"
        message_dict_S["query_response_status"] = "NF" # OK: success, NF: no data found, AE: error
        message_dict_S = combine_dicts(ack_r01_dict, message_dict_S)
        message_dict_S = combine_dicts(default_message_dict, message_dict_S)
        if remove_none:
            message_dict_S = {k: v for k, v in message_dict_S.items() if v is not None}
        response_payload = create_ack_message(message_dict_S, "QCK^Q02")
    else:
        print("Message type not supported.")
        print('message_payload other')
        print(hl7_message)
        message_other= parse_message(hl7_message, find_groups=False)

        print(message_other.children)
        message_dict_R = unpack_other(hl7_message, remove_none)
        # message_dict_S = combine_dicts(default_message_dict, ack_r01_dict)
        # print(message_dict_R)
        # create_ack_message(message_dict_S, "")
    pprint(message_dict_R)
    print('------------------')
    pprint(message_dict_S)
    print('------------------')
    # print("receiving")
    # print(message_payload.to_er7().replace("\r", "\n"))
    # print("sending")
    # print(ack_r01_payload.to_er7().replace("\r", "\n"))
    return message_dict_S, message_dict_R, response_payload


