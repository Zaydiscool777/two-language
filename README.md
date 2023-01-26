# two-language

Python only. To make it easier to code one-lang repo.

Actually, maybe everything except turning a C program into an executable. (thanks, Fabrice Bellard, for tcc.
And a bash script and an apt package.
Yeah.

Things that the repo does when you run `one -i` or `one --init`:
  
1. installs gh (to off this, append `-x gh` or `--ghoff`, and after `-i`. ex: `one -i -x gh` or `one -ix gh`, but not `one -xi gh`.)

2. runs with one of these:

    a. `gh repo clone Zaydiscool777/tcc` (off with `-x a` or `--xa` for option b. (also offs `gh install`.) (repo does *not* exist, so, uh, not yet.)

    b. `sudo apt install tcc` (off with `-x b` or`--xb` for option c.)
// wip