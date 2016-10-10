import zmq
import subprocess

if __name__ == '__main__' :
    context = zmq.Context()
    # Get reciever
    receiver = context.socket(zmq.PULL)
    receiver.connect('tcp://192.168.11.203:5555')
    sinker = context.socket(zmq.PUSH)
    sinker.connect('tcp://192.168.11.203:5556')
    while True:
        bash_cmd = receiver.recv_unicode()
        p = subprocess.check_call(bash_cmd, shell=True)
        if (p != 0):
            sinker.send_unicode(u'%s\tfails' % bash_cmd)
        elif ( p == 0):
            sinker.send_unicode(u"%s\tcompleted"  % bash_cmd)



