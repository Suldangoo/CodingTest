// 프로그래머스 Lv.0 배열 두배 만들기

#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> numbers) {
    vector<int> answer;
    for (auto num : numbers)
        answer.insert(answer.end(), num * 2); // vector의 가장 뒤에 numbers에서 2를 곱한 값을 추가
        
    return answer;
}