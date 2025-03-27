import argparse
from dataclasses import dataclass

KRKG_SIGNATURE = 0x4b524b47 # KRKG

@dataclass
class Vec3f:
    x: float
    y: float
    z: float

@dataclass
class Quatf:
    v: Vec3f
    w: float


@dataclass
class KRKG:
    @dataclass
    class Frame:
        pos:            Vec3f
        fullRot:        Quatf
        extVel:         Vec3f = None
        intVel:         Vec3f = None
        speed:          float = None
        acceleration:   float = None
        softSpeedLimit: float = None
        mainRot:        Quatf = None
        angVel2:        Vec3f = None
        raceCompletion: float = None
        checkpointId:   int   = None
        jugemId:        int   = None

    framecount: int
    version: tuple[int, int]
    data_offset: int

def read_krkg(filename: str) -> KRKG:
    pass

def read_csv(filename: str) -> KRKG:
    pass


def write_krkg(filename: str, krkg: KRKG):
    pass

def write_csv(filename: str, krkg: KRKG):
    pass



def read(mode: str, filename: str) -> KRKG:
    match mode:
        case 'krkg': return read_krkg(filename)
        case 'csv': return read_csv(filename)

def write(mode: str, filename: str, krkg: KRKG):
    match mode:
        case 'krkg': return write_krkg(filename, krkg)
        case 'csv': return write_csv(filename, krkg)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--from', choices=['csv', 'krkg'], required=True, dest='f')
    parser.add_argument('-t', '--to', choices=['csv', 'krkg'], required=True, dest='t')
    parser.add_argument('in_file')
    parser.add_argument('out_file')
    args = parser.parse_args()

    krkg = read(args.f, args.in_file)
    write(args.t, args.out_file, krkg)
    