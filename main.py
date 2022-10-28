'''
 > Code by Icy
 > FastLang Project
 > Github : https://github.com/SOON
'''

class Interpreter:
  def __init__(self, file:str):
    self.syntax = {'var': '$', 'const': '$$', 'print': '<<', 'comment':';', 'erase':'!'}
    self.memory = {'vars': {}, 'consts': {'_': 10101}}
    self.file = file
  
  def clear_memory(self) -> None:
      self.memory = {'vars': {}, 'consts': {'_': 10101}}
      
  def remove_var(self, var_type:str, var:str) -> None:
      self.memory[var_type].pop(var)
  
  def get_value(self, name:str) -> str:
    if name.startswith(self.syntax['const']):
      return self.memory['consts'][name.replace(self.syntax['const'], '')]
    elif name.startswith(self.syntax['var']):
      return self.memory['vars'][name.replace(self.syntax['var'], '')]
  
  def interpret(self) -> None:
    with open(self.file, 'r') as f:
      lines = f.readlines()
  
    for line in lines:
      if not line.startswith(self.syntax['comment']):
        line = line.replace('\n', '')
        if line.startswith(self.syntax['const']):
          temp = line.replace(self.syntax['const'], '', 1).split(' ')
          output = temp[1]
          if output.startswith(self.syntax['var']) or output.startswith(self.syntax['const']):
            output = str(self.get_value(output))
          self.memory['consts'][temp[0]] = eval(output)
        elif line.startswith(self.syntax['var']):
          temp = line.replace(self.syntax['var'], '', 1).split(' ')
          output = temp[1]
          if output.startswith(self.syntax['var']) or output.startswith(self.syntax['const']):
            output = str(self.get_value(output))
          print(output)
          self.memory['vars'][temp[0]] = eval(output)
        elif line.startswith(self.syntax['print']):
          outpt = ''
          keys = line.replace(self.syntax['print'], '').split(' ')
          for i in keys:
            if i.startswith(self.syntax['var']) or i.startswith(self.syntax['const']):
              outpt += str(self.get_value(i))
            else:
              outpt += i
          print('>', eval(outpt))
        elif line.startswith(self.syntax['erase']):
            vr = line.replace(self.syntax['erase'], '')
            if vr.startswith(self.syntax['const']):
                self.remove_var('consts', vr.replace(self.syntax['const'], ''))
            elif vr.startswith(self.syntax['var']):
                self.remove_var('vars', vr.replace(self.syntax['var'], ''))

if __name__ == '__main__':
  inter = Interpreter('a.fl')
  inter.interpret()