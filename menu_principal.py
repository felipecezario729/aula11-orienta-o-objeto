
# import runpy


def menu():
    while True: 
         print('\n --Menu de apções')
         print('1- converter metros para centimetros')
         print('2- calcular área do Circulo')
         print('3- calcular a área quadrada')
         print('0 - Sair')

         opcao = input('escolha uma opção') 
         

         if opcao == '1': 
            # runpy.run_path('5.py')
             exec(open('5.py').read())
         elif opcao == '2':   
            # runpy.run_path('6.py')
             exec(open('6.py').read())
         elif opcao == '3':   
            # runpy.run_path('7.py')
             exec(open('7.py').read())
         elif opcao == '0':
              print(' Saindo do programa. Ate Logo !')
              break 
         else:
             print('Opão invalida - Tente novamente')
# iniciar o menu
            
             
if __name__== "__main__":   
    menu()         
