class MercadoFacil:
    def __init__(self, nombre_usuario):
        self.nombre_usuario = nombre_usuario
        self.saldo_principal = 150.00  # Saldo inicial de ejemplo en soles (S/.)
        self.saldo_ahorro = 50.00     # Ahorro inicial
        self.prestamo_activo = 0.00   # Deuda de microcrédito actual
        self.historial_movimientos = []
        self.registrar_movimiento("Saldo inicial asignado", 150.00, "INGRESO")

    def registrar_movimiento(self, descripcion, monto, tipo):
        movimiento = {"descripcion": descripcion, "monto": monto, "tipo": tipo}
        self.historial_movimientos.append(movimiento)
        
        # Simulación de seguridad: Alerta por movimiento inusual (ej. montos mayores a S/. 300)
        if monto > 300.00:
            print(f"\n🚨 [ALERTA DE SEGURIDAD] ¡Atención {self.nombre_usuario}! Se detectó un movimiento inusual de S/. {monto:.2f}. Verifique si usted realizó esta operación.")

    def pagos_digitales(self):
        print("\n--- 📱 PAGOS DIGITALES ---")
        print("1. Enviar dinero")
        print("2. Recibir dinero")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            try:
                monto = float(input("Ingrese el monto a enviar (S/.): "))
                destino = input("Ingrese el número o nombre del destinatario: ")
                if monto <= 0:
                    print("❌ El monto debe ser mayor a cero.")
                elif monto > self.saldo_principal:
                    print("❌ Saldo insuficiente en su cuenta principal.")
                else:
                    self.saldo_principal -= monto
                    self.registrar_movimiento(f"Envío de dinero a {destino}", monto, "GASTO")
                    print(f"✅ ¡Envío exitoso! S/. {monto:.2f} enviados a {destino}.")
            except ValueError:
                print("❌ Ingrese un valor numérico válido.")
                
        elif opcion == "2":
            try:
                monto = float(input("Ingrese el monto a recibir (S/.): "))
                origen = input("Ingrese el nombre del remitente: ")
                if monto <= 0:
                    print("❌ El monto debe ser mayor a cero.")
                else:
                    self.saldo_principal += monto
                    self.registrar_movimiento(f"Recepción de dinero de {origen}", monto, "INGRESO")
                    print(f"✅ ¡Dinero recibido con éxito! S/. {monto:.2f} añadidos a su saldo.")
            except ValueError:
                print("❌ Ingrese un valor numérico válido.")

    def ahorro_digital(self):
        print("\n--- 💰 AHORRO DIGITAL ---")
        print(f"Saldo disponible principal: S/. {self.saldo_principal:.2f}")
        print(f"Saldo en su alcancía de ahorros: S/. {self.saldo_ahorro:.2f}")
        print("1. Guardar dinero en ahorros (para mercadería o emergencias)")
        print("2. Retirar de ahorros")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            try:
                monto = float(input("¿Cuánto desea ahorrar? (S/.): "))
                if monto <= 0:
                    print("❌ El monto debe ser mayor a cero.")
                elif monto > self.saldo_principal:
                    print("❌ No tiene suficiente saldo principal para mover a ahorros.")
                else:
                    self.saldo_principal -= monto
                    self.saldo_ahorro += monto
                    self.registrar_movimiento("Traslado a Ahorros Digitales", monto, "AHORRO")
                    print(f"✅ ¡Guardado con éxito! S/. {monto:.2f} pasaron a su fondo de ahorros.")
            except ValueError:
                print("❌ Ingrese un valor numérico válido.")
                
        elif opcion == "2":
            try:
                monto = float(input("¿Cuánto desea retirar de sus ahorros? (S/.): "))
                if monto <= 0:
                    print("❌ El monto debe ser mayor a cero.")
                elif monto > self.saldo_ahorro:
                    print("❌ No tiene tanto dinero guardado en sus ahorros.")
                else:
                    self.saldo_ahorro -= monto
                    self.saldo_principal += monto
                    self.registrar_movimiento("Retiro de Ahorros Digitales", monto, "RETIRO_AHORRO")
                    print(f"✅ ¡Retiro exitoso! S/. {monto:.2f} regresaron a su saldo principal.")
            except ValueError:
                print("❌ Ingrese un valor numérico válido.")

    def microcreditos(self):
        print("\n--- 🤝 MICROCRÉDITOS ---")
        print(f"Deuda de préstamo actual: S/. {self.prestamo_activo:.2f}")
        print("Reglas: Mínimo S/. 10 y Máximo S/. 500.")
        print("1. Solicitar préstamo")
        print("2. Pagar préstamo")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            if self.prestamo_activo > 0:
                print("⚠️ Ya cuenta con un microcrédito activo. Debe pagarlo antes de solicitar otro.")
                return
            try:
                monto = float(input("Ingrese el monto que desea solicitar (S/. 10 - S/. 500): "))
                if 10.0 <= monto <= 500.0:
                    self.prestamo_activo += monto
                    self.saldo_principal += monto
                    self.registrar_movimiento("Desembolso de Microcrédito", monto, "PRESTAMO")
                    print(f"✅ ¡Préstamo aprobado! S/. {monto:.2f} han sido abonados a su cuenta.")
                else:
                    print("❌ El monto está fuera del rango permitido (Mínimo S/. 10, Máximo S/. 500).")
            except ValueError:
                print("❌ Ingrese un valor numérico válido.")
                
        elif opcion == "2":
            if self.prestamo_activo <= 0:
                print("ℹ️ No tiene deudas de microcrédito pendientes.")
                return
            try:
                print(f"Su deuda total es de S/. {self.prestamo_activo:.2f}")
                monto = float(input("Ingrese cuánto va a abonar o pagar: "))
                if monto <= 0:
                    print("❌ El monto debe ser mayor a cero.")
                elif monto > self.saldo_principal:
                    print("❌ Saldo insuficiente en su cuenta principal para realizar este pago.")
                else:
                    if monto >= self.prestamo_activo:
                        pago_efectivo = self.prestamo_activo
                        self.prestamo_activo = 0.0
                        self.saldo_principal -= pago_efectivo
                        self.registrar_movimiento("Pago total de Microcrédito", pago_efectivo, "PAGO")
                        print("🎉 ¡Felicitaciones! Ha cancelado por completo su microcrédito.")
                    else:
                        self.prestamo_activo -= monto
                        self.saldo_principal -= monto
                        self.registrar_movimiento("Pago parcial de Microcrédito", monto, "PAGO")
                        print(f"✅ Pago registrado. Su deuda restante es de S/. {self.prestamo_activo:.2f}")
            except ValueError:
                print("❌ Ingrese un valor numérico válido.")

    def registro_movimientos(self):
        print("\n--- 📋 REGISTRO DE MOVIMIENTOS ---")
        if not self.historial_movimientos:
            print("No hay movimientos registrados.")
        else:
            print(f"{'N°':<3} | {'Descripción':<35} | {'Tipo':<15} | {'Monto':<10}")
            print("-" * 75)
            for i, mov in enumerate(self.historial_movimientos, 1):
                print(f"{i:<3} | {mov['descripcion']:<35} | {mov['tipo']:<15} | S/. {mov['monto']:<7.2f}")
        print(f"\n💳 Saldo Principal actual: S/. {self.saldo_principal:.2f}")
        print(f"💰 Saldo en Ahorros: S/. {self.saldo_ahorro:.2f}")

    def iniciar_app(self):
        print(f"\n🌟 ¡Bienvenido a Mercado Fácil, {self.nombre_usuario}! 🌟")
        while True:
            print("\n================ MENÚ PRINCIPAL ================")
            print("1. Pagos digitales (Enviar / Recibir)")
            print("2. Ahorro digital (Guardar / Retirar)")
            print("3. Microcréditos (Solicitar / Pagar)")
            print("4. Registro de movimientos y saldos")
            print("5. Salir")
            
            opcion = input("Elige una opción (1-5): ")
            
            if opcion == "1":
                self.pagos_digitales()
            elif opcion == "2":
                self.ahorro_digital()
            elif opcion == "3":
                self.microcreditos()
            elif opcion == "4":
                self.registro_movimientos()
            elif opcion == "5":
                print("\nGracias por usar Mercado Fácil. ¡Hasta pronto!")
                break
            else:
                print("❌ Opción inválida. Intente de nuevo.")

# Ejecución de la aplicación
if __name__ == "__main__":
    app = MercadoFacil("Comerciante de Mercado")
    app.iniciar_app()