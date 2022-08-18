Breve Descrição dos Arquivos

alien_invasion.py

O arquivo principal alien_invasion.py cria vários objetos importantes
usados no jogo: as configurações são armazenadas em ai_settings, a
superfície principal de display é armazenada em screen e uma instância
de ship é criada nesse arquivo. Também em alien_invasion.py está o laço
principal do jogo: um laço while que chama check_events(), ship.update()
e update_screen(). 
alien_invasion.py é o único arquivo que deve ser executado quando
você quiser jogar Invasão Alienígena. Os outros arquivos – settings.py,
game_functions.py, ship.py – contêm códigos que são importados, de
forma direta ou não, nesse arquivo.

settings.py

O arquivo settings.py contém a classe Settings. Essa classe tem apenas
um método __init__(), que inicializa os atributos para controlar a
aparência do jogo e a velocidade da espaçonave.

game_functions.py

O arquivo game_functions.py contém várias funções que executam a
maior parte das tarefas do jogo. A função check_events() detecta eventos
relevantes, como pressionamentos e solturas de teclas, além de
processar cada um desses tipos de evento por meio das funções
auxiliares check_keydown_events() e check_keyup_events(). Por enquanto,
essas funções administram o movimento da espaçonave. O módulo
game_functions também contém update_screen(), que redesenha a tela a
cada passagem pelo laço principal.

ship.py

O arquivo ship.py contém a classe Ship. A classe Ship tem um método
__init__(), um método update() para administrar a posição da
espaçonave e um método blitme() para desenhar a espaçonave na tela. A
imagem propriamente dita da espaçonave está armazenada em ship.bmp,
que está na pasta images.
