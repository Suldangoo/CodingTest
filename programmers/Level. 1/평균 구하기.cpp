// 프로그래머스 Lv.1 평균 구하기

#include <string>
#include <vector>

using namespace std;

double solution(vector<int> arr) {
    double answer = 0;
    
    for (int i : arr) {
        answer += i;
    }
    
    return answer / arr.size();
}