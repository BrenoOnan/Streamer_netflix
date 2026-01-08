#Não é projeto pessoal(de vídeo aula, usado para estudos#

class Netflix:

    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_plano = ['Basic', 'Premium']
        if plano in self.lista_plano:
            self.plano = plano
        else:
            print('Erro!')

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_plano:
            self.plano = novo_plano
            print(f'\nO plano foi alterado para {novo_plano}')
        else:
            print('Erro!')


    def ver_filmes(self):
        catalogo = [
            ['Harry Potter', 'Premium'],
            ['X-Men', 'Premium'],
            ['Senhor dos Anéis', 'Basic'],
            ['Vingadores', 'Premium'],
            ['Matrix', 'Basic'],
            ['Toy Story', 'Basic'],
            ['John Wick', 'Premium'],
            ['Jurassic Park', 'Basic']
        ]

        while True:
            print('-' * 45)
            print("\033[36mCATÁLOGO\033[m".center(45))
            print('-' * 45)
            print(f'{self.nome} | PLANO ATUAL: {self.plano}')
            print('-' * 45)

            for i, (filme, plano_filme) in enumerate(catalogo, start=1):
                print(f'{i}. \033[36m{filme:<25}\033[m | Plano: \033[36m{plano_filme}\033[m')

            print('-' * 45)
            opcao = int(input('Qual filme você deseja assistir? (\033[31m0\033[m para sair): '))


            if opcao == 0:
                print('\nSaindo do catálogo...')
                break

            elif 1 <= opcao <= len(catalogo):
                filme_escolhido, plano_filme = catalogo[opcao - 1]

                if self.plano == plano_filme or plano_filme == 'Basic':
                    print(f"\n🎬 {self.nome} pode assistir: {filme_escolhido}\n")
                    #fazer integração futura e anexar filme #

                else:
                    print(f"⛔ {self.nome} precisa do plano {plano_filme} para ver {filme}")
                    opcao = str(input('Você deseja trocar de plano?[S/N]:')).upper().strip()[0]
                    if opcao == 'S':
                        cliente_netflix.mudar_plano('Premium')
                        print()
                    elif opcao == 'N':
                        return

                    else:
                        print('⛔ Opcao invalida ⛔')

            else:
                print('⛔ Opcao invalida ⛔')
try:
    print('-' * 45)
    print('NETFLIX'.center(45))
    print('-' * 45)
    print('Faça o seu login!')
    cliente_nome = str(input('Digite o nome:')).capitalize()
    cliente_email = str(input('Digite o email:'))

    if not cliente_nome or not cliente_email:
        print("Os campos não podem ser vazio")

    else:
        while True:
            cliente_plano = int(input('PLANO - BASIC [1]\n'
                                      'PLANO - PREMIUM [2]\n'
                                      'Selecione um dos planos : '
            ))

            if not cliente_plano:
                print("Os campos não podem ser vazio")
            else:
                if cliente_plano == 1:
                    plano_escolhido = 'Basic'
                    break
                if cliente_plano == 2:
                    plano_escolhido = 'Premium'
                    break
                else:
                    print('\033[31mErro! Escolha 1 ou 2.\033[0m')

except:
    print('\033[31mErrO!\033[0m')


cliente_netflix = Netflix(cliente_nome, cliente_email, plano_escolhido)
print(f'\n\033[36mSeja bem vindo {cliente_nome}\033[m ')
cliente_netflix.ver_filmes()

