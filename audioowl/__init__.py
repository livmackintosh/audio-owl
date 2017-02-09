__version__ = '0.1.0'
__author__ = 'Olivia Mackintosh'
__email__ = 'livvy@base.nu'
__license__ = 'GPLv3'
__status__ = 'Development'

if __name__ == '__main__':
    from . import gui
    ow = gui.OwlyWindow()
    ow.run()
