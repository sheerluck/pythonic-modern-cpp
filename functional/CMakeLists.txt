cmake_minimum_required(VERSION 3.5)
project(functional)

include_directories(_vendor/pythonic/include)
include_directories(_vendor/folly/include)
include_directories(_vendor/catch/include)
include_directories(_vendor/catch-ext/include)
include_directories(_vendor/range-v3/include)
include_directories(_vendor/json/include)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++1z -stdlib=libc++ -g")
if (USE_MODULES)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++1z -stdlib=libc++ -fno-autolink -fmodules -fmodules-cache-path=${CMAKE_SOURCE_DIR}/build -v")
endif()
if (CMAKE_BUILD_TYPE STREQUAL "Debug")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g")
endif()
set(SOURCE_FILES main.cpp)
add_executable(functional ${SOURCE_FILES})
