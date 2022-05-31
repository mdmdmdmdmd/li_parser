from common import (
    parse_common,
    parse_oid,
    parse_ms_ts,
    NetworkIdentifier,
    CommunicationIdentifier,
    PSHeader,
    TimeStampQualifier,
)


def parse_ni(payload: bytes) -> dict:
    ilc, length, _ = parse_common(payload)
    position = 0
    result = {}
    while length > position:
        element, el_length, add_to_pos = parse_common(ilc.content[position:])
        idx = element.tag.nr
        if idx == NetworkIdentifier.operatorIdentifier.value:
            result[NetworkIdentifier.operatorIdentifier.name] = element.content.decode()
            position += add_to_pos
        if idx == NetworkIdentifier.networkElementIdentifier.value:
            result[NetworkIdentifier.networkElementIdentifier.name] = element.content.decode()
            position += add_to_pos
        if idx == NetworkIdentifier.eTSI671NEID.value:
            result[NetworkIdentifier.eTSI671NEID.name] = "parsing not implemented"
            position += add_to_pos
        position += el_length + 2
    return result


def parse_com_id(payload: bytes) -> dict:
    ilc, length, _ = parse_common(payload)
    position = 0
    result = {}
    while length > position:
        element, el_length, add_to_pos = parse_common(ilc.content[position:])
        idx = element.tag.nr
        if idx == CommunicationIdentifier.networkIdentifier.value:
            result[CommunicationIdentifier.networkIdentifier.name] = parse_ni(
                ilc.content[position:]
            )
            position += add_to_pos
        if idx == CommunicationIdentifier.communicationIdentityNumber.value:
            result[
                CommunicationIdentifier.communicationIdentityNumber.name
            ] = int.from_bytes(element.content, "big", signed=False)
            position += add_to_pos
        if idx == CommunicationIdentifier.deliveryCountryCode.value:
            result[
                CommunicationIdentifier.deliveryCountryCode.name
            ] = element.content.decode()
            position += add_to_pos
        if idx == CommunicationIdentifier.cINExtension.value:
            result[
                CommunicationIdentifier.cINExtension.name
            ] = "parsing not implemented"
            position += add_to_pos
        position += el_length + 2
    return result


def parse_ps_header(payload: bytes) -> dict:
    ilc, length, _ = parse_common(payload)
    position = 0
    result = {}
    while length > position:
        element, el_length, add_to_pos = parse_common(ilc.content[position:])
        idx = element.tag.nr
        if idx == PSHeader.li_psDomainId.value:
            _, oid = parse_oid(element.content)
            result[PSHeader.li_psDomainId.name] = oid
            position += add_to_pos
        if idx == PSHeader.lawfulInterceptionIdentifier.value:
            result[
                PSHeader.lawfulInterceptionIdentifier.name
            ] = element.content.decode()
            position += add_to_pos
        if idx == PSHeader.authorizationCountryCode.value:
            result[PSHeader.authorizationCountryCode.name] = element.content.decode()
            position += add_to_pos
        if idx == PSHeader.communicationIdentifier.value:
            result[PSHeader.communicationIdentifier.name] = parse_com_id(
                ilc.content[position:]
            )
            position += add_to_pos
        if idx == PSHeader.sequenceNumber.value:
            result[PSHeader.sequenceNumber.name] = int.from_bytes(
                element.content, "big", signed=False
            )
            position += add_to_pos
        if idx == PSHeader.timeStamp.value:
            result[PSHeader.timeStamp.name] = element.content.decode()
            position += add_to_pos
        if idx == PSHeader.interceptionPointID.value:
            result[PSHeader.interceptionPointID.name] = element.content.decode()
            position += add_to_pos
        if idx == PSHeader.microSecondTimeStamp.value:
            result[PSHeader.microSecondTimeStamp.name] = parse_ms_ts(
                ilc.content[position:]
            )
            position += add_to_pos
        if idx == PSHeader.timeStampQualifier.value:
            result[PSHeader.timeStampQualifier.name] = TimeStampQualifier(
                int.from_bytes(element.content, "big", signed=False)
            ).name
            position += add_to_pos
        position += el_length + 2
    return result
