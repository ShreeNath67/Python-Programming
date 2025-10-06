# Binary types
binary_data = b"data"      # bytes
mutable_binary = bytearray(b"data")  # bytearray
memory_view = memoryview(b"data")    # memoryview

print(binary_data, mutable_binary, memory_view)
print(type(binary_data), type(mutable_binary), type(memory_view))