#include "doctest/doctest.h"
#include "lgb.hpp"

TEST_CASE(
    "big "
    "Testing_Some_New_Feature") {
  CHECK(1);
  SUBCASE("Subtest_in_big_test") { CHECK(1); }
}
