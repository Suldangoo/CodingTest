// 프로그래머스 Lv.1 자릿수 더하기

#include <iostream>

using namespace std;
int solution(int n)
{
    int answer = 0;

    while (n > 0) {
        answer += n % 10;
        n /= 10;
    }

    return answer;
}