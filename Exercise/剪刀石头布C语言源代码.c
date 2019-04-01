#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<Windows.h>

int mieba() {  //灭霸随机出拳
	int a;
	srand((unsigned)time(NULL));
	a = rand() % 3 + 1;
	if (a == 1) {
		printf("灭霸出的是剪刀...\n");
		return 1;
	}
	else if (a == 2) {
		printf("灭霸出的是布...\n");
		return 2;
	}
	else if (a == 3) {
		printf("灭霸出的是石头...\n");
		return 3;
	}
	else {
		printf("程序出错QAQ\n");
		return 0;
	}
}

int judge(int com, int a) {  //判断胜负
	if (com == 1 && a == 1) {
		printf("平局！\n");
		printf("再来一次...\n");
		printf("请出拳：");
		return 1;
	}
	else if (com == 1 && a == 2) {
		printf("你成功的打败了灭霸！\n");
		return 0;
	}
	else if (com == 1 && a == 3) {
		printf("灭霸赢了！地球上一半人都消失了QAQ\n");
		return 0;
	}
	else if (com == 2 && a == 1) {
		printf("灭霸赢了！地球上一半人都消失了QAQ\n");
		return 0;
	}
	else if (com == 2 && a == 2) {
		printf("平局！\n");
		printf("再来一次...\n");
		printf("请出拳：");
		return 1;
	}
	else if (com == 2 && a == 3) {
		printf("你成功的打败了灭霸！\n");
		return 0;
	}
	else if (com == 3 && a == 1) {
		printf("你成功的打败了灭霸！\n");
		return 0;
	}
	else if (com == 3 && a == 2) {
		printf("灭霸赢了！地球上一半人都消失了QAQ\n");
		return 0;
	}
	else if (com == 3 && a == 3) {
		printf("平局！\n");
		printf("再来一次...\n");
		printf("请出拳：\n");
		return 1;
	}
	else return 2;
}


int main() {
	int t=1;
	int count1 = 0;  //记录输错的次数
	int choice;
	while (t) {
		printf("请选择你的出战英雄：\n");
		printf("1. 美国队长 2. 钢铁侠 3.蜘蛛侠\n");
		scanf("%d", &choice);
		int t3 = (int)choice;   //防止输入的不是数字
		if (t3 == 1) {
			printf("你选择的是美国队长！\n");
			t = 0;
		}
		else if (t3 == 2) {
			printf("你选择的是钢铁侠！\n");
			t = 0;
		}
		else if (t3 == 3) {
			printf("你选择的是蜘蛛侠！\n");
			t = 0;
		}
		else {
			printf("你输入有误！请重新选择！\n");
			printf("\n");
			t = 1;
			count1++;
		}
		if (count1 >= 3) {
			printf("由于你的瞎**输入，导致人类失去了一次抵抗灭霸的机会！！");
			exit(-1);
		}
	}
	printf("你将与灭霸对战！\n");
	printf("---------------------------------\n");
	int t1 = 1;
	int count2 = 0;  //记录出错次数
	int com;  //记录输入值
	printf("请你出拳：\n");
	while (t1) {
		printf("1. 剪刀 2. 布 3. 石头\n");
		scanf("%d", &com);
		int t4 = (int)com;  //防止输入的不是1 2 3
		int m;
		if (t4 == 1) {
			printf("你出的是剪刀...\n");
			Sleep(500);
			m = mieba();
			Sleep(500);
			t1 = judge(com, m);
		}
		else if (t4 == 2) {
			printf("你出的是布...\n");
			Sleep(500);
			m = mieba();
			Sleep(500);
			t1 = judge(com, m);
		}
		else if (t4 == 3) {
			printf("你出的是石头...\n");
			Sleep(500);
			m = mieba();
			Sleep(500);
			t1 = judge(com, m);
		}
		else {
			printf("地球的命运掌握在你手里！不要瞎出拳!\n");
			printf("\n");
			printf("请重新出拳：\n");
			count2++;
		}
		if (count2 >= 3) {
			printf("由于你的瞎**输入，导致人类失去了一次抵抗灭霸的机会！！");
			exit(-1);
		}
	}
}
