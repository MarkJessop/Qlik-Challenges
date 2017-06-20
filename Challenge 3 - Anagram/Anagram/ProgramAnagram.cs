using System;
using System.Linq;

namespace Anagram
{
    class ProgramAnagram
    {
        static void Main(string[] args)
        {
            const string s1 = "Debit Card";
            const string s2 = "Bad Credit";

            Console.Write($"First string: {s1}" + "\n" + $"Second string: {s2}" + "\n");

            bool isAnag = isAnagram(s1, s2);

            Console.Write(isAnag ? "These two strings of letters are anagrams" : "two strings of letters are NOT anagrams");
            Console.ReadKey();
        }

        static bool isAnagram(string a, string b)
        {
            var list1 = a.Replace(" ", "").ToLower().ToList<char>();
            var list2 = b.Replace(" ", "").ToLower().ToList<char>();

            list1.Sort();
            list2.Sort();

            return list1.SequenceEqual(list2);            
        }
    }
}
