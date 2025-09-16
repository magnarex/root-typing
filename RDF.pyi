from typing import Any, Generic, TypeVar, Union, overload
from numpy.typing import NDArray
from numpy import float64 as RDouble, float32 as RFloat

from enum import IntEnum

from .compression import RCompressionSetting
from .histograms  import TH1D, TH2D

from .io import TDirectory
from .tree import TTree


T = TypeVar('T')
columnType = TypeVar('columnType', bound=Any)

class RResultPtr(Generic[T]):
    """
    A wrapper around the result of RDataFrame actions able to trigger calculations lazily.
    Use `GetValue()` to retrieve the actual value.
    """
    def GetValue(self) -> T:
        """
        Get a const reference to the encapsulated object.

        Triggers event loop and execution of all actions booked in the associated RLoopManager. 
        """
        ...
    def GetPtr(self) -> T:
        """
        Get a pointer to the encapsulated object.

        Triggers event loop and execution of all actions booked in the associated RLoopManager.
        
        Notes
        -----
        Ownership is not transferred to the caller. 
        """
        ...

class ESnapshotOutputFormat(IntEnum):
    kDefault = 0
    kTTree = 1
    kRNTuple = 2

class RSnapshotOptions:
    """
    A collection of options to steer the creation of the dataset on file. 
    """

    def __init__(self,
                mode            : str = "RECREATE",
                comprAlgo       : RCompressionSetting.EAlgorithm | int = RCompressionSetting.EAlgorithm.kZLIB ,
                comprLevel      : int = 1,
                autoFlush       : int = 0,
                splitLevel      : int = 99,
                lazy            : bool = False,
                overwriteExists : bool = False,
                vector2RVec     : bool = True,
                basketSize      : int = -1,
                outputFormat    : ESnapshotOutputFormat = ESnapshotOutputFormat.kDefault,
            ) -> None:
        ...

    @property
    def fAutoFlush(self) -> int:
        """
        AutoFlush value for output tree.
        """
        return self.fAutoFlush
    @property
    def fBasketSize(self) -> int:
        """
        Set a custom basket size option.
        """
        return self.fBasketSize
    @property
    def fCompressionAlgorithm(self) -> RCompressionSetting.EAlgorithm:
        """
        Compression algorithm of the output file.
        """
        return self.fCompressionAlgorithm
    @property
    def fCompressionLevel(self) -> int:
        """
        Compression level of the output file.
        """
        return self.fCompressionLevel
    @property
    def fLazy(self) -> bool:
        """
        Do not start the event loop when `Snapshot` is called.
        """
        return self.fLazy
    @property
    def fMode(self) -> str:
        """
        Mode of creation of output file.
        """
        return self.fMode
    @property
    def fOutputFormat(self) -> ESnapshotOutputFormat:
        """
        Which data format to write to.
        """
        return self.fOutputFormat
    @property
    def fOverwriteExists(self) -> bool:
        """
        If `fMode` is "UPDATE", overwrite object in output file if it already exists.
        """
        return self.fOverwriteExists
    @property
    def fSplitLevel(self) -> int:
        """
        Split level of the output file.
        """
        return self.fSplitLevel
    @property
    def fVector2RVec(self) -> bool:
        """
        If set to true will convert `std::vector` columns to `RVec` when saving to disk.
        Only available for `ROOT v6.34` onwards.
        """
        return self.fVector2RVec
    
    
class RInterface(Generic[T]):
    """
    Base class for RDataFrame interface.
    
    Provides methods to interact with the ROOT DataFrame, such as defining new columns,
    filtering data, and performing actions on the DataFrame.
    
    This class is not meant to be instantiated directly. Use `RDataFrame` instead.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Initialize the RInterface with the given arguments.
        """
        ...
    
    def GetResultPtr(self) -> RResultPtr[Any]:
        """
        Get a pointer to the result of the last action performed on the DataFrame.
        """
        ...
    
    def Snapshot(self, treename, filename, columnList, options=RSnapshotOptions()) -> RResultPtr[RInterface]:
        """
        Take a snapshot of the DataFrame and save it to a file.
        
        Parameters:
        - treename: Name of the tree to create in the output file.
        - filename: Name of the output file.
        - columnList: List of columns to include in the snapshot.
        - options: Options for the snapshot (default is empty).
        
        Returns:
        A pointer to the result of the snapshot action.
        """
        ...
    
    def Max(self, columnName: str = "") -> RResultPtr[columnType]:
        """
        Return the maximum of processed column values (lazy action).

        Parameters
        ----------
        columnName: str
            The name of the branch/column to be treated.

        Returns
        -------
        RResultPtr[columnType]
            A pointer to the maximum value of the specified column.
        """
        ...

    def Mean(self, columnName: str = "") -> RResultPtr[columnType]:
        """
        Return the mean of processed column values (lazy action).

        Parameters
        ----------
        columnName: str
            The name of the branch/column to be treated.

        Returns
        -------
        RResultPtr[columnType]
            A pointer to the mean value of the specified column.
        """
        ...

    def Min(self, columnName: str = "") -> RResultPtr[columnType]:
        """
        Return the minimum of processed column values (lazy action). 
        
        Parameters
        ----------
        columnName: str
            The name of the branch/column to be treated.

        Returns
        -------
        RResultPtr[columnType]
            A pointer to the minimum value of the specified column.
        """
        ...
    
    @overload
    def Histo1D(self, model : TH1DModel, vName : str, wName : str) -> RResultPtr[TH1D]:
        """
        Fill and return a one-dimensional histogram with the weighted values of
        a column (lazy action).

        Parameters
        ----------
        model : TH1DModel
            The returned histogram will be constructed using this as a model.
        vName : str
            The name of the column that will fill the histogram.
        wName : str
            The name of the column that will provide the weights.

        Returns
        -------
        RResultPtr[TH1D]
            The monodimensional histogram wrapped in a RResultPtr.
        """
        ...
    @overload
    def Histo1D(self, model : TH1DModel) -> RResultPtr[TH1D]:
        """
        Fill and return a one-dimensional histogram with the weighted
        values of a column (lazy action).

        Parameters
        ----------
        model : TH1DModel
            The returned histogram will be constructed using this as a model.

        Returns
        -------
        RResultPtr[TH1D]
            The monodimensional histogram wrapped in a RResultPtr.

        Notes
        -----
        This overload will use the first two default columns as column names.
        
        See the description of the first `Histo1D()` overload for more details. 
        """
        ...
    @overload
    def Histo1D(self, model : TH1DModel, vName : str) -> RResultPtr[TH1D]:
        """
        Fill and return a one-dimensional histogram with the weighted
        values of a column (lazy action).

        Parameters
        ----------
        model : TH1DModel
            The returned histogram will be constructed using this as a model.
        vName : str
            The name of the column that will fill the histogram.

        Returns
        -------
        RResultPtr[TH1D]
            The monodimensional histogram wrapped in a RResultPtr.

        See the description of the first `Histo1D()` overload for more details. 
        """
        ...
    @overload
    def Histo1D(self, vName : str) -> RResultPtr[TH1D]:
        """
        Fill and return a one-dimensional histogram with the weighted
        values of a column (lazy action).

        Parameters
        ----------
        vName : str
            The name of the column that will fill the histogram.

        Returns
        -------
        RResultPtr[TH1D]
            The monodimensional histogram wrapped in a RResultPtr.

        Notes
        -----
        This overload uses a default model histogram TH1D(name, title, 128u, 0., 0.). The
        "name" and "title" strings are built starting from the input column name. 
        See the description of the first `Histo1D()` overload for more details. 
        """
        ...
    @overload
    def Histo1D(self, vName : str, wName : str) -> RResultPtr[TH1D]:
        """
        Fill and return a one-dimensional histogram with the weighted
        values of a column (lazy action).

        Parameters
        ----------
        vName : str
            The name of the column that will fill the histogram.
        wName : str
            The name of the column that will provide the weights.

        Returns
        -------
        RResultPtr[TH1D]
            The monodimensional histogram wrapped in a RResultPtr.

        Notes
        -----
        This overload uses a default model histogram TH1D(name, title, 128u, 0., 0.). The
        "name" and "title" strings are built starting from the input column name. 
        See the description of the first `Histo1D()` overload for more details. 
        """
        ...
    @overload
    def Histo2D(self, model : TH2DModel) -> RResultPtr[TH2D]:
        ...
    @overload
    def Histo2D(self, model : TH2DModel, v1Name : str, v2Name : str, wName : str) -> RResultPtr[TH2D]:
        """
        Fill and return a weighted two-dimensional histogram (lazy action).
        
        Parameters
        ----------
        model	TH2DModel
            The returned histogram will be constructed using this as a model.
        v1Name	str
            The name of the column that will fill the x axis.
        v2Name	str
            The name of the column that will fill the y axis.
        wName	str
            The name of the column that will provide the weights.
        
        Returns
        -------
        RResultPtr[TH2D]
            The bidimensional histogram wrapped in a RResultPtr.

        Notes
        -----
        This action is lazy: upon invocation of this method the calculation is
        booked but not executed. Also see RResultPtr.
        """
        ...
    @overload
    def Histo2D(self, model : TH2DModel, v1Name : str, v2Name : str) -> RResultPtr[TH2D]:
        """
        Fill and return a weighted two-dimensional histogram (lazy action).
        
        Parameters
        ----------
        model	TH2DModel
            The returned histogram will be constructed using this as a model.
        v1Name	str
            The name of the column that will fill the x axis.
        v2Name	str
            The name of the column that will fill the y axis.
        
        Returns
        -------
        RResultPtr[TH2D]
            The bidimensional histogram wrapped in a RResultPtr.

        Notes
        -----
        This action is lazy: upon invocation of this method the calculation is
        booked but not executed. Also see RResultPtr.
        """
        ...


class RDataFrame(RInterface):
    @overload
    def __init__(self, treeName: str, fileNameGlob: str, defaultColumns : list[str] = []) -> None:
        """
        Build the dataframe.

        Parameters
        ----------
            treeName: str
                Name of the tree contained in the directory
            fileNameGlob: str
                `TDirectory` where the tree is stored, e.g. a `TFile`.
            defaultColumns: list[str]
                Collection of default columns.

        The filename glob supports the same type of expressions as `TChain.Add()`, and it is
        passed as-is to `TChain`'s constructor.

        The default columns are looked at in case no column is specified in the booking
        of actions or transformations. 
        """
        ...
    @overload
    def __init__(self, treeName: str, fileNameGlobs: list[str], defaultColumns : list[str] = []) -> None:
        """
        Build the dataframe.

        Parameters
        ----------
            treeName: str
                Name of the tree contained in the directory
            fileNameGlobs: list[str]
                Collection of file names of filename globs
            defaultColumns: list[str]
                Collection of default columns.

        The filename glob supports the same type of expressions as `TChain.Add()`, and it is
        passed as-is to `TChain`'s constructor.

        The default columns are looked at in case no column is specified in the booking
        of actions or transformations. 
        """
        ...
    @overload
    def __init__(self, treeName: str, dirPtr: TDirectory, defaultColumns : list[str] = []) -> None:
        """
        Build the dataframe.

        Parameters
        ----------
            treeName: str
                Name of the tree contained in the directory
            dirPtr: TDirectory
                Pointer to a `TDirectory` where the tree is stored, e.g. a `TFile`.
            defaultColumns: list[str]
                Collection of default columns.

        The default columns are looked at in case no column is specified in the booking
        of actions or transformations. 
        """
        ...
    @overload
    def __init__(self, tree: TTree, defaultColumns : list[str] = []) -> None:
        """
        Build the dataframe.

        Parameters
        ----------
            tree: TTree
                The `TTree` to use as the source of the dataframe. 
            defaultColumns: list[str]
                Collection of default columns.

        The default columns are looked at in case no column is specified in the booking
        of actions or transformations. 
        """
        ...

    def Define(self, name: str, expression: str) -> 'RDataFrame':
        """
        Define a new column.
        
        Parameters
        ----------
        name : str
            The name of the defined column.
        exression : str
            Function, lambda expression, functor class or any other
            callable object producing the defined value. Returns the value
            that will be assigned to the defined column.
        
        Returns
        -------
        result : RDataFrame
            The first node of the computation graph for which the new quantity is defined.

        Notes
        -----
        Define a column that will be visible from all subsequent nodes of the functional chain.
        The expression is only evaluated for entries that pass all the preceding filters. A new
        variable is created called name, accessible as if it was contained in the dataset from
        subsequent transformations/actions.

        Use cases include:
            - caching the results of complex calculations for easy and efficient multiple access
            - extraction of quantities of interest from complex objects

        Raises
        ------
        An exception is thrown if the name of the new column is already in use in
        this branch of the computation graph.
        """
        ...
    def Redefine(self, name: str, expression: str) -> 'RDataFrame': ...
    def Filter(self, condition: str) -> 'RDataFrame': ...
    def Count(self) -> RResultPtr[int]: ...
    def GetColumnNames(self) -> list[str]: ...
    def GetColumnType(self, var: str) -> str:
    
        """
        Get the type of a column in the dataframe.
        
        Parameters
        ----------
        var : str
            The name of the column.
        
        Returns
        -------
        str
            The type of the column as a string.
        
        Notes
        -----
        The type is returned in lower case.
        """
        ...

class TH1DModel:
    """
    A class which stores some basic parameters of a `TH1D`.
    """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, model : 'TH1DModel') -> None: ...
    @overload
    def __init__(self, h : TH1D) -> None: ...
    @overload
    def __init__(self, name: str, title: str, nbinsx: int, xlow : float, xup : float) -> None: ...
    @overload
    def __init__(self, name: str, title: str, nbinsx : int, xbins: NDArray[Union[RFloat, RDouble]]) -> None: ...
    
class TH2DModel:
    """
    A class which stores some basic parameters of a `TH2D`.
    """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, h : 'TH2D') -> None: ...
    @overload
    def __init__(self, model : 'TH2DModel') -> None: ...
    @overload
    def __init__(self, name: str, title: str, nbinsx: int, xlow : float, xup : float, nbinsy: int, ylow : float, yup : float) -> None: ...
    @overload
    def __init__(self, name: str, title: str, nbinsx : int, xbins: NDArray[Union[RFloat, RDouble]], nbinsy: int, ybins: NDArray[Union[RFloat, RDouble]]) -> None: ...
    @overload
    def __init__(self, name: str, title: str, nbinsx: int, xlow : float, xup : float, nbinsy : int, ybins: NDArray[Union[RFloat, RDouble]]) -> None: ...
    @overload
    def __init__(self, name: str, title: str, nbinsx: int, xbins: NDArray[Union[RFloat, RDouble]], nbinsy : int, ylow : float, yup : float) -> None: ...

class RNodeBase:
    """
    Base class for non-leaf nodes of the computational graph.

    It only exposes the bare minimum interface required to work as a
    generic part of the computation graph. RDataFrames and results of
    transformations can be cast to this type via ROOT.RDF.AsRNode.
    """
    pass

class RNode(RInterface[RNodeBase]):
    pass

def AsRNode(node: RInterface) -> RNode:
    """
    Cast a RDataFrame node to the common type ROOT::RDF::RNode.

    Parameters
    ----------
    node
        Any node of a RDataFrame graph
    
    Returns
    -------
    RNode
        The node casted to the common type.
    """
    ...

