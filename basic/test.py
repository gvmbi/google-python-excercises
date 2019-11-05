import sys
import re

def main():
  txt = """
  <h3 align="center">Popularity in 1990</h3>
  ....
  <tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
  <tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
  <tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
  """
  x = re.search(r'\d',txt)
  print(x.group())


if __name__ == '__main__':
    main()