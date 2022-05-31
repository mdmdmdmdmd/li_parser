from common import parse_common, PS_PDU
from ps_header import parse_ps_header
from payload import parse_payload


def parse_ps_pdu(payload: bytes) -> tuple[int, dict]:
    ilc, length, _ = parse_common(payload)
    position = 0
    result = {}
    while length > position:
        element, el_length, add_to_pos = parse_common(ilc.content[position:])
        idx = element.tag.nr
        if idx == PS_PDU.pSHeader.value:
            result[PS_PDU.pSHeader.name] = parse_ps_header(ilc.content[position:])
            position += add_to_pos
        elif idx == PS_PDU.payload.value:
            result[PS_PDU.payload.name] = parse_payload(ilc.content[position:])
            position += add_to_pos
        else:
            raise Exception
            # position += add_to_pos
        position += el_length + 2
    return position, result
