from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Final, Literal

from .core          import *
from .colors        import *
from .containers    import *
from .compression   import *
from .graphics      import *
from .histograms    import *
from .io            import *
from .tree          import *
from .RDF           import RDataFrame

from . import RDF

# ========================= #
# Literal color definitions #
# ========================= #
kWhite      :Final[Literal[  0]] = 0
kBlack      :Final[Literal[  1]] = 1
kGray       :Final[Literal[920]] = 920
kRed        :Final[Literal[632]] = 632
kGreen      :Final[Literal[416]] = 416
kBlue       :Final[Literal[600]] = 600
kYellow     :Final[Literal[400]] = 400
kMagenta    :Final[Literal[616]] = 616
kCyan       :Final[Literal[432]] = 432
kOrange     :Final[Literal[800]] = 800
kSpring     :Final[Literal[820]] = 820
kTeal       :Final[Literal[840]] = 840
kAzure      :Final[Literal[860]] = 860
kViolet     :Final[Literal[880]] = 880
kPink       :Final[Literal[900]] = 900
kGrape      :Final[Literal[100]] = 100
kBrown      :Final[Literal[101]] = 101
kAsh        :Final[Literal[102]] = 102
kP6Blue     :Final[Literal[103]] = 103
kP6Yellow   :Final[Literal[104]] = 104
kP6Red      :Final[Literal[105]] = 105
kP6Grape    :Final[Literal[106]] = 106
kP6Gray     :Final[Literal[107]] = 107
kP6Violet   :Final[Literal[108]] = 108
kP8Blue     :Final[Literal[109]] = 109
kP8Orange   :Final[Literal[110]] = 110
kP8Red      :Final[Literal[111]] = 111
kP8Pink     :Final[Literal[112]] = 112
kP8Green    :Final[Literal[113]] = 113
kP8Cyan     :Final[Literal[114]] = 114
kP8Azure    :Final[Literal[115]] = 115
kP8Gray     :Final[Literal[116]] = 116
kP10Blue    :Final[Literal[117]] = 117
kP10Yellow  :Final[Literal[118]] = 118
kP10Red     :Final[Literal[119]] = 119
kP10Gray    :Final[Literal[120]] = 120
kP10Violet  :Final[Literal[121]] = 121
kP10Brown   :Final[Literal[122]] = 122
kP10Orange  :Final[Literal[123]] = 123
kP10Green   :Final[Literal[124]] = 124
kP10Ash     :Final[Literal[125]] = 125
kP10Cyan    :Final[Literal[126]] = 126

del TYPE_CHECKING