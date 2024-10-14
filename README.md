# Pong Game in Python

Este é um simples jogo de Pong desenvolvido em Python, utilizando a biblioteca Pygame para manipulação de gráficos e sons, e OpenGL para renderização 2D.

## Descrição

O jogo permite que dois jogadores controlem raquetes verticais para rebater uma bola que se move na tela. O objetivo é evitar que a bola passe pela raquete do jogador. O jogo inclui efeitos sonoros para a interação e uma música de fundo.

## Requisitos

- Python 3.x
- Pygame
- PyOpenGL

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu_usuario/pong.git
   cd pong

   ```

2. Instale as Dependências:

   ```bash
   pip install pygame PyOpenGL

   ```

3. Baixe ou crie os arquivos de som que são utilizados no jogo. Certifique-se de que eles estejam na pasta Pong.py/Sounds/.
## Estrutura do Projeto

 ```bash
 /pong
├── Pong.py
└── Sounds
    ├── EFEITOS SONOROS-1.wav
    ├── EFEITOS SONOROS-2.wav
    ├── EFEITOS SONOROS-3.wav
    ├── EFEITOS SONOROS-4.wav
    ├── EFEITOS SONOROS-5.wav
    └── spell1_0.wav
 ```
## Controles

**Jogador 1:**

- `W` - mover para cima
- `S` - mover para baixo

**Jogador 2:**

- `Seta para Cima` - mover para cima
- `Seta para Baixo` - mover para baixo

## Funcionalidades

- Efeitos sonoros para as interações (rebater a bola, marcar pontos).
- A música de fundo toca durante o jogo.
- A bola acelera após ser rebatida.
- A posição das raquetes é limitada para não sair da tela.

## Contribuição

Sinta-se à vontade para contribuir com melhorias e correções. Faça um fork do repositório e envie suas mudanças através de pull requests.

## Contribuidores

- [Jean Lima](https://github.com/jeanlima2112) - Desenvolvedor do jogo Pong.



## Licença

Este projeto está licenciado sob a Licença MIT.


