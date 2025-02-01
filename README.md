
# 🚀 Desafio: Ordenação da Viagem Temporal

## 📌 Objetivo

Escreva uma função que irá:

- Receber uma lista desordenada de números representando a viagem temporal realizada;
- Reconstruir e ordenar a viagem temporal na sequência correta;
- Os números devem ser tratados no formato de **string** para facilitar a inversão dos dígitos.

---

## 📥 Exemplo de Entrada

```python
["21", "12", "31", "13"]
```

## 📤 Exemplo de Saída Esperada

```python
["12", "21", "13", "31"]
```

---

## 🛠️ Lógica da Solução

1. **Receber a lista de números como strings**: Como os números representam viagens temporais e podem ter os dígitos invertidos, devemos tratá-los como strings.
2. **Normalizar os valores**: Para garantir que números como `"12"` e `"21"` sejam considerados iguais, pegamos o menor valor possível entre o número original e sua versão invertida.
3. **Remover duplicatas**: Convertendo a lista para um conjunto (`set`), eliminamos entradas redundantes.
4. **Ordenar a lista**: Convertendo o conjunto de volta para uma lista e ordenando os valores.

---

## 🔹 Código da Solução

```python
def ordenar_viagem(viagem):
    # Normaliza os valores pegando sempre o menor entre o número e sua inversão
    viagem_normalizada = {min(num, num[::-1]) for num in viagem}
    
    # Retorna a lista ordenada
    return sorted(viagem_normalizada)

# Exemplo de uso
entrada = ["21", "12", "31", "13"]
saida = ordenar_viagem(entrada)
print(saida)  # Saída esperada: ["12", "21", "13", "31"]
```

---

## 🔎 Explicação Passo a Passo

1. **Normalização dos valores**  
   - Pegamos o menor valor entre o número e sua versão invertida com `min(num, num[::-1])`.
   - Exemplo: `"21"` e `"12"` resultam em `"12"`.
   
2. **Removemos duplicatas usando `set`**  
   - Isso garante que `"21"` e `"12"` sejam considerados apenas uma vez.

3. **Ordenamos os valores**  
   - A lista é convertida novamente para **lista ordenada**, garantindo a sequência correta.

---

## 🧪 Testando com Outra Entrada

### Entrada:
```python
["43", "34", "22", "78", "87"]
```

### Saída Esperada:
```python
["22", "34", "43", "78"]
```

> `"34"` e `"43"` são equivalentes, assim como `"78"` e `"87"`.

---

## 🚀 Como Executar o Projeto

### ✅ **Requisitos**

- Python 3.x instalado
- Um editor de texto ou terminal

### ▶️ **Rodando o código**

1. **Clone ou crie o arquivo**  
   - Salve o código acima em um arquivo chamado `viagem_temporal.py`.

2. **Execute no terminal**  
   ```bash
   python viagem_temporal.py
   ```

3. **Confira a saída no terminal**  
   ```bash
   ["12", "21", "13", "31"]
   ```

---

## 💡 Contribuição

Caso tenha sugestões ou melhorias, fique à vontade para contribuir! 🚀

---

Divirta-se com sua viagem temporal! ⏳✨
