from FlightLib import FlightLib as f

f.init('server')
# from FlightLib import TelemLib
from FlightLib import LedLib as led
from time import sleep
import socket
import sys

sq = []

while True:
    try:
        sock = socket.socket()
        sock.connect(('192.168.1.6', 35001))
    except socket.error:
        print("No connection. Sleep 10 secs.")
        sleep(10)
    else:
        break


def animation():
    def start_animation_1(self):
        # xml parcer
        time.sleep(4.5)

        types = {

            'x': float,

            'y': float,

            'z': float,

            'yaw': float,

            'yaw_rate': float,

            'speed': float,

            'tolerance': float,

            'frame_id': str,

            'mode': str,

            'wait_ms': int,

            'timeout': int,

            'z_coefficient': float,

            'timeout_arm': int,

            'timeout_land': int,

            'preland': bool,

            'r': int,

            'g': int,

            'b': int,

        }

        def parse_xml(xml_file=None, xml_str=None):

            if (xml_file is None and xml_str is None) or (xml_file is not None and xml_str is not None):
                raise ValueError('You must use one parameter')

            if xml_str is None:

                with open(xml_file, 'r') as f:

                    xml = f.read().strip()

            else:

                xml = xml_str

            xmldict = xmltodict.parse(xml)

            xmldict = dict(xmldict['DroneSwarm'])['time']

            ready = {}

            if type(xmldict) != list:
                xmldict = [xmldict]

            for t in xmldict:

                time = float(t['@t'])

                ready[time] = {}

                try:

                    if type(t['copter']) != list:
                        t['copter'] = [t['copter']]

                    for copter in t['copter']:

                        copternum = int(copter['@n'])

                        ready[time][copternum] = []

                        copter.pop('@n')

                        for action in copter:

                            actiondict = {}

                            try:

                                for prm in dict(copter[action]):

                                    val = dict(copter[action])[prm]

                                    prm = str(prm.replace('@', ''))

                                    try:

                                        actiondict[prm] = types[prm](val)

                                    except KeyError:

                                        print("Types hasn't got " + prm + ', use str.')

                                        actiondict[prm] = str(val)

                                # print {action: actiondict}

                                ready[time][copternum].append({str(action): actiondict})

                            except ValueError:

                                raise ValueError('You can use only "n" parameter in "copter" tag')

                except KeyError:

                    pass

                try:

                    swarm = t['swarm']

                    copternum = 0

                    ready[time][copternum] = []

                    for action in swarm:

                        actiondict = {}

                        try:

                            if swarm[action] is not None:

                                for prm in dict(swarm[action]):

                                    val = dict(swarm[action])[prm]

                                    prm = str(prm.replace('@', ''))

                                    try:

                                        actiondict[prm] = types[prm](val)

                                    except KeyError:

                                        print("Types hasn't got " + prm + ', use str.')

                                        actiondict[prm] = str(val)

                            ready[time][copternum].append({str(action): actiondict})

                        except TypeError:

                            raise ValueError('You can use only one "swarm" tag')

                except KeyError:

                    pass

            return ready

        data = ''
        xm = parse_xml(xml.xml)
        print(xm)
        n = 0
        for i in xm:

            for k in xm[i]:
                # k =  copter number
                s = str(xm.keys())[str(xm.keys()).index('[') + 1:-2]
                p = s.split(', ')
                try:
                    timeout = str(((float(p[n + 1]) - float(p[n])) * 1000) - 2000)
                except:
                    print('end')

                for l in xm[i][k]:

                    o = str(l.keys())
                    f = o[o.index('[\'') + 2: -3]  # f =  function

                    # l[f] = parameters
                    if k == 0:
                        k = 'all'

                    if f == 'circle':
                        x = str(l[f]['x'])
                        y = str(l[f]['y'])
                        z = str(l[f]['z'])
                        r = str(l[f]['r'])

                        data = 'f.circle' + '(' + x + ',' + y + ',' + z + ',' + r + ',' + 'timeout =' + timeout + ')'

                        print(data, k)
                        print('_______________________')
                        self.sender(bytes(data, 'utf-8'), str(k))
                    if f == 'music':
                        file = str(l[f]['file'])

                        os.system(r"start" + file)
                        time.sleep(3)


                    elif f == 'led':
                        print(n)
                        r = float(l[f]['r'])
                        g = float(l[f]['g'])
                        b = float(l[f]['b'])

                        led.fill(r, g, b)

                        print(bytes(data, 'utf-8'), str(k))
                        print('_______________________')
                    elif f == 'reach':
                        x = float(l[f]['x'])
                        y = float(l[f]['y'])
                        z = float(l[f]['z'])
                        try:
                            speed = float(l[f]['speed'])
                            f.reach(x, y, z, speed=speed, timeout=timeout)

                        except:
                            speed = 0.6
                            f.reach(x, y, z, speed=speed, timeout=timeout)

                        print(bytes(data, 'utf-8'), str(k))
                        print('_______________________')
                    elif f == 'takeoff':
                        z = float(l[f]['z'])
                        try:
                            speed = float(l[f]['speed'])
                            f.takeoff(z, timeout_arm=1000, speed=speed, timeout_fcu=(float(timeout) - 1000) // 2,
                                      timeout=(float(timeout) - 1000) // 2)

                            print(bytes(data, 'utf-8'), str(k))
                        except:
                            f.takeoff(z, timeout_arm=1000, timeout_fcu=str((float(timeout) - 1000) // 2),
                                      timeout=(float(timeout) - 1000) // 2)

                            print(bytes(data, 'utf-8'), str(k))

                        print('_______________________')
                    elif f == 'land':
                        f.land(timeout=float(timeout))

                        print(bytes(data, 'utf-8'), str(k))
                        print('_______________________')
                    elif f == 'attitude':
                        z = float(l[f]['z'])
                        f.attitude(z, timeout=timeout)

                        print(bytes(data, 'utf-8'), str(k))
                        print('_______________________')
                    elif f == 'stay':
                        x = str(l[f]['x'])
                        y = str(l[f]['y'])

                        print(bytes(x + ' ' + y, 'utf-8'), str(k))
                        print('_______________________')

            s = str(xm.keys())[str(xm.keys()).index('[') + 1:-2]
            p = s.split(', ')
            print(p)

            try:
                time.sleep((float(timeout) + 1500) // 1000)

            except:
                print('end of list')
            n += 1


try:
    while True:
        data = str(sock.recv(1024))
        print(data)
        try:
            if b'programm' in data:
                xm = open('xml.xml', 'w')
                data = data[data.index(b'programm') + 8:]
                xm.write(data)

                while True:
                    data = str(sock.recv(1024))
                    if b'stop' in data:
                        xm.write(data[:data.index(b'stop')])

                        t_0 = Thread(target=animation)
                        t_0.daemon = True
                        t_0.start()

                        time.sleep(2)
                        break
                    else:
                        xm.write(data)

            else:
                try:
                    sq = data.split('$$')
                    for i in range(len(sq) - 1):
                        print(sq[i])
                        eval(sq[i])

                except Exception as e:
                    print(e)

        except:
            print('er')
    sock.close()
except KeyboardInterrupt:
    print("Shutting down")
    led.off()
    sock.close()
