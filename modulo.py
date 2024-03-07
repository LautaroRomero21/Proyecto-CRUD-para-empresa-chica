from peewee import (
    PeeweeException,
    fn,
    MySQLDatabase,
    Model,
    IntegerField,
    DoubleField,
    DateField,
    CharField,
    DoesNotExist,
)
from datetime import date

db = MySQLDatabase(
    "mi_base_de_datos",
    user="root",
    password="Lautaroromero_021",
    host="localhost",
    port=3306,
)


class Ventas(Model):
    id_venta = IntegerField(unique=True, primary_key=True)
    fecha = DateField()
    producto = CharField()
    cantidad = IntegerField()
    precio_unitario = DoubleField()
    precio_total = DoubleField()
    tipo_pago = CharField()

    class Meta:
        database = db


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


class Compras(Model):
    id_compra = IntegerField(unique=True, primary_key=True)
    fecha = DateField()
    producto = CharField()
    cantidad = IntegerField()
    costo_unitario = DoubleField()
    costo_total = DoubleField()
    tipo_pago = CharField()

    class Meta:
        database = db


class Stock(Model):
    id = IntegerField(unique=True, primary_key=True)
    producto = CharField(unique=True)
    stock = IntegerField()
    precio_unitario = DoubleField()

    class Meta:
        database = db


class Base:
    def __init__(self):
        try:
            db.connect()
            db.create_tables([Ventas, UsuariosAutorizados, Vendedores, Compras, Stock])
        except PeeweeException:
            print("Error al conectarse a la base de datos")

    def registrar_venta(
        self,
        id_producto,
        cantidad_vendida,
        tipo_pago,
    ):
        try:
            producto = Stock.get(Stock.id == id_producto)
            Ventas.create(
                id_venta=self.mayor_id_ventas() + 1,
                fecha=date.today(),
                producto=producto.producto,
                cantidad=cantidad_vendida,
                precio_unitario=producto.precio_unitario,
                precio_total=producto.precio_unitario * cantidad_vendida,
                tipo_pago=tipo_pago,
            )

            producto_a_actualizar = Stock.update(
                stock=producto.stock - cantidad_vendida,
            ).where(Stock.id == id_producto)
            producto_a_actualizar.execute()
        except PeeweeException:
            print("Error al registrar la Ventas en la Base de Datos")

    def agregar_venta(
        self,
        fecha,
        producto,
        cantidad,
        precio_unitario,
        tipo_pago,
    ):
        try:
            Ventas.create(
                id_venta=self.mayor_id_ventas() + 1,
                fecha=fecha,
                producto=producto,
                cantidad=cantidad,
                precio_unitario=precio_unitario,
                precio_total=cantidad * precio_unitario,
                tipo_pago=tipo_pago,
            )
        except PeeweeException:
            print("Error al agregar la Venta en la Base de Datos")

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
            venta_modificada = Ventas.update(
                fecha=nueva_fecha,
                producto=nuevo_producto,
                cantidad=nueva_cantidad,
                precio_unitario=nuevo_precio_unitario,
                precio_total=nuevo_precio_total,
                tipo_pago=nuevo_tipo_pago,
            ).where(Ventas.id_venta == id_a_modificar)
            venta_modificada.execute()
        except PeeweeException:
            print("Error al modificar la Ventas en la Base de Datos")

    def consultar_total_vendido(self, fecha_inicial, fecha_final):
        try:
            total_vendido = (
                Ventas.select(fn.Sum(Ventas.precio_total))
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
                Ventas.select(fn.Sum(Ventas.precio_total))
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
        return Ventas.select().order_by(Ventas.fecha.desc())

    def obtener_ventas_segun_tipo_pago(self, tipo_pago):
        return (
            Ventas.select()
            .where(Ventas.tipo_pago == tipo_pago)
            .order_by(Ventas.fecha.desc())
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

    def registrar_compra(self, fecha, producto, cantidad, costo_unitario, tipo_pago):
        try:
            Compras.create(
                id_compra=self.mayor_id_compra() + 1,
                fecha=fecha,
                producto=producto,
                cantidad=cantidad,
                costo_unitario=costo_unitario,
                costo_total=cantidad * costo_unitario,
                tipo_pago=tipo_pago,
            )
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
        nuevo_tipo_pago,
    ):
        try:
            compra_modificada = Compras.update(
                fecha=nueva_fecha,
                producto=nuevo_producto,
                cantidad=nueva_cantidad,
                costo_unitario=nuevo_costo_unitario,
                costo_total=nuevo_costo_total,
                tipo_pago=nuevo_tipo_pago,
            ).where(Compras.id_compra == id_a_modificar)
            compra_modificada.execute()
        except PeeweeException:
            print("Error al modificar la Ventas en la Base de Datos")

    def obtener_compras_ordenadas(self):
        return Compras.select().order_by(Compras.fecha.desc())

    def obtener_compras_segun_tipo_pago(self, tipo_pago):
        return (
            Compras.select()
            .where(Compras.tipo_pago == tipo_pago)
            .order_by(Compras.fecha.desc())
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

    def consultar_total_gastado_segun_tipo_pago(
        self, fecha_inicial, fecha_final, tipo_pago
    ):
        try:
            total_gastado = (
                Compras.select(fn.Sum(Compras.costo_total))
                .where(
                    (Compras.fecha >= fecha_inicial)
                    & (Compras.fecha <= fecha_final)
                    & (Compras.tipo_pago == tipo_pago)
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

    def obtener_datos_producto(self, id_producto):
        try:
            producto = Stock.get(Stock.id == id_producto)
            return producto
        except DoesNotExist:
            print(f"El producto con ID {id_producto} no existe.")
            return None

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

    def agregar_producto_a_stock(self, producto, cantidad_inicial, precio_unitario):
        try:
            Stock.create(
                id=self.mayor_id_stock() + 1,
                producto=producto,
                stock=cantidad_inicial,
                precio_unitario=precio_unitario,
            )
        except PeeweeException:
            print("Error al registrar el producto en el stock")

    def modificar_producto_en_stock(
        self,
        id_a_modificar,
        nuevo_producto,
        nueva_cantidad,
        nuevo_precio_unitario,
    ):
        try:
            producto_en_stock = Stock.update(
                producto=nuevo_producto,
                stock=nueva_cantidad,
                precio_unitario=nuevo_precio_unitario,
            ).where(Stock.id == id_a_modificar)
            producto_en_stock.execute()
        except PeeweeException:
            print("Error al modificar el producto en stock")

    def aumentar_stock_producto(self, id_producto, cantidad):
        try:
            producto = Stock.get(Stock.id == id_producto)
            nuevo_stock = producto.stock + cantidad
            producto_a_actualizar = Stock.update(stock=nuevo_stock).where(
                Stock.id == id_producto
            )
            producto_a_actualizar.execute()
        except DoesNotExist:
            print("El producto no existe")
        except Exception:
            print("Error al aumentar el stock")

    def producto_repetido_en_stock(self, nombre_producto):
        try:
            Stock.get(Stock.producto == nombre_producto)
            return True
        except DoesNotExist:
            return False

    def modificar_precio_general_stock(self, porcentaje):
        try:
            productos = Stock.select()
            for producto in productos:
                nuevo_precio = producto.precio_unitario * (1 + porcentaje / 100)
                Stock.update(precio_unitario=round(nuevo_precio, 2)).where(
                    Stock.id == producto.id
                ).execute()
        except PeeweeException:
            print(f"Error al modificar el precio general")

    def obtener_productos_stock(self):
        return Stock.select().order_by(Stock.producto)

    def eliminar_producto_en_stock(self, id_a_eliminar):
        try:
            producto_a_eliminar = Stock.get(Stock.id == id_a_eliminar)
            producto_a_eliminar.delete_instance()
        except PeeweeException:
            print("Error al eliminar el producto del stock")

    def mayor_id_stock(self):
        try:
            max_id = Stock.select(fn.Max(Stock.id)).scalar() or 0
            return max_id
        except PeeweeException:
            print("Error al obtener el mayor ID de prodcutos en stock")
            return None

    def restar_stock_producto(self, id_producto, cantidad_vendida):
        try:
            producto = Stock.get(Stock.id == id_producto)
            producto.cantidad -= cantidad_vendida
            producto.save()
        except Stock.DoesNotExist:
            print(f"Producto con ID {id_producto} no encontrado en el stock.")
        except PeeweeException:
            print("Error al restar la cantidad vendida al stock del producto")

    def consultar_ganancias_totales(self, fecha_inicial, fecha_final):
        try:
            total_ganado = (
                Ventas.select(fn.Sum(Ventas.precio_total))
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
                Ventas.select(fn.Sum(Ventas.precio_total))
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


base_datos = Base()

# if __name__ == "__main__":
