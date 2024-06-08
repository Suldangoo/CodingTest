// 프로그래머스 Lv.1 체육복

#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    // 1. 학생 배열 정의
    vector<int> student(n + 2, 0); // 학생 수 +2 까지의 크기만큼 0으로 초기화
    
    // 2. 도난당한 학생들의 체육복 감소
    for (int l : lost)
        student[l]--;
    
    // 3. 여벌이 있는 학생들의 체육복 증가
    for (int r : reserve)
        student[r]++;
    
    // 4. 체육복 대여
    for (int i = 1; i <= n; i++) {
        if (student[i] > 0) // 체육복 여벌이 존재한다면
        {
            if (student[i-1] < 0)
            {
                student[i]--;
                student[i-1]++;
            }
            else if (student[i+1] < 0)
            {
                student[i]--;
                student[i+1]++;
            }
        }
    }
    
    // 5. 체육복이 0 이상인 학생들의 수를 count
    int answer = 0;
    
    for (int i = 1; i <= n; i++)
        if (student[i] >= 0)
            answer++;
    
    return answer;
}