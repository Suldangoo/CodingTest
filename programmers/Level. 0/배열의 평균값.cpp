// 프로그래머스 Lv.0 배열의 평균값

#include <string>
#include <vector>
#include <numeric>

using namespace std;

double solution(vector<int> numbers) {
    return accumulate(numbers.begin(), numbers.end(), 0.0) / numbers.size();
}