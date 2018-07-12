import xmltodict
from pprint import pprint

xml = '''<DroneSwarm>
    <time t="1.03">
        <copter n="1">
            <reach x="5" y="6" z="1" />
            <led function="rainbow" />
        </copter>
        <swarm>
            <led function="rainbow" />
        </swarm>
    </time>
</DroneSwarm>'''

xmlfile = open('xml.xml', 'r')
xml = xmlfile.read().strip()
xmlfile.close()


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
                prm = prm.replace('@', '')
                actiondict[prm] = val
            # print {action: actiondict}
            ready[time][copternum].append({action: actiondict})

    swarm = t['swarm']
    copternum = 0
    ready[time][copternum] = []
    for action in swarm:
        actiondict = {}
        for prm in dict(swarm[action]):
            val = dict(swarm[action])[prm]
            prm = prm.replace('@', '')
            actiondict[prm] = val
        # print {action: actiondict}
        ready[time][copternum].append({action: actiondict})
pprint(ready)
