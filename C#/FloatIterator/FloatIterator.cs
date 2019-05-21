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
            Console.WriteLine("Float Based Iterator");
            Console.WriteLine(" ");
            Console.WriteLine("Counting Float Values with for");
            Console.WriteLine("=================================");

            // The F suffix is required to initialize the value of f as a float
            // Otherwise f will be initialized as a double and will cause issues later.

            // First method, for loop. Note that the test value must be outside the intended range
            // Otherwise due to the impercision of floats, a boundry value will met early 
            for (float f = 0.1F; f < 10.1F; f +=0.1F)
            {
                Console.WriteLine("Start: {0:F2}", f);
            }

            /*
            Second method, while loop. 
            Note that the test value greater precision than the target value
            In this case 10.0 is the final target 
            but 10.01 has enough added precision to test as intended
            */
            Console.WriteLine(" ");
            Console.WriteLine("Counting Float Values with while 2");
            Console.WriteLine("==================================");
            float myF = 0.1F;
            while (myF < 10.01F)
            {
                Console.WriteLine("Start: {0:F2}", myF);
                myF += 0.1F;
            }

            /*
            third method, Integer loop. 
            We can accurately determine the number of steps needed to loop through
            the intended number of steps and count this with an integer
            However, we must take care in calculating the number of steps and the
            test condition must be inclusive of the last step. Requiring the <= test
            */
            Console.WriteLine(" ");
            Console.WriteLine("Counting Float Values with Integer");
            Console.WriteLine("==================================");
            myF = 0.5F;
            float myTarget = 10.0F;
            float myStep = 0.1F;
            int mySteps = (int)((myTarget - myF) / myStep);
            for (int i = 0; i <= mySteps; i++)
            {
                Console.WriteLine("Start: {0:F2}", myF);
                myF += 0.1F;
            }
     
        } 
    }
}
