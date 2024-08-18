// 프로그래머스 Lv.1 행렬의 덧셈

#include <string>
#include <vector>

using namespace std;

vector<vector<int>> solution(vector<vector<int>> arr1, vector<vector<int>> arr2) {
    int column = arr1.size();
    int row = arr1[0].size();
    
    for(int i = 0; i < column; i++) {
        for(int j = 0; j < row; j++) {
            arr1[i][j] += arr2[i][j];
        }
    }
    
    return arr1;
}