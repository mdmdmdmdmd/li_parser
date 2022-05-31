import json
import os
import sys

from scapy.all import rdpcap, TCP

from ps_pdu import parse_ps_pdu


def parse_pcap(filename: str, save=False, func=None) -> list[dict]:
    payload = b""
    packets = rdpcap(filename)
    count = 0
    for packet in packets:
        if TCP in packet:
            count += 1
            print(f"Processing TCP Packet {count}", end="\r")
            if func is not None:
                func(f"processing TCP Packet {count}")
            payload += bytes(packet[TCP].payload)[:-16]
    print("")
    position = 0
    length = len(payload)
    count = 0
    pdu_list = []
    while length > position:
        count += 1
        print(f"Processing PDU {count}", end="\r")
        if func is not None:
            func(f"processing PDU {count}")
        while length > position:
            try:
                add_to_pos, result = parse_ps_pdu(payload[position:])
                pdu_list.append(result)
                break
            except:
                position += 1
                continue
        position += add_to_pos + 4
    print("")
    if save:
        with open(f"{filename}.json", "w") as f:
            json.dump(pdu_list, f, indent=4)
    return pdu_list


def main():
    if len(sys.argv) < 2:
        print("please specify a file name to parse")
        return
    filename = sys.argv[1]
    if not os.path.exists(filename):
        print(f"{filename} does not exist")
        return
    parse_pcap(filename, save=True)


if __name__ == "__main__":
    main()
