# Duplex Communication between Android and Raspberry pi using Bluetooth

Raspberry pie is done using python 2.7. I have used [pyBluez](https://github.com/karulis/pybluez) for the communication.

I have just followed the following command to install pyBluez

    sudo apt-get update
    sudo apt-get install python-pip python-dev ipython

    sudo apt-get install bluetooth libbluetooth-dev
    sudo pip install pybluez

I have got two error while using pyBluez

    bluetooth.btcommon.BluetoothError: (2, 'No such file or directory')
        
I have followed this [article](https://raspberrypi.stackexchange.com/a/42262/76919) to solve the issue

    bluetooth.btcommon.BluetoothError: (13, 'Permission denied')
    
I have followed this [article](https://stackoverflow.com/a/42306883/4161269) to solve the issue.

In the android part, You have to add the following permission in *AndroidManifest.xml*

    <uses-permission android:name="android.permission.BLUETOOTH" />
    <uses-permission android:name="android.permission.BLUETOOTH_ADMIN" />
    
I have used maual pairing system in order to communicate. I will work on the auto pairing system. When i do, i will update this git. 

I you have any issue, feel free to create issue.

Thanks.
