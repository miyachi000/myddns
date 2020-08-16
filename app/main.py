import os
from bottle import run, route, request, response, hook

#from bottle import debug
#debug(True)

from util import j, dom_to_path, make_A_record
from etcdclient import Etcd

SKYDNS_PREFIX = "/skydns"

domain = os.getenv("DDNS_DOMAIN")
BASE_KEY = SKYDNS_PREFIX + "/" + dom_to_path(domain)

etcd_host = os.getenv("ETCD_HOST")
etcd_port = os.getenv("ETCD_PORT")
etcd = Etcd(BASE_KEY, host=etcd_host, port=etcd_port)

########
# hook #
########
@hook('after_request')
def content_type_json():
    response.headers['Content-Type'] = "application/json"

#########
# route #
#########
@route("/ping", method="GET")
def ping():
    return j({"ping": "pong"})

@route("/api/ddns/list", method="GET")
def list():
    return j(etcd.get_all())

@route("/api/ddns/:name", method="GET")
def get_ddns(name):
    return j(etcd.get(name))

@route("/api/ddns/:name/update", method="GET")
def update_ddns(name):
    ip = request.remote_route[0]

    if ip is None:
      return j({"result": "NG"})

    etcd.put(name, make_A_record(ip))

    return j({"result": "OK", "host": ip})

if __name__ == '__main__':
    run(host="0.0.0.0", port=8082)

