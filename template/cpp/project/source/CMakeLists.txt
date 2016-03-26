# Copyright © 2016 {{info.author}}. All Rights Reserved.
# @file CMakeLists.txt
# @brief CMakeLists.txt for cmake build system
# @author {{info.author}}
# @version {{info.ver}}
# @date {{info.date}}

FIND_PACKAGE(Qt5 5.5.1 REQUIRED Gui Qml)
FIND_PACKAGE(Boost 1.60.0 REQUIRED)
INCLUDE_DIRECTORIES(${Boost_INCLUDE_DIRS})
SET(CMAKE_AUTOMOC ON)
SET(CMAKE_AUTORCC ON)
SET(CMAKE_AUTOUIC ON)
SET(INCLUDE_CURRENT_DIRECTION ON)
SET(Boost_USE_MULTITHREAD ON)
SET(ResLists ../resource/qml.qrc
    ../resource/main.qml
    ../resource/MainMenu.qml
    ../resource/MainStatusBar.qml
)
SET(SrcLists main.cpp
    AppManager.cpp AppManager.h
    test.cpp test.h
)
ADD_EXECUTABLE(${PROJECT_NAME} ${SrcLists} ${ResLists})
TARGET_LINK_LIBRARIES(${PROJECT_NAME} Qt5::Core Qt5::Gui Qt5::Qml)
