// 프로그래머스 Lv.1 완주하지 못한 선수
// Sorting / Loop를 활용

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    // 1. 두 배열을 정렬한다.
    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());
    
    // 2. 두 배열이 다를 때까지찾는다.
    int i = 0;
    for (; i < completion.size(); i++)
        if (participant[i] != completion[i])
            break;
    
    // 3. 마지막까지 완주하지 못한 선수를 리턴한다.
    return participant[i];
}