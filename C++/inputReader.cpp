#include "MazeSolver.h"

#include <fstream>
#include <vector>
#include <string>
#include <iostream>

using namespace std;

InputReader::InputReader(string filepath)
{
    this->filepath = filepath;
}

Solution InputReader::readInput()
{
    ifstream fileIn(filepath);

    if(!fileIn.is_open())
    {
        cout << filepath << " - is not present\n";
        return Solution({}, 0, 0);
    }

    vector<vector<char>> matrix;
    int rows=0, cols=0;

    while(!fileIn.eof())
    {
        vector<char> currentRow;
        string currentLine;
        getline(fileIn, currentLine);

        for(int i=0;i<currentLine.size();i++)
            currentRow.push_back(currentLine[i]);

        matrix.push_back(currentRow);
        cols = currentLine.size();
        rows++;
    }

    fileIn.close();
    return Solution(matrix, rows, cols);
}