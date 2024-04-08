# Sem type hint

idade = 30
altura = 1.75
nome = "Alice"
is_estudante = True

# No Python não precisa tipar, ela é feita automaticamente por inferência
# Não precisa declarar o tipo da variável

# A vantagem de tipar é que quem lê o código sabe o que era esperado naquela variável

# Com type hint
type_idade: int = 30
type_altura: float = 1.75
type_nome: str = "Alice"
type_is_estudante: bool = True

# Se eu coloco uma str na idade, ele não converte ela para int. Ele é só uma dica, mas da forma que você colocar, ele vai armazenar.
# Pra que serve? Para ajudar o desenvolvedor.
# A tipagem não é estática

# Python tem uma tipagem forte, ou seja, não permite fazer transformações de tipos em tempo de execução

