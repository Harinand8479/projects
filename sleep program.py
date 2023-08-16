import ctypes

# Call SetSuspendState to put the system to sleep
ctypes.windll.powrprof.SetSuspendState(0, 0, 0)
