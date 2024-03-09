#include "MazeSolver.h"
#include <iostream>
using namespace std;

Solution::Solution(vector<vector<char>> maze, int rows, int cols) {
    this->maze = maze;
    this->solvedMaze = maze;
    this->rows = rows;
    this->cols = cols;
    this->largestPathwayLength = 0;
}

bool Solution::isValid(int i, int j, int m, int n)
{
    return (i >= 0 && i < m && j >= 0 && j < n);
}

int Solution::getLargestPathwayLength()
{
    return largestPathwayLength;
}

void Solution::printMaze()
{
    int i,j;
    for(i=0;i<rows;i++)
    {
        for(j=0;j<cols;j++)
            cout << maze[i][j] << " ";
        cout << "\n";
    }
}

void Solution::printSolvedMaze()
{
    int i,j;
    for(i=0;i<rows;i++)
    {
        for(j=0;j<cols;j++)
            cout << solvedMaze[i][j] << " ";
        cout << "\n";
    }
}

void Solution::recurse(int i, int j, int pi, int pj, int in, vector<vector<bool>>& currentStack)
{
    // cout << i << " , " << j << "\n";
    if(i == rows && in > largestPathwayLength)
    {
        largestPathwayLength = in;
        solvedMaze = maze;
        return;
    }
    if(!isValid(i, j, rows, cols) || maze[i][j] == '#' || currentStack[i][j])
        return;


    int dirs[] = {
        -1, -1, -1, 0, -1, 1,
        0, -1,         0, 1,
        1, -1,  1, 0,  1, 1,
    };

    maze[i][j] = char('0' + in);
    currentStack[i][j] = 1;

    int k;
    for(k=0;k<8;k++)
    {
        int ni = i + dirs[2*k];
        int nj = j + dirs[2*k+1];

        if(ni != pi || nj != pj)
            recurse(ni, nj, i, j, in+1, currentStack);
    }
    maze[i][j] = '.';
    currentStack[i][j] = 0;

}

bool Solution::solve()
{
    int i;
    vector<vector<bool>> currentStack(rows, vector<bool>(cols));
    for(i=0;i<cols;i++)
        recurse(0, i, -1, -1, 0, currentStack);

    if(largestPathwayLength == 0)
        return false;
    else
        return true;
}