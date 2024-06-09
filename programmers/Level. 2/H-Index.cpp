// 프로그래머스 Lv.2 H-Index

#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<int> citations) {
    // 1. 논문 인용수를 내림차순으로 정렬
    sort(citations.begin(), citations.end(), greater<>());
    
    if(!citations[0]) return 0; // 가장 큰 값이 0이라면, H-index는 0
    
    int answer = 0;
    
    // 2. i + 1회 이상 인용된 논문이라면 H-Index 증가
    for(int i = 0; i < citations.size(); i++)
        if(citations[i] > i)
            answer++;
        else
            break;
    
    return answer;
}