from typing import Any, overload
from enum import Enum

from numpy import iinfo, int64
from .core import TNamed, TAttFill

class TTree(TNamed, TAttFill()):
    kMaxEntries : int = iinfo(int64).max
    def __init__(self, name: str, title: str) -> None: ...
    def Branch(self, name: str, obj: Any, leaflist: str = "") -> Any: ...
    def Fill(self) -> int: ...
    def GetEntries(self) -> int: ...
    def Draw(self, varexp: str, selection: str = "", option: str = "") -> int: ...

class TChain(TTree):
    class Mode(Enum):
        kWithoutGlobalRegistration = 0
        kWithGlobalRegistration = 1
    @overload
    def __init__(self, mode : TChain.Mode = Mode.kWithGlobalRegistration) -> None:
        """
        Default constructor.
        """
        ...
    @overload
    def __init__(self, name: str, title: str, mode: TChain.Mode = Mode.kWithGlobalRegistration) -> None:
        """
        Create a chain.

        A `TChain` is a collection of `TFile` objects. the first parameter "name" is the name of the
        `TTree` object in the files added with `Add`. Use `TChain.Add` to add a new element to this chain.

        In case the Tree is in a subdirectory, do, eg:
        ```
        ch = TChain("subdir/treename")
        ```
        Example: Suppose we have 3 files f1.root, f2.root and f3.root. Each file contains a `TTree` object named "T".
        ```python
        ch = TChain("T")  # creates a chain to process a Tree called "T"
        ch.Add("f1.root")
        ch.Add("f2.root")
        ch.Add("f3.root")
        ch.Draw("x")
        ```
        The Draw function above will process the variable "x" in Tree "T" reading sequentially the 3 files in the chain ch.

        The TChain data structure:

        Each TChainElement has a name equal to the tree name of this TChain and a title equal to the file name. So, to loop over the TFiles that have been added to this chain:
        ```python
        fileElements=chain.GetListOfFiles()

        for chEl in fileElements:
            f = chEl.GetTitle()
            #... do something with f ...
        ```
        """
        ...
    @overload
    def Add(self, name : str, nentries : int = TTree.kMaxEntries) -> int:
        """
        Add a new file to this chain.

        Parameters
        ----------
        name : str
            The path to the file to be added. See below for details.
        nentries : int
            Number of entries in the file. This can be an estimate or queried from the file.
            See below for details.

        Returns
        -------
        There are different possible return values:
        - If nentries>0 (including the default of TTree.kMaxEntries) and no wildcarding is used,
        ALWAYS returns 1 irrespective of whether the file exists or contains the correct tree.
        - If wildcarding is used, regardless of the value of nentries, returns the number of files
        matching the name irrespective of whether they contain the correct tree.
        - If nentries<=0 and wildcarding is not used, returns 1 if the file exists and contains the
        correct tree and 0 otherwise.
        """
    @overload
    def Add(self, chain : 'TChain') -> int:
        """
        Add all files referenced by the passed chain to this chain.
        
        Parameters
        ----------
        chain : TChain
            The chain whose files are to be added.

        Returns
        -------
        int : total number of files connected. 
        """
        ...
    