// 프로그래머스 Lv.1 둘만의 암호

#include <string>
#include <vector>

using namespace std;

string solution(string s, string skip, int index) {
    string answer = "";

    // 문자열 하나씩 처리
    for (char i : s) {
        int loop = index; // loop 변수 초기화

        // loop가 1 이상일 경우 반복
        while (loop) {
            // 현재 문자열의 아스키코드가 122(z)라면
            if (i >= 'z') {
                i = 'a'; // a로 변경
            } else {
                i = i + 1; // 다음 알파벳으로 변환
            }

            // 현재 알파벳이 skip 리스트에 존재하지 않는다면
            if (skip.find(i) == string::npos) {
                loop--; // loop 변수 감소
            }
        }

        answer += i; // 문자열 추가
    }

    return answer;
}
