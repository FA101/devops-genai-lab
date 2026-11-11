import unittest
from app import calculate_shipping

class TestOrderService(unittest.TestCase):
    
    def test_shipping_calculation(self):
        # Este teste simula a chamada da função interna
        # Passando "5.50" como string para forçar o erro
        result = calculate_shipping(100.00, "5.50")
        self.assertEqual(result, 105.50)

if __name__ == '__main__':
    unittest.main()