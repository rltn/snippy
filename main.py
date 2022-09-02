from classes.Snippet import Snippet
from classes.Container import Container
from classes.Loader import Loader

def main():
    loader = Loader(filepath='save.json')
    main_container = loader.load_object()
    
    loader.save_object(main_container)
    print(main_container)

if __name__ == '__main__':
    main()