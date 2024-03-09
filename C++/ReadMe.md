# C++ challenge

JDE Robotics - [C++ challenge](https://drive.google.com/file/d/1GO0GJIi7rNqZXhPEaV8Qf0Ds4qFHczJ2/view)

## Project Structure

- **workspace:** This folder contains all the C++ source files and headers needed for the labyrinth solver.

- **build:** This directory will be used to store all the generated build files and executables. You can create it by running the following commands in the project root directory:

    ```bash
    cmake -S . -B ./build
    ```

## Building the Project

To build the project, follow these steps:

1. Open a terminal and navigate to the project root directory.

2. Create the build directory:

    ```bash
    cmake -S . -B ./build
    ```

3. Navigate to the build directory:

    ```bash
    cd build
    ```

4. Build the project using `make`:

    ```bash
    make
    ```

## Running the Executable

Once the project is successfully built, you can run the executable by executing the following command from the build directory:

```bash
./labyrinth
```

## Input Options

You can provide input to the program using either of the following methods:

1. **Using an Input Text File in Workspace:**
   
    Place your input in a text file named `in.txt` in the `workspace` folder. After that, build and run the code as explained [here](#building-the-project).

2. **Directly Changing Input in Build Directory:**

    Alternatively, you can directly modify the `in.txt` file located in the `build` directory. This file serves as the input source for the program. Update the input values as needed before running the executable.

