from common import (
    parse_address,
    parse_common,
    parse_oid,
    parse_ms_ts,
    parse_address,
    IRIPayload,
    IRIType,
    TimeStampQualifier,
    PayloadDirection,
    IRIContents,
    IPMMIRI,
    IPIRIContents,
    SIPMessage,
    IPAddress,
    IPType,
    IPAssignment,
    IP_Value,
)


def parse_ip_value(payload: bytes) -> dict:
    ilc, length, _ = parse_common(payload)
    position = 0
    result = {}
    while length > position:
        element, el_length, add_to_pos = parse_common(ilc.content[position:])
        idx = element.tag.nr
        if idx == IP_Value.iPBinaryAddress.value:
            result[IP_Value.iPBinaryAddress.name] = parse_address(element.content)
            position += add_to_pos
        if idx == IP_Value.iPTextAddress.value:
            result[IP_Value.iPTextAddress.name] = element.content.decode()
            position += add_to_pos
        position += el_length + 2
    return result


def parse_ip_addr(payload: bytes) -> dict:
    ilc, length, _ = parse_common(payload)
    position = 0
    result = {}
    while length > position:
        element, el_length, add_to_pos = parse_common(ilc.content[position:])
        idx = element.tag.nr
        if idx == IPAddress.iP_type.value:
            result[IPAddress.iP_type.name] = IPType(
                int.from_bytes(element.content, "big", signed=False)
            ).name
            position += add_to_pos
        if idx == IPAddress.iP_value.value:
            result[IPAddress.iP_value.name] = parse_ip_value(ilc.content[position:])
            position += add_to_pos
        if idx == IPAddress.iP_assignment.value:
            result[IPAddress.iP_assignment.name] = IPAssignment(
                int.from_bytes(element.content, "big", signed=False)
            ).name
            position += add_to_pos
        if idx == IPAddress.iPv6PrefixLength.value:
            result[IPAddress.iPv6PrefixLength.name] = int.from_bytes(
                element.content, "big", signed=False
            )
            position += add_to_pos
        if idx == IPAddress.iPv4SubnetMask.value:
            result[IPAddress.iPv4SubnetMask.name] = parse_address(element.content)
            position += add_to_pos
        position += el_length + 2
    return result


def parse_sip_msg(payload: bytes) -> dict:
    ilc, length, _ = parse_common(payload)
    position = 0
    result = {}
    while length > position:
        element, el_length, add_to_pos = parse_common(ilc.content[position:])
        idx = element.tag.nr
        if idx == SIPMessage.iPSourceAddress.value:
            result[SIPMessage.iPSourceAddress.name] = parse_ip_addr(
                ilc.content[position:]
            )
            position += add_to_pos
        if idx == SIPMessage.iPDestinationAddress.value:
            result[SIPMessage.iPDestinationAddress.name] = parse_ip_addr(
                ilc.content[position:]
            )
            position += add_to_pos
        if idx == SIPMessage.sIPContent.value:
            result[SIPMessage.sIPContent.name] = element.content.decode()
            position += add_to_pos
        position += el_length + 2
    return result


def parse_ipiri_contents(payload: bytes) -> dict:
    ilc, length, _ = parse_common(payload)
    position = 0
    result = {}
    while length > position:
        element, el_length, add_to_pos = parse_common(ilc.content[position:])
        idx = element.tag.nr
        if idx == IPIRIContents.originalIPMMMessage.value:
            result[
                IPIRIContents.originalIPMMMessage.name
            ] = "parsing not implemented"
            position += add_to_pos
        if idx == IPIRIContents.sIPMessage.value:
            result[IPIRIContents.sIPMessage.name] = parse_sip_msg(
                ilc.content[position:]
            )
            position += add_to_pos
        if idx == IPIRIContents.h323Message.value:
            result[
                IPIRIContents.h323Message.name
            ] = "parsing not implemented"
            position += add_to_pos
        if idx == IPIRIContents.nationalIPMMIRIParameters.value:
            result[
                IPIRIContents.nationalIPMMIRIParameters.name
            ] = "parsing not implemented"
            position += add_to_pos
        if idx == IPIRIContents.xCAPMessage.value:
            result[
                IPIRIContents.xCAPMessage.name
            ] = "parsing not implemented"
            position += add_to_pos
        position += el_length + add_to_pos
    return result


def parse_ipmmiri(payload: bytes) -> dict:
    ilc, length, _ = parse_common(payload)
    position = 0
    result = {}
    while length > position:
        element, el_length, add_to_pos = parse_common(ilc.content[position:])
        idx = element.tag.nr
        if idx == IPMMIRI.iPMMIRIObjId.value:
            _, oid = parse_oid(element.content)
            result[IPMMIRI.iPMMIRIObjId.name] = oid
            position += add_to_pos
        if idx == IPMMIRI.iPMMIRIContents.value:
            result[IPMMIRI.iPMMIRIContents.name] = parse_ipiri_contents(
                ilc.content[position:]
            )
            position += add_to_pos
        if idx == IPMMIRI.targetLocation.value:
            result[IPMMIRI.targetLocation.name] = "parsing not implemented"
            position += add_to_pos
        if idx == IPMMIRI.additionalSignalling.value:
            result[
                IPMMIRI.additionalSignalling.name
            ] = "parsing not implemented"
            position += add_to_pos
        position += el_length + 2
    return result


def parse_iri_contents(payload: bytes) -> dict:
    ilc, length, _ = parse_common(payload)
    position = 0
    result = {}
    while length > position:
        element, el_length, add_to_pos = parse_common(ilc.content[position:])
        idx = element.tag.nr
        if idx == IRIContents.iPMMIRI.value:
            result[IRIContents.iPMMIRI.name] = parse_ipmmiri(ilc.content[position:])
            position += add_to_pos
        position += el_length + 2
    return result


def parse_iri_payload(payload: bytes) -> dict:
    ilc, length, _ = parse_common(payload)
    position = 0
    result = {}
    while length > position:
        element, el_length, add_to_pos = parse_common(ilc.content[position:])
        idx = element.tag.nr
        if idx == IRIPayload.iRIType.value:
            result[IRIPayload.iRIType.name] = IRIType(
                int.from_bytes(element.content, "big", signed=False)
            ).name
            position += add_to_pos
        if idx == IRIPayload.timeStamp.value:
            result[IRIPayload.timeStamp.name] = element.content.decode()
            position += add_to_pos
        if idx == IRIPayload.iRIContents.value:
            result[IRIPayload.iRIContents.name] = parse_iri_contents(
                ilc.content[position:]
            )
            position += add_to_pos
        if idx == IRIPayload.microSecondTimeStamp.value:
            result[IRIPayload.microSecondTimeStamp.name] = parse_ms_ts(
                ilc.content[position:]
            )
            position += add_to_pos
        if idx == IRIPayload.timeStampQualifier.value:
            result[IRIPayload.timeStampQualifier.name] = TimeStampQualifier(
                int.from_bytes(element.content, "big", signed=False)
            ).name
            position += add_to_pos
        if idx == IRIPayload.sessionDirection.value:
            result[IRIPayload.sessionDirection.name] = PayloadDirection(
                int.from_bytes(element.content, "big", signed=False)
            ).name
            position += add_to_pos
        if idx == IRIPayload.payloadDirection.value:
            result[IRIPayload.payloadDirection.name] = PayloadDirection(
                int.from_bytes(element.content, "big", signed=False)
            ).name
            position += add_to_pos
        position += el_length + 2
    return result
