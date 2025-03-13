import threading
import time

class MyThread(threading.Thread):
    def __init__(self, msg):
        threading.Thread.__init__(self)
        self.msg = msg 
        self.daemon = True
        
    def run(self):
        while True:
            time.sleep(1)
            print(self.msg)
            
            
    # 3개 스레드 생성
    for msg in ['You','need','python']:
        t = MyThread(msg)
        t.start()
        
    for i in range(100):
        time.sleep(0.1)
        print(1)

        
            
