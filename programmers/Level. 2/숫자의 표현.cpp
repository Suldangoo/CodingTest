// 프로그래머스 Lv.2 숫자의 표현

#include <string>
#include <vector>
#include <numeric>

using namespace std;

int solution(int n) {
    vector<int> numbers(10001); // 크기가 10,001인 벡터 생성
    iota(numbers.begin(), numbers.end(), 1); // 1부터 시작하는 값으로 채움
    
    int x = 0;
    int y = 1;
    int answer = 0;
    
    while (numbers[x] <= n) {
        int sum = accumulate(numbers.begin() + x, numbers.begin() + y, 0);
        
        if (sum < n) {
            y++;
        }
        else if (sum > n) {
            x++;
        }
        else {
            answer++;
            x++;
        }
    }
    
    return answer;
}