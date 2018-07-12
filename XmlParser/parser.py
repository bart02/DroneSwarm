from bs4 import BeautifulStoneSoup
import xmltodict
from pprint import pprint

try:
    import xml.etree.cElementTree as ElementTree
except ImportError:
    import xml.etree.ElementTree as ElementTree


xml = '''<DroneSwarm>
    <time t="1.03">
        <copter n="1">
            <reach x="5" y="6" z="1" />
        </copter>
        <swarm>
            <led function="rainbow" />
        </swarm>
    </time>
    <time t="1.05">
        <copter n="1">
            <reach x="5" y="6" z="1" />
        </copter>
        <swarm>
            <led function="rainbow" />
        </swarm>
    </time>
</DroneSwarm>'''




xmldict = xmltodict.parse(xml)
xmldict = dict(xmldict['DroneSwarm'])['time']
for e in xmldict:
    time = e['@t']
    for copter in e['copter']:
        print e['copter'][copter]

