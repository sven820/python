__author__ = "JJ.sven"

import hashlib

print('md'.center(50, '='))
m = hashlib.md5()
m.update('jinxiaofei'.encode())
print(m.hexdigest())
m.update('ios coder'.encode())
print(m.digest())

print('sha1'.center(50, '='))
sha1 = hashlib.sha512()
sha1.update('jinxiaofei'.encode())
print(sha1.hexdigest())
sha1.update('ios coder'.encode())
print(sha1.hexdigest())


# 一半用于消息加密，速度快
import hmac
h = hmac.new(b'wo shi key', b'message content')
print(h.digest())
print(h.hexdigest())