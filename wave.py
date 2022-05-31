import construct


FACT = construct.Struct(
    "extraparams" / construct.Int16ul,
    "fact_chunk_id" / construct.Const(b"fact"),
    "fact_chunk_size" / construct.Int32ul,
    "samplelength" / construct.Int32ul
)


WAVE = construct.Struct(
    "riff_chunk_id" / construct.Const(b"RIFF"),
    "riff_chunk_size" / construct.Int32ul,
    "wave_format" / construct.Const(b"WAVE"),
    "fmt_chunk_id" / construct.Const(b"fmt "),
    "fmt_chunk_size" / construct.Int32ul,
    "audioformat" / construct.Int16ul,
    "numchannels" / construct.Int16ul,
    "samplerate" / construct.Int32ul,
    "byterate" / construct.Int32ul,
    "bytespersample" / construct.Int16ul,
    "bitspersample" / construct.Int16ul,
    "fact" / construct.IfThenElse(construct.this.fmt_chunk_size == 18, FACT, construct.Bytes(0)),
    "data_chunk_id" / construct.Const(b"data"),
    "data_chunk_size" / construct.Int32ul,
    "data" / construct.Bytes(construct.this.data_chunk_size)
)


def build_wave(data: bytes, numofchannels:int=1, samplerate:int=8000, bitspersample:int=8, audioformat:int=7) -> bytes:
    datalength = len(data)
    fact = {
        "extraparams": 0,
        "fact_chunk_size": 4,
        "samplelength": datalength
    }
    wave = WAVE.build({
        "riff_chunk_size": 50 + len(data),
        "fmt_chunk_size": 18,
        "audioformat": audioformat,
        "numchannels": numofchannels,
        "samplerate": samplerate,
        "byterate": int(numofchannels * samplerate * (bitspersample/8)),
        "bytespersample": int(numofchannels*(bitspersample/8)),
        "bitspersample": bitspersample,
        "fact": fact,
        "data_chunk_size": datalength,
        "data": data
    })
    return wave
