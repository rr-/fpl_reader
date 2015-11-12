from collections import OrderedDict


class PseudoObject(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self._values = OrderedDict()

    def __setattr__(self, k, v):
        if k.startswith('_'):
            return super(PseudoObject, self).__setattr__(k, v)
        self._values[k] = v

    def __getattr__(self, k):
        if k.startswith('_'):
            return super(PseudoObject, self).__getattribute__(k)
        return self._values[k]

    def __repr__(self):
        keys = self._values
        items = ("\t{}: {!r}".format(k, self._values[k]) for k in keys)
        return '{}({{\n{}}})'.format(type(self).__name__, ",\n".join(items))

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
