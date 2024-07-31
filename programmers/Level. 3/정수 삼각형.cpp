// 프로그래머스 Lv.3 정수 삼각형

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> triangle) {
    // 1. 이중 반복문을 통해 위 층의 숫자를 아래층에 더함
    for(int i = 1; i<triangle.size(); i++)
        for(int j = 0; j<triangle[i].size(); j++)
        {
            // 가장 왼쪽 숫자라면 왼쪽 숫자를 더함
            if(j == 0)
                triangle[i][j] += triangle[i - 1].front();
            // 가장 오른쪽 숫자라면 오른쪽 숫자를 더함
            else if(j == triangle[i].size() - 1)
                triangle[i][j] += triangle[i - 1].back();
            // 그 외라면 위의 두 숫자중 큰 숫자를 더함
            else
            {
                int bigger = max(triangle[i - 1][j - 1],triangle[i - 1][j]);
                triangle[i][j] += bigger;
            }
        }
    
    // 2. 가장 마지막 층까지 도달했다면 *max_element로 최댓값 리턴
    return *max_element(triangle.back().begin(), triangle.back().end());
}