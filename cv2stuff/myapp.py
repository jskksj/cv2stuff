# myapp.py
import logging
import mylib

def main():
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.info('Started')
    mylib.do_something()
    logging.info('Finished')

if __name__ == '__main__':
    main()
