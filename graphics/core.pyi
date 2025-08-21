from typing import Optional, overload

from ..core import TColorNumber

class TAttText:
    def SetTextSize(self, size: float = 1) -> None:
        """
        Set the text size.
        """
        ...
    def SetTextFont(self, font: int = 62) -> None:
        """
        Set the text font.
        """
        ...
    def SetTextAlign(self, align: int = 11) -> None:
        """
        Set the text alignment.
        """
        ...
    @overload
    def SetTextColor(self, tcolor: int = 1) -> None:
        """
        Set the text color.
        """
        ...
    @overload
    def SetTextColor(self, lcolor: TColorNumber) -> None:
        """
        Set the text color.
        """
        ...
    def SetTextColorAlpha(self, tcolor: int, alpha: float) -> None:
        """
        Set the text color and transparency.
        """
        ...
class TAttBBox2D:
    """
    Abstract base class for elements drawn in the editor.

    Classes inheriting from `TAttBBox2D` implementing the `TAttBBox2D` virtual classes,
    and using `TPad.ShowGuideLines` in `ExecuteEvent` will automatically get the guide
    lines drawn when moved in the pad. All methods work with pixel coordinates. 
    """
    def SetBBoxX1(self, x1: float) -> None:
        """
        Set left hand side of BoundingBox to a value (resize in x direction on left).
        
        Parameters
        ----------
        x1 : float
            The new X1 coordinate.
        """
        ...
    def SetBBoxY1(self, y1: float) -> None:
        """
        Set top of BoundingBox to a value (resize in y direction on top).
        
        Parameters
        ----------
        y1 : float
            The new Y1 coordinate.
        """
        ...
    def SetBBoxX2(self, x2: float) -> None:
        """
        Set right hand side of BoundingBox to a value (resize in x direction on right).
        
        Parameters
        ----------
        x2 : float
            The new X2 coordinate.
        """
        ...
    def SetBBoxY2(self, y2: float) -> None:
        """
        Set bottom of BoundingBox to a value (resize in y direction on bottom).
        
        Parameters
        ----------
        y2 : float
            The new Y2 coordinate.
        """
        ...
