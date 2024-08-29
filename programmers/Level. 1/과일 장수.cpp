// 프로그래머스 Lv.1 과일 장수

#include <string>
#include <vector>
#include <algorithm> // sort 함수를 사용하기 위해 필요

using namespace std;

int solution(int k, int m, vector<int> score) {
    int answer = 0; // 누적 이익값

    // 사과를 내림차순으로 정렬
    sort(score.begin(), score.end(), greater<int>());

    int n = m - 1; // 포인터
    while (n < score.size()) {
        answer += score[n] * m; // 최저사과 점수 * 사과 개수 값을 이익에 누적
        n += m; // 포인터 증감
    }

    return answer;
}
