// 프로그래머스 Lv.2 카펫

#include <string>
#include <vector>
#define MAX 2000

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    
    for(int i = 1; i <= MAX; i++)
        for(int j = 1; j <= MAX; j++)
            if(i*2 + j*2 - 4 == brown && (i-2) * (j-2) == yellow)
            {
                answer.push_back(max(i, j));
                answer.push_back(min(i, j));
                return answer;
            }
}