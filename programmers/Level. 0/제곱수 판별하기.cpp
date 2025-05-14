// 프로그래머스 Lv.0 제곱수 판별하기

#include <string>
#include <vector>
#include <cmath>

using namespace std;

int solution(int n) {
    float num = sqrt(n);
    
    if (num - (int)num == 0)
        return 1;
    else
        return 2;
}