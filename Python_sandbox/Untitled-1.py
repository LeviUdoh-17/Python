# //check my laptop details with python?  
import platform
machine = platform.machine()
version = platform.version()
platform1 = platform.platform()
uname = platform.uname()
system = platform.system()
processor = platform.processor()
print(machine, version, platform1, uname, system, processor)