from bluetooth import *
'''import lightblue'''
'''import base64
import cStringIO'''


'''image = open('clippy.jpg', 'rb')
image_read = image.read()
img64_encode = base64.encodestring(image_read)
img64_dencode = base64.decodestring(img64_encode)
a = open('clippy2.jpg','wb')
a.write(img64_dencode)'''

'''with open('clippy.jpg', 'rb') as img:
  es = base64.b64encode(img.read())
  print "assilam"'''
  

'''a = open('clippy4.jpg','wb')
a.write(es.decode('base64'))
a.close()'''

'''print img64_encode'''


server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

advertise_service( server_sock, "SampleServer",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ],
#                   protocols = [ OBEX_UUID ]
                    )

print "Waiting for connection on RFCOMM channel %d" % port

client_sock, client_info = server_sock.accept()
print "Accepted connection from ", client_info

try:
    while True:
        data = client_sock.recv(1024)
        if len(data) == 0: break 
        print "received [%s]" % data
        data = "Welcome to Jurassic Park"
        client_sock.send(data)
        print "sending [%s]" % data
        
except IOError:
    client_sock.close()
    pass

print "disconnected"


