from game_code.Enemy import Enemy
from game_code.Entity import Entity
from game_code.Player import Player


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):  # metodo estatico privado que verifica se passou a janela
        if isinstance(ent, Enemy):  # Se passar da tela o inimigo zera a vida
            if ent.rect.right < 0:
                ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):  # metodo que pega a lista de entitys
        for i in range(len(entity_list)):  # intera até o tamanho da lista de entidades
            entity1 = entity_list[i]  # pega cada entidade um de cada vez
            EntityMediator.__verify_collision_window(entity1)  # chama o outro metodo para verificar a janela
            for j in range(i + 1,
                           len(entity_list)):  # Voce pega uma entidade e compara com todas as outras entidades, e para que não tenha redundancia para não pegar o mesmo, some + 1
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        # Valida se for verdadeiro a colisão do player com o inimigo
        valid_interaction = isinstance(ent1, Player) and isinstance(ent2, Enemy) or \
                    isinstance(ent2, Player) and isinstance(ent1, Enemy)
        if valid_interaction:  # Se a borda direita estiver maior ou igual a esquerda, no caso a borda direita do ent1 vai ficar a esquerda do ent2 e assim por diante
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage  # a vida da entidade 1 vai diminuir com o dano da entidade 2
                ent2.health -= ent1.damage

    @staticmethod
    def give_score(entity_list: list[Entity]): # Para cada Player que for do tipo Player, dentro da lista entity, vai ser filtrado e caso o inimigo passe, conta um ponto
        for ent in entity_list:
            if isinstance(ent, Enemy): # Se for uma entidade do tipo inimigo
                for player in filter (lambda e: isinstance(e, Player), entity_list): # Este for ignora tudo que não é o player
                    # Se caso o inimigo passou o player ele conta um ponto
                    if not ent.passed_player[player.name] and ent.rect.right < player.rect.left: # verifica se o inimigo ainda não contou ponto e se ja passou pelo lado esquerdo do jogador
                        player.score += 1
                        ent.passed_player[player.name] = True # Marcar um ponto apenas, para cada jogador


    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:  # verificar a lista de entidades
            if ent.health <= 0:  # se a vida for menor ou igual a zero
                entity_list.remove(ent)  # remove a entidade da lista, e excluindo da tela
