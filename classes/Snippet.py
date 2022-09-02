from classes.ArgObject import ArgObject
from copy import copy

class Snippet(ArgObject):
    """Container is object that contains only one snippet of code"""

    def __init__(self, **arg):
        super(Snippet, self).__init__(**arg)
    
    def load(self, **arg):
        self.arg['language'] = arg.get('language', 'txt')
        self.arg['name'] = arg.get('name', '')
        self.arg['content'] = arg.get('content', '')
        self.arg['tags'] = arg.get('tags', [])
        
    def dumpd(self):
        arg = copy(self.arg)
        arg['type'] = 'Snippet'
        return arg
        
    def __str__(self):
        return f'<{self.arg["language"]}:{self.arg["name"]}>\n{self.arg["content"]}'
        
    def __repr__(self):
        return f'Snippet <{self.arg["language"]}:{self.arg["name"]}>'