#include "catch.hpp"
#include "source/test.h"

TEST_CASE("test case 2", "[test2]") {
    WARN("The number is " << "youyou\n");
    REQUIRE(linuor::test(1) == 101);

    SECTION("test(2)") {
        REQUIRE(linuor::test(2) == 102);
    }

    SECTION("test(3)") {
        REQUIRE(linuor::test(3) == 103);
    }
}
