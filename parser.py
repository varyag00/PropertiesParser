"""Parses instances of simple classes into its properties.HasProperties equivalent

Note on primitives:
- this extends the definition of "primitive" to include subclasses of primitives, e.g.

class MyStr(str):
    ...

"""

# import pickle
import properties

DICT_TEMPLATE = '\nproperties.Dictionary(\'{docstring}\', key_prop={key_prop}, value_prop={value_prop})\n'
LIST_TEMPLATE = '\nproperties.List(\'{docstring}\', {props})\n'

PRIMITIVE_TEMPLATES = {
    'str': '{name} = properties.String(\'{docstring}\')\n',
    'unicode': '{name} = properties.String(\'{docstring}\')\n',
    'bool': '{name} = properties.Bool(\'{docstring}\')\n',
    'int': '{name} = properties.Int(\'{docstring}\')\n',
    'float': '{name} = properties.Float(\'{docstring}\')\n',
}   # Nonetype = String?

PRIMITIVES = (str, unicode, bool, int, float, type(None))


def is_primitive(value):
    result = isinstance(value, PRIMITIVES)
    return result


def format_primitive(value, name):
    primitive = PRIMITIVE_TEMPLATES[get_primitive(value).__name__].format(
        name=name,
        docstring='test docstring',
    )
    return primitive


def get_primitive(value):
    for prim in PRIMITIVES:
        if not isinstance(value, prim): continue
        return prim
    else:
        raise ValueError('Unable to find {} primitive for {}'.value())


def parse_attr(name, val):
    parsed = ''

    if is_primitive(val):
        template = format_primitive(val, name)
        parsed += template

    if type(val) in (dict,):
        parsed += DICT_TEMPLATE.format(
            docstring='test docstring',
            key_prop='properties.String(\'docstring\')',
            value_prop='properties.String(\'docstring\')',
        )

    return parsed

def parse_instance(instance):

    parsed = 'class Parsed(properties.hasProperties):\n'

    for name, val in instance.__dict__.items():
        parsed += parse_attr(name, val)

    return parsed
