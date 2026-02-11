#  Atividade Prática - Teoria dos Conjuntos em Python

**Disciplina:** Lógica e Matemática Discreta (EECP0015)  
**Curso:** Engenharia da Computação - UFMA  
**Professor:** Prof. Rondineli Seba  
**Autor:** Ana Poliana Mesquita de Jesus de Sousa
**Matrícula:** 20250013597 

---

## Descrição da atividade 
Essa atividade tem o objetivo de Aplicar os conceitos de teoria dos conjuntos (união, interseção, diferença, com-
plemento, cardinalidade etc.) em um programa em Python.

## Explicação do Programa

O programa inicia solicitando que o usuário defina seu próprio **conjunto (A)** , digitando entre 4 e 8 elementos, que podem ser números inteiros ou palavras. Com sistema valida se a quantidade de elemntos inserida pelo usuario está correta, remove duplicadas, caso exista e converte strings numéricas para inteiros. Isso evita erros nas operações, pois o Python diferencia, por exemplo, 5 (inteiro) de "5" (string), o que comprometeria a interseção e a diferença entre os conjuntos


Com isso, o programa gera aleatoriamente um segundo **conjunto (B)** , também com 4 a 8 elementos, sorteados de forma aleatória entre Números inteiros (definidos no programa de 1 até 10) e uma lista de palavras.

Por fim, o programa faz as operações  com base na Teoria dos conjuntos e exibe os resultados

União (`A ∪ B`)
Interseção (`A ∩ B`)
Diferença (`A - B` e `B - A`)
Diferença simétrica (`A Δ B`)
Cardinalidade (`|A|`, `|B|`, `|A ∪ B|`)

| Operação | Descrição | Notação |
|----------|-----------|---------|
| **União** | Elementos que estão em A ou em B | `A ∪ B` |
| **Interseção** | Elementos que estão em A e em B | `A ∩ B` |
| **Diferença (A - B)** | Elementos que estão em A mas não em B | `A - B` |
| **Diferença (B - A)** | Elementos que estão em B mas não em A | `B - A` |
| **Diferença Simétrica** | Elementos que estão em A ou B, mas não em ambos | `A Δ B` |
| **Cardinalidade** | Tamanho (quantidade de elementos) de cada conjunto | `\|A\|`, `\|B\|`, `\|A ∪ B\|` |

### Pré-requisitos para exercução

- **Python 3.7+** instalado no seu computador
- **VS Code** 
- **Git** 

### Passo a passo

1. **Clone o repositório:**
   git Clone https://github.com/AnaPolianaMesquita/conjuntosAtv.git
   No terminal, cd conjuntosAtv

2. **Para rodar pelo Vscode:**  
No terminal, 
python3 main.py

## Organização do Código
`obter_conjunto_usuario()` : Entrada e validação do conjunto A
 `gerar_conjunto_aleatorio()` : Geração aleatória do conjunto B
`mostrar_resultados()` ":"Cálculo e exibição das operações

## Exemplo da aplicação


---

```markdown

--------------------------------------------------
CONJUNTO DO USUÁRIO (A)
--------------------------------------------------

Digite números inteiros ou palavras.
Separe os elementos por espaço (exemplo: 5 10 bola asa)

Digite de 4 a 8 elementos: 2 3 5 6 7
(⬆️ Dados inseridos pelo usuário)

--------------------------------------------------
RESULTADOS DAS OPERAÇÕES
--------------------------------------------------

Conjunto A (usuário):  {2, 3, 5, 6, 7}
Conjunto B (aleatório): {'cachorro', 10, 'arvore', 7}

--------------------------------------------------
OPERAÇÕES
--------------------------------------------------

União (A ∪ B):  {2, 3, 5, 6, 7, 10, 'arvore', 'cachorro'}
Interseção (A ∩ B):  {7}
Diferença (A - B):  {2, 3, 5, 6}
Diferença (B - A):  {10, 'arvore', 'cachorro'}
Diferença simétrica (A Δ B):  {2, 3, 5, 6, 10, 'arvore', 'cachorro'}

--------------------------------------------------
CARDINALIDADES
--------------------------------------------------

|A| = 5
|B| = 4
|A ∪ B| = 8

--------------------------------------------------
FIM!
--------------------------------------------------