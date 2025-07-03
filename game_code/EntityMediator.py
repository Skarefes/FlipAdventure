from game_code.Enemy import Enemy
from game_code.Entity import Entity


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):  # metodo estatico privado que verifica se passou a janela
        if isinstance(ent, Enemy): # Se passar da tela o inimigo zera a vida
            if ent.rect.right < 0:
                ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):  # metodo que pega a lista de entitys
        for i in range(len(entity_list)):  # intera até o tamanho da lista de entidades
            test_entity = entity_list[i]  # pega cada entidade um de cada vez
            EntityMediator.__verify_collision_window(test_entity)  # chama o outro metodo para verificar a janela

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list: # verificar a lista de entidades
            if ent.health <= 0: # se a vida for menor ou igual a zero
                entity_list.remove(ent) # remove a entidade da lista, e excluindo da tela