# cube_scrambler
A simple command line scrambler for cubes written in python. Work in progress.

Known bugs and imperfections:
- (FIXED as of 23.3.2018. A simple elif was left out.) After running a 2x2 scramble, trying to quit gives the user "invalid argument" response. I have no idea. Just type it again and the program exits as it should. A trivial bug for now.

To-do list:
- (FIXED as of 21.3.2018. Redid the code, should take care of everything.) Make it impossible to get the same move-set multiple times in a row.
  - (See previous) Also: No back-to-back moves that counter each other, for example: 2L and 2L, M and M' etc.
  - (See previous) Also: No back-to-back moves that are singular/plural, for example: L, 2L, L, M, 2M etc.
- (ADDED as of 1.4.2018. Still need to figure out the minxes. Might get left out.) Add scrambles for larger cubes, minxes etc.
- (ADDED as of 23.3.2018) (DISABLED as of 1.4.2018. Needs reworking. You can re-enable it by removing the documentation of the timer() function.) Add a timer?
