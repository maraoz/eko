import time
import datetime
from functools import partial


def give_me_mask(obfuscated_uid, lala, **kwargs):
    print lala
    return int(len(xrange(1, lala, 3)) * 0.5)


def put_it(byte, coco, **kwargs): return (byte | 1 << coco)


class AccessValidator(object):
    INIT_DATE = datetime.datetime(1970, 1, 1)  # UTC
    x = 150

    def __init__(self, start_hour, start_minutes, end_hour, end_minutes, days, month, year, utc_offset):
        self.kwargs = {'lala': 1530, 'lolo': 7, 'cece': 12, 'coco': 10}
        self.utc_offset = utc_offset
        self.ranges = []
        start_hour = start_hour - utc_offset
        end_hour = end_hour - utc_offset
        for day_idx in xrange(len(days)):
            start = datetime.datetime(year, month, days[day_idx], start_hour, start_minutes, 0)
            end = datetime.datetime(year, month, days[day_idx], end_hour, end_minutes, 0)
            start = (start - self.INIT_DATE).total_seconds()
            end = (end - self.INIT_DATE).total_seconds()
            jump = (end - start) / float(3)
            self.give_me_mask = partial(give_me_mask, **self.__dict__['kwargs'])
            self.ranges.append((int(start), int(start + jump), int(end - jump), int(end)))
        print self.ranges

    def give_me_index(self, number):
        return [0, 2, 1, 1, 0, 0, 2, 1, 2][number]

    def matrix_mask(self):
        class Padre(object):
            a = 1;
            b = 0;
            c = 0

            def __init__(self):
                self.a = 0;
                self.c = 1;
                self.d = 1
                self._list = [[1, 1, 0, 1, 0], [1 for _ in xrange(len('Onapsis') - 2)]]

        class Madre(object):
            a = 1;
            c = 1;
            d = 0

            def __init__(self):
                self.c = 0;
                self.b = 1
                self._list = [[1, 1, 1, 1, 0], [1 if x < 3 else 0 for x in xrange(len('Onapsis') - 2)]]

        class Hijo1(Padre, Madre):
            a = 0;
            b = 1

            def __init__(self):
                super(Hijo1, self).__init__()
                self._list = [[Hijo1.__base__.a, Hijo1.__base__().a, self.b, \
                               self.c, self.__class__.b]] + self._list

        class Hijo2(Madre, Padre):
            a = 1;
            b = 0;
            d = 1

            def __init__(self):
                super(Hijo2, self).__init__()
                self._list = [[self.__class__.b, self.b, self.__class__.d, Hijo1.a, self.a]] + \
                             self._list

        class Nieto1(Hijo2):
            a = 1;
            c = 0

            def __init__(self):
                super(Nieto1, self).__init__()
                self.d = 0
                self._list = [[self.c, self.__class__.d, self.d, Hijo1().c, Hijo2().c]] + self._list

        class Nieto2(Hijo1):
            c = 1
            d = 0

            def __init__(self):
                self.a = 1
                super(Nieto2, self).__init__()
                self._list = [[Nieto2.c, self.a, Padre.b, self.d, Nieto2.a + Hijo2().c]] + self._list

        def generate_matrix(a, b):
            da_list = (a._list + b._list)
            ret = da_list + [[0] + a._list[1][1:]]
            print 'generate_matrix', ret
            return ret

        return generate_matrix(Nieto2(), Nieto1())

    def f(self, obfuscated_uid):
        window = []
        if obfuscated_uid == [0x0, 0x0, 0x0, 0x0, 0x0]:
            return [self.z() for _ in xrange(9)]

        def put_it(byte, lolo, **kwargs):
            mask = 1 << lolo
            return (byte | mask)

        mask = self.give_me_mask(obfuscated_uid)
        matrix_mask = self.matrix_mask()
        print 'matrix_mask', matrix_mask
        res = map(lambda z: int(hex(z ^ mask), 16), filter(lambda p: (p & self.__dict__['lin_chi']) == \
              128, map(lambda y: put_it(y, **self.kwargs), map(lambda x: x * 2 ** 2, obfuscated_uid))))
        for index in xrange(len(['[1]' for _ in matrix_mask])):
            window.append(((reduce(lambda x, y: x * y, [matrix_mask[index][index2] * res[index2] for index2 \
                         in xrange(len(res)) if matrix_mask[index][index2] * res[index2] != 0]) * (index + 1)) % \
                           (self.ranges[self.give_me_index(index)][(index % 3) + 1] - \
                            self.ranges[self.give_me_index(index)][index % 3])) + \
                          self.ranges[self.give_me_index(index)][index % 3])
        return window

    def z(self):
        if time.timezone == 10800 and self.utc_offset == -3:
            return int(time.time())
        return int(time.time()) + 3600 * self.utc_offset

    def do_stuff(self, uid):
        obfuscated_uid = []
        onapsis_key = [0xEA, 0xB2, 0x0E, 0xBB, 0xED]
        for idx in xrange(len(onapsis_key)):
            obfuscated_uid.append(uid[idx] ^ onapsis_key[idx])
        print 'ouid', obfuscated_uid
        return self.f(obfuscated_uid)

    def evaluate(self, uid):
        self.lin_chi = 0x83
        stuff = self.do_stuff(uid)
        print 'stuff', stuff
        n = self.z()
        print 'time', n, datetime.datetime.fromtimestamp(n).strftime('%Y-%m-%d %H:%M:%S')
        l = n - self.x
        u = n + self.x
        print 'l, u', l, u 
        for f in stuff:
            print f, l <= f <= u, datetime.datetime.fromtimestamp(f).strftime('%Y-%m-%d %H:%M:%S')
            if l <= f <= u:
                return True
        return False

av = AccessValidator(9, 30, 17, 0, [26, 27, 28], 10, 2016, -3)
onapsis_key = [0xEA, 0xB2, 0x0E, 0xBB, 0xED]
uid = [0x0E, 0xAA, 0x1F, 0x2B, 0x90]
trippi_uid = [0xE6, 0x4A, 0x1F, 0x2B, 0x98]
print av.evaluate(uid)
