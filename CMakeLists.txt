cmake_minimum_required(VERSION 3.20 FATAL_ERROR)

# project name and language
project(gb_fake LANGUAGES C)

# require C++11
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_EXTENSIONS OFF)
set(CMAKE_C_STANDARD_REQUIRED ON)

set(CMAKE_C_FLAGS "${CMAKE_CXX_FLAGS} -g --coverage")

include_directories(${CMAKE_SOURCE_DIR}/include)
add_library(gb_fake SHARED ${CMAKE_SOURCE_DIR}/src/gb_fake.c)

#
# Testing
#
enable_testing()
add_subdirectory(test)