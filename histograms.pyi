from typing import Generic, TypeVar, Union, overload

from .core import *
from .containers import TArrayD, TArrayF

from numpy import float64 as RDouble, float32 as RFloat
from numpy.typing import NDArray

ContentType = TypeVar('ContentType', RDouble, RFloat)

class TAxis(TNamed, TAttAxis):
    def GetBinLowEdge(self, bin: int) -> float:
        """
        Return bin lower edge for 1D histogram.
        """
        ...

    def GetBinWidth(self, bin: int) -> float:
        """
        Return bin width for 1D histogram.
        """
        ...

    def GetNbinsX(self) -> int:
        """
        Return the number of bins for 1D histogram.
        """
        ...

    def GetBinCenter(self, bin: int) -> float:
        """
        Return bin center for 1D histogram.
        """
        ...
    def GetXbins(self) -> TArrayD:
        """
        Return the bin edges.
        """
        ...
    def SetRangeUser(self, ufirst: float, ulast: float) -> None:
        """
        Set the viewing range for the axis from `ufirst` to `ulast`
        (in user coordinates, that is, the "natural" axis coordinates).

        To set a range using the axis bin numbers, use TAxis.SetRange.

        If `ulast` > `fXmax`, the overflow bin is included in the range
        and will be displayed during drawing. If `ufirst` < `fXmin`, the underflow
        bin is included in the range and will be displayed during drawing.        
        
        Parameters
        ----------
        xmin : float
            Minimum value of the axis.
        xmax : float
            Maximum value of the axis.
        """
        ...

class TH1(TNamed, TAttLine, TAttFill, TAttMarker, Generic[ContentType]):
    @overload
    def __init__(self, name: str, title: str, nbins: int, xlow : float, xup : float):
        """
        Constructor for fix bin size histograms.

        Parameters
        ----------
        name : str
            Name of the histogram (avoid blanks).
        title : str
            Histogram title. If the title is of the form `'stringt;stringx;stringy;stringz'`,
            the histogram title is set to `'stringt'`, the x axis title to `'stringx'`,
            the y axis title to `'stringy'`, etc.
        nbins : int
            Number of bins.
        xlow : float
            Low edge of the first bin.
        xup : float
            Upper edge of the last bin (not included in the last bin).
            
        Notes
        -----
        Creates the main histogram structure.
        """
        ...
    @overload
    def __init__(self, name: str, title: str, nbins: int, xbins : NDArray[Union[RFloat, RDouble]]):
        """
        Constructor for fix bin size histograms.

        Parameters
        ----------
        name : str
            Name of the histogram (avoid blanks).
        title : str
            Histogram title. If the title is of the form `'stringt;stringx;stringy;stringz'`,
            the histogram title is set to `'stringt'`, the x axis title to `'stringx'`,
            the y axis title to `'stringy'`, etc.
        nbins : int
            Number of bins.
        xbins : Sequence[float]
            array of low-edges for each bin. This is an array of type float and size nbins+1.

        Notes
        -----
        Creates the main histogram structure.
        """
        ...
    def GetBinLowEdge(self, bin : int) -> float:
        """
        Return bin lower edge for 1D histogram.

        Better to use `th1.GetXaxis().GetBinLowEdge(bin)` instead.
        
        To get the bin low edge of the first bin, use `th1.GetXaxis().GetBinLowEdge(1)`.
        """
        ...
    def GetBinUpEdge(self, bin : int) -> float:
        """
        Return bin upper edge for 1D histogram.

        Better to use `th1.GetXaxis().GetBinUpEdge(bin)` instead.
        
        To get the bin up edge of the last bin, use `th1.GetXaxis().GetBinUpEdge(nbins)`.
        """
        ...
    def GetBinWidth(self, bin : int) -> float:
        """
        Return bin width for 1D histogram.

        Better to use `th1.GetXaxis().GetBinWidth(bin)` instead.
        """
        ...
    def GetBinContent(self, bin : int) -> ContentType:
        """
        Return bin content for 1D histogram.
        
        Better to use `th1.GetXaxis().GetBinContent(bin)` instead.
        """
        ...
    def GetNbinsX(self) -> int:
        """
        Return the number of bins for 1D histogram.
        """
        ...
    def GetBinCenter(self, bin : int) -> float:
        """
        Return bin center for 1D histogram.

        Better to use `th1.GetXaxis().GetBinCenter(bin)` instead.
        """
        ...
    def GetXaxis(self) -> TAxis:
        """
        Return the X axis of the histogram.
        """
        ...
    def GetYaxis(self) -> TAxis:
        """
        Return the Y axis of the histogram.
        """
        ...

    def GetEntries(self) -> float:
        """
        Return the current number of entries.
        """
        ...
    def GetNbinsY(self) -> int:
        """
        Return the number of bins on the Y axis.
        """
        ...
    @overload
    def Integral(self, binx1 : int, binx2 : int, option : str = "") -> float:
        """
        Return integral of bin contents in range [binx1,binx2].

        By default the integral is computed as the sum of bin contents
        in the range. if option "width" is specified, the integral is the
        sum of the bin contents multiplied by the bin width in x. 
        """
        ...
    @overload
    def Integral(self, option : str = "") -> float:
        """
        Return integral of bin contents.

        Only bins in the bins range are considered.

        By default the integral is computed as the sum of bin contents in the
        range. if option "width" is specified, the integral is the sum of the
        bin contents multiplied by the bin width in x.
        """
        ...
    def SetEntries(self, entries: float) -> None:
        """
        Set the current number of entries.
        """
        ...
    def SetBinContent(self, bin: int, content: float) -> None:
        """
        Set bin content see convention for numbering bins in `TH1.GetBin`.
        
        In case the bin number is greater than the number of bins and the timedisplay
        option is set or CanExtendAllAxes(), the number of bins is automatically
        doubled to accommodate the new bin.
        """
        ...
    @overload
    def SetBinError(self, bin: int, error: float) -> None:
        """
        Set the bin Error Note that this resets the bin error option to be of
        Normal Type and for the non-empty bin the bin error is set by default
        to the square root of their content.

        Note that in case the user sets after calling SetBinError explicitly a
        new bin content (e.g. using SetBinContent) he needs then to provide also
        the corresponding bin error (using SetBinError) since the bin error will
        not be recalculated after setting the content and a default error = 0 will
        be used for those bins.
        """
        ...
    @overload
    def SetBinError(self, binx: int, biny: int, error: float) -> None:
        """
        See convention for numbering bins in TH1.GetBin.
        """
        ...
    @overload
    def SetBinError(self, binx: int, biny: int, binz: int, error: float) -> None:
        """
        See convention for numbering bins in TH1.GetBin.
        """
        ...
    def SaveAs(self, filename: str = "hist", option : str = "") -> None:
        """
        Save the histogram as .csv, .tsv or .txt.

        In case of any other extension, fall back to TObject.SaveAs,
        which saves as a .C macro (but with the file name extension specified by the user)

        The Under/Overflow bins are also exported (as first and last lines).
        The fist 2 columns are the lower and upper edges of the bins Column
        3 contains the bin contents The last column contains the error in y.
        If errors are not present, the column is left empty

        The result can be immediately imported into Excel,
        gnuplot, Python or whatever, without the needing to
        install pyroot, etc.

        Parameters
        ----------
            filename : str
                the name of the file where to store the histogram
            option : str
                some tuning options

        Notes
        -----
        The file extension defines the delimiter used:

            .csv : comma
            .tsv : tab
            .txt : space

        If option = "title" a title line is generated. If the y-axis has a title,
        this title is displayed as column 3 name, otherwise, it shows "BinContent"
        """
        ...
    def GetXaxis(self) -> 'TAxis':
        """
        Return the X axis of the pad.  
        """
        ...
    def GetYaxis(self) -> 'TAxis':
        """
        Return the Y axis of the pad.
        """
        ...
        
class TH1D(TH1[RDouble], TArrayD):
    pass

class TH1F(TH1[RFloat], TArrayF):
    pass

class TH2(TH1, Generic[ContentType]):
    pass
class TH2D(TH2[RDouble], TArrayD):
    pass
class TH2F(TH2[RFloat], TArrayF):
    pass

class TH3(TH1):
    pass
