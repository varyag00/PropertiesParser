import parser

class MyTestClass(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


def test_is_primitive():
    primitives = (
        42,
        True,
        False,
        3.141592653589793238462648898,
        'A primitive',
        u'Another primitive',
        None,
    )
    for prim in primitives:
        assert parser.is_primitive(prim)


def test_parser():
    my_test_instance = MyTestClass(
        x=42,
        y={'test': 'dictionary'},
        z=['my list']
    )

    parsed = parser.parse_instance(my_test_instance)
    print(parsed)
