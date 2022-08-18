# Sandbox for LGB Test Suites

## Options
|   Name    | Support C  | Header Only | CMake Interface | Catches Errors | Speed of Running Tests |
| :-------: | :--------: | :---------: | :-------------: | :------------: | :--------------------: |
| Criterion |    Yes     |     No      |       Yes       |      Yes       |          Slow          |
|    Tau    |    Yes     |     Yes     |       Yes       |       No       |          Fast          |
|  doctest  |     No     |     Yes     |       Yes       |      Yes       |          Fast          |
| cpputest  | not really |     No      |       Yes       |       ?        |           ?            |
|  cmocka   |    Yes     |     No      |       Yes       |      Yes       |           ?            |

- [Criterion](https://github.com/Snaipe/Criterion)
- [Doctest](https://github.com/doctest/doctest)
- [tau](https://github.com/jasmcaus/tau)
- [cpputest](https://github.com/cpputest/cpputest)
- [cmocka](https://cmocka.org/)

## Goals

- Fast execution of tests
- Granular execution of tests within a single executable
- Granular logging to a standard format, preferably json or toml, but xml is ok
- CMake interface
- Catch errors so a whole set of tests don't crash
- Reduce the number of files
- User parametrized tests to minimize repeated code
- Ideally run both LGB and SSGB so we don't need to keep the output data, but I think we have to hardcode the SSGB data
- Parallelizable over tests within a single executable (a bit of a pipe dream especially since we'll eventually want to do this with the simulator)

## Notes
- Swap out different data sets
- Dynamically swap libraries during run time