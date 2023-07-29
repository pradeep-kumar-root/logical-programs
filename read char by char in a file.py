import os,sys
sys.path.append("/Users/pradeek")

print(os.getcwd())
ptr = open("/ws/pradeek-bgl/pyats/projects/asr1k_platform/sample.txt",'r')
lt = list()
while(1):
    r = ptr.read(1)
    if not r:
        break
    print(r)
ptr.close()
