cmake_minimum_required(VERSION 3.15 FATAL_ERROR)

# project name and language
project(lgb_test LANGUAGES CXX)

# require C++11
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include_directories(${CMAKE_SOURCE_DIR}/include)
add_library(lgb SHARED ${CMAKE_SOURCE_DIR}/src/lgb.cpp)

#
# Testing
#
enable_testing()

# Add doctest_discover_tests()
# include(${CMAKE_SOURCE_DIR}/external/doctest/doctest.cmake)
# MESSAGE(STATUS ${CMAKE_SOURCE_DIR}/external/doctest/doctest.cmake)

# Make test executables
include(FetchContent)
FetchContent_Declare(
        DocTest
        GIT_REPOSITORY "https://github.com/doctest/doctest"
        GIT_TAG "2.4.5"
)
FetchContent_MakeAvailable(DocTest)
include(${doctest_SOURCE_DIR}/scripts/cmake/doctest.cmake)

# Small Tests (aka regression)
add_executable(
    small_tests 
    ${CMAKE_SOURCE_DIR}/test/big_tests.cpp # Split the main function out into it's own file
    ${CMAKE_SOURCE_DIR}/test/tests_p1.cpp # and put the tests themselves in smaller files
    ${CMAKE_SOURCE_DIR}/test/tests_p2.cpp # so compilitation parallelizes better
    )
target_link_libraries(small_tests PUBLIC lgb doctest::doctest)


# Big Tests (aka fullspec)
add_executable(
    big_tests 
    ${CMAKE_SOURCE_DIR}/test/big_tests.cpp #Similar to above except with more
    ${CMAKE_SOURCE_DIR}/test/tests_p3.cpp
    )
target_link_libraries(big_tests PUBLIC lgb doctest::doctest)

# HUGE Tests (testing CTests limits)
add_executable(
    huge_tests 
    ${CMAKE_SOURCE_DIR}/test/huge_tests.cpp
    )
target_link_libraries(huge_tests PUBLIC lgb doctest::doctest)


doctest_discover_tests(big_tests ADD_LABELS "big")
doctest_discover_tests(small_tests ADD_LABELS "small")
doctest_discover_tests(huge_tests ADD_LABELS "huge")
