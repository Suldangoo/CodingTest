#include <iostream>
#include <vector>
using namespace std;

int main() {
    int testCases;
    cin >> testCases;

    while (testCases--)
    {
        int days;
		cin >> days;
		vector<int> prices(days);
        for (int i = 0; i < days; i++)
        {
			cin >> prices[i];
        }

        long profit = 0; // 현재 이익
        int maxProfit = 0; // 최대 이익

		// 뒤에서부터 순회하며 최댓값이 갱신되기 전까지 모두 판매
		for (int i = days - 1; i >= 0; i--)
		{
			// 현재까지의 최댓값 확인
			if (prices[i] > maxProfit)
			{
				maxProfit = prices[i];
			}
			// 그날의 주식을 최댓값에 팔아서 이익 확보
			profit += maxProfit - prices[i];
		}

		cout << profit << endl;
    }

    return 0;
}