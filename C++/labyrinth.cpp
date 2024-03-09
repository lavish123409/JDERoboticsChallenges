#include "MazeSolver.h"

#include <iostream>

using namespace std;


int main() {

    vector<vector<char>> mat, ans;

    InputReader inputReader("in.txt");
    Solution obj = inputReader.readInput();
    if(obj.solve())
    {
        cout << obj.getLargestPathwayLength() << "\n";
    }
    else
    {
        cout << "-1\n";

    }
    obj.printSolvedMaze();


    return 0;
}