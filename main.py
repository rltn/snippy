from classes.Snippet import Snippet
from classes.Container import Container
from classes.Loader import Loader

def create_example(loader):
    main_container = loader.load_object()
    sub_container = Container(name='sub')
    snippet = Snippet(name='greetings', content='hi')
    main_container.append(sub_container)
    sub_container.append(snippet)
    sn = Snippet(name='snippet', content='snippet at root container')
    main_container.append(sn)
    loader.save_object(main_container)

def main():
    loader = Loader(filepath='save.json')
    
    print(main_container)

if __name__ == '__main__':
    main()