import struct
BID = "2EF3BB19EAC3B0A5697768F8A453953F"
addr = 0x02AA03B4            # 7102aa03b4: mov w19,w0  ->  mov w19,#60
d = bytes.fromhex("93078052")
out = b"IPS32" + struct.pack(">I", addr + 0x100) + struct.pack(">H", len(d)) + d + b"EEOF"
name = BID.ljust(64, "0") + ".ips"
open(name, "wb").write(out)
print(name)
