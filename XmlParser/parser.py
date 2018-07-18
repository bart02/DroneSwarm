import xmltodict
# from pprint import pprint

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
                                print "Types hasn't got " + prm + ', use str.'
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
                                print "Types hasn't got " + prm + ', use str.'
                                actiondict[prm] = str(val)
                        # print {action: actiondict}
                    ready[time][copternum].append({str(action): actiondict})
                except TypeError:
                    raise ValueError('You can use only one "swarm" tag')
        except KeyError:
            pass
    return ready


# pprint(parse_xml(xml_file='alex.xml'))
