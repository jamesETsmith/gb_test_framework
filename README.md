# Sandbox for GraphBLAS Test Suites
This project is a place for me to test out drastic changes to a GraphBLAS test suite I'm working on. Changes may be breaking so use with caution.

## Building
Requirements:
- `gcov` or `llvm-cov` to match compiler
- `python` and `pip` installable packages `gcovr` and optionally `xmltodict`.

From `gb_test_framework`
```
cmake -S . -B build
cmake --build build --parallel
cmake --build build --target test
```

## Goals

- Fast execution of tests
- Granular execution of tests within a single executable
- Granular logging to a standard format, preferably json or toml, but xml is ok
- Easy CMake interface
- Catch errors so a whole set of tests don't crash
- Reduce the number of files
- User parametrized tests to minimize repeated code
- Ideally run both LGB and SSGB so we don't need to keep the output data, but I think we have to hardcode the SSGB data
- Swap out different data sets
- Parallelizable over tests within a single executable (a bit of a pipe dream especially since we'll eventually want to do this with the simulator)
- Work well with tools like gcov/llvm-cov


## Survey of the Options
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

For now, due to simplicity, I'll just be using `tau`.

Problems with `tau` so far:
- Filtering tests works ok when you want to filter only one thing, but I haven't figured out how to use multiple filters yet (it might not be possible).
- The xml output isn't as useful as other test suites like doctest, it doesn't capture stdout, and doesn't report test status.
- 

## Notes
- Dynamically swap libraries during run time