from typing import Any, overload

from .core import TNamed
from .tree import TTree
from .compression import RCompressionSetting

class TDirectory(TNamed):
    pass

class TDirectoryFile(TDirectory):
    pass

class TFileOpenHandle(TNamed):
    pass

class TFile(TDirectoryFile):
    def __init__(self, name: str, option: str = "READ") -> None: ...
    def Get(self, name: str) -> TTree: ...
    def Close(self) -> None: ...
    def Write(self) -> int: ...
    def __enter__(self) -> 'TFile': ...
    def __exit__(self, *args: Any) -> None: ...
    @overload
    def Open(url : str,
             options : str = "",
             ftitle = "",
             compress : RCompressionSetting.EDefaults = RCompressionSetting.EDefaults.kUseCompiledDefault,
             netopt = 0
            ) -> 'TFile':
        """
        Create / open a file.

        The type of the file can be either a TFile, TNetFile, TWebFile or any TFile derived class for which an plugin
        library handler has been registered with the plugin manager (for the plugin manager see the TPluginManager
        class). The returned type of TFile depends on the file name specified by 'url'. If 'url' is a '|'-separated
        list of file URLs, the 'URLs' are tried sequentially in the specified order until a successful open. If the
        file starts with "root:", "roots:" or "rootk:" a TNetFile object will be returned, with "http:" a TWebFile,
        with "file:" a local TFile, etc. (see the list of TFile plugin handlers in $ROOTSYS/etc/system.rootrc for
        regular expressions that will be checked) and as last a local file will be tried. Before opening a file via
        TNetFile a check is made to see if the URL specifies a local file. If that is the case the file will be opened
        via a normal TFile. To force the opening of a local file via a TNetFile use either TNetFile directly or specify
        as host "localhost". The netopt argument is only used by TNetFile. For the meaning of the options and other
        arguments see the constructors of the individual file classes. In case of error, it returns a nullptr.

        For TFile implementations supporting asynchronous file open, see TFile::AsyncOpen(...), it is possible to
        request a timeout with the option TIMEOUT=<secs>: the timeout must be specified in seconds and it will be
        internally checked with granularity of one millisec. For remote files there is the option: CACHEREAD opens
        an existing file for reading through the file cache. The file will be downloaded to the cache and opened
        from there. If the download fails, it will be opened remotely. The file will be downloaded to the directory
        specified by SetCacheFileDir().

        The caller is responsible for deleting the pointer. In READ mode, a nullptr is returned if the file does
        not exist or cannot be opened. In CREATE mode, a nullptr is returned if the file already exists or cannot
        be created. In RECREATE mode, a nullptr is returned if the file can not be created. In UPDATE mode, a
        nullptr is returned if the file cannot be created or opened.
        """
        ...
    @overload
    def Open(self, fh : TFileOpenHandle) -> 'TFile':
        """
        Waits for the completion of an asynchronous open request.

        Returns the pointer to the associated TFile, transferring ownership of the handle to the TFile instance. 
        """
        ...