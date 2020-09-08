project(CMSIS5)
#set(ROOT "${PROJECT_SOURCE_DIR}")
set(ROOT "${CMAKE_CURRENT_SOURCE_DIR}")
message("ROOT ${ROOT}")
if (CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
  # using Clang
elseif (CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
  # using GCC
  set(GCC ON)
elseif (CMAKE_CXX_COMPILER_ID STREQUAL "Intel")
  # using Intel C++
elseif (CMAKE_CXX_COMPILER_ID STREQUAL "MSVC")
  # using Visual Studio C++
endif()
add_subdirectory(CMSIS/DSP/Source)
