from typing import Optional, overload, Any

from ..core import TObject, TAttFill, TVirtualPad, TNamed, TAttLine
from ..containers import TList
from .core  import TAttText, TAttBBox2D

class TPad(TVirtualPad, TAttBBox2D):
    def Modified(self) -> None:
        """
        Mark pad modified will be repainted when TCanvas.Update() will be called next time.    
        """
        ...
    def GetListOfPrimitives(self) -> 'TList[TPad]':
        """
        Return the list of primitives in this pad.
        
        The list of primitives is a `TList` containing all objects drawn in this pad.
        """
        ...
    def cd(self, subpadnumber: int = 0) -> 'TPad':
        """
        Set Current pad.

        When a canvas/pad is divided via `Divide`, one can directly set the current
        path to one of the subdivisions. See `Divide` for the convention to number sub-pads.

        Returns the new current pad, or 0 in case of failure.

        For example:
        ```
        c1.Divide(2,3) # create 6 pads (2 divisions along x, 3 along y).
        ```

        To set the current pad to the bottom right pad, do
        ```
        c1.cd(6)
        ```

        Note1: `c1.cd()` is equivalent to `c1.cd(0)` and sets the current pad to `c1` itself.

        Note2: after a statement like `c1.cd(6)`, the global variable gPad points to the current
        pad. One can use gPad to set attributes of the current pad.

        Note3: One can get a pointer to one of the sub-pads of pad with:
        `subpad = pad.GetPad(subpadnumber)`
        """
        ...
    def Close(self) -> None:
        """
        Delete all primitives in pad and pad itself.

        Pad cannot be used anymore after this call. Emits signal "Closed()".
        """
        ...
    def Update(self) -> None:
        """
        Update pad.
        """
        ...
    def GetListOfPrimitives(self) -> 'TList[TObject]':
        """
        Return the list of primitives in this pad.
        
        The list of primitives is a `TList` containing all objects drawn in this pad.
        """
        ...
class TCanvas(TPad):
    def __init__(self, name: str = "", title: str = "", ww: int = 800, wh: int = 600) -> None: ...
    def Update(self) -> None:
        """
        Update canvas pad buffers.
        """
        ...
    def SaveAs(self, filename: str = "", option : str = "") -> None:
        """
        Save the pad content in a file.

        The file's format used to save the pad is determined by the filename extension:

        - if filename is empty, the file produced is padname.ps
        - if filename starts with a dot, the padname is added in front
        - if filename ends with `.ps`, a Postscript file is produced
        - if filename ends with `.eps`, an Encapsulated Postscript file is produced
        - if filename ends with `.pdf`, a PDF file is produced
            NOTE: `TMathText` will be converted to TLatex; q.e.d., symbols only available
            in `TMathText` will not render properly.
        - if filename ends with `.svg`, a SVG file is produced
        - if filename ends with `.tex`, a TeX file is produced
        - if filename ends with `.gif`, a GIF file is produced
        - if filename ends with `.gif+NN`, an animated GIF file is produced
            See comments in `TASImage.WriteImage` for meaning of NN and other .gif sufix variants
        - if filename ends with `.xpm`, a XPM file is produced
        - if filename ends with `.png`, a PNG file is produced
        - if filename ends with `.bmp`, a BMP file is produced
        - if filename ends with `.jpg` or `.jpeg` a JPEG file is produced
            NOTE: JPEG's lossy compression will make all sharp edges fuzzy.
        - if filename ends with `.tiff`, a TIFF file is produced
        - if filename ends with `.C`, `.cxx`, `.cpp` or `.cc`, a C++ macro file is produced
        - if filename ends with `.root`, a Root file is produced
        - if filename ends with `.xml`, a XML file is produced
        - if filename ends with `.json`, a JSON file is produced
        """
        ...
    def Close(self) -> None:
        """
        Close canvas.

        Delete window/pads data structure
        """
        ...
        
class TBox(TObject, TAttFill, TAttLine, TAttBBox2D):
    def Draw(self, option: str = "") -> None:
        """
        Draw this box with its current attributes.

        - if the box has no fill style (ie fill style=0), the box contour is drawn
        - if the box has a fill style, the box contour is not drawn by default.
        
        To force the contour to be drawn, specify option "l"
        """
        ...
    def GetX1(self) -> float:
        """
        Get the X1 coordinate of the box.
        """
        ...
    def GetY1(self) -> float:
        """
        Get the Y1 coordinate of the box.
        """
        ...
    def GetX2(self) -> float:
        """
        Get the X2 coordinate of the box.
        """
        ...
    def GetY2(self) -> float:
        """
        Get the Y2 coordinate of the box.
        """
        ...


class TPave(TBox):
    pass

class TLegend(TPave, TAttText):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, x1 : float, y1: float, x2: float, y2: float, header: Optional[str] = "", option : Optional[str] = "brNDC") -> None: ...
    @overload
    def __init__(self, w : float, h : float, header: Optional[str] = "", option: Optional[str] = "brNDC") -> None: ...

    @overload
    def AddEntry(self, name: str, label: str = "", option: str = "lpf") -> None:
        """
        Add a new entry to this legend.
        
        Parameters
        ----------
        name : str
            The name of an object in the pad to be represented..
        label : str, optional
            The text you wish to associate with obj in the legend if `label` is `None` or empty, the title of the object will be used.
        option : str, optional
            The option string to be used for drawing the object in the legend.
            Options are:
                - `L`: draw line associated with TAttLine if obj inherits from TAttLine
                - `P`: draw polymarker associated with TAttMarker if obj inherits from TAttMarker
                - `F`: draw a box with fill associated wit TAttFill if obj inherits TAttFill
                - `E`: draw vertical error bar if option "L" is also specified
        """
        ...
    @overload
    def AddEntry(self, obj: Any, label: str = "", option: str = "lpf") -> None:
        """
        Add a new entry to this legend.
        
        Parameters
        ----------
        obj : TObject
            The object to be represented.
        label : str, optional
            The text you wish to associate with obj in the legend if `label` is `None` or empty, the title of the object will be used.
        option : str, optional
            The option string to be used for drawing the object in the legend.
            Options are:
                - `L`: draw line associated with TAttLine if obj inherits from TAttLine
                - `P`: draw polymarker associated with TAttMarker if obj inherits from TAttMarker
                - `F`: draw a box with fill associated wit TAttFill if obj inherits TAttFill
                - `E`: draw vertical error bar if option "L" is also specified
        """
        ...
    def Draw(self, option: str = "") -> None:
        """
        Draw this legend with its current attributes.
        
        Parameters
        ----------
        option : str, optional
            The option string to be used for drawing the legend.
            Default is an empty string, which means the legend will be drawn in the default way.
        """

class TText(TNamed, TAttText, TAttBBox2D):
    def SetNDC(isNDC : bool = True):
        """
        Set the NDC (Normalized Device Coordinates) flag for this text object.
        These coordinates are from (0,0) at the bottom left corner to (1,1) at
        the top right corner of the pad.

        Parameters
        ----------
        isNDC : bool, optional
            If True, the text will be drawn in normalized coordinates.
            Default is True.
        """
        ...

class TLatex(TText, TAttLine):
    @overload
    def __init__(self) -> None:
        """
        Default constructor.
        """
    @overload
    def __init__(self, x: float, y: float, text: str) -> None:
        """
        Normal constructor.

        Parameters
        ----------
        x : float
            X coordinate of the text.
        y : float
            Y coordinate of the text.
        text : str
            The text to be displayed.
        """
        ...
    @overload
    def __init__(self, text : 'TLatex') -> None:
        """
        Copy constructor.
        
        Parameters
        ----------
        text : TLatex
            The TLatex object to be copied.
        """
        ...
    def DrawLatex(x : float, y : float, text : str) -> None:
        """
        Draw the text at the specified coordinates.

        Parameters
        ----------
        x : float
            X coordinate where the text will be drawn.
        y : float
            Y coordinate where the text will be drawn.
        text : str
            The text to be displayed.
        """
        ...


class TPaveText(TPave, TAttText):
    pass

class TVirtualPaveStats:
    pass

class TPaveStats(TPaveText, TVirtualPaveStats):
    def SetOptStat(self, stat: int = 1) -> None:
        """
        Set the option for the statistics box.
        
        Parameters
        ----------
        stat : int
            The option integer to set for the statistics box.
            For example, 1 to show mean and error.
            
        Notes
        -----
        The "`mode`" has up to nine digits that can be set to on (1 or 2), off (0). 
        mode = ksiourmen  (default = 000001111)
        k = 1;  kurtosis printed
        k = 2;  kurtosis and kurtosis error printed
        s = 1;  skewness printed
        s = 2;  skewness and skewness error printed
        i = 1;  integral of bins printed
        o = 1;  number of overflows printed
        u = 1;  number of underflows printed
        r = 1;  rms printed
        r = 2;  rms and rms error printed
        m = 1;  mean value printed
        m = 2;  mean and mean error values printed
        e = 1;  number of entries printed
        n = 1;  name of histogram is printed    
        
        """
        ...
