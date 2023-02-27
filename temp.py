#Gersaniba
import unittest
def temp(Fahrenheit):
    Fahrenheit = 32
    Celcius = ((Fahrenheit-32)*(5/9))

    return Celcius

class Mytest(unittest.TestCase):
    def test(self):

        self.assertEqual(temp(32),0)
    def test2(self):

        self.assertEqual(temp(32),1)

if __name__ =='__main__':
    unittest.main()
   
   