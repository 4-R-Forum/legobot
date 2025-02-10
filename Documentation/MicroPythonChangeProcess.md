# MicroBit Change Process for micro:bit

MicroPython is designed for use on multiple platforms including micro:bit, the microbit-foundation publishes editor at https://python.microbit.org which includes very useful features: Reference and API documentation, pop-up syntax prompts and  syntax checkingd, and simulator with serial output. Although the editor is published on GitHub, it does not seem to have a feature to save code to GitHub like MakeCode.

VS Code does have GitHub integration and a choice of micro:bit extension but I have not seen one with the MicroPython Editor features.

I have been using both with copy and paste, and found the hard way that it is easy to make a fumble and lose work. This process is intended to minimize risk of a fumble with the benefits of both tools.

1. Write code in VSCode and commit to GitHub.
1. In micro:bit MicroPyton editorProject, open main.py from git repo
1. For any modules in the rpo, create a file and copy and paste code. (I don't see another way to do this with source code, you could keep .hex files in git but that is not what git is for.)
1. Resolve any sytax errors in MicroPython
1. Run code in the simulator, resolve any runtime errors.
1. Set browser download loction to repo, avoids cut and past fumbles.
1. Use MicroPython Project at left to save files individually
    -problem, prenames, won't overwrite!
1. Load 