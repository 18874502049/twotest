import _thread
import threading
import time
import logging

logging.basicConfig(level=logging.INFO)

loops = [2,4]
class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name
    def run(self):
        self.func(*self.args)
def loop(nloop,nesc):
    logging.info("start loop " + str(nloop)+ " at " +time.ctime())
    time.sleep(nesc)
    logging.info("end loop " + str(nloop) + " at " +time.ctime())




def main():
    logging.info("start all at " +time.ctime())
    nloops = range(len(loops))
    threads = []
    for i in nloops:
        t= MyThread(loop,(i,loops[i]),loop.__name__)
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    logging.info("end all at " +time.ctime())

if __name__ == '__main__':
    main()