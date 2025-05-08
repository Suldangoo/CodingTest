// 프로그래머스 Lv.0 양꼬치

#include <string>
#include <vector>

using namespace std;

int solution(int n, int k) {
    int answer = n * 12000; // 양꼬치값 계산
    answer += (k - n / 10) * 2000; // 음료수값 계산
    return answer;
}