cmake_minimum_required(VERSION 3.22.1)
project(labyrinth)

set( SOURCE_FILES
    mazeSolver.cpp
    inputReader.cpp
)

configure_file(${PROJECT_SOURCE_DIR}/in.txt ${PROJECT_SOURCE_DIR}/build/in.txt COPYONLY)

add_executable(${PROJECT_NAME} ${PROJECT_SOURCE_DIR}/labyrinth.cpp ${SOURCE_FILES})