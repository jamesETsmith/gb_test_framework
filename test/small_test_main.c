#include "tau/tau.h"

TAU_MAIN()

TEST(a, count) {
  int count = 10000000;
  REQUIRE_EQ(count, 10000000);
}