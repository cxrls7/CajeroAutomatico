## Simulador de Cajero Automático 
Este proyecto consiste en un programa de consola que simula las operaciones fundamentales de un cajero automático (ATM). El objetivo principal es gestionar un saldo inicial fijo y procesar un número determinado de transacciones mediante validaciones lógicas.

---

## 📋 Reglas del Sistema
El simulador opera bajo una estructura de flujo de control definida por las siguientes reglas:

## ⚙️ Configuración Inicial
Saldo Inicial: El sistema arranca con un fondo predefinido de $1000.

Contador de Operaciones: El usuario define al inicio cuántas transacciones desea realizar antes de que el programa finalice.

---

## 🕹️ Funcionalidades del Menú
El sistema presenta tres opciones principales por cada ciclo de operación:

Consultar Saldo: Muestra el estado actual de la cuenta.

Retirar Dinero: * Verifica que el monto sea positivo (reintento obligatorio en caso de números negativos).

Valida si existen fondos suficientes para completar la transacción.

Depositar Dinero: * Permite incrementar el saldo tras validar que el monto a depositar sea mayor a cero.

---

## 🛠️ Lógica de Validación
Para garantizar la robustez del programa, se han implementado las siguientes protecciones:

Validación de Entradas: Si se selecciona una opción fuera del rango (1-3), el sistema notifica "Opción inválida".

Persistencia de Errores: En los depósitos y retiros, el sistema no permite avanzar hasta que se ingrese un monto válido (no negativo).

Cierre Seguro: Una vez cumplido el número de operaciones solicitadas, el programa se despide formalmente.

---

## 🚀 Conceptos de Programación Aplicados
Variables y Tipos de Datos: Manejo de saldos flotantes/enteros.

Estructuras Iterativas: Uso de bucles (for o while) para repetir las operaciones.

Estructuras Condicionales: Implementación de if/else o switch para la toma de decisiones.

Validación de Datos: Bucles de control para asegurar entradas de usuario correctas.


---


## Author: Carlos Daniel Molina
