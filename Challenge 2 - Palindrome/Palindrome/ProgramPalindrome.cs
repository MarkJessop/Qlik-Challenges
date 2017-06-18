using System;


namespace Palindrome
{
    class ProgramPalindrome
    {
        static void Main(string[] args)
        {
            long maxPalindrome = 0;
            int m1 = 0;
            int m2 = 0;
            const int upperBound = 999;
            const int lowerBound = (upperBound + 1) / 10;

            for (int i = upperBound; i > lowerBound; i--)
            {
                for (int j = i; j > lowerBound; j--)
                {
                    long product = Math.BigMul(i, j);
                    if (product > maxPalindrome && isPalindome(product))
                    {
                        maxPalindrome = product;
                        m1 = i;
                        m2 = j;
                    }
                }
            }
            Console.WriteLine("The largest palindrome made from the product of two 3-digit numbers is:" + "\n" 
                + $"{maxPalindrome} = {m1} * {m2}");
            Console.ReadKey();
        }

        public static bool isPalindome(long Num)
        {
            string stringNum = Num.ToString();
            for (int i = 0; i < stringNum.Length / 2; i++)
            {
                if (stringNum[i] != stringNum[stringNum.Length  - i - 1])
                {
                    return false;
                }                    
            }
            return true;
        }
    }
}
