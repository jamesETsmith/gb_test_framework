import click

DOCTEST_HEADER = """#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include \"doctest/doctest.h\"\n#include <iostream>"""

@click.command()
@click.option("--n_tests", "-n", type=int, help="Number of tests to generate")
def make_huge_tests(n_tests:int):
    with open("huge_tests.cpp", "w") as f:
        f.write(DOCTEST_HEADER)
        f.write("\n\n")

        for n in range(n_tests):
            f.write(f"TEST_CASE(\"huge: Test {n}\") ")
            f.write(" {\n")
            f.write(f" CHECK({n} == {n}); \n")
            f.write(f" std::cout << \"Here I am\" << std::endl; \n")
            f.write(f" std::cout << \"Here I am\" << std::endl; \n")
            f.write(f" std::cout << \"Here I am\" << std::endl; \n")
            f.write(f" std::cout << \"Here I am\" << std::endl; \n")
            f.write(f" std::cout << \"Here I am\" << std::endl; \n")
            f.write("}\n")

if __name__ == "__main__":
    make_huge_tests()