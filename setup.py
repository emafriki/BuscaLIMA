"""Setup file for a buscaminas game package"""

from setuptools import setup

setup(name='buscaminas',
      version='0.1',
      description='creating a graphical minesweeper using python',
      url='https://github.com/emafriki/BuscaLIMA',
      author='Alma Rocio Patiño Chavez, Maritza Nazareth Cruz Aviles, Mauritania Meneses Bote, Mariana Chavez Perales',
      author_email='pa401981@uaeh.edu.mx, cr441643@uaeh.edu.mx,me340563@uaeh.edu.mx,ch400795@uaeh.edu.mx',
      license='MIT',
      packages=['buscaminas'],
      include_package_data = True,
      package_data = {
          '' : ['*.jpg'],
          '' : ['*.yml'],
      },
      zip_safe=False)
