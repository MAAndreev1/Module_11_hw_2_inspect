from pprint import pprint
import inspect


def introspection_info(obj):
    info = dict()
    info['type'] = type(obj)
    info['callable'] = callable(obj)
    info['attributes'] = [x for x in dir(obj) if not callable(getattr(obj, x))]
    info['methods'] = [x for x in dir(obj) if callable(getattr(obj, x))]
    info['modul'] = inspect.getmodule(obj)
    return info


number_info = introspection_info(pprint)
pprint(number_info)
