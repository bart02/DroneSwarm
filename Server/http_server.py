#!/usr/bin/env python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from json import dumps as json
from mwt import MWT
import rospy
from clever import srv


rospy.init_node('telem_server')
get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)


@MWT(timeout=0.1)
def get_telem(frame_id):
    return get_telemetry(frame_id=frame_id)


class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        path = path.replace('/', '')
        try:
            params = ['armed', 'frame_id', 'mode', 'pitch', 'roll', 'voltage', 'vx', 'vy', 'vz', 'x', 'y', 'yaw',
                      'yaw_rate', 'z']
            telemetry = get_telem(frame_id=path)
            telem = {}
            for e in params:
                attr = getattr(telemetry, e)
                if type(attr) is float:
                    attr = round(attr, 3)
                telem[e] = attr
            resp = json(telem)
            self.send_response(200)
            self.send_header('content-type', 'application/json')
            self.end_headers()
            self.wfile.write(resp)
        except rospy.service.ServiceException as e:
            self.send_response(404)
            self.end_headers()
            self.wfile.write('404: ' + str(e))
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write('500: ' + str(e))


server_address = ('', 8081)
httpd = HTTPServer(server_address, HttpProcessor)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print('exit')
