from common import (
    parse_common,
    parse_ms_ts,
    parse_oid,
    IPMMCC,
    CCPayload,
    CCContents,
    FrameType,
    MMCCprotocol,
    PayloadDirection,
    TimeStampQualifier,
)


def parse_ipmmcc(payload: bytes) -> dict:
    ilc, length, _ = parse_common(payload)
    position = 0
    result = {}
    while length > position:
        element, el_length, add_to_pos = parse_common(ilc.content[position:])
        idx = element.tag.nr
        if idx == IPMMCC.iPMMCCObjId.value:
            _, oid = parse_oid(element.content)
            result[IPMMCC.iPMMCCObjId.name] = oid
            position += add_to_pos
        if idx == IPMMCC.mMCCContents.value:
            result[IPMMCC.mMCCContents.name] = element.content.hex()
            position += add_to_pos
        if idx == IPMMCC.frameType.value:
            result[IPMMCC.frameType.name] = FrameType(
                int.from_bytes(element.content, "big", signed=False)
            ).name
            position += add_to_pos
        if idx == IPMMCC.streamIdentifier.value:
            result[IPMMCC.streamIdentifier.name] = element.content.decode()
            position += add_to_pos
        if idx == IPMMCC.mMCCprotocol.value:
            result[IPMMCC.mMCCprotocol.name] = MMCCprotocol(
                int.from_bytes(element.content, "big", signed=False)
            ).name
            position += add_to_pos
        position += el_length + 2
    return result


def parse_ccc_contents(payload: bytes) -> dict:
    ilc, length, _ = parse_common(payload)
    position = 0
    result = {}
    while length > position:
        element, el_length, add_to_pos = parse_common(ilc.content[position:])
        idx = element.tag.nr
        if idx == CCContents.emailCC.value:
            result[CCContents.emailCC.name] = "parsing not implemented"
            position += add_to_pos
        if idx == CCContents.iPCC.value:
            result[CCContents.iPCC.name] = "parsing not implemented"
            position += add_to_pos
        if idx == CCContents.uMTSCC.value:
            result[CCContents.uMTSCC.name] = "parsing not implemented"
            position += add_to_pos
        if idx == CCContents.l2CC.value:
            result[CCContents.l2CC.name] = "parsing not implemented"
            position += add_to_pos
        if idx == CCContents.tTRAFFIC_1.value:
            result[CCContents.tTRAFFIC_1.name] = "parsing not implemented"
            position += add_to_pos
        if idx == CCContents.cTTRAFFIC_1.value:
            result[CCContents.cTTRAFFIC_1.name] = "parsing not implemented"
            position += add_to_pos
        if idx == CCContents.tTRAFFIC_2.value:
            result[CCContents.tTRAFFIC_2.name] = "parsing not implemented"
            position += add_to_pos
        if idx == CCContents.cTTRAFFIC_2.value:
            result[CCContents.cTTRAFFIC_2.name] = "parsing not implemented"
            position += add_to_pos
        if idx == CCContents.pstnIsdnCC.value:
            result[CCContents.pstnIsdnCC.name] = "parsing not implemented"
            position += add_to_pos
        if idx == CCContents.iPMMCC.value:
            result[CCContents.iPMMCC.name] = parse_ipmmcc(ilc.content[position:])
            position += add_to_pos
        if idx == CCContents.cCIPPacketHeader.value:
            result[CCContents.cCIPPacketHeader.name] = "parsing not implemented"
            position += add_to_pos
        if idx == CCContents.messagingCC.value:
            result[CCContents.messagingCC.name] = "parsing not implemented"
            position += add_to_pos
        if idx == CCContents.ePSCC.value:
            result[CCContents.ePSCC.name] = "parsing not implemented"
            position += add_to_pos
        if idx == CCContents.uMTSCC_CC_PDU.value:
            result[CCContents.uMTSCC_CC_PDU.name] = "parsing not implemented"
            position += add_to_pos
        if idx == CCContents.ePSCC_CC_PDU.value:
            result[CCContents.ePSCC_CC_PDU.name] = "parsing not implemented"
            position += add_to_pos
        if idx == CCContents.messagingMMCC.value:
            result[CCContents.messagingMMCC.name] = "parsing not implemented"
            position += add_to_pos
        if idx == CCContents.confCC_CC_PDU.value:
            result[CCContents.confCC_CC_PDU.name] = "parsing not implemented"
            position += add_to_pos
        if idx == CCContents.voipCC_CC_PDU.value:
            result[CCContents.voipCC_CC_PDU.name] = "parsing not implemented"
            position += add_to_pos
        if idx == CCContents.gcseCC_CC_PDU.value:
            result[CCContents.gcseCC_CC_PDU.name] = "parsing not implemented"
            position += add_to_pos
        if idx == CCContents.cSvoice_CC_PDU.value:
            result[CCContents.cSvoice_CC_PDU.name] = "parsing not implemented"
            position += add_to_pos
        if idx == CCContents.threeGPP33128DefinedCC.value:
            result[CCContents.threeGPP33128DefinedCC.name] = "parsing not implemented"
            position += add_to_pos
        position += el_length + 2
    return result


def parse_cc_payload(payload: bytes) -> dict:
    ilc, length, _ = parse_common(payload)
    position = 0
    result = {}
    while length > position:
        element, el_length, add_to_pos = parse_common(ilc.content[position:])
        idx = element.tag.nr
        if idx == CCPayload.payloadDirection.value:
            result[CCPayload.payloadDirection.name] = PayloadDirection(
                int.from_bytes(element.content, "big", signed=False)
            ).name
            position += add_to_pos
        if idx == CCPayload.timeStamp.value:
            result[CCPayload.timeStamp.name] = element.content.decode()
            position += add_to_pos
        if idx == CCPayload.cCContents.value:
            result[CCPayload.cCContents.name] = parse_ccc_contents(
                ilc.content[position:]
            )
            position += add_to_pos
        if idx == CCPayload.microSecondTimeStamp.value:
            result[CCPayload.microSecondTimeStamp.name] = parse_ms_ts(
                ilc.content[position:]
            )
            position += add_to_pos
        if idx == CCPayload.timeStampQualifier.value:
            result[CCPayload.timeStampQualifier.name] = TimeStampQualifier(
                int.from_bytes(element.content, "big", signed=False)
            ).name
            position += add_to_pos
        position += el_length + 2
    return result
