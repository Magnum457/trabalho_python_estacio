class Produto:
  def __init__(self, valor : float, nomeItem : str, qtd : int):
    self._valor = valor
    self._nomeItem = nomeItem
    self._qtd = qtd
    
  @property
  def valor(self):
    return self._valor
  
  @property
  def nomeItem(self):
    return self._nomeItem
  
  @property
  def qtd(self):
    return self._qtd
  
  @valor.setter
  def valor(self, novoValor):
    self._valor = novoValor

  @nomeItem.setter
  def nomeItem(self, novoNomeItem):
    self._valor = novoNomeItem
    
  @qtd.setter
  def qtd(self, novoQtd):
    self._qtd = novoQtd

  def calculaImposto(self):
    return self._valor + (self._valor * 0.15)