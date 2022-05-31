import enum

import construct


class Classes(enum.Enum):
    Universal = 0
    Application = 1
    Context = 2
    Private = 3


class Types(enum.Enum):
    Primitive = 0
    Constructed = 1


class Numbers(enum.Enum):
    EndOfContent = 0
    Boolean = 1
    Integer = 2
    BitString = 3
    OctetString = 4
    Null = 5
    ObjectIdentifier = 6
    ObjectDescriptor = 7
    External = 8
    Real = 9
    Enumerated = 10
    EmbeddedPDV = 11
    UTF8String = 12
    RelativeOID = 13
    Time = 14
    Reserved = 15
    Sequence = 16
    Set = 17
    NumericString = 18
    PrintableString = 19
    T61String = 20
    VideotexString = 21
    IA5String = 22
    UTCTime = 23
    GeneralizedTime = 24
    GraphicString = 25
    VisibleString = 26
    GeneralString = 27
    UniversalString = 28
    CharacterString = 29
    BMPString = 30
    Date = 31
    TimeOfDay = 32
    DateTime = 33
    Duration = 34
    OIDIRI = 35
    RelativeOIDIRI = 36


class PS_PDU(enum.Enum):
    pSHeader = 1
    payload = 2


class PSHeader(enum.Enum):
    li_psDomainId = 0
    lawfulInterceptionIdentifier = 1
    authorizationCountryCode = 2
    communicationIdentifier = 3
    sequenceNumber = 4
    timeStamp = 5
    interceptionPointID = 6
    microSecondTimeStamp = 7
    timeStampQualifier = 8


class CommunicationIdentifier(enum.Enum):
    networkIdentifier = 0
    communicationIdentityNumber = 1
    deliveryCountryCode = 2
    cINExtension = 3


class NetworkIdentifier(enum.Enum):
    operatorIdentifier = 0
    networkElementIdentifier = 1
    eTSI671NEID = 2


class TimeStampQualifier(enum.Enum):
    unknown = 0
    timeOfInterception = 1
    timeOfMediation = 2
    timeOfAggregation = 3


class MicroSecondTimeStamp(enum.Enum):
    seconds = 0
    microSeconds = 1


class Payload(enum.Enum):
    iRIPayloadSequence = 0
    cCPayloadSequence = 1
    tRIPayload = 2
    hI1_Operation = 3
    encryptionContainer = 4
    threeGPP_HI1_Operation = 5
    iLHIPayload = 6
    hI4Payload = 7


class IRIPayload(enum.Enum):
    iRIType = 0
    timeStamp = 1
    iRIContents = 2
    microSecondTimeStamp = 3
    timeStampQualifier = 4
    sessionDirection = 5
    payloadDirection = 6


class IRIType(enum.Enum):
    iRI_Begin = 1
    iRI_End = 2
    iRI_Continue = 3
    iRI_Report = 4


class IRIContents(enum.Enum):
    emailIRI = 1
    iPIRI = 2
    iPIRIOnly = 3
    uMTSIRI = 4
    eTSI671IRI = 5
    l2IRI = 6
    l2IRIOnly = 7
    tARGETACTIVITYMONITOR_1 = 8
    tARGETACTIVITYMONITOR_2 = 9
    pstnIsdnIRI = 10
    iPMMIRI = 11
    lAESProtocol = 12
    cDMA2000LAESMessage = 13
    messagingIRI = 14
    ePSIRI = 15
    confIRI = 16
    proseIRI = 17
    gcseIRI = 18
    threeGPP33128DefinedIRI = 19


class IPMMIRI(enum.Enum):
    iPMMIRIObjId = 0
    iPMMIRIContents = 1
    targetLocation = 2
    additionalSignalling = 3


class IPIRIContents(enum.Enum):
    originalIPMMMessage = 0
    sIPMessage = 1
    h323Message = 2
    nationalIPMMIRIParameters = 3
    xCAPMessage = 4


class SIPMessage(enum.Enum):
    iPSourceAddress = 0
    iPDestinationAddress = 1
    sIPContent = 2


class H323Message(enum.Enum):
    iPSourceAddress = 0
    iPDestinationAddress = 1
    h323Content = 2


class H323MessageContent(enum.Enum):
    h225CSMessageContent = 0
    h225RASMessageContent = 1
    h245MessageContent = 2
    genericMessageContent = 3


class NationalIPMMIRIParameters(enum.Enum):
    countryCode = 1


class AdditionalSignalling(enum.Enum):
    sipHeaderLine = 0


class IPAddress(enum.Enum):
    iP_type = 1
    iP_value = 2
    iP_assignment = 3
    iPv6PrefixLength = 4
    iPv4SubnetMask = 5


class IPType(enum.Enum):
    iPV4 = 0
    iPV6 = 1


class IPAssignment(enum.Enum):
    static = 1
    dynamic = 2
    notKnown = 3


class IP_Value(enum.Enum):
    iPBinaryAddress = 1
    iPTextAddress = 2


class PayloadDirection(enum.Enum):
    fromTarget = 0
    toTarget = 1
    indeterminate = 2
    combined = 3
    notapplicable = 4


class CCPayload(enum.Enum):
    payloadDirection = 0
    timeStamp = 1
    cCContents = 2
    microSecondTimeStamp = 3
    timeStampQualifier = 4


class CCContents(enum.Enum):
    emailCC = 1
    iPCC = 2
    uMTSCC = 4
    l2CC = 6
    tTRAFFIC_1 = 7
    cTTRAFFIC_1 = 8
    tTRAFFIC_2 = 9
    cTTRAFFIC_2 = 10
    pstnIsdnCC = 11
    iPMMCC = 12
    cCIPPacketHeader = 13
    messagingCC = 14
    ePSCC = 15
    uMTSCC_CC_PDU = 16
    ePSCC_CC_PDU = 17
    messagingMMCC = 18
    confCC_CC_PDU = 19
    voipCC_CC_PDU = 20
    gcseCC_CC_PDU = 21
    cSvoice_CC_PDU = 22
    threeGPP33128DefinedCC = 23


class IPMMCC(enum.Enum):
    iPMMCCObjId = 0
    mMCCContents = 1
    frameType = 2
    streamIdentifier = 3
    mMCCprotocol = 4


class FrameType(enum.Enum):
    ipFrame = 0
    udpFrame = 1
    rtpFrame = 2
    audioFrame = 3
    tcpFrame = 4
    artificialRtpFrame = 5
    udptlFrame = 6
    msrpFrame = 7


class MMCCprotocol(enum.Enum):
    rTP = 0
    mSRP = 1
    uDPTL = 2


ILC = construct.Struct(
    "tag"
    / construct.BitStruct(
        "cls" / construct.BitsInteger(2),
        "typ" / construct.BitsInteger(1),
        "nr" / construct.BitsInteger(5),
    ),
    "length" / construct.Int8ub,
    "exp_length"
    / construct.IfThenElse(
        construct.this.length > 128,
        construct.IfThenElse(
            construct.this.length == 129, construct.Int8ub, construct.Int16ub
        ),
        construct.Padding(0),
    ),
    "content"
    / construct.IfThenElse(
        construct.this.length > 128,
        construct.Bytes(construct.this.exp_length),
        construct.Bytes(construct.this.length),
    ),
)


def parse_address(raw: bytes) -> str:
    address = ""
    divider = "."
    if len(raw) > 4:
        divider = ":"
    for number in raw:
        address += f"{number}{divider}"
    return address[:-1]


def parse_oid(raw: bytes) -> tuple[list[int], str]:
    oid: list[int] = [0]
    oid_str: str = "0"
    for number in raw:
        oid.append(number)
        oid_str += f".{number}"
    return oid, oid_str


def parse_common(payload: bytes) -> tuple[ILC, int, int]:
    ilc = ILC.parse(payload)
    position = 0
    length = ilc.length
    if length == 129:
        position = 1
    if length == 130:
        position = 2
    if ilc.exp_length is not None:
        length = ilc.exp_length
    return ilc, length, position


def parse_ms_ts(payload: bytes) -> dict:
    ilc, length, _ = parse_common(payload)
    position = 0
    result = {}
    while length > position:
        element, el_length, add_to_pos = parse_common(ilc.content[position:])
        idx = element.tag.nr
        if idx == MicroSecondTimeStamp.seconds.value:
            result[MicroSecondTimeStamp.seconds.name] = int.from_bytes(
                element.content, "big", signed=False
            )
            position += add_to_pos
        if idx == MicroSecondTimeStamp.microSeconds.value:
            result[MicroSecondTimeStamp.microSeconds.name] = int.from_bytes(
                element.content, "big", signed=False
            )
            position += add_to_pos
        position += el_length + 2
    return result
