from peewee import (
    PeeweeException,
    fn,
    MySQLDatabase,
    Model,
    IntegerField,
    DoubleField,
    DateField,
    CharField,
    AutoField,
    DoesNotExist,
)
from datetime import date
import json


db = MySQLDatabase(
    "mi_base_de_datos",
    user="root",
    password="Lautaroromero_021",
    host="localhost",
    port=3306,
)


class UsuariosAutorizados(Model):
    usuario = CharField(unique=True, primary_key=True)
    contraseña = CharField()

    class Meta:
        database = db


class Vendedores(Model):
    usuario = CharField(unique=True, primary_key=True)
    contraseña = CharField()

    class Meta:
        database = db


class Ventas(Model):
    id_venta = IntegerField(unique=True, primary_key=True)
    fecha = DateField()
    producto = CharField()
    cantidad = IntegerField()
    precio_unitario = DoubleField()
    precio_total = DoubleField()
    ingreso_neto = DoubleField()
    tipo_pago = CharField()

    class Meta:
        database = db


class Compras(Model):
    id_compra = IntegerField(unique=True, primary_key=True)
    fecha = DateField()
    empresa = CharField()
    producto = CharField()
    cantidad = IntegerField()
    costo_unitario = DoubleField()
    costo_total = DoubleField()

    class Meta:
        database = db


class Stock(Model):  # no lo normalizo debido al costo computacional
    id_producto = AutoField(primary_key=True, unique=True)
    producto = CharField(unique=True)
    empresa = CharField()
    stock = IntegerField()
    costo_inicial = DoubleField()
    iva = DoubleField()
    descuento_1 = DoubleField(null=True)
    descuento_2 = DoubleField(null=True)
    costo_parcial_1 = DoubleField(null=True)
    costo_parcial_2 = DoubleField(null=True)
    costo_total = DoubleField()
    aumento_efectivo = DoubleField()
    precio_efectivo = DoubleField()
    aumento_mercadolibre = DoubleField()
    precio_mercadolibre = DoubleField()
    aumento_constructores = DoubleField()
    precio_constructores = DoubleField()

    class Meta:
        database = db


class Base:
    def __init__(self):
        try:
            db.connect()
            db.create_tables([Ventas, UsuariosAutorizados, Vendedores, Compras, Stock])
            self.impuestos = self.cargar_impuestos()
            self.ultima_verificacion = None
        except PeeweeException:
            print("Error al conectarse a la base de datos")

    def cargar_impuestos(self):
        try:
            with open("impuestos.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print(
                "El archivo de impuestos no existe. Se creará uno nuevo con valores predeterminados."
            )
            impuestos_default = {
                "mercadolibre": 13,
                "posnet": 7,
                "efectivo": 0,
                "constructores": 0,
            }
            with open("impuestos.json", "w") as file:
                json.dump(impuestos_default, file)
            return impuestos_default

    def guardar_impuestos(self):
        with open("impuestos.json", "w") as file:
            json.dump(self.impuestos, file)

    def modificar_impuesto(self, impuesto_a_modificar, nuevo_impuesto):
        try:
            self.impuestos[impuesto_a_modificar] = nuevo_impuesto
            self.guardar_impuestos()
            self.impuestos = self.cargar_impuestos()
        except ValueError:
            print("Error al modificar impuesto en la lista de impuestos")

    def obtener_comision(self, tipo_pago):
        return self.impuestos[tipo_pago]

    #######################   VENTAS    #######################
    def registrar_venta(
        self,
        id_producto,
        cantidad_vendida,
        tipo_pago,
    ):
        try:
            producto_info = self.buscar_informacion_producto(id_producto)
            precio = self.obtener_precio(producto_info, tipo_pago)
            porcentaje_perdido = self.impuestos[tipo_pago]
            if tipo_pago == "constructores":
                tipo_pago = "efectivo"
            Ventas.create(
                id_venta=self.mayor_id_ventas() + 1,
                fecha=date.today(),
                producto=producto_info.producto,
                cantidad=cantidad_vendida,
                precio_unitario=precio,
                precio_total=precio * cantidad_vendida,
                ingreso_neto=round(
                    precio * cantidad_vendida * (1 - porcentaje_perdido / 100), 2
                ),
                tipo_pago=tipo_pago,
            )
            self.restar_stock_producto(id_producto, cantidad_vendida)
        except PeeweeException:
            print("Error al registrar la Ventas en la Base de Datos")

    def modificar_venta(
        self,
        id_a_modificar,
        nueva_fecha,
        nuevo_producto,
        nueva_cantidad,
        nuevo_precio_unitario,
        nuevo_precio_total,
        nuevo_tipo_pago,
    ):
        try:
            porcentaje_perdido = self.impuestos[nuevo_tipo_pago]
            nuevo_ingreso_neto = round(
                nuevo_precio_total * (1 - porcentaje_perdido / 100), 2
            )
            venta_modificada = Ventas.update(
                fecha=nueva_fecha,
                producto=nuevo_producto,
                cantidad=nueva_cantidad,
                precio_unitario=nuevo_precio_unitario,
                precio_total=nuevo_precio_total,
                ingreso_neto=nuevo_ingreso_neto,
                tipo_pago=nuevo_tipo_pago,
            ).where(Ventas.id_venta == id_a_modificar)
            venta_modificada.execute()
        except PeeweeException:
            print("Error al modificar la Ventas en la Base de Datos")

    def consultar_total_vendido(self, fecha_inicial, fecha_final):
        try:
            total_vendido = (
                Ventas.select(fn.Sum(Ventas.ingreso_neto))
                .where((Ventas.fecha >= fecha_inicial) & (Ventas.fecha <= fecha_final))
                .scalar()
                or 0
            )
            return total_vendido
        except PeeweeException:
            print("Error al consultar el total vendido en la Base de Datos")
            return None

    def consultar_total_vendido_segun_tipo_pago(
        self, fecha_inicial, fecha_final, tipo_pago
    ):
        try:
            total_vendido = (
                Ventas.select(fn.Sum(Ventas.ingreso_neto))
                .where(
                    (Ventas.fecha >= fecha_inicial)
                    & (Ventas.fecha <= fecha_final)
                    & (Ventas.tipo_pago == tipo_pago)
                )
                .scalar()
                or 0
            )
            return total_vendido
        except PeeweeException:
            print("Error al consultar el total vendido en la Base de Datos")
            return None

    def eliminar_venta(self, id_a_eliminar):
        try:
            venta_a_eliminar = Ventas.get(Ventas.id_venta == id_a_eliminar)
            venta_a_eliminar.delete_instance()
        except PeeweeException:
            print("Error al eliminar la venta de la Base de Datos")

    def obtener_ventas_ordenadas(self):
        return Ventas.select().order_by(Ventas.fecha.desc(), Ventas.id_venta.desc())

    def obtener_ventas_segun_tipo_pago(self, tipo_pago):
        return (
            Ventas.select()
            .where(Ventas.tipo_pago == tipo_pago)
            .order_by(Ventas.fecha.desc(), Ventas.id_venta.desc())
        )

    def mayor_id_ventas(self):
        try:
            max_id = Ventas.select(fn.Max(Ventas.id_venta)).scalar() or 0
            return max_id
        except PeeweeException:
            print("Error al obtener el mayor ID de ventas de la Base de Datos")
            return None

    def obtener_datos_venta(self, id):
        try:
            return Ventas.get(Ventas.id_venta == id)
        except DoesNotExist:
            print("No existe la venta con el id indicado")

    def stock_suficiente(self, id_producto, cantidad_a_vender):
        producto_info = self.buscar_informacion_producto(id_producto)
        return producto_info.stock >= cantidad_a_vender

    #######################   COMPRAS    #######################
    def registrar_compra(self, fecha, id_producto, cantidad_comprada):
        try:
            producto_info = self.buscar_informacion_producto(id_producto)
            costo_unitario = producto_info.costo_total
            Compras.create(
                id_compra=self.mayor_id_compra() + 1,
                fecha=fecha,
                empresa=producto_info.empresa,
                producto=producto_info.producto,
                cantidad=cantidad_comprada,
                costo_unitario=costo_unitario,
                costo_total=cantidad_comprada * costo_unitario,
            )
            self.aumentar_stock_producto(id_producto, cantidad_comprada)
        except PeeweeException:
            print("Error al registrar la compra en la Base de Datos")

    def modificar_compra(
        self,
        id_a_modificar,
        nueva_fecha,
        nuevo_producto,
        nueva_cantidad,
        nuevo_costo_unitario,
        nuevo_costo_total,
    ):
        try:
            compra_modificada = Compras.update(
                fecha=nueva_fecha,
                producto=nuevo_producto,
                cantidad=nueva_cantidad,
                costo_unitario=nuevo_costo_unitario,
                costo_total=nuevo_costo_total,
            ).where(Compras.id_compra == id_a_modificar)
            compra_modificada.execute()
        except PeeweeException:
            print("Error al modificar la Ventas en la Base de Datos")

    def obtener_compras_ordenadas(self):
        return Compras.select().order_by(Compras.fecha.desc(), Compras.id_compra.desc())

    def obtener_compras_segun_empresa(self, empresa):
        return (
            Compras.select()
            .where(Compras.empresa == empresa)
            .order_by(Compras.fecha.desc(), Compras.id_compra.desc())
        )

    def consultar_total_gastado(self, fecha_inicial, fecha_final):
        try:
            total_gastado = (
                Compras.select(fn.Sum(Compras.costo_total))
                .where(
                    (Compras.fecha >= fecha_inicial) & (Compras.fecha <= fecha_final)
                )
                .scalar()
                or 0
            )
            return total_gastado
        except PeeweeException:
            print("Error al consultar el total gastado en la Base de Datos")
            return None

    def consultar_total_gastado_segun_empresa(
        self, fecha_inicial, fecha_final, empresa
    ):
        try:
            total_gastado = (
                Compras.select(fn.Sum(Compras.costo_total))
                .where(
                    (Compras.fecha >= fecha_inicial)
                    & (Compras.fecha <= fecha_final)
                    & (Compras.empresa == empresa)
                )
                .scalar()
                or 0
            )
            return total_gastado
        except PeeweeException:
            print("Error al consultar el total gastado en la Base de Datos")
            return None

    def eliminar_compra(self, id_a_eliminar):
        try:
            compra_a_eliminar = Compras.get(Compras.id_compra == id_a_eliminar)
            compra_a_eliminar.delete_instance()
        except PeeweeException:
            print("Error al eliminar la compra de la Base de Datos")

    def mayor_id_compra(self):
        try:
            max_id = Compras.select(fn.Max(Compras.id_compra)).scalar() or 0
            return max_id
        except PeeweeException:
            print("Error al obtener el mayor ID de compras de la Base de Datos")
            return None

    def obtener_datos_compra(self, id):
        try:
            return Compras.get(Compras.id_compra == id)
        except DoesNotExist:
            print("No existe la compra con el id indicado")

    ##################   USUARIOS    ####################
    def agregar_usuario_autorizado(self, nuevo_usuario, nueva_contraseña):
        UsuariosAutorizados.create(usuario=nuevo_usuario, contraseña=nueva_contraseña)

    def eliminar_usuario_autorizado(self, usuario):
        try:
            usuario_a_eliminar = UsuariosAutorizados.get(
                UsuariosAutorizados.usuario == usuario
            )
            usuario_a_eliminar.delete_instance()
        except DoesNotExist:
            print("Usuario no encontrado")
        except PeeweeException:
            print("Error al agregar usuario autorizado")

    def obtener_usuarios_autorizados_ordenados(self):
        return UsuariosAutorizados.select().order_by(UsuariosAutorizados.usuario)

    def usuario_autorizado_existe(self, usuario, contraseña):
        try:
            usuario_autorizado = UsuariosAutorizados.get(
                (UsuariosAutorizados.usuario == usuario)
                & (UsuariosAutorizados.contraseña == contraseña)
            )
            return (
                usuario_autorizado.usuario == usuario
                and usuario_autorizado.contraseña == contraseña
            )
        except DoesNotExist:
            return False
        except PeeweeException:
            print("Error al buscar usuario autorizado")
            return None

    def usuario_autorizado_ya_cargado(self, usuario):
        try:
            UsuariosAutorizados.get((UsuariosAutorizados.usuario == usuario))
            return True
        except DoesNotExist:
            return False
        except PeeweeException:
            return True

    def agregar_vendedor(self, nuevo_usuario, nueva_contraseña):
        Vendedores.create(usuario=nuevo_usuario, contraseña=nueva_contraseña)

    def eliminar_vendedor(self, usuario):
        try:
            vendedor_a_eliminar = Vendedores.get(Vendedores.usuario == usuario)
            vendedor_a_eliminar.delete_instance()
        except DoesNotExist:
            print("Vendedor no encontrado")
        except PeeweeException:
            print("Error al eliminar vendedor")

    def obtener_vendedores_ordenados(self):
        return Vendedores.select().order_by(Vendedores.usuario)

    def vendedor_existe(self, usuario, contraseña):
        try:
            vendedor = Vendedores.get(
                (Vendedores.usuario == usuario) & (Vendedores.contraseña == contraseña)
            )
            return vendedor.usuario == usuario and vendedor.contraseña == contraseña
        except DoesNotExist:
            return False
        except PeeweeException:
            print("Error al buscar vendedor")
            return None

    def vendedor_ya_cargado(self, usuario):
        try:
            Vendedores.get((Vendedores.usuario == usuario))
            return True
        except DoesNotExist:
            return False
        except PeeweeException:
            return True

    ##############   STOCK   #################
    def agregar_producto_a_stock(
        self,
        producto,
        empresa,
        stock,
        costo_inicial,
        iva=10.5,
        descuento_1=None,
        descuento_2=None,
        aumento_efectivo=0,
        aumento_mercadolibre=0,
        aumento_constructores=0,
    ):
        try:
            costos_producto = self.calcular_costos(
                empresa,
                costo_inicial,
                iva,
                descuento_1,
                descuento_2,
            )
            precio_efectivo = round(
                costos_producto["costo_total"] * (1 + (aumento_efectivo / 100)), 2
            )
            precio_mercadolibre = round(
                costos_producto["costo_total"] * (1 + (aumento_mercadolibre / 100)), 2
            )
            precio_constructores = round(
                costos_producto["costo_total"] * (1 + (aumento_constructores / 100)), 2
            )
            Stock.create(
                producto=producto,
                empresa=empresa,
                stock=stock,
                costo_inicial=costo_inicial,
                iva=iva,
                descuento_1=descuento_1,
                descuento_2=descuento_2,
                costo_parcial_1=costos_producto["costo_parcial_1"],
                costo_parcial_2=costos_producto["costo_parcial_2"],
                costo_total=costos_producto["costo_total"],
                aumento_efectivo=aumento_efectivo,
                precio_efectivo=precio_efectivo,
                aumento_mercadolibre=aumento_mercadolibre,
                precio_mercadolibre=precio_mercadolibre,
                aumento_constructores=aumento_constructores,
                precio_constructores=precio_constructores,
            )
        except PeeweeException:
            print("Error al registrar el producto en el stock")

    def buscar_informacion_producto(self, id_producto):
        try:
            producto_info = Stock.select().where(Stock.id_producto == id_producto).get()
            return producto_info  # Devuelve la fila del producto encontrado
        except DoesNotExist:
            return None  # Si no se encuentra el producto en ningún stock

    def obtener_precio(self, producto_info, tipo_pago):
        if tipo_pago == "mercadolibre":
            return producto_info.precio_mercadolibre
        elif tipo_pago == "posnet":
            return producto_info.precio_mercadolibre
        elif tipo_pago == "efectivo":
            return producto_info.precio_efectivo
        elif tipo_pago == "constructor":
            return producto_info.precio_constructores

    def eliminar_producto(self, id_producto):
        try:
            producto = Stock.get(Stock.id_producto == id_producto)
            producto.delete_instance()
        except PeeweeException:
            print("Error al eliminar el producto:")

    def aumentar_stock_producto(self, id_producto, cantidad):
        try:
            producto_info = self.buscar_informacion_producto(id_producto)
            nuevo_stock = producto_info.stock + cantidad
            actualizacion = Stock.update(stock=nuevo_stock).where(
                Stock.id_producto == id_producto
            )
            actualizacion.execute()
        except DoesNotExist:
            print("El producto no existe")
        except Exception:
            print("Error al aumentar el stock:")

    def restar_stock_producto(self, id_producto, cantidad):
        try:
            producto_info = self.buscar_informacion_producto(id_producto)
            nuevo_stock = producto_info.stock - cantidad
            actualizacion = Stock.update(stock=nuevo_stock).where(
                Stock.id_producto == id_producto
            )
            actualizacion.execute()
        except DoesNotExist:
            print("El producto no existe")
        except Exception:
            print("Error al aumentar el stock:")

    def producto_repetido_en_stock(self, producto):
        try:
            Stock.get(Stock.producto == producto)
            return True  # Si encuentra el producto en alguna tabla, devuelve True
        except DoesNotExist:
            return False

    def obtener_productos_para_compra(self):
        try:
            productos = Stock.select(
                Stock.id_producto,
                Stock.producto,
                Stock.empresa,
                Stock.stock,
                Stock.costo_total,
            ).order_by(Stock.producto)
            return productos  # Devuelve el resultado de la consulta
        except PeeweeException:
            print("Error al obtener productos para compra")
            return None

    def obtener_productos_para_venta(self):
        try:
            productos = Stock.select(
                Stock.id_producto,
                Stock.producto,
                Stock.stock,
                Stock.precio_efectivo,
                Stock.precio_mercadolibre,
                Stock.precio_constructores,
            ).order_by(Stock.producto)
            return productos  # Devuelve el resultado de la consulta
        except PeeweeException:
            print("Error al obtener productos para venta")
            return None

    def obtener_productos_filtrados(self, empresa):
        try:
            productos_filtrados = (
                Stock.select().where(Stock.empresa == empresa).order_by(Stock.producto)
            )
            return productos_filtrados  # Devuelve el resultado de la consulta
        except PeeweeException:
            print("Error al obtener productos filtrados")
            return None

    def modificar_producto_de_stock(
        self,
        id_producto_a_modificar,
        nuevo_producto,
        nuevo_stock,
        nuevo_costo_inicial,
        nuevo_iva=10.5,
        nuevo_descuento_1=None,
        nuevo_descuento_2=None,
        nuevo_aumento_efectivo=0,
        nuevo_aumento_mercadolibre=0,
        nuevo_aumento_constructores=0,
    ):
        try:
            producto_a_modificar_info = self.buscar_informacion_producto(
                id_producto_a_modificar
            )
            costos_producto = self.calcular_costos(
                producto_a_modificar_info.empresa,
                nuevo_costo_inicial,
                nuevo_iva,
                nuevo_descuento_1,
                nuevo_descuento_2,
            )

            precio_efectivo = round(
                costos_producto["costo_total"] * (1 + (nuevo_aumento_efectivo / 100)),
                2,
            )
            precio_mercadolibre = round(
                costos_producto["costo_total"]
                * (1 + (nuevo_aumento_mercadolibre / 100)),
                2,
            )
            precio_constructores = round(
                costos_producto["costo_total"]
                * (1 + (nuevo_aumento_constructores / 100)),
                2,
            )

            producto_en_stock = Stock.update(
                producto=nuevo_producto,
                stock=nuevo_stock,
                costo_inicial=nuevo_costo_inicial,
                iva=nuevo_iva,
                descuento_1=nuevo_descuento_1,
                descuento_2=nuevo_descuento_2,
                costo_parcial_1=costos_producto["costo_parcial_1"],
                costo_parcial_2=costos_producto["costo_parcial_2"],
                costo_total=costos_producto["costo_total"],
                aumento_efectivo=nuevo_aumento_efectivo,
                precio_efectivo=precio_efectivo,
                aumento_mercadolibre=nuevo_aumento_mercadolibre,
                precio_mercadolibre=precio_mercadolibre,
                aumento_constructores=nuevo_aumento_constructores,
                precio_constructores=precio_constructores,
            ).where(Stock.id_producto == id_producto_a_modificar)
            producto_en_stock.execute()
        except PeeweeException:
            print("Error al modificar el producto en stock")

    def aumentar_costo_inicial_general(self, empresa, porcentaje):
        try:
            productos = self.obtener_productos_filtrados(empresa)
            for producto in productos:
                producto_info = self.buscar_informacion_producto(producto)
                nuevo_costo_inicial = round(
                    producto.costo_inicial * (1 + porcentaje / 100), 2
                )
                costos = self.calcular_costos(
                    producto_info.empresa,
                    nuevo_costo_inicial,
                    producto_info.iva,
                    producto_info.descuento_1,
                    producto_info.descuento_2,
                )
                producto.costo_inicial = nuevo_costo_inicial
                producto.costo_parcial_1 = costos["costo_parcial_1"]
                producto.costo_parcial_2 = costos["costo_parcial_2"]
                producto.costo_total = costos["costo_total"]
                producto.precio_efectivo = round(
                    costos["costo_total"] * (1 + (producto.aumento_efectivo / 100)), 2
                )
                producto.precio_mercadolibre = round(
                    costos["costo_total"] * (1 + (producto.aumento_mercadolibre / 100)),
                    2,
                )
                producto.precio_constructores = round(
                    costos["costo_total"]
                    * (1 + (producto.aumento_constructores / 100)),
                    2,
                )
                producto.save()  # Guardar el cambio en el costo inicial y los valores dependientes
        except PeeweeException:
            print("Error al aumentar el costo inicial")

    def modificar_productos_gral(self, empresa, columna, nuevo_valor):
        try:
            productos = self.obtener_productos_filtrados(empresa)
            for producto in productos:
                setattr(producto, columna, nuevo_valor)

                nuevos_costos = self.calcular_costos(
                    producto.empresa,
                    producto.costo_inicial,
                    producto.iva,
                    producto.descuento_1,
                    producto.descuento_2,
                )
                nuevos_precios = self.calcular_precios(
                    nuevos_costos["costo_total"],
                    producto.aumento_efectivo,
                    producto.aumento_mercadolibre,
                    producto.aumento_constructores,
                )
                producto.costo_parcial_1 = nuevos_costos["costo_parcial_1"]
                producto.costo_parcial_2 = nuevos_costos["costo_parcial_2"]
                producto.costo_total = nuevos_costos["costo_total"]
                producto.precio_efectivo = nuevos_precios["precio_efectivo"]
                producto.precio_mercadolibre = nuevos_precios["precio_mercadolibre"]
                producto.precio_constructores = nuevos_precios["precio_constructores"]
                producto.save()
        except PeeweeException:
            print("error al modificar columna general")

    def calcular_costos(
        self, empresa, costo_inicial, iva=10.5, descuento_1=None, descuento_2=None
    ):
        costos = {}
        if empresa == "cregar":
            costos["costo_parcial_1"] = round(
                costo_inicial * (1 - descuento_1 / 100), 2
            )
            costos["costo_parcial_2"] = round(
                costos["costo_parcial_1"] * (1 + iva / 100), 2
            )
            costos["costo_total"] = round(
                costos["costo_parcial_2"] * (1 - descuento_2 / 100), 2
            )
        if empresa == "fara":
            costos["costo_parcial_1"] = round(
                costo_inicial * (1 - descuento_1 / 100), 2
            )
            costos["costo_parcial_2"] = round(
                costos["costo_parcial_1"] * (1 - descuento_2 / 100), 2
            )
            costos["costo_total"] = round(
                costos["costo_parcial_2"] * (1 + iva / 100), 2
            )
        if empresa == "fontana":
            costos["costo_parcial_1"] = None
            costos["costo_parcial_2"] = None
            costos["costo_total"] = round(costo_inicial * (1 + iva / 100), 2)
        return costos

    def calcular_precios(
        self,
        costo_total,
        aumento_efectivo,
        precio_mercadolibre,
        precio_constructores,
    ):
        precios = {}
        precios["precio_efectivo"] = round(
            costo_total * (1 + aumento_efectivo / 100), 2
        )
        precios["precio_mercadolibre"] = round(
            costo_total * (1 + precio_mercadolibre / 100), 2
        )
        precios["precio_constructores"] = round(
            costo_total * (1 + precio_constructores / 100), 2
        )
        return precios

    #################   GANANCIAS   #################
    def consultar_ganancias_totales(self, fecha_inicial, fecha_final):
        try:
            total_ganado = (
                Ventas.select(fn.Sum(Ventas.ingreso_neto))
                .where((Ventas.fecha >= fecha_inicial) & (Ventas.fecha <= fecha_final))
                .scalar()
                or 0
            )
            return total_ganado
        except PeeweeException:
            print("Error al consultar el total ganado en la Base de Datos")
            return None

    def consultar_ganancias_segun_tipo_pago(
        self, fecha_inicial, fecha_final, tipo_pago
    ):
        try:
            total_ganado = (
                Ventas.select(fn.Sum(Ventas.ingreso_neto))
                .where(
                    (Ventas.fecha >= fecha_inicial)
                    & (Ventas.fecha <= fecha_final)
                    & (Ventas.tipo_pago == tipo_pago)
                )
                .scalar()
                or 0
            )
            return total_ganado
        except PeeweeException:
            print(
                f"Error al consultar el total ganado en {tipo_pago} en la Base de Datos"
            )
            return None


if __name__ == "__main__":
    base_datos = Base()
