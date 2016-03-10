import pickle
import namedtuple


Point = namedtuple('Point', ['x', 'y'])
Point.__doc__ += 'A doc string'
p1 = Point(11, 22)

protocol_version_4 = 4


def saveini(o, fp):
    with open(fp, 'wb') as f:
        pickle.dump(o, f, protocol_version_4)


def loadini(fp):
    with open(fp, 'rb') as f:
        return(pickle.load(f))
