from enum import IntEnum

class RCompressionSetting:
    class EAlgorithm(IntEnum):
        kInherit = -1
        kUseGlobal = 0
        kZLIB = 1
        kLZMA = 2
        kOldCompressionAlgo = 3
        kLZ4 = 4
        kZSTD = 5
        kUndefined = 6