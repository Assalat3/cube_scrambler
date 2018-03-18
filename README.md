# cube_scrambler
A simple command line scrambler for cubes written in python. Work in progress, will update later.

Known bugs and imperfections:
- Currently the script only spits out variables from the list. You will get:
  - (Possibly FIXED as of 12.3.2018.) The same movesets multiple times in a row (R, R, R...)
  - Movesets that counter each other (R2, R2'...)
  - Movesets that don't scramble the cube at all (R2, R2, U, U, U, U...)
  - Identical singular/plural movesets appear back to back (U, 2U, R, 2R...).

To-do list:
- (Possibly FIXED as of 12.3.2018. Self-countering move sets still occur.) Make it impossible to get the same move-set multiple times in a row.
  - Also: No back-to-back moves that counter each other, for example: 2L and 2L, M and M' etc.
  - Also: No back-to-back moves that are singular/plural, for example: L, 2L, L, M, 2M etc.
- Add scrambles for larger cubes, minxes etc.
- Add a timer?
