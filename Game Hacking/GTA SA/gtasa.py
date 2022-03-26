from ReadWriteMemory import ReadWriteMemory

pr = ReadWriteMemory()
offsets = [0x77CE50, 0x433, 0x9E7F8]
base_addr = 0x009E7F8
base_addr2 = 0x00B7CE50
process = pr.get_process_by_name("gta_sa.exe") # Get Process Name - PID Not Required ! -
process.open() # Open [pr.get_process_by_name] Process

hack = process.get_pointer(base_addr, offsets=offsets) # Must be Hex Code

print(process.read(hack))


hack2 = process.get_pointer(base_addr2, offsets=offsets)
print(process.read(hack2))
# 00B7CE50
# 45805B