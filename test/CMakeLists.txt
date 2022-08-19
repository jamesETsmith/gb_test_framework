#
# Include dependencies
#

find_package(Python COMPONENTS Interpreter REQUIRED)

# Tau
include(FetchContent)
FetchContent_Declare(
    Tau
    URL https://github.com/jasmcaus/tau/archive/dev.zip
)

FetchContent_MakeAvailable(Tau)
include_directories(${Tau_SOURCE_DIR})


#
# Setup tests
#


# Small Tests (aka regression)
add_executable(
    small_test
    ${CMAKE_SOURCE_DIR}/test/small_test_main.c # Split the main function out into it's own file
    ${CMAKE_SOURCE_DIR}/test/small_test1.c # and put the tests themselves in smaller files
    ${CMAKE_SOURCE_DIR}/test/small_test2.c # so compilitation parallelizes better
    )
target_link_libraries(small_test gb_fake)

add_test(NAME small_test COMMAND small_test)

# Huge tests
add_custom_command(
    COMMAND python 
        ${CMAKE_SOURCE_DIR}/test/make_huge_test.py 
            -n 10000
            -o ${CMAKE_SOURCE_DIR}/test/huge_test.c
    OUTPUT ${CMAKE_SOURCE_DIR}/test/huge_test.c
    DEPENDS ${CMAKE_SOURCE_DIR}/test/make_huge_test.py
    )
add_executable(huge_test ${CMAKE_SOURCE_DIR}/test/huge_test.c)
add_test(NAME huge_test COMMAND huge_test)
