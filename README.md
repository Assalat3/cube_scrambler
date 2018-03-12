# cube_scrambler
A simple command line scrambler for cubes written in python. Work in progress, will update later.

Known bugs and imperfections:
- Currently the script only spits out variables from the list. You will get:
  - (Possibly FIXED as of 12.3.2018.) The same movesets multiple times in a row (R, R, R...)
  - Movesets that counter each other (R2, R2'...)
  - Movesets that don't scramble the cube at all (R2, R2, U, U, U, U...)

To-do list:
- (Possibly FIXED as of 12.3.2018. Self-countering move sets still occur.) Make it impossible to get the same move-set multiple times in a row.
  - Also: No back-to-back moves that counter each other, for example: 2L and 2L, M and M' etc.
- Add scrambles for larger cubes, minxes etc.
- Add a timer?
