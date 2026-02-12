import numpy as np
import matplotlib.pyplot as pit

class IntArray:
  def __init__(self, int_array):
    if not isinstance(int_array, np.ndarray) or int_array.dtype != int:
      raise ValueError("Input must be a NUMPY array of integors")

    self.int_array = int_array

  def display(self):
    print(self.int_array)

  def salary(self):
    array_shape = self.int_array.shape
    money_per_product = np.full(array_shape, 7)
    salariers = self.int_array * money_per_product

    print(f'People made {self.int_array} products and this is their salaries {salariers}')

  def show_data(self):
    x = np.arange(len(self.int_array))
    pit.plot(x, self.int_array, marker='o')
    pit.title('Productivity of employees')
    pit.xlabel('rank of employees')
    pit.ylabel('products/month')
    pit.xticks(x)
    pit.grid()
    pit.show()