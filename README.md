[![test_coverage](https://github.com/jamesETsmith/gb_test_framework/actions/workflows/ci_build.yml/badge.svg?branch=main)](https://github.com/jamesETsmith/gb_test_framework/actions/workflows/ci_build.yml)
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

If you want to filter and run an individual subtest, you can run something like the following:
```
$ ./build/test/small_test --filter="small.add*"
[==========] Running 2 test suites.
[ RUN      ] small.add_numbers_1
[       OK ] small.add_numbers_1 (3.00us)
[ RUN      ] small.add_numbers_2
[       OK ] small.add_numbers_2 (5.00us)
[==========] 2 test suites ran
[  PASSED  ] 2 suites
[  FAILED  ] 0 suites

Summary:
    Total test suites:          7
    Total suites run:           2
    Total warnings generated:   0
    Total suites skipped:       5
    Total suites failed:        0
SUCCESS: 2 test suites passed in 0.27ms
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

