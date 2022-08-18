#include "doctest/doctest.h"
#include "lgb.hpp"

TEST_CASE(
    "small "
    "Testing Func1") {
  func1();
  CHECK(1);
}

TEST_CASE(
    "small "
    "Testing Func2") {
  func2();
  CHECK(1);
}