class No:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

class Pilha:
    def __init__(self) -> None:
        self.top = None
        self.size = 0

    def push(self, no):
        no.next = self.top
        self.top = no
        self.size += 1
        print(f"Elemento {no.valor} inserido")

    def pop(self):
        if self.size > 0:
            valor_removido = self.top.valor
            self.top = self.top.next
            self.size -= 1
            return valor_removido
        else:
            return None

    def topo(self):
        if self.top is not None:
            return self.top.valor
        else:
            return None

    def tamanho(self):
        return self.size

    def __str__(self):
        if self.top is not None:
            no = self.top
            pilha_listagem = []
            while no is not None:
                pilha_listagem.append(f"{no.valor}")
                no = no.next
            return "\n-----\n".join(pilha_listagem)
        else:
            return "A pilha está vazia"

def calcular_rpn(expressao):
    pilha = Pilha()
    tokens = expressao.split()

    for token in tokens:
        try:
            numero = float(token)
            pilha.push(No(numero))
        except ValueError:
            # Verifica se há operandos suficientes
            if pilha.tamanho() < 2:
                return "Erro: Expressão inválida (muitos operadores)"

            operando2 = pilha.pop()
            operando1 = pilha.pop()

            if token == '+':
                resultado = operando1 + operando2
            elif token == '-':
                resultado = operando1 - operando2
            elif token == '*':
                resultado = operando1 * operando2
            elif token == '/':
                if operando2 == 0:
                    return "Erro: Divisão por zero"
                resultado = operando1 / operando2
            elif token == '^':
                resultado = operando1 ** operando2
            else:
                return f"Erro: Operador inválido '{token}'"

            pilha.push(No(resultado))

    if pilha.tamanho() == 1:
        return pilha.pop()
    else:
        return "Erro: Expressão inválida (muitos operandos)"

# Exemplos de teste
if __name__ == "__main__":
    expressoes = [
        "2 5 + 5 *",     
        "10 2 / 3 -",    
        "3 4 5 +",     
    ]

    for exp in expressoes:
        print(f"\nExpressão: {exp}")
        resultado = calcular_rpn(exp)
        print(f"Resultado: {resultado}")