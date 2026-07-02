---

# Gerador de Senhas Aleatórias

Um gerador de senha simples feito em CLI

## 🚀 Escopo V1 (30-06-2026)

O objetivo principal do projeto é permitir que o usuário insira um valor natural $n$ para gerar uma senha com caracteres aleatórios de comprimento $n$.

### 🎯 Objetivos e Regras de Negócio

* **Comprimento da senha:** Mínimo de 8 e máximo de 32 caracteres.
* **Variedade:** Uso de caracteres diferentes (evitando repetições sequenciais).

---

## ✨ Funcionalidades

### ⚙️ Já Implementadas

* **Geração Aleatória:** Criação de senhas únicas com fator de aleatoriedade.
* **Cópia Rápida:** Atalho de teclado para copiar a senha gerada instantaneamente.

### ⏳ Próximas Implementações (Backlog)

* [x] **Validação Sequencial:** Impedir estritamente a repetição de caracteres de forma sequencial (ex: `aa`, `11`).
* [ ] **Histórico Local:** Armazenamento de um histórico de senhas geradas com retenção de até 1 semana

---

## 🛠️ Como Usar

1. Insira o tamanho desejado para a sua senha (entre 8 e 32).
2. Gere a senha.
3. Pressione Enter para copiar a senha gerada automaticamente para a sua área de transferência.

---

