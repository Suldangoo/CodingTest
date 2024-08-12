// 프로그래머스 Lv.1 나누어 떨어지는 숫자 배열

#include <string>
#include <vector>
#include <algorithm> // sort 함수 사용을 위해 필요

using namespace std;

vector<int> solution(vector<int> arr, int divisor) {
    vector<int> answer;
    
    for (int i : arr) {
        if (i % divisor == 0)
            answer.push_back(i);
    }
    
    if (answer.empty())
        answer.push_back(-1); // 나눠지는 숫자가 없는 경우 -1 추가
    
    sort(answer.begin(), answer.end()); // 오름차순 정렬
    
    return answer;
}