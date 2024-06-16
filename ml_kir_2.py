import cv2
import numpy as np
from tensorflow import keras
import tensorflow as tf


def inference(image_bytes, m_path):
    test_arr = []
    physical_devices = tf.config.list_physical_devices('GPU')
    if len(physical_devices) > 0:
        tf.config.experimental.set_memory_growth(physical_devices[0], True)
        print(f"Using GPU: {physical_devices[0].name}")
    else:
        print("No GPU found. Using CPU.")
    nparr = np.frombuffer(image_bytes, np.uint8)
    # test_image = cv2.imread(img_path)
    test_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    test_image = cv2.resize(test_image, (32, 32))
    test_image = np.array(test_image)
    test_image = test_image / 255
    test_image = test_image.reshape(1, 32, 32, 3)
    test_arr.append(test_image)
    model = keras.models.load_model(m_path)
    res = model.predict(test_arr)
    return res[0][0], res[0][1]


# test_img_path = "images\\image_707_0.jpg"
# model_path = 'model.keras'
# print(inference(test_img_path, model_path))

test_image_bytes = b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x02\x00\x00\x01\x00\x01\x00\x00\xff\xdb\x00C\x00\x03\x02\x02\x03\x02\x02\x03\x03\x03\x03\x04\x03\x03\x04\x05\x08\x05\x05\x04\x04\x05\n\x07\x07\x06\x08\x0c\n\x0c\x0c\x0b\n\x0b\x0b\r\x0e\x12\x10\r\x0e\x11\x0e\x0b\x0b\x10\x16\x10\x11\x13\x14\x15\x15\x15\x0c\x0f\x17\x18\x16\x14\x18\x12\x14\x15\x14\xff\xdb\x00C\x01\x03\x04\x04\x05\x04\x05\t\x05\x05\t\x14\r\x0b\r\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\xff\xc0\x00\x11\x08\x01\x00\x01\x00\x03\x01"\x00\x02\x11\x01\x03\x11\x01\xff\xc4\x00\x1f\x00\x00\x01\x05\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\xff\xc4\x00\xb5\x10\x00\x02\x01\x03\x03\x02\x04\x03\x05\x05\x04\x04\x00\x00\x01}\x01\x02\x03\x00\x04\x11\x05\x12!1A\x06\x13Qa\x07"q\x142\x81\x91\xa1\x08#B\xb1\xc1\x15R\xd1\xf0$3br\x82\t\n\x16\x17\x18\x19\x1a%&\'()*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz\x83\x84\x85\x86\x87\x88\x89\x8a\x92\x93\x94\x95\x96\x97\x98\x99\x9a\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xff\xc4\x00\x1f\x01\x00\x03\x01\x01\x01\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\xff\xc4\x00\xb5\x11\x00\x02\x01\x02\x04\x04\x03\x04\x07\x05\x04\x04\x00\x01\x02w\x00\x01\x02\x03\x11\x04\x05!1\x06\x12AQ\x07aq\x13"2\x81\x08\x14B\x91\xa1\xb1\xc1\t#3R\xf0\x15br\xd1\n\x16$4\xe1%\xf1\x17\x18\x19\x1a&\'()*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x92\x93\x94\x95\x96\x97\x98\x99\x9a\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xff\xda\x00\x0c\x03\x01\x00\x02\x11\x03\x11\x00?\x00\xe7\xc5\xf9^\x83\x1f\x8dZK\xa0\xfdF?\x1a\xa9\xe5)\xe8\x05H \xe0\xf5\xad\xed\xd9\x8a\xfd\xc9%h\xce*\x8c\xcd\x18\xc7?\xadXh\x98\xf7\xaa\xd2\xda1\xef\xd0zS\xd7\xb8\xac\x8c\xdb\xa7W\n\x00\xdc;\x823YS\xa8\xe3\xe4Q\xf8V\xe3\xda\x05\x07\xe9U\xe4\x88zv\xa6\xbc\xc5c\x9dd<p?\n\xb1gbd\xdd\xf2\x9e\xde\x95\xa8`BG\x1f\xadO\x04AH\xc0\xefR\xdfB\x92\xb9b\x08U\x0bp9\xf6\xab>FzR\xc0\xa0\x8e\xb8\xe6\xad,`\x0e\x0ei\\v [@\xd5 \xb0\x00\x1e\x7fJ\x99N\xc3\xd2\xa7\x8c\x17 \xfb\xd5&"\xa8\x84\xa9\xc7<\xfbU\x98U\x81\xe7\xb9\xabIn\x1b\x92*U\xb7\xe4`R\xdcw\xb0\xe8\x17=}j\xfa@$\x1c\x9flUx`9\x1fZ\xd0\x86\x12q\xf5\xa5\xa8\xb7!\x16@t\xc0\xa9V-\x9dy\xab\xb1\xc3\x85\xf5\xa9<\xb1\x8eE;\xdfp\xd8\xab\x19\xe2\x95\xa3\xde\x0f\xae1N\x98m\xce:Ucp"?J6\xd47\x19=\xb9\x19\xcf\xa5Q\x9a 3\xf4\xabs\xeaC\r\xc7\xe9Y\xf3\xdd\x87$\xe2\x9f0\xacV\x9a-\xdc\xf5\x18\xaa\x17p\x00\xad\xdb\xe5\xe9W\xe5\xbaP\xa7\x83\x9f\xa5g^J\x1f~\x0f\xa5\nAc\x1eu\xe4\x8cv\xaa\xfeX\x03\x9e*\xc5\xd4\xa1\x0b\xe4\x0e\xd5JK\xa03SpH\x97z\xa7L\xd2o\x04\xf0?J\xa8n\xd4\xb7Z\x9a\x19\x91\xc8\xf7\xa5q\xd8\xb2\x8e\x05Z\x86P08?\x85V]\xb8\x07#\xf3\xa9\x12P\xb8\xc7\xe9L\x0bm \xc6x\xa8\xdaP\x14\x80(G\xde\x05<&i\xadI\xb1\xb0\x91\x11\x8e\xbd}*FS\xd8\x1a\xb0\xab\xce0*U\x80\xb0\x07\x14[\xa9Fk#\x1e\xd5\x0c\x91\xe4\x1f\xa5kInv\x9e\x05T\x92\x02\t\xe2\x81\x98\xb7\x10\x95\x07\x92\x061T\x9d:\x8c\xd6\xec\xf1\x0c0\xaa\x8d\x08\x19\xefF\x821\xfc\xb3\x9apV^A?\x9dj\x88A\xed\xcd4\xdb\xf3\xd2\x93\xb3\x1e\xa5$\x99\x81\x1d\x7f:\x9d/\xe4C\xc8\xe3\xebS}\x99\x88\xe2\x93\xec\xb98a\x9a\\\xa9\x8e\xe5\xdb\x1b\xb4\xb8(\xac0N{\xd6\xbc0\xa9\x03\x06\xb1\xed-\xb6\x14#\x8cf\xb5-\xcb\x82\xa3\xb0\xf7\xa1]\x05\x91y \xe0q\xc5L\xb0\x90\x052&p\x06z}j\xccM\x93N\xe1ac\x84\xe0U\x88Sk\x0c\xd3\xe2\\\x81\x8fL\xd4\xcb\t\xc84\t1\xc8\x0e\x061JP\x93\x93J&1\x0f\xa5G%\xe1$\xe7\x8eh\xd8,$\xd1|\xa4\xe2\xb3/\x11F\xfe\x99\xe3\xb5[\x92b\xf9\xe7\xbdP\xb8\x00\xe7\x9e\xf4\xee+\x19\xb7/\xb7wqY\x97\x17,\xc5\x95G\xebZ\xb7\x11o\x18\xf7\xaa2Z\xaae\xbdM=\xc3\xa9\x9e\x15\x9c\xe5\xb3\xf9TS\xc2H;G5\x7fh\x04\xd1\x94S\xce?*4\x16\xb72\x1a\xc5\xdf\xefc\x9f\xadT\x93O\xc1<\x93\xce8\xae\x89\xf6\x95\x18\x03\xf2\xaa\xcf\x00$\x9cSV\x13\xf39\xe9t\xf0I\'4\xc8\xed\xb6\xb6\x01\xe9[o\x06I\x00g\x9a\x84\xdb\xe0\x9a\x02\xf6(\xac]\xb2jTC\xd0T\xe6#@R\xa7\x9a\x92\xaeK\x14d\x81\xce8\xa9\x80\x0b\xd4\xd3\x11\x88\x14JN\x00\xe9B\x03\xb3\x86>A<\x9a\x98\xe1W\xa75\x1clF\x0f\xb5+I\xbb\x8a.\xc0l\x87p9\xcf>\x95Jh\xf2\xc4\x80j\xe3\x1c\x0e\x95\x03\xff\x00Zw\x032x\xf3\x9e\x9dj\xb3B3Z\xb2\xc5\x91\x9fz\x80@K\x1e\xff\x00\x85!\\\xa4\xb1\x0e\xc34\x9eQ$\xd6\xa2[\x91\xfc=\xaaAfI\xce\x0f\xe1E\x8a3\x12\x0c\xfeU:Y\x0e\xb8\xedZQ\xd8\x9e{\x8fz\xb2\x96@\x0e\xd4\x08\xa1og\x83\xd0\xf4\xf4\xab\xf1\xdaaF\x078\xabQ[\x85\x1d\x07\x03\x15n8@\xea(\xbd\x87b\xa4v\xcd\xc7\x1d\xaah\xe0\xda\xd9 \x8e*\xe8\x88\x0e\x86\x9f\xb00\xe9B\x02(\xb6\x9c\x02\x0f\x03\xbdLUp)D t\x19\xa51\x83\xde\x97\xa0\x15\xe4\xc1\xfc\xea\xbb\xc6*\xfb\xae1\x81\x9a\x8d\xd78\xa6\x06d\xab\x80\x00\x15B\\\x9f\xc4\xd6\x9c\xd1\xb0\xc7\x15A\xd3\xa5\x16\x15\xcam\x83Q<\x01\xfd\xaa\xd8E\x1dE8\xa0\xf4\xa3`h\xc7\x96\xdb?\xfe\xaa\x83\xca5\xa9*\x8e*\xa3!\x1d\x050+4M\xf4\xa8\x82\xe3\xde\xac\xcaXc?\xce\xa2P0OZ\x90#X\x079\x14\xd7\x80z\n\x95\xe5>\x95\x0b\xca\xd5W\xb0\xacBc\x1e\x95\x13 \x1f\xfe\xaa\x91\xd8\xe7\xda\x98pzQ\xa8\r\'\x1d)\\g\x19\xa3h\x00\xd4n\xfd\xba\xf1K`;\xa5\xc1\xa7\xaa\x13\x9a\x85X\xf3\xc5YBNx\xc5\x03\x1a\xe9\xd35X\xc2=j\xcc\xa4\xf1\xcd@)\xb6\x04/\x18\xe2\x968\xc0\xcf\x02\xa6\xda\x0fz\x95\x02\xfd)\\,4E\x8e\xd5\'\x92\xdd\x85L\x9b{\x91\xf9\xd5\x8f1GzZ\x0e\xcc\x8a;\\g5*\xc6\x06x\xa6\x99I<P\xac{\xd1q\x93\xe3\x1d\xf3N\x0cEF\xaf\x8a\x900=h\xb8l*9\xa9\x81\xc5E\xbd@\xf7\xa4\xf3sG\xa0\xcb\x8a\xc0\x9aqQ\x8c\xe3\xa5R\x12{\xd3\xbc\xe6\xe9\xd6\x96\xa1bw`\x0f\x1c\xd4eK\x0e\x98\xa6\x07\xe7\xd2\xa4Y\x01\xeai\x88\x86X\x8b~UNK\x10zzV\x938\xcd5\x99J\x9e9\xc5RdX\xc7\x92\xd3`?L\xd5I#=9\xe9\xe9Z\xf2\xaes\x9fJ\xa1t\xbbs\x8c\xe0\x0cS\x11@\xc4\x01\xe4\x8f\xc6\x99+F\x80\xe4\x8e\x99\xebL\xb9v]\xddx\x18\xebYw\x12\x92\xc7$\xf01\xd6\xa5\xdd\x14Z\x96dc\xc1\xedUdp\x0f\x18<f\xab\xb4\xe0\x03\x8a\xab5\xc7\'\'\xf4\xa9\xb8\xecZ\x96\xe5T\x10A\xce=*\xa4\x97`\x02r:zU;\x89\x01\xdd\x8ej\xa3\xb19\x00S\xd444>\xd8\x1b\xa9\xfc\xb3J.\x07nk5\x03\x06\x19\xab1\xe4\x81\x80iX\x0b/9 \xfd*\x07\x91\xb0i\xc26#=\x051\xfePEQ\'\xa3\xc2H\xfc\xeaW\x98*\x9f\xa7z\xcbK\xf1\x8e\x9f\xad<\xce\xd2\xf4\xe8i^\xe5\x93<\xdb\x8f\x1f\xa5\x0b\xc8\xaa\xe0\x95\xe0\x8ejDbqN\xc2\'Q\x9aq\x1c\xd4;\x8f\xe1G\x99\x83H\x0b(\x0fZ\x999\x15R9rEZ\x89\x89\xc7\xa5\x05\x12\x059\x14\xec\x11NQ\xf2\x8a\\\x81@\xae4\x02G"\x9e\xbf(\xa4-\xc7ZM\xd9\x18\xa0\t\x03\xfeT\xf1\x82\x01\xefQ\xa0\x18\x19?\x85;z\xa8\xa0d\xa3\x18\xe9\xcd\x1cb\xa03\x01\xd3\x9a\x8aI\xd8\x92\x07\x02\x8b\xf4\x11o#=i\xc3\x1dsY\x8d#g9\xa6\x99\x9b\x1d3\xf8R\xbb\r\r)e\x08\xa4\xe6\xab\xb5\xf2\x83\x8a\xa2\xd2\xb1\xcfo\xa5D\xd2~~\xf4\x06\x86\x83_\x8c`\x01\xf9\xd4o(\x95I\xe0g\xde\xa8\xef\xefJ\t=\xcf\xe1Mn\'f6\xe6\x10\xe5\xbas\x8e\xf5\x95yfp\xf8\xeb\xc5k9\xdb\xc99\xaa\xf2\x15~\x18w\xaa\xbfrm\xd8\xe6\xa7\xb6\x91Y\xb8?QT\xe4Lg\'?Z\xea%\xb3G\xe8;\xe6\xb3\xae\xb4\xc22FNOa\x9a\xab&.f\xb70\x1c\x02H\xa4\x083\xd2\xad\\\xd9K\x1eH\r\xf7\xb1\xf7j\x98\xdc\x8cw\x03\xe9\xd2\xa5\xc5\xa1\xa6\x99(\x83\'8\x06\xac\xc3o\x9cq\x8e*(\xa4\x03\x19\xe3\x8e\xf5v\x19\xe3\x00s\xdb\xd6\xa6\xfd\xc7`0lPMU\xb8 \x03\x8f\\U\xc9&V_l\xf6\xaa3H\xaa\xc7=\xcfz{\xa1\x1d%\xb4y\xdaI\xf5\xad\x18S\xe4\x03\xadf[1\xc8\x03\xa8\x1e\xb5\xa5\x03\x91\x8c\xfaR\xd8\xbb\x12\x98\xc1=)@\xdb\xd8SM\xce\xda\x8aK\xa2}\x07>\xb4\xeeM\x89\x9d\xbeS\x9e*\xac\x8crq\xd2\xaa\xdcN\xc7=z\xfaT\x02r\x0f<\xd2\xd4v5!v\\U\x94\xbc\xdb\xc7qX\x9fk\xc7aOK\xb2\xe6\xa4\xa3p]\x9c\xe79\xf6\xa7\x8b\xb2x\xc8\xacU\x9d\xbdO\xe7SD\xec\xc7\xafj,\x1b\x1af\xe4\x03\xc9\xa5\x179\xe9\x83U\x157w\xfc\xeaeM\xa0qN\xc0[I\x01\x03\xe9J\xf2q\xd75\\6\xde\x94\xdd\xdb\xbb\xd0\x04\xe2@\x0f4\xd3&\xe2@\xa87R\xe7\x1d\xe8\x02R\xc0u\xa4\xde* }\xc5\x05O\xb52G8\xc8\xe2\xa1(X\x9c\xd4\xd8&\x98\xc7\x1f\xfdjb\x00\xaa\x00\xa7\xa8\xc1\xa6\x06ZRM\x05\x04\x98#\x8a\xae\xd1\x92r*l\xe3\xde\x9b\xbb\x14\n\xc4[\x08\xec)D!\xfa\xe2\xac\xae\xd6\xedN\x00\x0e\x94\x08\xa3%\x92H0Pz\xf4\x15\x93u\xa4\xa3\xb0*\x00\xcf\'\xe5\x15\xd03\n\xae\xe5\rZ\x91\x0e\'%-\x91\\g\x1c\xfbS\x16 \xbd\xab\xa0\xb8\x84q\xc9\xac\xb9\xe2\xc1\x1cRz\x8d\x15\n\xe7\xa7\x15\x0b[\x86\xabL\xbbi\x0b\xa8\xec?*\x9d\x87\xb9\xd2\xa4*\xb8\xc9\xed\xebN\xf3\xd1@\nrj\x84\x97\xf8\xc75RK\xe01Cv*\xc8\xd8f-Q\xb6\x05f\x0b\xc7=\x1b\xf9S\x96\xe8\xafV\xcf\xe5J\xe1b\xc4\xd2\xa8\x03\xde\xab\t\x94\x9a\x86Y\xc3c\x9a\x88\x9fq@\x8b,\xeazsO\x8d\xb1\x9e\xd5MG\xa1\xa9\xa2\xc9\xcehcF\x92>*\xdco\xb75B6\x0395*\xc9\x9e\xf4\x86h$\xd9\xcf5(\x9b=\xaa\x9c\\\xfe\'\x15gi\xc18\xa0\x05\x12\x9aA#R(\x06\xa4\x03\x03\x9a\x06 \xc9\xa7\x95&\x90>)I\rO\xa8\x84S\x8e\xd9\xa9P\x0e\xfc\xd3\x11y\x1c\x8e\xb50\xc7L\xd2\x0b\x8b\x80:\nk&q\xc5L\x13\x82i\x00\xa6\x98\x8a\xfeN=\xe9\x8f\xb8U\xa65\x13\x8c\x9a.\x05F\'\xb0\xa8\xb2P\xf3W\x19\x07\xd2\xa2hCs@\x11\xac\x84\xf4\xe9N2\xe0\x1ei\x0cX4\xc9\x13\x00\xd3H\x18\xa6`{\xe6\xa2v\x07\xda\xa2v\xc1\xa8\xd8\xee4\x0b\xa1#\x8d\xdd\xfbUY\xa0\x07#\x1d\xaam\xc1*9g\x1c\x9c~T\xefaZ\xe5\x19`\x11\xb6=\xb3Q<j{~\xb5i\xe5Y\t\x18\xe7\xdcTN\x83\x04\xd3\xb8\xadb\x8c\xf7\x87#\x03\xa0\xaa\xafr\xc7\xf0\xa9&V\xcfN\xde\xb5]\xc6\xe3\xe9Sb\x93\x17\xed\xce\xad\x8c\xe3?Z\x91.\x9d\xfb\xf7\xa8\x165R\t=\rK\xe6\x8c\xe0T\xd9\x0e\xe5\x94b\xde\xdc\xd4\xa0\x1c\xd4\x1098\xe3\xa9\xab\x03$\x8c\nhD\xd0\xc4[\x1c\xe3\x9a\xb5\xe4\x04\x1d}\xea\x08\x9c\xaa\xfb\xd4\xa2M\xc3\x9c\xd1p`_o\x19\xa5\x8d\xc9a\x8fZc&zS\xa1R\xa4f\x8b\x14i\xdbJT\x0f\xad]\x12\x87SY\xf6\xe3\x85\xabA\xb1\xc5H\xef\xdc\x99O\xa0\xa7\x00MB\xb2\x0c\xf5\xa9\x16S\xc7\xa5\x03\xb1 _Zw\x97\xf2\xe74)\xde\x07\xbd)\x18\xe3\xb52\x18\x88\xa4\x1a\x95\x00\xdc2j5\x15"\x81\xc1\xebLd\x8cF2)\x85\xcfL~4\x16\x00\xf7\xa0\xba\xe3$\xd2\rD-\x9e\xbdi2;\xd4RN\xab\x9c\x1a\xab-\xe6\xdc\xe0\x13\xf8\xd0;\x16\xe4e\xc1\xe6\xa22c\x8a\xa6n\x99\xc9\xc7\x14\xf5\xdc\xdc\x9a\x04Y\x0f\xc75\x14\xf2\xa8F\xe7\x9f\xa5D\xca\xc7\xff\x00\xd5Q\x98\xc9&\xa9!\x10\xc8\xd9$\xf6\xa6\x19\x00\xf7\xa9e\x80\xe3\xf1\xa8\x1a2\x06\x06(hI\x8c\x96^\rVp[\'\xbd>E \x9c\x9e\xf5\x1eph\x10\xc0\x18\x1e\xbf\xa5++b\xa4\x02\xa6X\xf2\x07\xd2\x9e\x831\xa5\x90yd\x91\x9a\xcc\xb9\xb9\xc32\xaf\x1d9\xad;\xb8S\x0c\xab\xcfj\xca\x96\xd83\xb7Q\xf8Qa\\\xae&\x91\x9f\x198\xfa\xd5\xebS\xca\xe7\xde\x92\xde\xd9Sn{\n\xb6\x8a\t\xc61PU\xc9\xe2+\xb4z\xfd*\xd4N\x9cg\xadSQ\xdb\x9a\x910\x0f_\xd6\x8d@\xb8\xd8*H\xe2\x96$\xdcG\xf3\xa8\xe3\x19\x03\x93\xd2\xac\xc6\xa4c\xe9@\xb6\x1e\xa8G\xbd.\xd3\x9a\x9a1\x908\xedJV\x9a\x01\xa8\xc5@\xe2\xa4Y\xcfN\xd5]\x99\x90\x9e;\xd2\xa3w4\xac2\xda\xc8z\xd4\xab(\xf5\xaa\x83\xeb@ \x1a\x06iE>8\xa9\x84\xc1\xb8\xac\x91.;\xd3\xc4\xd9\xa2\xc0j\tG\xa5!\x98t\xaaQ\xcaO\x1d\x87\xa5HO\xd6\x98\xc9]\xea2\xc4\xd2\x1e;\x9aC\x93R\x01\x82M0\xc6I\xa9\x87"\xa4\x8c)\xcf\x14\xc5b\x04\xb6\xee}*\xc2\xc4\x00\x14\xa0\xfaTMp\xcb\xda\xab\xd0D\xbeX\x15\x1c\xa81\xc7\x075\x11\xbb~\xf9\xfc\xaa\xabJx\xe6\x96\xa1o2y\x1cc\x15FY\x80\xe9\xcf5\x1b\xcaN8\xfd*\xac\xb7\x18\xc7\x06\x81X\x92G\xdd\xd7\xa6j2Tz~u\\\xdc\x13L\x12\x93KQ\xd8\xb8\xb2z\xf4\xa9\x05\xc2\'z\xcd\xf3\xf1\xde\x8f7\xcc\xe9\xda\x80#\x9a`GNsPm\xdcr{\xd5D\x97y$\x9a\x90ILE\xb8\xe2\x0cq\xd3\x8a\xb4\x91*\x00N\x0f\x1e\x95MN\xde\xe2\xa4\x17\x02\x95\xd8X\x99\xc8\xec)\xaa\x99\'\x8a\x03\xee\xecEN\x80\x0c\xf1L\x114\x10\x9e\xe3\xa0\xabQ\xc6A\xa8\xe38\xcdHe\xc7zC-\xc2B\xf7\x1d1So_Z\xcb7\x03\xb15e\x1cs\x93Ih-\xc5\x9c\xee\xc7\x15I\x9d\x93\xbfZ\xb8\xee8\xe2\xaa\xban\xc6\x0f\xe9V\x1b\x0b\x1c\xc5\xb3S#\x83\x9a\x81c#56\xe5N\xe3\xf3\xa5k\x15\xb9`G\xf8\xd3\xc4@Uu\xbcE\xcf"\x93\xed\xa0\xf4\xc5\x17\x0b\x16\x83\xec\xedR\x07\x07\xa5RYwu9\xfaT\xe9(\xcd+\x8d\x16\x01-M*\xc7\xb1\xfc\xa9\xd1\xca\xab\xff\x00\xea\xa9\x96t$\x0e?*\x15\x80D\xc8\xcf\x15.i\x0b\xa1\xe9FA\xa6+\x08\xcc#\xf7\xa8\x1a@{T\xb2\x11\xd7\xda\xa0i\x07\xd3\xf1\xa6!\x8c\xc2\xa1,\x00\xe6\x9e\xec\x0f9\x1d*\xbb\xc8:g\xb5\x03\xb1\x1c\xcc\x008\x1d\x06k2y0@>\x95v\xe1\x80\x04\xe4t\xf5\xac\xd9\xe4R\xdd\xcf\x14\xaeH\x85\xbd\rF\xef\xcfZQ\xf7I\xa8\\n4j0i\x00=iR`\x07QP\xbc,\xc7\x82i\xa2&S\xcd\x16\x04\xd1\x9c\x92m8\xc9\xe6\xad\tMe\x17"E\xe3\xd2\xaf[\xb0#\x9fZv\r\xcd\x04- \xe0\x91S\x08\xf8\xe4\xd5h\xa4\x03\xb8\xeb\xebS\x89\x03\x0cdzT\xec\x04\xe2A\x9cU\xd8%\x1e\x98\xc9\xc7Z\xcdD\xe3\xadL\x8cW\x80O_Z7\r\rC"/q\xf9\xd42J?\x87\xd2\xab(f\xe6\xa6H\x89\xedOQ\t\x1f8\'\xb1\xabKp\x07\x15\x10\x84\xe0\x8cP\xb0`\xf2h\xb0\\\x9c\xcc\x0f\xad \x93\x00\xe2\x95\x15E<\x81\x8cg\x14\xc6B\xd7\x04)\xe9\xd2\xaaMs\xd7\xe6=*\xdc\xb1\x02\x0fJ\xcf\xba\x89\x946\xd1\x9a,\x17"7eO$\xfet\xe5\xbe\xe39\xfd+2\xe7\xccVo\x94\xf1\xedUL\xf2\xa1\xc6\n\x8f|\xe2\x93\x8b\x1f2:\x05\xbf$\xf5\xc5J\x97\x87#\xe6\x1d}\xab\x02\x1b\x868\xdc\x7f*\xb9\x13\x86\xc75\x16\xeeU\xcd\xe8o\x14\x903\x93\x9e\xd8\xab\xd0\xdc\x8c\x0f\xads\xd0\x10\x19y\xad\x08gP\xa0g\x9a\x00\xda[\x91\x8c\xd2\x1b\xbc\x03\xfd+0\xdd\x05\\\xe7\x8a\x82K\xec\x92(\xb8\x1a\x8fzy\xebP\xc9vry\x18\xac\xb9.\x8e\x0f\x15\x03]\x1c\x9e\xa0\xd3\xd4F\x9c\x97\x80\x03\xcej\xb4\x97\x83\x93\xcf\xe7U<\xe2\xde\xa7\xf0\xa8\xe5\'\x04\xe3\xad1\x0e\xb9\xbcgf\x19\xe2\xaa\xf9\x84\xb7?\x9d2F\xf9\x8d R\xdc\xe6\x81hO\xe6\x901M,\xccx\xe2\x98\x14\xe6\xa4U&\x98\\P\x8f\xb79\x14\x81\x1c\xb7#\x8fj\x95\x15\x87\xff\x00\xae\x9eO\x1d9\xa6I\xcc\xcc\x826\'\xd2\x9a.\x82\xf0\x0f\xe5QJZL\xe7\xbdBT\xaf@hj\xe3Z\x16Z\xf5\xc7L\xff\x00\xdfT\xf4\xd5eV\x19\xfe\x9f\xe1UcB\xec\t\xe2\xa7\x16\xb9\x19\xcdO*es\x1a\x10j\xccB\xe7\xfc\xfe\x95r+\xe2\xcc\x0f\x1f\x9dc\xc7nT\x8ezU\xdbe\x1cd\xe3\x14\xad`M3z\xca\xe3yL\xfb\xd6\xa4E0\x18\xff\x00:\xe7!\xb8Xv\xe0\xf4\xab)z\xcex\'\x1fZC\xb1\xbd\x94n\x86\x98\xd1\x8c\x93\x9a\xa5m1 \r\xc7\xa6y\xab~r\x803T\x9b%\xa11\x83\xd7\x8az\xa6prj\t&\x1d\xbdj\x11u\xb1\xb9<S\xb8"\xfbB\n\xfb\xd5y\xa3P\x0eq\xf9T\x0f|\xb8\xe1\xbf\x95G%\xca\xb2\x8c\xb0\xfc\xe8R\x0b\x10\xcf\x0cn\xed\x93\x9a\xa7=\xba\r\xdbG\xd0\xd4\xd2O\x1a\x93\xf3\xf7\xf5\x15\x14\xb7H\x14q\x9ez\xe2\x9f6\xa2\xe5(\xb8\xdaO\x19\xa4\xdc\xd8\xe0b\x89\'\xdc\xcd\x81\x8ehW\x07\xbd&\xc6\xb4\x1f\x14\xaf\xbb\x04\xf4\xf6\xab\xd1\xbe\x00\'\xd2\xaa ^\xa3\xaf\xd2\xa6F\x03\xa8\xe2\x95\x91W/F\xe5\xb8\x1d1\xda\xa4\x0b\x9a\xaf\x14\xca\x9e\xdcT\xdew\xf9\xcd\n\xc08\xc7H \\\xe7\xbd8L\x08\xe7\x1f\x9d1\xa4\x03\xa1\xa7rI\x92\x05P\t\xc7OJ\x86x\xcb\x0e=jH\x9csR2\x86\xa3\xd4\x19\x95-\xb9\x19>\xf5\x0e\x18q\x9a\xd4xs\xd6\xab<8\xa7a\\\xaa\x13\xbdJ\x8cA\xe7\xa5?h\x14\xcd\xb4\xac\x04\xe9\x86\xf6\xa9\x92 \xd5]x\xefV\xa2\xc9\xce\r\x17\xb0\xecy\xe1\xbfec\x92?Zr\xea)\x9ej\x03\x8c\xf2\r+C\x1c\x80u_\xc6\x8eQ_\xc8\xb9\x1d\xda\x13\xc1\xedS\x0b\xde\xc0\xfe\x95\x96-\xb6\x9f\x94\x9aq\x0e\xb8\xe6\x95\x98\\\xd9\x8e\xef#\xafj\x9e9\xc3w\x1d=k\x166c\x9eO\x1e\xf5b\'#<\xd2.\xe6\xc0\xc1\xe6\xa6I\xc4@t\xe9\x8a\xcb\x8e\xe0\xa8\xe7\xf9\xd3\x9eRq\xc9\xa0\r\xb8o\xc0\xc7 qW\xa2\xbd\xc8\x04\xe4\x8cW.\x931\xcf5/\xda\x1b\xd6\x90;\x1b\xd3jJ8\xc69\xee*\x94\x9a\x88|\xfc\xc3\xaf`k"K\xa6ls\x9a\xaaX\x8e\x87\x14\xec\xc4mI\xa8 \x03\x93\x9f\xc6\xab\xb6\xa6\xc7\xa1?\x89\xcdg!\xdd\x9ax\x84\xb7L\xd3\xb5\xc2\xe4\xb2\xdf\xbbw\xf7\xa8\r\xf3\xf7\xa9\r\x8b\xf7o\xd6\xab\xb5\xb9\\r\r5\x12y\x8b\x02\xeb\xdb\xf5\xa9R\xe1Fpj\xb0\x8b=\xaax\xad\xb2O\xbd\x1c\xa3\xb9\xa1\x15\xcesS\x07\r\xedP$;s\x9cT\xca\x14\xf4\x14X7\'^}j`\xde\xb5\x10\x14\xa5\xf1\xde\x8b\x05\xc9\t#\xb9\xa6oo\xaf\xe3Q4\xe1G\\T\x0fq\x93\xd74\\\rh\xa6\x0358\x9dGZ\xc2[\x9d\xbe\x95"]\xb3\x11\xcf\xe5Hf\xd1\x99OJ\x81\xa5\x1f\xe4\xd55\xba\xe3\x074\x8f.z\x1e\xd4\xc9c\xe4"\xa2g&\x9b\xbf=\xe9\xaeX\x9e\x9f\xad;\x01b\'\x07\xf15\xa1j7u\xeeqYP\x92\x08\xfa\xd6\x85\xbc\xac\x07\x1e\xb4\xac4p\x86\x10}?*Qn[\xb6*\xda\x855*\x10\xa0\xd5\xdfB,U\x16\xbbz\x9ao\x94\x05Zr3B\x85=E&\xc1\x14X\x1fCDA\xb9\xce\x7f*\xd2\xf2P\x8c\xe0~T\xc7TPp\x07OJZ\x0e\xec\xaf\x9cTO\x93\xe9\xf8T\xe4\x83H"\xddE\x8a\xb8\xc4\x99\x96\xa6Y\x0b\x8fO\xa5*[\xf23\xebR\x15\xd80\x05$+\x90\x98\xe9\x85\x00`*\x7f\xbdN\x10\xe7\x9c\x8f\xce\xa8[\x04\x08\xbe\x83\xaf\xa5[H\xd0\n\xa9\x81\x1f9\xe9R\xc7.\xe1H4,\x16\xc7\x03\x91NX\x95\xc6O\x06\xa3E-\x83\x9a\x9dF\x05\x00Fm\x01?/4\xf4\xb7d\xea9\xa9\x16@\x87\x9ax\x98;\n/\xd0\x08\xb6\xb0\x19"\x95$\xc7Q\xde\xa7b6\x13U%p\xb9\xc0\xa1\xae\xc0\x9fr\xda\xca\x08\xe9Q\xcd\xdf\xe9U\xa3\x90\x97\x1e\x95`(a\xd4f\x85\xa0\xca\xacX\xd39\xfcj\xe3\xa8T>\xb5Ny\x82\x16\xc9\xe9E\x85q\xc1\x0bT\x8b\x19QT~\xd8\x03|\xa4T\x82\xed\x8fZW\x19p\xb8^M(\xb8\x18\xaabm\xfdiA\x04\xe0\x1a\x04\\\xf3\x81\xef\xcd=\\\xb6=*\xa2\x9c\x01O\xf3\xb6\xaf\x06\x81\x9a0\x94\x1bry\xf4\xab?hX\xd3\x01y\xfaV:\xcaN\t<R\xc9p<\xb2\x01\xef\x8a5\x03\x16#\x91\xf8\xd4\xb9#\xa5f\xa5\xd7#\x03?\x85N\x97$\x00q\xfaS\x02y\'\x0b\x90z\xd4bM\xe4\x11Un.rX\xe3\xf4\xa8\xe2\xba\xc3\x0f\xebC\x11\xab\x1b\x101M\x91\xb2NA\xa6Z\xcf\xe6\x15\x07\x1c\xe7\xb5[h\x83)\xe9\xf9P\x81\xe8R,\x14\x1a\x16}\xa7\xb5>X@$g\xf4\xa8\x8c\x03\xaey\xa7d\t\xd8\xb5\x14\xf9\xc6ju!\xc7z\xa3\x1am\xc5N\xb3\x04\x03\x91\xf9\xd4\xda\xc3\xdd\x13l\xc3{S\x8f\tU^pI \xf3QI+m=\x0e}i\xfa\t\x13HNH\x15$\x04\x82\xb9\xaa\x11\xcb\xf3sS\x8b\x80\xaa\x08\xa43M_\x8e\xb4\x190+-o\x0e\xea\x9b\xed\x8aTr3\xf44\\\x0b\xa2@z\xd1\xe6\xe1\xba\x8a\xa8g\x0c\xa3\x07\xf2\xa8L\xa41\xe4\x9ab6Re\xf2\x80$g\xebQ\xbc\xaa\t\xc8\xc8\xacYu\x07A\x8c\xf48\xaa\x92_\xbb\x13\xcfzI;X4l\xe8\xbc\xe4\x07\x81\x8f\xc2\x9an\xb6\x9e\x1b\xf9\xd7<.\x1c\xf7\xa9\x10\xb3u4j3u\xee\xf7&9\xc9\xef\x9a\xa1q!$\x92z\x9cUu\r\xe9\x9ac\xee=E4\x9aD\xb6H\x1b\x9e\xb5"\xbdRi\nw\xa1.\xb2{\xd2z\x14\x8d\x05~z\xd4\xc2A\xb4`\xe0\xd5\x05\x98\x11\xd6\xa4\xf3\x06\x074\t\x97V@\x0f\xde\x1f\x9dI\x13\x82\xc7\x9e\xd5\x90.\x80\'\xadM\x1d\xd8\x07\x83@nk3aA\x15Q\xe6%\x8f\'\xadD/wq\x9al\x8d\xbb\xbdRw\x11\x9f\x1a\x10\x00\xc5L\x80\x0e\xa2\xa0\x82\xed\x18\xf1\xd7\x15z\x12\x92c t\xcfJ\x15\x83R"\x8a\xfcb\xa2h\x82\x9c\x81Z\x02\xddz\xd3\x1e\x0c\xf4\x15B\xd8\xab\x06Cr8\xc5hF\xff\x00(\x1d\xb1P\xac\x07=1S\xc4\x02\x9e})Z\xcc{\x90>w\x13\x83\xd6\x9a\x1c\x03\xd2\xa5\x95\xd7\xb7\xadV|g\xafZ7\x04>I>^8\xa8\x0b\x16\'\x9aFr{\xe2\xa2i\x88\xefR2\xc0`\x074\xc9\xa7\x01\x7f\x1a\xa1%\xe7L\x9a\xaf\xf6\x82\xfd\x06h\x02\xd4\x97\x8c\t\xc7\x1c\xd3\x05\xe6O&\xb3\xe6\x9d\xc68\xaa\x8ft\xc3\x14X.i\xcfx\xcc0\x18u\xf6\xa2\x0b\x92\x18\x96n1\xedXbiO\x7f\xd6\xae\xc3\x14\x8d\xbb$\x8f\xc6\x9d\x98\xael6\xaa\x91\x01\x93\x9f\xca\x94jc=\x07\xf9\xfck0\xd87\xf1\x1c\xfdiY\x0faC\x80)\x1a\xe2u\x9b#\xf1\xe2\xab\xcd0Lq\xd6\xa9\x87q\xdb\x14\xd2\xec\xfdA\xa6\x93\x16\x85\x84\xbf\x1c\xf2?#Z\x16\xd3n\xdd\x9e\xd5\x9c\x96\xe7\x9c\x03\xf8\xd5\xa4\x0c\xb9\xe4R\xe5\x1aw7\x14\x05\xec*\xac\x988\xc1\xaa\x82\xe9\xbd\x05H\xb2\xee\xa16\xc5a\xc6\x00j\xa4\x91\x0e+A:\x13P\xcb\x08$`\x1a\xa4\xc0\xa0\xccW\xa1\xa7\xfd\xab\x1e\xb4\xf9 \xc1\xa6-\xbd.P\xe6"y\xbaqQ\xad\xeb\'\x02\xadIn\xa4\x13\x9eqT\xa5\xb6\xc7#\xb0\xa7\xcbpL\xb6\x97\xa7\x9c\xe6\xa57\x8c\xd8\xf9\x8f\xebX\xcc\xee\x9c\x00M4L\xdb\x87\x04TZ\xc3\xb9\xff\xd9'
model_path = 'model.keras'
print(inference(test_image_bytes, model_path))