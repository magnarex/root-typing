from typing import overload, TYPE_CHECKING

from .RDF import RInterface

if TYPE_CHECKING:
    from .io import TDirectory
    from .tree import TTree
    from .RDF import RResultPtr
    

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
    def __init__(self, treeName: str, dirPtr: 'TDirectory', defaultColumns : list[str] = []) -> None:
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
    def __init__(self, tree: 'TTree', defaultColumns : list[str] = []) -> None:
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
    def Count(self) -> 'RResultPtr[int]': ...
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
