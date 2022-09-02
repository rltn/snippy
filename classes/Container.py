from classes.ArgObject import ArgObject
from classes.Snippet import Snippet
from copy import copy

class Container(ArgObject):
    """Container is the storage object that contains Snippet or Container objects"""

    def __init__(self, **arg):
        super(Container, self).__init__(**arg)
    
    def load(self, **arg):
        self.arg['name'] = arg.get('name', '')
        self.arg['language'] = arg.get('language', '')
        self.arg['storage'] = arg.get('storage', list())
        self.arg['dump_storage'] = arg.get('dump_storage', list())
        self.arg['decription'] = arg.get('decription', '')
        self.arg['tags'] = arg.get('tags', [])
        self._parse()
    
    def _parse(self):
        while self.arg['dump_storage']:
            item = self.arg['dump_storage'].pop(0)
            if item['type'] == 'Container':
                citem = Container(**item)
            elif item['type'] == 'Snippet':
                citem = Snippet(**item)
            self.append(citem)
                
    
    def dumpd(self):
        arg = copy(self.arg)
        arg['type'] = 'Container'
        for item in arg['storage']:
            arg['dump_storage'].append(item.dumpd())
        del arg['storage']
        return arg
    
    def append(self, item):
        self.arg['storage'].append(item)
    
    def __str__(self):
        s = f'Container <{self.arg["name"]}, {len(self.arg["storage"])} item{"s" if len(self.arg["storage"]) == 1 else ""}> {"{"}\n'
        for item in self.arg['storage']:
            s += f'    {repr(item)}\n'
        s += '}'
        return s
        
    def __repr__(self):
        return f'Container <{self.arg["name"]}, {len(self.arg["storage"])} item{"s" if len(self.arg["storage"]) == 1 else ""}>'