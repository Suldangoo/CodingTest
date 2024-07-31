// 프로그래머스 Lv.2 의상

#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    // 1. Hashmap 생성 및 할당
    unordered_map<string, int> map;
    for (vector<string> wear : clothes)
        map[wear[1]]++;
    
    // 2. 각 Hashmap 요소에 입지 않는 경우도 포함하여 모두 곱하기
    int answer = 1;
    
    for (auto it = map.begin(); it != map.end(); it++)
        answer *= it->second + 1; // iterator로 순회하여 두 번째 값 (value) 곱하기
    
    // 3. 모두 입지 않은 경우를 제외한 경우의 수 반환
    return answer - 1;
}