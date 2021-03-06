# Lab 3: Auditing a Workstation

>The main goal of this lab work is to develop a desktop application which
will help us to parse and scan .audit policy files, which are provided by
some Security Companies (like CIS or Tenable). The parsed files should be
saved locally in a structured form and include next features:

### Required features:

(from previous lab)
- Choose which options they would like to run (by selecting or deselecting options);
- Search by name for an option (via a search bar);
- Select or deselect all options in one click;
- Create and save a policy that contains only the selected options under the same name or
a different one.

(new features)
- Perform an audit of the workstation, using the options that were selected;
- Output the results of the audit on screen.

### Used Technologies:

- Windows 10 
- Python
- Tkinter GUI package
- Xming Server
- PyCharm

### Installation
This lab requires [Xming](https://sourceforge.net/projects/xming/) to run. Also install Tkinter before running the main.py.

To run the application write the following command (using Python 3.8.2): 
```sh
$  python3 main.py
```
> All the information about lab is reflected in .py scripts in form of commentaries.
