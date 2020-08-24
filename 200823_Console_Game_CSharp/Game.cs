using System;

namespace ConsoleGame
{
  class Game : SuperGame
  {     /* explanation on the use of 'out' https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/out-parameter-modifier */
        public new static void UpdatePosition(string KeyPressed, out int X_Axis, out int Y_Axis)
            {
            switch(KeyPressed)
            {
                case "DownArrow":
                    X_Axis = 0;
                    Y_Axis = 1;
                    break;
                case "UpArrow":
                    X_Axis = 0;
                    Y_Axis = -1;
                    break;
                case "LeftArrow":
                    X_Axis = -1;
                    Y_Axis = 0;
                    break;
                case "RightArrow":
                    X_Axis = 1;
                    Y_Axis = 0;
                    break;
                default:
                    X_Axis = 0;
                    Y_Axis = 0;
                    break;
            }
        }
            /*Following some forum support I have source a better way to build this code block, however I thought best to leave 'my' solution in place
            to allow for discussion*/
                public new static char UpdateCursor(string KeyPressed)
            {
            char key = 'x';
            switch(KeyPressed)
            {
                case "DownArrow":
                    key = 'v';
                    break;
                case "UpArrow":
                    key =  '^';
                    break;
                case "LeftArrow":
                    key = '<';
                    break;
                case "RightArrow":
                    key =  '>';
                    break;
            }
            return key;
        }

        /*Logic allows character to leave one side of screen and return on other*/
        public new static int KeepInBounds(int Coordinate, int MaxValue)
            {
            if (Coordinate < 0)
            {
                return MaxValue - 1;
            }
            else if (Coordinate >= MaxValue)
            {
                return 0;
            }
            else
            {
                return Coordinate;
            }
        }

        public new static bool DidScore(int X_Char, int Y_Char, int X_Fruit, int Y_Fruit)
            {
            return (X_Char == X_Fruit && Y_Char == Y_Fruit)? true : false;
        }
  }
}

