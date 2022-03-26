from ReadWriteMemory import ReadWriteMemory

pr = ReadWriteMemory()
offsets = [0x84, 0x70C, 0xC, 0x4, 0x684]
base_addr = 0x14A69084
process = pr.get_process_by_name("Setup.exe") # Get Process Name - PID Not Required ! -
process.open() # Open [pr.get_process_by_name] Process

hack = process.get_pointer(base_addr, offsets=offsets) # Must be Hex Code

print(process.read(hack))


# static address
# 14A69084

# Offsets
# 84
# 70C
# C
# 4
# 684