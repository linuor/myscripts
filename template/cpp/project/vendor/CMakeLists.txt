# Copyright © 2016 linuor. All Rights Reserved.
# @file CMakeLists.txt
# @brief script file for cmake build system
# @author linuor
# @version 0.1
# @date 2016-01-10

CMAKE_MINIMUM_REQUIRED(VERSION 3.0)
PROJECT(Vendor)
INCLUDE(ExternalProject)
FIND_PACKAGE(Git REQUIRED)

ExternalProject_Add(
    catch
    SOURCE_DIR ${VendorDir}/catch
    GIT_REPOSITORY https://github.com/philsquared/Catch.git
    TIMEOUT 10
    UPDATE_COMMAND ${GIT_EXECUTABLE} pull
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND ""
    LOG_DOWNLOAD ON
)
# Expose required variable (CATCH_INCLUDE_DIR) to parent scope
ExternalProject_Get_Property(catch source_dir)
SET(CATCH_INCLUDE_DIR ${source_dir}/single_include CACHE INTERNAL "Path to single_include folder for catch")

ExternalProject_Add(
    sqlite
    SOURCE_DIR ${VendorDir}/sqlite
    URL http://sqlite.org/2016/sqlite-amalgamation-3100200.zip
    TIMEOUT 10
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND ""
    LOG_DOWNLOAD ON
)
# Expose required variable (CATCH_INCLUDE_DIR) to parent scope
ExternalProject_Get_Property(sqlite source_dir)
SET(SQLITE_INCLUDE_DIR ${source_dir} CACHE INTERNAL "Path to src folder for sqlite")
