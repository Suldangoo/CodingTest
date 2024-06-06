// 프로그래머스 Lv.0 두 수의 나눗셈

#include <string>
#include <vector>

using namespace std;

int solution(int num1, int num2) {
    float num = num1; // float로 형변환
    float answer = num / num2; // 형변환한 값을 넣고, float 변수에 할당
    return answer * 1000;
}