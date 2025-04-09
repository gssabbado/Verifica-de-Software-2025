from cadastro import Cadastro

def verificar_cadastro(Cadastro):
    categorias = ["infantil", "juvenil", "adulto"]
    
    if Cadastro.idade < 10 or Cadastro.idade > 60:
        return False
    
    if Cadastro.categoria not in categorias:
        return False

    if Cadastro.tempoEstimado < 30 or Cadastro.tempoEstimado > 180:
        return False

    if not Cadastro.assinaturaTermo:
        return False
    
    if Cadastro.categoria == "infantil" and (Cadastro.idade < 10 or Cadastro.idade > 14):
        return False

    if Cadastro.categoria == "juvenil" and (Cadastro.idade < 15 or Cadastro.idade > 17):
        return False 

    if Cadastro.categoria == "adulto" and (Cadastro.idade < 18 or Cadastro.idade > 60):
        return False
    
    return True