## The Problem

We want you to create a command-line application that reads a listing of game
results for a soccer league, grouped by matchday, and returns the top teams at
the end of each matchday.

### Input/output

The input and output will be text. Your solution should parse the provided
sample-input.txt file via stdin (pipe or redirect) or by parsing a file passed
by name on the command line. Your solution should output the correct result via
stdout to the console.

The input contains results of games, one per line and grouped by matchday. All
teams play exactly once during a matchday, e.g. given a league of six teams,
each matchday would consist of three games. There is no specific delimiter
between matchdays so your application should recognize the start and end of
a matchday. See sample-input.txt for details.

The output should list the top three teams, ordered from most to least points,
at the end of each matchday. See the expected format specified in
expected-output.txt.

Your solution should handle error cases due to invalid input for example. We
leave it up to you to identify these cases and decide how to handle them.

### The rules

In this league, a draw (tie) is worth 1 point and a win is worth 3 points. A
loss is worth 0 points. If two or more teams among the top three teams have
the same number of points, they should have the same rank and be printed in
alphabetical order. That said, at most three teams should be listed in the
output per matchday.

### Guidelines

This should be implemented in a language with which you are familiar. We would
prefer that you use ruby, javascript, typescript, or python, if you are
comfortable doing so. If none of these are comfortable, please choose a
language that is both comfortable for you and suited to the task.

Your solution should be able to be run (and if applicable, built) from the
command line. Please include appropriate scripts and instructions for
running your application and your tests.

If you use other libraries installed by a common package manager
(rubygems/bundler, npm, pip, gradle), it is not necessary to commit the
installed packages.

We write automated tests and we would like you to do so as well.

We appreciate well factored, object-oriented or functional designs.

Anything that isn't explicitly specified or is unclear is up to you to
decide.

### Platform support

This will be run in a unix-ish environment (OS X). If you choose to use a
compiled language, please keep this in mind. (Dependency on Xcode is acceptable
for objective-c solutions) Please use platform-agnostic constructs where
possible (line-endings and file-path-separators are two problematic areas).

Please email your sponsor at Jane if you have any questions.
