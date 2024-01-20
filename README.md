# Human Benchmark Solver

This is a small project to beat the
[Human Benchmark](https://humanbenchmark.com/) tests. It is a collection of
Python scripts that can individually outperform (at least) 95% of all humans
taking the tests.

This project is heavily inspired by videos from
[Code Bullet](https://www.youtube.com/@codebulletsdayoff582).

# Script Details

## Reaction Time

The file `src/ReactionTime.py` contains a script that simply reads the pixel
position for a colored value, and upon sensing a particular red value,
continually clicks. This loop is fairly optimized, and the reaction time of the
script sits at 23ms, which beats an estimated 100.0%th percentile of test
takers.

The script uses `mss` as a screengrabbing tool as well as `mouse`, which are
some of the faster libraries for screenshotting and mouse clicking respectively.

# License TL;DR

This project is distributed under the MIT license. This is a paraphrasing of a
[short summary](https://tldrlegal.com/license/mit-license).

This license is a short, permissive software license. Basically, you can do
whatever you want with this software, as long as you include the original
copyright and license notice in any copy of this software/source.

## What you CAN do:

-   You may commercially use this project in any way, and profit off it or the
    code included in any way;
-   You may modify or make changes to this project in any way;
-   You may distribute this project, the compiled code, or its source in any
    way;
-   You may incorporate this work into something that has a more restrictive
    license in any way;
-   And you may use the work for private use.

## What you CANNOT do:

-   You may not hold me (the author) liable for anything that happens to this
    code as well as anything that this code accomplishes. The work is provided
    as-is.

## What you MUST do:

-   You must include the copyright notice in all copies or substantial uses of
    the work;
-   You must include the license notice in all copies or substantial uses of the
    work.

If you're feeling generous, give credit to me somewhere in your projects.
