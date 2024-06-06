// 프로그래머스 Lv.0 분수의 덧셈

#include <string>
#include <vector>

using namespace std;

// 유클리드 호제법
int gcd(int a, int b)
{
    if (b == 0) return a; // b가 0이라면 a가 최대 공약수
    return gcd(b, a % b); // a % b로 재귀
}

vector<int> solution(int numer1, int denom1, int numer2, int denom2) {
    vector<int> answer;
    
    int numer = numer1 * denom2 + numer2 * denom1; // 공통분모 후 덧셈한 분자
    int denom = denom1 * denom2; // 공통분모 후 덧셈한 분모
    
    int g = gcd(numer, denom);
    
    answer.insert(answer.end(), numer / g);
    answer.insert(answer.end(), denom / g);
    
    return answer;
}