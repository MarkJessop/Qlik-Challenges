using System;


namespace Sorting
{
    class ProgramSorting
    {
        static void Main(string[] args)
        {
            const int upperBound = 100;
            const int lowerBound = 1;
            const int total = 100;
            int[] array = new int [total];

            Random random = new Random();
            for (int i = 0; i < total; i++)
            {
                array[i] = random.Next(lowerBound, upperBound);
            }

            Console.Write("Generate a list of 100 random integers between 1 and 99:" + "\n");
            foreach (int element in array)
            {
                Console.Write(element + " ");
            }
            Console.Write("\n" + "Press any key to sort" + "\n");
            Console.ReadKey();

            array = countingSort(array, upperBound+1);

            foreach (int element in array)
            {
                Console.Write(element + " ");
            }
            Console.Write("\n" + "The list is sorted" + "\n");
            Console.ReadKey();
        }

        public static int[] countingSort(int[] originalArray, int k)
        {
            int[] counterArray = new int[k];

            for (int i = 0; i < originalArray.Length; i++)
            {
                counterArray[originalArray[i]]++;
            }

            for (int i = 1; i < k; i++)
            {
                counterArray[i] += counterArray[i - 1];
            }
                
            int[] sortedArray = new int[originalArray.Length];

            for (int i = originalArray.Length - 1; i >= 0; i--)
            {
                sortedArray[--counterArray[originalArray[i]]] = originalArray[i];
            }
                
            return sortedArray;
        }
    }
}