import click

DOCTEST_HEADER = """#include <tau/tau.h>

TAU_MAIN()

"""

@click.command()
@click.option("--n_tests", "-n", type=int, help="Number of tests to generate")
@click.option("--output", "-o", type=str, help="The file path to write to.")
def make_huge_tests(n_tests:int, output: str):
    with open(output, "w") as f:
        f.write(DOCTEST_HEADER)
        f.write("\n\n")

        for n in range(n_tests):
            f.write(f"TEST(huge, test_{n})")
            f.write(" {\n")
            f.write(f"  CHECK({n} == {n}); \n")
            f.write("  printf(\"Useful debug info\\n\");\n")
            f.write("  printf(\"Useful debug info\\n\");\n")
            f.write("  printf(\"Useful debug info\\n\");\n")
            f.write("  printf(\"Useful debug info\\n\");\n")
            f.write("  printf(\"Useful debug info\\n\");\n")
            f.write("}\n")

if __name__ == "__main__":
    make_huge_tests()