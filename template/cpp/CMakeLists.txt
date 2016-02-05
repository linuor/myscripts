# Copyright © 2016 {{info.author}}. All Rights Reserved.
# @file CMakeLists.txt
# @brief CMakeLists.txt for cmake build system
# @author {{info.author}}
# @version {{info.ver}}
# @date {{info.date}}

PROJECT({{info.dest}} CXX)
CMAKE_MINIMUM_REQUIRED(VERSION 3.0)
SET(CMAKE_CXX_STANDARD 11)
SET(TEST_COMMAND ${PROJECT_NAME}test)
INCLUDE_DIRECTORIES(${PROJECT_SOURCE_DIR})
SET(VendorDir ${PROJECT_SOURCE_DIR}/vendor)

ADD_SUBDIRECTORY(vendor)
ADD_SUBDIRECTORY(source)
ADD_SUBDIRECTORY(test)

ENABLE_TESTING()
ADD_TEST(NAME RunTests COMMAND ${TEST_COMMAND})
