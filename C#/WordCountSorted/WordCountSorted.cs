using System;
using System.Collections.Generic;
using System.Linq;
using System.Collections.Concurrent;

namespace C__Samples
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            Dictionary<string, int> myDict = new Dictionary<string, int>();

            myDict.Add("daddy", 1);
            myDict.Add("mommy", 3);
            myDict.Add("Daddy", 5);
            myDict.Add("Child", 10);

            Console.WriteLine("Sorted by Key");
            Console.WriteLine("====================");

            // Simple Method
             foreach (KeyValuePair<string, int> item in myDict.OrderBy(key => key.Key))
            {
                Console.WriteLine("Key: {0}, Value: {1}", item.Key, item.Value);
            }
            
            Console.WriteLine(" ");
            Console.WriteLine("Sorted by Key");
            Console.WriteLine("====================");

             foreach (KeyValuePair<string, int> item in myDict.OrderBy(key => key.Value))
            {
                Console.WriteLine("Key: {0}, Value: {1}", item.Key, item.Value);
            }


            Console.WriteLine(" ");
            Console.WriteLine("Using Add to Dictionary");
            Console.WriteLine("==========================");

            ConcurrentDictionary<string, int> lowerDict = new ConcurrentDictionary<string, int>();

            foreach (KeyValuePair<string, int> item in myDict)
            {
                String lowerKey = item.Key.ToString().ToLower();
                lowerDict.AddOrUpdate(item.Key.ToString().ToLower(), 1 , (id, count) => count + 1);
                Console.WriteLine("Addin Raw: {0},  Lower: {1}", item.Key, lowerKey);
            }

            Console.WriteLine(" ");
            Console.WriteLine("Output of Dictionary");
            Console.WriteLine("==========================");

            foreach (KeyValuePair<string, int> item in lowerDict.OrderBy(key => key.Key))
            {
                Console.WriteLine("Entry - Key: {0}, Value: {1}", item.Key, item.Value);
            }
        } 
    }
}
