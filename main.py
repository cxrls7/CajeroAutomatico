import os

def limpiar():
   os.system("cls" if os.name == "nt" else "clear")

while True: 

    print("\n--- CAJERO AUTOMATICO ---")
    print()
   
    saldo_inicial = 1000 
    print("1. Consultar saldo")
    
    print("2. Depositar dinero")
  
    print("3. Retirar dinero")
    
    print("4. Salir")
    print()
    
    opcion= input("- Que operacion quieres realizar: ")
 
    if opcion == "1":
         limpiar()
         print("\n--- MENU DE CONSULTA DE SALDO ---")
         print()
         print("- Tu saldo actual es de", saldo_inicial)
         print()
         input("Presione ENTER para volver al menu...")
         limpiar()
        

    elif opcion == "2":
        limpiar()
        while True:
         print("\n--- MENU DE DEPOSITO DE DINERO ---")
         print()
         print("1. Depositar dinero")
         print()
         print("2. Volver al menu principal")
         print()
         opcion_deposito = input("- Ingrese una opcion: ")
         print()

         if opcion_deposito == "1":
            while True:
               try:
                deposito = float(input("- Cuanto quieres depositar: "))
                saldo_inicial+= deposito
                print()
                print("Depositaste", deposito, "tu saldo actual es de", saldo_inicial)
                break
               except ValueError:
                  print("- Ingresa un valor valido")
                 
                  
         elif opcion_deposito == "2":
            limpiar()
            break
         else:
            print("Opcion invalida")

        
    elif opcion == "3":
        limpiar()
        while True:
         
          print("\n--- MENU DE RETIROS ---")
          print()
          print("1. Retirar dinero")
          print()
          print("2. Volver al menu principal")
          print()
          opcion_retiro = input("- Ingresa una opcion: ")
          print()


          if opcion_retiro == "1":
           while True: 
            try:
             retiro= float(input("- Cuanto quieres retirar: "))
             print()
             if retiro>saldo_inicial:
              print("No tienes saldo suficiente")

             else: 
                saldo_inicial-= retiro
                print("Retiraste", retiro , "tu saldo actual es de", saldo_inicial)
                break
            except:
               print("Ingrese una opcion valida")
              

          elif opcion_retiro== "2":
           limpiar()
           break
          else:
             print("-ERROR Selecciona una opcion valida")
           
            
    if opcion == "4":
           print()
           print("Gracias por usar el cajero automatico")
           break
    


     



