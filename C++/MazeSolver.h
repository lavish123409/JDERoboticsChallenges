#include <string>
#include <vector>

class Solution {

    std::vector<std::vector<char>> maze, solvedMaze;
    int rows, cols, largestPathwayLength;

public:
    Solution(std::vector<std::vector<char>>, int, int);
    bool isValid(int i, int j, int m, int n);
    int getLargestPathwayLength();
    void printMaze();
    void printSolvedMaze();
    void recurse(int i, int j, int pi, int pj, int in, std::vector<std::vector<bool>>& currentStack);
    bool solve();

};

class InputReader {
    std::string filepath;

public:
    InputReader(std::string);
    Solution readInput();
};
