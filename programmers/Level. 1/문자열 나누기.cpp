// 프로그래머스 Lv.1 문자열 나누기

#include <string>
#include <vector>

using namespace std;

int solution(string s) {
    int answer = 0;
    char point = '_'; // 처음 읽어들일 비교할 문자
    
    int a = 0; // 처음 읽은 문자의 개수
    int b = 0; // 그 외 문자의 개수
    
    for (char i : s) {
        if (point == '_') { // point가 비어있다면 할당
            point = i;
            a++;
            continue;
        }
        
        // 문자를 읽고 개수 증가
        if (point == i)
            a++;
        else
            b++;
        
        // 두 문자의 개수가 같아지는 순간
        if (a == b) {
            answer++; // 문장 분할
            
            point = '_';
            a = 0;
            b = 0;
        }
    }
    
    // 모든 문장을 분할한 후 뒤에 남아있는 문장이 있을 경우도 포함
    if (a > 0 || b > 0)
        answer++;
    
    return answer;
}