# Jogo do Peixinho + Arduino
## Introdução e Objetivo
Este projeto apresenta um software destinado a auxiliar pacientes com dificuldades motoras a interagir com computadores e outros dispositivos eletrônicos. Inspirado no jogo do dinossauro do Google Chrome, o programa capta sinais de contrações musculares por meio de um Arduino e um sensor de eletromiografia (EMG). Os dados coletados são enviados e processados pelo software, transformando as contrações musculares em ações e mecânicas dentro do jogo.

A mecânica do jogo foi recriada no ambiente Python, mantendo a essência do jogo original do dinossauro, com modificações apenas nos personagens e nos recursos visuais. O jogador, conectado a sensores musculares, controla o personagem para pular e desviar dos obstáculos através de contrações musculares voluntárias. O software é capaz de diferenciar entre contrações voluntárias, movimentos comuns e espasmos musculares menores.

Tela de Configuração
Ao iniciar o programa, uma tela de pré-configuração é apresentada, permitindo ao usuário definir informações sobre o paciente, o jogo e a conexão com o Arduino. A interface foi projetada para acomodar a diversidade de pacientes que podem usar o software, permitindo ajustes personalizados conforme as necessidades específicas de cada um.

## Funcionalidades Técnicas
Utilizando a biblioteca Tkinter do Python, foi desenvolvida uma interface intuitiva que auxilia o usuário na configuração do jogo e na descrição do paciente. A janela de configuração inclui os seguintes campos de entrada:

- Paciente: Nome, idade e comorbidades.
- Jogo: Tempo, dificuldade e nível de força.
- Arduino: Porta de conexão e frequência.

Valores padrão são fornecidos para todas as informações obrigatórias.
Alguns campos, como frequência e porta de conexão, apresentam listas de opções pré-definidas para facilitar a escolha pelo usuário.

Após realizar as configurações desejadas, o usuário pode clicar em "Jogar" para iniciar o jogo com as definições selecionadas. É importante que o Arduino e os sensores estejam configurados corretamente para garantir a precisão do sinal e um bom desempenho no jogo.

### Exemplo:
![Interface](imagens/exemplo.png)

## Bibliotecas Utilizadas
O desenvolvimento do software utilizou diversas bibliotecas para implementar a interface gráfica, a lógica do jogo e a comunicação com o hardware. As principais bibliotecas empregadas foram:

- Pygame: Utilizada para recriar a mecânica do jogo e gerenciar gráficos, sons e eventos.
- Sys: Oferece acesso a funcionalidades específicas do sistema, como a saída do programa.
- Os: Usada para interações com o sistema operacional, como manipulação de arquivos e diretórios.
- Random: Utilizada para gerar valores aleatórios, essencial para a criação de obstáculos no jogo.
- Serial: Responsável pela comunicação serial com o Arduino, permitindo a leitura dos sinais de eletromiografia.
- Threading: Implementa o gerenciamento de threads para operações paralelas, garantindo uma resposta mais ágil do software.
- Matplotlib.pyplot: Utilizada para a criação de gráficos que representam o desempenho do paciente durante o jogo.

Essas bibliotecas foram escolhidas por sua eficiência e facilidade de integração, contribuindo para um desenvolvimento mais ágil e um desempenho robusto do software.

## Resultados e Análise
Ao final do tempo de jogo, uma lista com todas as informações do usuário e seu desempenho é apresentada. Esta lista, acompanhada de representações gráficas, destaca os valores mais altos de força que o paciente conseguiu atingir. A partir desses dados, é possível obter uma boa indicação sobre a capacidade motora do paciente. Este jogo representa um passo significativo no desenvolvimento de um modelo mais abrangente de interação homem-máquina.