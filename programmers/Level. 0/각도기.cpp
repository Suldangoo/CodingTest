// 프로그래머스 Lv.0 각도기

#include <string>
#include <vector>

using namespace std;

int solution(int angle) {
    if (angle < 90)
        return 1;
    else if (angle == 90)
        return 2;
    else if (angle == 180)
        return 4;
    else
        return 3;
}