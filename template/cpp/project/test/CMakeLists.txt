# Copyright © 2016 {{info.author}}. All Rights Reserved.
# @file CMakeLists.txt
# @brief CMakeLists.txt for cmake build system
# @author {{info.author}}
# @version {{info.ver}}
# @date {{info.date}}

INCLUDE_DIRECTORIES(${CATCH_INCLUDE_DIR} ${COMMON_INCLUDES})
SET(SrcLists2 test.cpp test2.cpp ../source/test.cpp ../source/test.h)
ADD_EXECUTABLE(${TEST_COMMAND} ${SrcLists2})
