// 프로그래머스 Lv.2 더 맵게

#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    
    // 1. min heap 우선순위 큐 생성
    priority_queue<int, vector<int>, greater<int>> pq(scoville.begin(), scoville.end());
    
    // 2. 음식이 2개 이상에, 제일 맵지 않은 음식이 K보다 작다면 반복
    while (pq.size() >= 2 && pq.top() < K) {
        int first = pq.top();
        pq.pop();
        int second = pq.top();
        pq.pop();
        
        pq.push(first + (second * 2));
        answer++;
    }
    
    // 3. 가장 맵지 않은 음식이 K 미만이라면 -1 리턴
    if (pq.top() < K) {
        answer = -1;
    }
    
    return answer;
}