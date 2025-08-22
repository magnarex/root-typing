# ROOT Typing
A simple package containing Python implementation files (`.pyi`) to enable syntax analysis and suggestions for the Python version of CERN's `ROOT` data analysis package (`pyROOT`).
## Installation
Install this repository into your `typings` directory and enjoy (:
```
git clone https://github.com/magnarex/root-typing.git ROOT
```
### For VSCode users
For your syntax analyzer to detect this package, you need to add it to the list of paths used for analysis.
- You can do this via your `settings.json` file. To open it, go to `Settings [Ctrl+,]` and open the `.json` clicking on the top right corner file icon with an arrow.
- Alternatively, you may type `Preferences: Open Default Settings (JSON)` on the command palette.

Then, you need to add the path to the `python.analysis.extraPaths` setting:
- If you are editing the `.json` file directly and you don't have the `python.analysis.extraPaths` option still configured, you may add it. **Keep in mind it is a list, see example below!**
- You may do this also from the settings menu, using the top search bar to look for the settings ID and adding the path using the GUI.

If you have installed the repository in `/path/to/my/typings/ROOT`, it should look something like this:
```json
{
  "python.analysis.extraPaths": [
    "/path/to/my/typings"
  ]
}
```

> NOTE: Always use the parent directory, as you would do with your custom python packages.
