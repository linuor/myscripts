#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"
#include "source/test.h"

TEST_CASE("test case 1", "[test1]") {
    WARN("The number is " << "fuckfuck\n");
    REQUIRE(linuor::test(1) == 101);

    SECTION("test(2)") {
        REQUIRE(linuor::test(2) == 102);
    }

    SECTION("test(3)") {
        REQUIRE(linuor::test(3) == 103);
    }
}
