import json

def j(obj):
    return json.dumps(obj)

def o(json_str):
    return json.loads(json_str)

def make_A_record(ip, **kwargs):
    ret = {
      "host": ip,
      "ttl": 600
    }
    ret.update(kwargs)

    return ret

def dom_to_path(domain):
    """
    ドメインをetcdに格納する形式のパスに変換する

    Parameters
    ----------
    domain : str
        変換したいドメイン(hoge.huga.com)

    Returns
    -------
    path : str
        変換後のパス(com/huga/hoge)
    """

    if "" in domain.split("."):
        raise ValueError(f"'{domain}' includes consecutive dots.")

    if domain[0] == "." or domain[-1] == ".":
        raise ValueError(f"'{domain}' starts/ends with dot.")

    return "/".join(reversed([ d for d in domain.split(".") ]))

def squeeze(path, delim):
    """
    受け取った文字列の連続する文字を一つにする

    Parameters
    ----------
    path : str
        連続する文字が入った文字列(e.g. "///hoge///huga//com")
    delim : str
        連続する文字(e.g. "/")

    Returns
    -------
    path : str
        変換後のパス(/hoge/huga/com)
    """

    ret = ""

    for p in path:
        if len(ret) == 0 or ret[-1] != p:
            ret += p

    return ret
