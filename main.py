from views.menu import MenuView
from controllers.base import Controller


if __name__ == '__main__':
    controller= Controller(MenuView())
    controller.run()