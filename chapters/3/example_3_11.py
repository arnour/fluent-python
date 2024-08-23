# shows some basic operations supported by all dictionary views

d = dict(a=10, b=20, c=30)

values = d.values()

assert list(values) == [10, 20, 30]

d['z'] = 99

assert list(values) == [10, 20, 30, 99]