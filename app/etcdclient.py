import etcd3

from util import j, o, squeeze

class Etcd:
    def __init__(self, base_key, **kwargs):
        self.etcd = etcd3.client(**kwargs)
        self.base_key = squeeze("/" + base_key, "/")

    def __getattr__(self, attrname):
        # dynamic proxy
        # 呼び出しもとで実行され、引数は直接扱えないため、こうなっている
        print(f"proxy to self.etcd.{attrname}")

        def func(*args):
            return getattr(self.etcd, attrname)(*args)

        return func

    def _build_key(self, key):
        return squeeze(self.base_key + "/" + key, "/")

    def get(self, key):
        k = self._build_key(key)
        (v, m) = self.etcd.get(k)

        if v is None:
            return None

        v = v.decode('utf-8')
        print(f"{k} => {v}")
        return o(v)

    def put(self, key, value):
        k = self._build_key(key)
        v = j(value)
        print(f"{k} => {v}")
        return self.etcd.put(k, v.encode('utf-8'))

    def get_all(self):
        ret = []

        for (val, meta) in self.etcd.get_all():
            key = meta.key.decode('utf-8')
            value = o(val.decode('utf-8'))

            ret.append({key: value})

        return ret

