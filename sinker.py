import zmq

if __name__ == '__main__':
    context = zmq.Context()
    # Get reciever
    receiver = context.socket(zmq.PULL)
    receiver.bind('tcp://*:5556')
    while True:
        msg = receiver.recv_unicode()
        print(msg)
