# Task 8

# Please write a program to compress and decompress the string "Music industry hails passage of the Music Modernization Act".
import zlib
import sys
String = "ritqySthMZfrutjmlmLHlGyTTzQjTFJHvuYEZFbpLmVaGNYhBCAiJOtotbLwfAlIRzHHpnZOEHThXPrygaliAecPEXSYXWdQvPzJ"
print("Before Compress::=>", String.__sizeof__())
afterCompress = zlib.compress(String.encode())
print("After Compress::=>", afterCompress.__sizeof__())
print('**********---************')
# print(afterCompress)
# print("After Decompress::=>", zlib.decompress(afterCompress))