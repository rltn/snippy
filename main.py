from classes.Snippet import Snippet
from classes.Container import Container
from classes.Loader import Loader

def main():
    loader = Loader(filepath='save.json')
    main_container = loader.load_object()
    sub_container = Container(name='sub')
    snippet = Snippet(name='greetings', content='hi')
    main_container.append(sub_container)
    sub_container.append(snippet)
    sn = Snippet(name='snippet', content='snippet at root container')
    main_container.append(sn)
    loader.save_object(main_container)
    print(main_container)

if __name__ == '__main__':
    main()