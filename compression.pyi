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
    class EDefaults(IntEnum):
        kUseGlobal = 0
        kUseCompiledDefault = 1
        kUseAnalysis = 2
        kUseGeneralPurpose = 3
        kUseSmallest = 4