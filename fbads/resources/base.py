# coding: utf-8
import dateutil.parser
from decimal import Decimal


class Resource(object):
    datetime_fields = []
    cents_to_decimal = []

    def __init__(self, manager, data):
        self.manager = manager
        self._data = data
        self._set_attributes()

    def _set_attributes(self):
        for k, v in self._data.iteritems():
            if k in self.cents_to_decimal:
                """
                Convert from cents to dollar (Decimal)
                """
                v = v / Decimal('100.00')

            elif k in self.datetime_fields:
                """
                If defined as date field, instantiate a Python datetime object
                """
                v = dateutil.parser.parse(v)

            setattr(self, k, v)

    def __getattr__(self, k):
        if k not in self.__dict__:
            raise AttributeError(k)
        else:
            return self.__dict__[k]

    def __repr__(self):
        reprkeys = sorted(k for k in self.__dict__.keys() if k[0] != '_' and k != 'manager')
        info = u", ".join("%s=%s" % (k, repr(getattr(self, k))) for k in reprkeys)
        return u"<%s %s>" % (self.__class__.__name__, info)

    def to_dict(self):
        return self._data
