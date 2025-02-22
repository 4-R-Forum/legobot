# MicroBit Change Process for micro:bit

MicroPython is designed for use on multiple platforms including micro:bit, the microbit-foundation publishes editor at https://python.microbit.org which includes very useful features: Reference and API documentation, pop-up syntax prompts and  syntax checkingd, and simulator with serial output. Although the editor is published on GitHub, it does not seem to have a feature to save code to GitHub like MakeCode.

VS Code does have GitHub integration and a choice of micro:bit extension but I have not seen one with the MicroPython Editor features.

I have been using both with copy and paste, and found the hard way that it is easy to make a fumble and lose work. This process is intended to minimize risk of a fumble with the benefits of both tools.

## For each PDCA iteration
1. Open microbit Python editor at https://python.microbit.org/v/3
1. Name the project for the PDCA, this will be used as filename for saving .hex and .py files
1. Open main.py from the repo in the editor, this prompts and overwrites code in the editor
1. Create a new python file for other modules, copy and paste code from the repo. (no other way to do this found). Hopefully such modules are fairly stable.
1. Test code in simulator, to reveal any runtime 
1. Download code to microbit using USB cable
1. Run the code for bench or field test
1. If any lot is all numeric, download and review in preview, save as png with snipping tool
    1. Else download open and save in Excel
1. Save code as hex (contains main and modules) to downloads folder. This is a safety backup in case needed
1. Update PDCA in repo
1. Commit changes in git