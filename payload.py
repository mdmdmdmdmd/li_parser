from common import parse_common, Payload
from iri_payload import parse_iri_payload
from cc_payload import parse_cc_payload


def parse_payload(result: bytes) -> dict:
    ilc, length, _ = parse_common(result)
    position = 0
    result = {}
    while length > position:
        element, el_length, add_to_pos = parse_common(ilc.content[position:])
        idx = element.tag.nr
        if idx == Payload.iRIPayloadSequence.value:
            result[Payload.iRIPayloadSequence.name] = parse_iri_payload(element.content)
            position += add_to_pos
        if idx == Payload.cCPayloadSequence.value:
            result[Payload.cCPayloadSequence.name] = parse_cc_payload(element.content)
            position += add_to_pos
        position += el_length + 2
    return result
