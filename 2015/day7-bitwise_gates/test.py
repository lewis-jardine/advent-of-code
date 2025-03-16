from ctypes import c_uint8

val = 156

not_val = c_uint8(~val)

print(val)
print(not_val.value)