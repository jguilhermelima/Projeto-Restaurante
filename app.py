from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Melancia', 5.0, 'grande')
bebida_suco.aplicar_desconto()
prato_panzionho = Prato('Paozinho',2.00,'O melhor pão da cidade')
prato_panzionho.aplicar_desconto()
sobremesa_pudim = Sobremesa('Pudim', 7.0, 'doce' ,'medio')
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_panzionho)
restaurante_praca.adicionar_no_cardapio(sobremesa_pudim)


def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()