import os
import pytest

import etcdclient

@pytest.fixture(scope="session")
def etcd():
    key = "_test_"
    etcd_host = os.getenv("ETCD_HOST")
    etcd_port = os.getenv("ETCD_PORT")
    etcd = etcdclient.Etcd(key, host=etcd_host, port=etcd_port)
    etcd.put("hoge", {"value": "huga"})

    yield etcd

    etcd.delete("hoge")

def test_etcdclient_buid_key(etcd):
    actual = etcd._build_key("//hoge")
    expect = "/_test_/hoge"

    assert(actual == expect)

def test_etcdclient_put(etcd):
    etcd.put("piyo", {"value": "moge"})
    actual = etcd.get("piyo")
    expect = {"value": "moge"}

    assert(actual == expect)

def test_etcdclient_get(etcd):
    actual = etcd.get("hoge")
    expect = { "value": "huga" }

    assert(actual == expect)

def test_etcdclient_get_all(etcd):
    actual = etcd.get_all()
    expect = [
        {'/_test_/hoge': {'value': 'huga'}},
        {"/_test_/piyo": {"value": "moge"}}
    ]

    assert(actual == expect)

