#include "tau/tau.h"

TEST(b, require) {
  REQUIRE_LE(1, 1);
  REQUIRE_LE(1, 2);
}