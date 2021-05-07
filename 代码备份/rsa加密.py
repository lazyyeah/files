from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.PublicKey import RSA
import multiprocessing as mp
import threading as td
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import base64
def 加密(a):
    message = a
    cipher_text = base64.b64encode(cipher.encrypt(message.encode('utf-8')))
    # print(cipher_text.decode('utf-8'))
    return str(cipher_text.decode('utf-8'))

def 解密(e):
    cipher_text =e
    encrypt_text = cipher_text.encode('utf-8')
    text = cipher.decrypt(base64.b64decode(encrypt_text), "解密失败")
    # print(text)

# 伪随机数生成器
random_generator = Random.new().read
# rsa算法生成实例
rsa = RSA.generate(1024, random_generator)
# 私钥的生成
private_pem = rsa.exportKey()
with open("private.pem", "wb") as f:
    f.write(private_pem)
# 公钥的生成
public_pem = rsa.publickey().exportKey()
with open("public.pem", "wb") as f:
    f.write(public_pem)

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import base64,time


a=time.time()
rsakey = RSA.importKey(open("public.pem").read())
cipher = Cipher_pkcs1_v1_5.new(rsakey)  # 创建用于执行pkcs1_v1_5加密或解密的密码
for i in range(100):
    e=加密("130602199480584225")
# p1 = mp.Process(target=加密,args="130602199480584225")
# p1.start()
# p1.join()
print("加密用时",time.time()-a)


a=time.time()
rsakey = RSA.importKey(open("private.pem").read())
cipher = Cipher_pkcs1_v1_5.new(rsakey)      #创建用于执行pkcs1_v1_5加密或解密的密码
for i in range(100):
    解密(e)
print("解密用时",time.time()-a)
