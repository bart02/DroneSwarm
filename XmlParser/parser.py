import xmltodict
from pprint import pprint

types = {
    'x': float,
    'y': float,
    'z': float,
    'yaw': float,
    'yaw_rate': float,
    'speed': float,
    'tolerance': float,
    'frame_id': str,
    'wait_ms': int,
    'timeout': int,
    'z_coefficient': float,
    'timeout_arm': int,
    'timeout_land': int,
    'preland': bool,

}

xml = '''<DroneSwarm>
    <time t="1.03">
        <copter n="1">
            <reach x="5" y="6" z="1" />
        </copter>
        <swarm>
            <led mode="rainbow" />
        </swarm>
    </time><time t="4.20">
        <copter n="3">
            <led mode="blink" r="255" g="0" b="100"/>
        </copter>
        <swarm>
            <circle x="1" z="1.5" y="2" r = "3"/>
        </swarm>
    </time>

</DroneSwarm>'''

xmldict = xmltodict.parse(xml)
xmldict = dict(xmldict['DroneSwarm'])['time']
ready = {}
if type(xmldict) != list:
    xmldict = [xmldict]
for t in xmldict:
    time = float(t['@t'])
    ready[time] = {}
    # print time
    if type(t['copter']) != list:
        t['copter'] = [t['copter']]
    for copter in t['copter']:
        copternum = int(copter['@n'])
        # print copternum
        ready[time][copternum] = []
        copter.pop('@n')
        for action in copter:
            actiondict = {}
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

    swarm = t['swarm']
    copternum = 0
    ready[time][copternum] = []
    for action in swarm:
        actiondict = {}
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
pprint(ready)
