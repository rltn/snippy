from classes.ArgObject import ArgObject
from classes.Container import Container
import json

# TODO: loader realization
class Loader(ArgObject):
    """Loader object makes all loading/saving work"""

    def __init__(self, **arg):
        super(Loader, self).__init__(**arg)
    
    def load(self, **arg):
        self.arg['filepath'] = arg.get('filepath', None)
        
    def filepath_check(self, filepath):
        if filepath == None:
            if self.arg['filepath'] == None:
                raise ValueError('load_stuff method has no parseable file path')
            filepath = self.arg['filepath']
        return filepath
        
    def load_object(self, filepath = None):
        filepath = self.filepath_check(filepath)
        
        try:
            with open(filepath, 'r') as o:
                datas = o.read()
                data = json.loads(datas)
        except FileNotFoundError:
            data = {}
            with open(filepath, 'w') as o:
                o.write('{}')
        
        return Container(**data)
        
    
    def save_object(self, obj, filepath = None):
        filepath = self.filepath_check(filepath)
        
        with open(filepath, 'w') as o:
            datas = json.dumps(obj.dumpd(), sort_keys=True, indent=4)
            o.write(datas)
        
    def __str__(self):
        return f'Loader <{self.arg["filepath"] if self.arg["filepath"] else "  "}>'
        
    def __repr__(self):
        return f'Loader <{self.arg["filepath"] if self.arg["filepath"] else "  "}>'