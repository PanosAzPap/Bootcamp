using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Exercise6
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Insert a number (1-6):");
            int number = Convert.ToInt32(Console.ReadLine());


            colors col = new colors();
            col = (colors)number;



            switch (col)
            {
                case colors.yellow:
                    Console.WriteLine("Your color is yellow");
                    break;
                case colors.green:
                    Console.WriteLine("Your color is green");
                    break;
                case colors.blue:
                    Console.WriteLine("Your color is blue");
                    break;
                case colors.red:
                    Console.WriteLine("Your color is red");
                    break;
                case colors.orange:
                    Console.WriteLine("Your color is orange");
                    break;
                case colors.pink:
                    Console.WriteLine("Your color is pink");
                    break;                
            }

            Console.ReadLine();
        }
    }
}
