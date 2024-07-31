// 프로그래머스 Lv.1 K번째수

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    
    // 1. commands에서 요소를 하나씩 불러오기
    for (vector<int> command : commands) {
        // 2. 원하는 범위까지 슬라이싱
        vector<int> newArray(array.begin() + command[0] - 1, array.begin() + command[1]);
        // 3. 정렬
        sort(newArray.begin(), newArray.end());
        // 4. 원하는 부분 인덱싱 후 answer에 삽입
        answer.push_back(newArray[command[2] - 1]);
    }
    
    return answer;
}