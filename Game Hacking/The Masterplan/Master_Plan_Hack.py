# Import The Library
from ReadWriteMemory import ReadWriteMemory

pr = ReadWriteMemory()
process = pr.get_process_by_name("The Masterplan.exe") # Get Process Name - PID Not Required ! -
process.open() # Open [pr.get_process_by_name] Process

hack = process.get_pointer(0x0AC418B0, offsets=[0x4C]) # Must be Hex Code

print(process.read(hack))

# process.write(hack, 1) # Write to Process



# Offset = 4C
# This -> Address = 0AC418B0
# - Base Address = 197B5558 -