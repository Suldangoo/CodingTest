// 프로그래머스 Lv.1 기사단원의 무기

#include <string>
#include <vector>
#include <cmath> // sqrt 함수를 사용하기 위해 필요

using namespace std;

int solution(int number, int limit, int power) {
    int answer = 0;

    for (int i = 1; i <= number; ++i) {
        int n = 0; // 약수의 개수 초기화
        
        // i의 제곱근까지의 약수를 구해 빠르게 약수의 개수 정리
        for (int j = 1; j <= sqrt(i); ++j) {
            if (j * j == i) {
                n += 1;
            } else if (i % j == 0) {
                n += 2;
            }
        }
        
        // 제한수치를 초과할 경우, 그 약수의 개수를 power로 교체
        if (n > limit) {
            answer += power;
        } else {
            answer += n;
        }
    }

    return answer;
}
