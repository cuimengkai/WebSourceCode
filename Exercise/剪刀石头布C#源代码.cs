using System;

namespace study
{
    class Program
    {
        public static int Duishou(string duishou)
        {
            int seed =(int) DateTime.Now.Ticks;  //作为种子
            Random rd = new Random(seed);
            int b = rd.Next(1, 3);
            if (b == 1)
            {
                Console.WriteLine("{0}出的是剪刀...",duishou);
            }
            else if (b == 2)
            {
                Console.WriteLine("{0}出的是石头...",duishou);
            }
            else Console.WriteLine("{0}出的是布...",duishou);
            return b;
        }
        public static int Judge(string a,int b)
        {
            if (a == "1" && b == 1)
            {
                Console.WriteLine("平局！");
                return 0;
            }
            else if (a == "1" && b == 2)
            {
                Console.WriteLine("你输了!");
                return 2;
            }
            else if (a == "1" && b == 3)
            {
                Console.WriteLine("你赢了！");
                return 1;
            }
            else if (a == "2" && b == 1)
            {
                Console.WriteLine("你赢了！");
                return 1;
            }
            else if (a == "2" && b == 2)
            {
                Console.WriteLine("平局！");
                return 0;
            }
            else if (a == "2" && b == 3)
            {
                Console.WriteLine("你输了！");
                return 2;
            }
            else if (a == "3" && b == 1)
            {
                Console.WriteLine("你输了！");
                return 2;
            }
            else if (a == "3" && b == 2)
            {
                Console.WriteLine("你赢了！");
                return 1;
            }
            else return 0;
        }
        static void Main(string[] args)
        {
            Console.WriteLine("请选择你的战斗对象（1. 灭霸 2. 多玛姆 3. 罗南）：");
            string a;         //存储输入的数字
            string duiShou;   //存储选择对手的名字
            while (true) {
                a = Console.ReadLine();
                if (a == "1")
                {
                    duiShou="灭霸";
                    break;
                }
                else if (a == "2")
                {
                    duiShou="多玛姆";
                    break;
                }
                else if (a == "3")
                {
                    duiShou="罗南";
                    break;
                }
                else
                {
                    Console.WriteLine("地球的命运在你手中，不要瞎输入！");
                }
            }
            Console.WriteLine("你选择了与{0}对战！", duiShou);
            Console.WriteLine("--------------------");
            int countwin = 0;  //赢的局数
            int countfail = 0; //输的局数
            int count = 0;     //总局数
            while (true)
            {
                Console.WriteLine("请你出拳（1. 剪刀 2. 石头 3. 布）：");
                string b = Console.ReadLine();
                if (b == "1")
                {
                    Console.WriteLine("你出的是剪刀...");
                    int c = Program.Duishou(duiShou);  //对手出拳
                    int e=Judge(b, c);                 //判断输赢
                    if(e == 1) countwin++; 
                    if (e == 2) countfail++;
                    Console.WriteLine("------------------");
                    Console.WriteLine("是否继续游戏（y/n):");
                    string d=Console.ReadLine();
                    if (d == "n")                      //退出游戏
                        break;
                    else count++;
                }
                else if (b == "2")
                {
                    Console.WriteLine("你出的是石头...");
                    int c = Program.Duishou(duiShou);
                    int e=Judge(b, c);
                    if (e == 1) { countwin++; }
                    if (e == 2) countfail++;
                    Console.WriteLine("------------------");
                    Console.WriteLine("是否继续游戏（y/n):");
                    string d = Console.ReadLine();
                    if (d == "n")
                        break;
                    else count++;
                }
                else if (b == "3")
                {
                    Console.WriteLine("你出的是布...");
                    int c = Program.Duishou(duiShou);
                    int e = Judge(b, c);
                    if (e == 1) { countwin++; }
                    if (e == 2) countfail++;
                    Console.WriteLine("------------------");
                    Console.WriteLine("是否继续游戏（y/n):");
                    string d = Console.ReadLine();
                    if (d == "n")
                        break;
                    else count++;
                }
                else
                {
                    Console.WriteLine("你的输入有误！");
                }
            }
            Console.WriteLine("*****************");
            Console.WriteLine("你一共玩了{0}局...\n赢了{1}局，输了{2}局", count,countwin,countfail);
            if (countwin > countfail)
            {
                Console.WriteLine("恭喜你最终打败了{0}，拯救了地球！",duiShou);
            }
            else if (countwin < countfail)
            {
                Console.WriteLine("很遗憾，你失败了QAQ");
            }
            else Console.WriteLine("你最终和{0}打成平手！",duiShou);
            Console.ReadKey();
        }
    }
}
