ptr = open("/ws/pradeek-bgl/pyats/projects/asr1k_platform/sample.txt",'r')
ptr1 = open("/ws/pradeek-bgl/pyats/projects/asr1k_platform/output.txt",'w')
for f in ptr:
    ptr1.write(f.replace("is","was"))
  
