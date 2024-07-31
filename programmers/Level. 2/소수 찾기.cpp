// 프로그래머스 Lv.2 소수 찾기

#include <string>
#include <vector>
#include <set>
#include <cmath>

using namespace std;

set<int> numberSet;

bool isPrime(int number)
{
    // 1. 0과 1은 소수가 아니다.
    if (number == 0 || number == 1)
        return false;
    
    // 2. 에라토스테네스의 체
    int lim = sqrt(number); // 해당 수의 루트값까지만 배수를 구해서 빼면 된다.
    for (int i = 2; i <= lim; i++)
        if (number % i == 0)
            return false;
    
    return true;
}

// 지금까지 모인 문자열, 아직 쓰지 않은 문자열을 받는 재귀함수
void recursive(string comb, string others)
{
    // 1. 현 조합을 numberSet에 추가한다.
    if(comb != "")
        numberSet.insert(stoi(comb));
    
    // 2. 현 조합 + others[i] 조합하여 새로운 조합을 만든다.
    for (int i = 0; i < others.size(); i++)
        recursive(comb + others[i], others.substr(0, i) + others.substr(i+1));
}

int solution(string numbers) {
    // 1. 모든 숫자 조합을 만든다.
    recursive("", numbers);
    
    // 2. 소수의 개수를 에라토스테네스의 체를 활용해 구한다.
    int answer = 0;
    
    for (int number : numberSet)
        if (isPrime(number))
            answer++;

    // 3. 소수의 개수를 리턴한다.
    return answer;
}