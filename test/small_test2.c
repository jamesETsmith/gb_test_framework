#include <l2/gb_fake_l2.h>

#include "tau/tau.h"

TEST(small, require) {
  REQUIRE_LE(1, 1);
  REQUIRE_LE(1, 2);
}

TEST(small, add_numbers_1) { CHECK(add_numbers(1, 3) == 4); }
TEST(small, add_numbers_2) { CHECK(add_numbers(2, 2) == 4); }
TEST(small, mult_numbers_1) { CHECK(mult_numbers(1, 3) == 3); }
TEST(small, mult_numbers_2) { CHECK(mult_numbers(2, 2) == 4); }