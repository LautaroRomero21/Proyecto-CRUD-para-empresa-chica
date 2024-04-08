from PyQt5 import QtWidgets, QtCore, QtGui
from datetime import date
from ventanas.bienvenida import Ui_UserSelection
from ventanas.login import Ui_Form
from ventanas.ventana_principal_autorizada import Ui_VentanaPrincipalAutorizada
from ventanas.registrar_ventas_vendedor import Ui_RegistrarVentaVendedor
from ventanas.registrar_ventas_autorizado import Ui_RegistrarVentasAutorizado
from ventanas.usuarios import Ui_Usuarios
from ventanas.elegir_empresa import Ui_ElegirEmpresa
from ventanas.stock_cregar import Ui_StockCregar
from ventanas.stock_fara import Ui_StockFara
from ventanas.stock_fontana import Ui_StockFontana
from ventanas.registrar_compras import Ui_RegistrarCompras
from ventanas.consultar_ganancias import Ui_ConsultarGanancias
from ventanas.historial_compras import Ui_HistorialCompras
from ventanas.historial_ventas import Ui_HistorialVentas
from ventanas.modificar_comisiones import Ui_ModificarComisiones

global base_datos, ventana_bienvenida, ventana_login, ventana_registrar_ventas_autorizado, ventana_registrar_ventas, ventana_principal_usuario_autorizado, ventana_usuarios, ventana_elegir_empresa, ventana_stock_cregar, ventana_stock_fara, ventana_stock_fontana, ventana_registrar_compras, ventana_historial_compras, ventana_historial_ventas, ventana_consultar_ganancias, ventana_modificar_comisiones


class Ventana(QtWidgets.QWidget):

    def actualizar_treeview(self, treeview, modelo, productos, atributos):
        modelo.removeRows(0, modelo.rowCount())
        if productos:
            for producto in productos:
                row = []
                for attr in atributos:
                    valor = getattr(producto, attr)
                    # Verificar si el tipo de dato es doublefield y agregar "$"
                    if isinstance(valor, float):
                        if (
                            attr == "aumento_efectivo"
                            or attr == "aumento_mercadolibre"
                            or attr == "aumento_constructores"
                            or attr == "iva"
                            or attr == "descuento_1"
                            or attr == "descuento_2"
                        ):
                            valor = f"{valor}%"
                        else:
                            valor = f"${valor}"  # Agregar signo "$" al valor
                    item = QtGui.QStandardItem(str(valor))
                    item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
                    row.append(item)

                modelo.appendRow(row)
            treeview.setModel(modelo)

    def mostrar_error_temporal(self, label, mensaje):
        label.setText(mensaje)
        QtCore.QTimer.singleShot(2000, lambda: label.clear())

    def volver(self):
        self.hide()
        self.ocultar_campos()
        self.ventana_anterior.show()


class VentanaBienvenida(QtWidgets.QWidget, Ui_UserSelection):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boton_vendedor.clicked.connect(lambda: self.ir_a_login("vendedor"))
        self.boton_usuario_autorizado.clicked.connect(
            lambda: self.ir_a_login("usuario_autorizado")
        )
        self.tipo_usuario = None

    def ir_a_login(self, tipo_usuario):
        self.hide()
        self.tipo_usuario = tipo_usuario
        ventana_login.show()


class VentanaLogin(Ventana, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boton_ingresar.clicked.connect(self.verificar_usuario)
        self.boton_volver.clicked.connect(self.volver)
        global base_datos, ventana_bienvenida
        self.base_datos = base_datos
        self.ventana_anterior = ventana_bienvenida

    def verificar_usuario(self):
        if ventana_bienvenida.tipo_usuario == "vendedor":
            self.verificar_vendedor()
        else:
            self.verificar_usuario_autorizado()

    def verificar_vendedor(self):
        usuario = self.usuario_ingresado.text()
        contrasenia = self.contrasenia_ingresada.text()
        if self.base_datos.vendedor_existe(usuario, contrasenia):
            self.hide()
            ventana_registrar_ventas.show()
        else:
            self.mostrar_error_temporal(
                self.campos_no_validos, "Usuario y/o contraseña incorrecto/s"
            )

    def verificar_usuario_autorizado(self):
        usuario = self.usuario_ingresado.text()
        contrasenia = self.contrasenia_ingresada.text()
        if self.base_datos.usuario_autorizado_existe(usuario, contrasenia):
            self.hide()
            ventana_principal_usuario_autorizado.show()
        else:
            self.mostrar_error_temporal(
                self.campos_no_validos, "Usuario y/o contraseña incorrecto/s"
            )

    def ocultar_campos(self):
        self.usuario_ingresado.clear()
        self.contrasenia_ingresada.clear()

    def volver(self):
        super().volver()
        self.ventana_anterior.tipo_usuario = None


class VentanaRegistrarVentas(Ventana):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boton_buscar_producto.clicked.connect(self.buscar_y_enfocar_producto)
        self.boton_registrar_venta.clicked.connect(self.verificar_cantidad_a_vender)
        self.boton_todos.clicked.connect(self.actualizar_treeview_productos)
        self.boton_cregar.clicked.connect(lambda: self.filtrar_productos("cregar"))
        self.boton_fara.clicked.connect(lambda: self.filtrar_productos("fara"))
        self.boton_fontana.clicked.connect(lambda: self.filtrar_productos("fontana"))
        self.boton_actualizar.clicked.connect(self.actualizar_treeviews)
        global base_datos
        self.base_datos = base_datos

        self.actualizar_treeviews()

    def actualizar_treeviews(self):
        self.actualizar_treeview_productos()
        self.actualizar_treeview_ventas()

    def actualizar_treeview_productos(self):
        productos = self.base_datos.obtener_productos_para_venta()
        self.actualizar_treeview(
            self.treeview_productos,
            self.modelo_productos,
            productos,
            [
                "id_producto",
                "producto",
                "stock",
                "precio_efectivo",
                "precio_mercadolibre",
                "precio_constructores",
            ],
        )

    def filtrar_productos(self, filtro):
        productos_filtrados = self.base_datos.obtener_productos_filtrados(filtro)
        self.actualizar_treeview(
            self.treeview_productos,
            self.modelo_productos,
            productos_filtrados,
            [
                "id_producto",
                "producto",
                "stock",
                "precio_efectivo",
                "precio_mercadolibre",
                "precio_constructores",
            ],
        )

    def actualizar_treeview_ventas(self):
        ventas = self.base_datos.obtener_ventas_ordenadas()
        self.actualizar_treeview(
            self.treeview_ventas,
            self.modelo_ventas,
            ventas,
            [
                "id_venta",
                "fecha",
                "producto",
                "cantidad",
                "precio_unitario",
                "tipo_pago",
            ],
        )

    def buscar_y_enfocar_producto(self):
        nombre_producto = self.input_buscar_producto.text().lower()
        if len(nombre_producto) > 0:
            items = self.modelo_productos.findItems(
                nombre_producto, QtCore.Qt.MatchContains, 1
            )  # Columna 1 es la columna de "Producto"

            if items:
                item = items[0]
                index = self.modelo_productos.indexFromItem(item)
                self.treeview_productos.setCurrentIndex(index)
                self.treeview_productos.scrollTo(index)
            else:
                self.mostrar_error_temporal(
                    self.producto_no_encontrado, "Producto no encontrado"
                )
        else:
            self.mostrar_error_temporal(
                self.producto_no_encontrado, "Producto no encontrado"
            )

    def ocultar_campos(self):
        pass

    def verificar_cantidad_a_vender(self):
        pass


class VentanaRegistrarVentasVendedor(VentanaRegistrarVentas, Ui_RegistrarVentaVendedor):
    def __init__(self):
        super().__init__()

    def verificar_cantidad_a_vender(self):
        producto_seleccionado = self.treeview_productos.currentIndex()

        if not producto_seleccionado.isValid():
            self.mostrar_error_temporal(
                self.label_cantidad_invalida,
                "Seleccione un producto primero",
            )
            return

        producto = self.modelo_productos.itemFromIndex(
            producto_seleccionado.siblingAtColumn(0)
        ).text()

        try:
            cantidad_a_vender = int(self.input_cantidad_vendida.text())
            if cantidad_a_vender < 1:
                self.mostrar_error_temporal(
                    self.label_cantidad_invalida,
                    "Por favor Ingrese una cantidad válida",
                )
                return

            if not self.base_datos.stock_suficiente(producto, cantidad_a_vender):
                self.mostrar_error_temporal(
                    self.label_cantidad_invalida,
                    "No hay stock suficiente para esa venta",
                )
                return

            tipo_pago_seleccionado = None
            if (
                self.eleccion_efectivo.isChecked()
                or self.eleccion_constructor.isChecked()
            ):
                tipo_pago_seleccionado = "efectivo"
            elif self.eleccion_posnet.isChecked():
                tipo_pago_seleccionado = "posnet"
            else:
                self.mostrar_error_temporal(
                    self.label_tipo_pago_no_elegido,
                    "Seleccione el precio de venta",
                )
                return

            self.base_datos.registrar_venta(
                producto, cantidad_a_vender, tipo_pago_seleccionado
            )
            QtWidgets.QMessageBox.information(
                self, "Venta Cargada", "Venta registrada con éxito"
            )
            self.limpiar_campos()
            self.actualizar_treeviews()

        except ValueError:
            self.mostrar_error_temporal(
                self.label_cantidad_invalida,
                "Por favor ingrese una cantidad válida",
            )

    def limpiar_campos(self):
        self.input_cantidad_vendida.setText("")
        self.eleccion_constructor.setChecked(False)
        self.eleccion_efectivo.setChecked(False)
        self.eleccion_posnet.setChecked(False)


class VentanaRegistrarVentasAutorizado(
    VentanaRegistrarVentas, Ui_RegistrarVentasAutorizado
):
    def __init__(self):
        super().__init__()
        self.boton_volver.clicked.connect(self.volver)
        global ventana_principal_usuario_autorizado
        self.ventana_anterior = ventana_principal_usuario_autorizado

    def verificar_cantidad_a_vender(self):
        producto_seleccionado = self.treeview_productos.currentIndex()

        if not producto_seleccionado.isValid():
            self.mostrar_error_temporal(
                self.label_cantidad_invalida,
                "Seleccione un producto primero",
            )
            return

        producto = self.modelo_productos.itemFromIndex(
            producto_seleccionado.siblingAtColumn(0)
        ).text()

        try:
            cantidad_a_vender = int(self.input_cantidad_vendida.text())
            if cantidad_a_vender < 1:
                self.mostrar_error_temporal(
                    self.label_cantidad_invalida,
                    "Por favor Ingrese una cantidad válida",
                )
                return

            if not self.base_datos.stock_suficiente(producto, cantidad_a_vender):
                self.mostrar_error_temporal(
                    self.label_cantidad_invalida,
                    "No hay stock suficiente para esa venta",
                )
                return

            tipo_pago = None
            opciones_pago = {
                self.eleccion_efectivo: "efectivo",
                self.eleccion_constructor: "constructor",
                self.eleccion_posnet: "posnet",
                self.eleccion_mercadolibre: "mercadolibre",
            }
            for opcion, pago in opciones_pago.items():
                if opcion.isChecked():
                    tipo_pago = pago
                    break

            if tipo_pago is None:
                self.mostrar_error_temporal(
                    self.label_tipo_pago_no_elegido,
                    "Seleccione el precio de venta",
                )
                return

            self.base_datos.registrar_venta(producto, cantidad_a_vender, tipo_pago)
            QtWidgets.QMessageBox.information(
                self, "Venta Cargada", "Venta registrada con éxito"
            )
            self.limpiar_campos()
            self.actualizar_treeviews()

        except ValueError:
            self.mostrar_error_temporal(
                self.label_cantidad_invalida,
                "Por favor ingrese una cantidad válida",
            )

    def limpiar_campos(self):
        self.input_cantidad_vendida.setText("")
        self.eleccion_constructor.setChecked(False)
        self.eleccion_efectivo.setChecked(False)
        self.eleccion_posnet.setChecked(False)
        self.eleccion_mercadolibre.setChecked(False)


class VentanaPrincipalUsuarioAutorizado(
    QtWidgets.QMainWindow, Ui_VentanaPrincipalAutorizada
):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.boton_registrar_ventas.clicked.connect(
            lambda: self.abrir_ventana_seleccionada(ventana_registrar_ventas_autorizado)
        )
        self.boton_usuarios.clicked.connect(
            lambda: self.abrir_ventana_seleccionada(ventana_usuarios)
        )
        self.boton_stock_disponible.clicked.connect(
            lambda: self.abrir_ventana_seleccionada(ventana_elegir_empresa)
        )
        self.boton_registrar_compras.clicked.connect(
            lambda: self.abrir_ventana_seleccionada(ventana_registrar_compras)
        )
        self.boton_historial_compras.clicked.connect(
            lambda: self.abrir_ventana_seleccionada(ventana_historial_compras)
        )
        self.boton_historial_ventas.clicked.connect(
            lambda: self.abrir_ventana_seleccionada(ventana_historial_ventas)
        )
        self.boton_consultar_ganancias.clicked.connect(
            lambda: self.abrir_ventana_seleccionada(ventana_consultar_ganancias)
        )
        self.boton_modificar_comisiones.clicked.connect(
            lambda: self.abrir_ventana_seleccionada(ventana_modificar_comisiones)
        )

        self.configurar_boton(
            self.boton_registrar_ventas, "imagenes/registrar_ventas.png"
        )

        self.configurar_boton(
            self.boton_registrar_compras, "imagenes/registrar_compras.png"
        )

        self.configurar_boton(self.boton_consultar_ganancias, "imagenes/ganancias.png")

        self.configurar_boton(
            self.boton_historial_ventas, "imagenes/historial_ventas.png"
        )

        self.configurar_boton(
            self.boton_historial_compras, "imagenes/historial_compras.png"
        )

        self.configurar_boton(
            self.boton_stock_disponible, "imagenes/stock_disponible.png"
        )

    def abrir_ventana_seleccionada(self, ventana):
        self.hide()
        ventana.actualizar_treeviews()
        ventana.show()

    def configurar_boton(self, boton, imagen_path):
        background_style = (
            f"background-image: url('{imagen_path}'); border-radius: 15px;"
        )
        boton.setStyleSheet(background_style)


class VentanaUsuarios(Ventana, Ui_Usuarios):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.confirmar = None
        global base_datos, ventana_principal_usuario_autorizado
        self.base_datos = base_datos
        self.ventana_anterior = ventana_principal_usuario_autorizado

        self.boton_volver.clicked.connect(self.volver)
        self.boton_registrar_vendedor.clicked.connect(self.registrar_vendedor)
        self.boton_eliminar_vendedor.clicked.connect(self.eliminar_vendedor)
        self.boton_registrar_usuario_autorizado.clicked.connect(
            self.registrar_usuario_autorizado
        )
        self.boton_eliminar_usuario_autorizado.clicked.connect(
            self.eliminar_usuario_autorizado
        )
        self.boton_confirmar_registro.clicked.connect(self.confirmar_registro)
        self.ocultar_campos()

        self.actualizar_treeviews()

    def actualizar_treeview_vendedores(self):
        vendedores = self.base_datos.obtener_vendedores_ordenados()
        self.actualizar_treeview(
            self.treeview_vendedores,
            self.modelo_vendedores,
            vendedores,
            ["usuario", "contraseña"],
        )

    def actualizar_treeview_usuarios_autorizados(self):
        usuarios_autorizados = self.base_datos.obtener_usuarios_autorizados_ordenados()
        self.actualizar_treeview(
            self.treeview_usuarios_autorizados,
            self.modelo_usuarios_autorizados,
            usuarios_autorizados,
            ["usuario", "contraseña"],
        )

    def actualizar_treeviews(self):
        self.actualizar_treeview_usuarios_autorizados()
        self.actualizar_treeview_vendedores()

    def registrar_vendedor(self):
        self.mostrar_campos()
        self.label_ingresar_usuario.setText(
            "Ingrese cual sera el usuario del nuevo vendedor:"
        )
        self.label_ingresar_contrasenia.setText(
            "Ingrese cual sera la contraseña del nuevo vendedor:"
        )
        self.confirmar = "vendedor"

    def eliminar_vendedor(self):
        self.ocultar_campos()
        vendedor_seleccionado = self.treeview_vendedores.currentIndex()
        if vendedor_seleccionado.isValid():
            respuesta = QtWidgets.QMessageBox.question(
                self, "Confirmación", "¿Esta seguro de que desea eliminar este usuario?"
            )
            if respuesta == QtWidgets.QMessageBox.Yes:
                vendedor = self.modelo_vendedores.data(vendedor_seleccionado)
                self.base_datos.eliminar_vendedor(vendedor)
                self.actualizar_treeview_vendedores()
        else:
            self.mostrar_error_temporal(
                self.label_vendedor_no_seleccionado,
                "Seleccione un vendedor de la lista primero",
            )

    def registrar_usuario_autorizado(self):
        self.mostrar_campos()
        self.label_ingresar_usuario.setText(
            "Ingrese cual sera el usuario del nuevo autorizado:"
        )
        self.label_ingresar_contrasenia.setText(
            "Ingrese cual sera la contraseña del nuevo autorizado:"
        )
        self.confirmar = "usuario_autorizado"

    def eliminar_usuario_autorizado(self):
        self.ocultar_campos()
        usuario_autorizado = self.treeview_usuarios_autorizados.currentIndex()
        if usuario_autorizado.isValid():
            respuesta = QtWidgets.QMessageBox.question(
                self, "Confirmación", "¿Esta seguro de que desea eliminar este usuario?"
            )
            if respuesta == QtWidgets.QMessageBox.Yes:
                usuario = self.modelo_usuarios_autorizados.data(usuario_autorizado)
                self.base_datos.eliminar_usuario_autorizado(usuario)
                self.actualizar_treeview_usuarios_autorizados()
        else:
            self.mostrar_error_temporal(
                self.label_vendedor_no_seleccionado_2,
                "Seleccione un usuario de la lista primero",
            )

    def mostrar_campos(self):
        self.boton_confirmar_registro.setVisible(True)
        self.nuevo_usuario.setVisible(True)
        self.nueva_contrasenia.setVisible(True)

    def ocultar_campos(self):
        self.label_ingresar_usuario.clear()
        self.label_ingresar_contrasenia.clear()
        self.nuevo_usuario.clear()
        self.nueva_contrasenia.clear()
        self.boton_confirmar_registro.setVisible(False)
        self.nuevo_usuario.setVisible(False)
        self.nueva_contrasenia.setVisible(False)

    def confirmar_registro(self):
        nuevo_usuario = self.nuevo_usuario.text()
        nueva_contrasenia = self.nueva_contrasenia.text()
        if self.confirmar == "vendedor":
            if not self.base_datos.vendedor_ya_cargado(nuevo_usuario):
                self.base_datos.agregar_vendedor(nuevo_usuario, nueva_contrasenia)
                QtWidgets.QMessageBox.information(
                    self, "Confirmacion", "Usuario Cargado Con exito"
                )
                self.actualizar_treeview_vendedores()
                self.ocultar_campos()
            else:
                QtWidgets.QMessageBox.information(self, "Error", "El usuario ya existe")
        elif self.confirmar == "usuario_autorizado":
            if not self.base_datos.usuario_autorizado_ya_cargado(nuevo_usuario):
                self.base_datos.agregar_usuario_autorizado(
                    nuevo_usuario, nueva_contrasenia
                )
                QtWidgets.QMessageBox.information(
                    self, "Confirmacion", "Usuario Cargado Con exito"
                )
                self.actualizar_treeview_usuarios_autorizados()
                self.ocultar_campos()
            else:
                QtWidgets.QMessageBox.information(self, "Error", "El usuario ya existe")


class VentanaElegirEmpresa(Ventana, Ui_ElegirEmpresa):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        global ventana_principal_usuario_autorizado
        self.ventana_anterior = ventana_principal_usuario_autorizado

        self.boton_volver.clicked.connect(self.volver)
        self.boton_cregar.clicked.connect(
            lambda: self.abrir_ventana(ventana_stock_cregar)
        )
        self.boton_fara.clicked.connect(lambda: self.abrir_ventana(ventana_stock_fara))
        self.boton_fontana.clicked.connect(
            lambda: self.abrir_ventana(ventana_stock_fontana)
        )

    def abrir_ventana(self, ventana):
        self.hide()
        ventana.actualizar_treeviews()
        ventana.show()

    def actualizar_treeviews(self):
        pass

    def ocultar_campos(self):
        pass


class VentanaStock(Ventana):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        global base_datos, ventana_elegir_empresa
        self.base_datos = base_datos
        self.ventana_anterior = ventana_elegir_empresa
        self.ocultar_campos()
        self.mostrar_productos()
        self.actualizar_treeview_productos()

        self.boton_volver.clicked.connect(self.volver)
        self.boton_buscar_producto.clicked.connect(self.buscar_y_enfocar_producto)
        self.boton_agregar_producto.clicked.connect(self.agregar_producto)
        self.boton_confirmar_registro.clicked.connect(self.confirmar_registro)
        self.boton_eliminar_producto.clicked.connect(self.eliminar_producto)
        self.boton_modificar_producto.clicked.connect(self.modificar_producto)
        self.boton_confirmar_modificacion.clicked.connect(self.confirmar_modificacion)
        self.boton_cancelar_modificacion.clicked.connect(self.cancelar_modificacion)
        self.boton_modificar_productos_gral.clicked.connect(
            self.modificar_productos_gral
        )
        self.boton_modificar_costo_inicial.clicked.connect(self.modificar_costo_inicial)
        self.boton_modificar_descuento_1.clicked.connect(self.modificar_descuento_1)
        self.boton_modificar_iva.clicked.connect(self.modificar_iva)
        self.boton_modificar_descuento_2.clicked.connect(self.modificar_descuento_2)
        self.boton_modificar_aumento_efectivo.clicked.connect(
            self.modificar_aumento_efectivo
        )
        self.boton_modificar_aumento_mercadolibre.clicked.connect(
            self.modificar_aumento_mercadolibre
        )
        self.boton_modificar_aumento_constructores.clicked.connect(
            self.modificar_aumento_constructores
        )
        self.boton_cancelar_modificacion_gral.clicked.connect(
            self.cancelar_modificacion_gral
        )

    def actualizar_treeview_productos(self):
        pass

    def actualizar_treeviews(self):
        self.actualizar_treeview_productos()

    def actualizar(self):
        pass

    def buscar_y_enfocar_producto(self):
        nombre_producto = self.input_buscar_producto.text().lower()
        if len(nombre_producto) > 0:
            items = self.modelo_productos.findItems(
                nombre_producto, QtCore.Qt.MatchContains, 1
            )  # Columna 0 es la columna de "Producto"

            if items:
                item = items[0]
                index = self.modelo_productos.indexFromItem(item)
                self.treeview_productos.setCurrentIndex(index)
                self.treeview_productos.scrollTo(index)
            else:
                self.mostrar_error_temporal(
                    self.producto_no_encontrado, "Producto no encontrado"
                )
        else:
            self.mostrar_error_temporal(
                self.producto_no_encontrado, "Producto no encontrado"
            )

    def agregar_producto(self):
        self.limpiar_campos()
        self.mostrar_campos_agregar_producto()

    def confirmar_registro(self):
        pass

    def eliminar_producto(self):
        producto_seleccionado = self.treeview_productos.currentIndex()

        if not producto_seleccionado.isValid():
            self.mostrar_error_temporal(
                self.label_eliminar_producto,
                "Seleccione un producto de la lista",
            )
            return

        producto_nombre = self.modelo_productos.itemFromIndex(
            producto_seleccionado.siblingAtColumn(0)
        ).text()

        respuesta = QtWidgets.QMessageBox.question(
            self,
            "Confirmación",
            "¿Está seguro de que desea eliminar el producto '{}'?".format(
                producto_nombre
            ),
        )

        if respuesta == QtWidgets.QMessageBox.Yes:
            try:
                self.base_datos.eliminar_producto(producto_nombre)
                QtWidgets.QMessageBox.information(
                    self, "Confirmación", "Producto eliminado con éxito."
                )
                self.actualizar_treeview_productos()
            except Exception as e:
                QtWidgets.QMessageBox.critical(
                    self, "Error", "Error al eliminar el producto: {}".format(str(e))
                )

    def modificar_producto(self):
        self.ocultar_campos()
        producto_seleccionado = self.treeview_productos.currentIndex()
        if producto_seleccionado.isValid():
            self.id_producto_a_modificar = self.modelo_productos.itemFromIndex(
                producto_seleccionado.siblingAtColumn(0)
            ).text()
            self.mostrar_campos_modificar_producto()
            self.actualizar_lineedits_producto_seleccionado()
        else:
            self.mostrar_error_temporal(
                self.label_modificar_producto,
                "Seleccione un producto de la lista",
            )

    def actualizar_lineedits_producto_seleccionado(self):
        producto_info = self.base_datos.buscar_informacion_producto(
            self.id_producto_a_modificar
        )
        self.nombre_viejo_producto = producto_info.producto

        self.input_nombre_producto.setText(producto_info.producto)
        self.input_stock.setText(str(producto_info.stock))
        self.input_costo_inicial.setText(str(producto_info.costo_inicial))
        self.input_descuento_1.setText(str(producto_info.descuento_1))
        self.input_descuento_2.setText(str(producto_info.descuento_2))
        self.input_iva.setText(str(producto_info.iva))
        self.input_aumento_efectivo.setText(str(producto_info.aumento_efectivo))
        self.input_aumento_mercadolibre.setText(str(producto_info.aumento_mercadolibre))
        self.input_aumento_constructores.setText(
            str(producto_info.aumento_constructores)
        )

    def confirmar_modificacion(self):
        pass

    def cancelar_modificacion(self):
        self.ocultar_campos()
        self.mostrar_productos()

    def cancelar_modificacion_gral(self):
        self.widget_modificar_gral.setVisible(False)
        self.limpiar_campos()
        self.mostrar_productos()

    def modificar_productos_gral(self):
        self.mostrar_campos_modificar_productos_gral()

    def modificar_parametro(self, parametro, mensaje):
        self.widget_ingresar_porcentaje.setVisible(True)
        self.label_ingrese_porcentaje.setText(mensaje)
        try:
            self.boton_confirmar_modificacion_gral.clicked.disconnect()
        except TypeError:
            pass
        self.boton_confirmar_modificacion_gral.clicked.connect(
            lambda: self.confirmar_modificar_gral(parametro)
        )

    def modificar_costo_inicial(self):
        self.modificar_parametro(
            "costo_inicial",
            "Ingrese el porcentaje de aumento del costo inicial para todos los productos",
        )

    def modificar_descuento_1(self):
        self.modificar_parametro(
            "descuento_1",
            "Ingrese el nuevo porcentaje de descuento_1 para todos los productos",
        )

    def modificar_descuento_2(self):
        self.modificar_parametro(
            "descuento_2",
            "Ingrese el nuevo porcentaje de descuento_2 para todos los productos",
        )

    def modificar_iva(self):
        self.modificar_parametro(
            "iva", "Ingrese el nuevo porcentaje de iva para todos los productos"
        )

    def modificar_aumento_efectivo(self):
        self.modificar_parametro(
            "aumento_efectivo",
            "Ingrese el nuevo porcentaje de aumento_efectivo para todos los productos",
        )

    def modificar_aumento_mercadolibre(self):
        self.modificar_parametro(
            "aumento_mercadolibre",
            "Ingrese el nuevo porcentaje de aumento_mercadolibre para todos los productos",
        )

    def modificar_aumento_constructores(self):
        self.modificar_parametro(
            "aumento_constructores",
            "Ingrese el nuevo porcentaje de aumento_constructores para todos los productos",
        )

    def confirmar_modificar_gral(self, columna):
        pass

    def mostrar_campos_modificar_productos_gral(self):
        self.ocultar_campos()
        self.widget_lista_productos.setVisible(False)
        self.widget_modificar_gral.setVisible(True)
        self.widget_ingresar_porcentaje.setVisible(False)

    def mostrar_productos(self):
        self.widget_lista_productos.setVisible(True)

    def mostrar_campos_agregar_producto(self):
        self.widget_lista_productos.setVisible(False)
        self.widget_agregar_producto.setVisible(True)
        self.boton_confirmar_modificacion.setVisible(False)
        self.boton_confirmar_registro.setVisible(True)

    def mostrar_campos_modificar_producto(self):
        self.widget_lista_productos.setVisible(False)
        self.widget_agregar_producto.setVisible(True)
        self.boton_confirmar_registro.setVisible(False)
        self.boton_confirmar_modificacion.setVisible(True)

    def ocultar_campos(self):
        self.widget_agregar_producto.setVisible(False)
        self.widget_modificar_gral.setVisible(False)
        self.widget_ingresar_porcentaje.setVisible(False)

    def limpiar_campos(self):
        self.input_nombre_producto.setText("")
        self.input_stock.setText("")
        self.input_costo_inicial.setText("")
        self.input_descuento_1.setText("")
        self.input_descuento_2.setText("")
        self.input_iva.setText("")
        self.input_aumento_constructores.setText("")
        self.input_aumento_efectivo.setText("")
        self.input_aumento_mercadolibre.setText("")
        self.input_nuevo_porcentaje.setText("")


class VentanaStockCregar(VentanaStock, Ui_StockCregar):
    def __init__(self):
        super().__init__()

    def actualizar_treeview_productos(self):
        productos_cregar = self.base_datos.obtener_productos_filtrados("cregar")
        self.actualizar(productos_cregar)

    def actualizar(self, productos):
        self.actualizar_treeview(
            self.treeview_productos,
            self.modelo_productos,
            productos,
            [
                "id_producto",
                "producto",
                "stock",
                "costo_inicial",
                "descuento_1",
                "costo_parcial_1",
                "iva",
                "costo_parcial_2",
                "descuento_2",
                "costo_total",
                "aumento_efectivo",
                "precio_efectivo",
                "aumento_mercadolibre",
                "precio_mercadolibre",
                "aumento_constructores",
                "precio_constructores",
            ],
        )

    def confirmar_registro(self):
        try:
            nuevo_producto = self.input_nombre_producto.text()
            stock = int(self.input_stock.text())
            costo_inicial = round(float(self.input_costo_inicial.text()), 2)
            descuento_1 = round(float(self.input_descuento_1.text()), 2)
            iva = round(float(self.input_iva.text()), 2)
            descuento_2 = round(float(self.input_descuento_2.text()), 2)
            aumento_efectivo = round(float(self.input_aumento_efectivo.text()), 2)
            aumento_mercadolibre = round(
                float(self.input_aumento_mercadolibre.text()), 2
            )
            aumento_constructores = round(
                float(self.input_aumento_constructores.text()), 2
            )
            if not self.base_datos.producto_repetido_en_stock(nuevo_producto):
                self.base_datos.agregar_producto_a_stock(
                    nuevo_producto,
                    "cregar",
                    stock,
                    costo_inicial,
                    iva,
                    descuento_1,
                    descuento_2,
                    aumento_efectivo,
                    aumento_mercadolibre,
                    aumento_constructores,
                )
                QtWidgets.QMessageBox.information(
                    self, "Confirmacion", "Nuevo producto registrado con exito."
                )
                self.actualizar_treeview_productos()
                self.ocultar_campos()
                self.mostrar_productos()
                self.limpiar_campos()
            else:
                self.mostrar_error_temporal(self.label_error, "Producto ya existente")
        except ValueError:
            self.mostrar_error_temporal(self.label_error, "Campos no validos.")

    def confirmar_modificacion(self):
        try:
            nuevo_producto = self.input_nombre_producto.text()
            if (
                self.nombre_viejo_producto.lower() != nuevo_producto.lower()
                and self.base_datos.producto_repetido_en_stock(nuevo_producto)
            ):
                self.mostrar_error_temporal(self.label_error, "Producto ya existente")
            else:
                nuevo_stock = int(self.input_stock.text())
                nuevo_costo_inicial = round(float(self.input_costo_inicial.text()), 2)
                nuevo_descuento_1 = round(float(self.input_descuento_1.text()), 2)
                nuevo_descuento_2 = round(float(self.input_descuento_2.text()), 2)
                nuevo_iva = round(float(self.input_iva.text()), 2)
                nuevo_aumento_efectivo = round(
                    float(self.input_aumento_efectivo.text()), 2
                )
                nuevo_aumento_mercadolibre = round(
                    float(self.input_aumento_mercadolibre.text()), 2
                )
                nuevo_aumento_constructores = round(
                    float(self.input_aumento_constructores.text()), 2
                )
                self.base_datos.modificar_producto_de_stock(
                    self.id_producto_a_modificar,
                    nuevo_producto,
                    nuevo_stock,
                    nuevo_costo_inicial,
                    nuevo_iva,
                    nuevo_descuento_1,
                    nuevo_descuento_2,
                    nuevo_aumento_efectivo,
                    nuevo_aumento_mercadolibre,
                    nuevo_aumento_constructores,
                )
                self.actualizar_treeview_productos()
                QtWidgets.QMessageBox.information(
                    self, "Confirmacion", "Producto modificado con exito"
                )
                self.ocultar_campos()
                self.mostrar_productos()
        except ValueError:
            self.mostrar_error_temporal(self.label_error, "Campos no validos.")

    def confirmar_modificar_costo_inicial(self):
        try:
            porcentaje = round(float(self.input_nuevo_porcentaje.text()), 2)
            self.base_datos.aumentar_costo_inicial_general("cregar", porcentaje)
            QtWidgets.QMessageBox.information(
                self, "Confirmacion", "Precios actualizados con exito."
            )
            self.actualizar_treeview_productos()
            self.ocultar_campos()
            self.limpiar_campos()
            self.widget_lista_productos.setVisible(True)
        except ValueError:
            self.mostrar_error_temporal(
                self.label_ingrese_porcentaje_valido, "Ingrese un porcentaje valido"
            )

    def confirmar_modificar_gral(self, columna):
        try:
            porcentaje = round(float(self.input_nuevo_porcentaje.text()), 2)
            self.base_datos.modificar_productos_gral("cregar", columna, porcentaje)
            QtWidgets.QMessageBox.information(
                self, "Confirmacion", "Precios actualizados con exito."
            )
            self.actualizar_treeview_productos()
            self.ocultar_campos()
            self.limpiar_campos()
            self.widget_lista_productos.setVisible(True)
        except ValueError:
            self.mostrar_error_temporal(
                self.label_ingrese_porcentaje_valido, "Ingrese un porcentaje valido"
            )


class VentanaStockFara(VentanaStock, Ui_StockFara):
    def __init__(self):
        super().__init__()

    def actualizar_treeview_productos(self):
        productos_fara = self.base_datos.obtener_productos_filtrados("fara")
        self.actualizar(productos_fara)

    def actualizar(self, productos):
        self.actualizar_treeview(
            self.treeview_productos,
            self.modelo_productos,
            productos,
            [
                "id_producto",
                "producto",
                "stock",
                "costo_inicial",
                "descuento_1",
                "costo_parcial_1",
                "descuento_2",
                "costo_parcial_2",
                "iva",
                "costo_total",
                "aumento_efectivo",
                "precio_efectivo",
                "aumento_mercadolibre",
                "precio_mercadolibre",
                "aumento_constructores",
                "precio_constructores",
            ],
        )

    def confirmar_registro(self):
        try:
            nuevo_producto = self.input_nombre_producto.text()
            stock = int(self.input_stock.text())
            costo_inicial = round(float(self.input_costo_inicial.text()), 2)
            descuento_1 = round(float(self.input_descuento_1.text()), 2)
            descuento_2 = round(float(self.input_descuento_2.text()), 2)
            iva = round(float(self.input_iva.text()), 2)
            aumento_efectivo = round(float(self.input_aumento_efectivo.text()), 2)
            aumento_mercadolibre = round(
                float(self.input_aumento_mercadolibre.text()), 2
            )
            aumento_constructores = round(
                float(self.input_aumento_constructores.text()), 2
            )
            if not self.base_datos.producto_repetido_en_stock(nuevo_producto):
                self.base_datos.agregar_producto_a_stock(
                    nuevo_producto,
                    "fara",
                    stock,
                    costo_inicial,
                    iva,
                    descuento_1,
                    descuento_2,
                    aumento_efectivo,
                    aumento_mercadolibre,
                    aumento_constructores,
                )
                QtWidgets.QMessageBox.information(
                    self, "Confirmacion", "Nuevo producto registrado con exito."
                )
                self.actualizar_treeview_productos()
                self.ocultar_campos()
                self.mostrar_productos()
                self.limpiar_campos()
            else:
                self.mostrar_error_temporal(self.label_error, "Producto ya existente")
        except ValueError:
            self.mostrar_error_temporal(self.label_error, "Campos no validos.")

    def confirmar_modificacion(self):
        try:
            nuevo_producto = self.input_nombre_producto.text()
            if (
                self.nombre_viejo_producto.lower() != nuevo_producto.lower()
                and self.base_datos.producto_repetido_en_stock(nuevo_producto)
            ):
                self.mostrar_error_temporal(self.label_error, "Producto ya existente")
            else:
                nuevo_stock = int(self.input_stock.text())
                nuevo_costo_inicial = round(float(self.input_costo_inicial.text()), 2)
                nuevo_descuento_1 = round(float(self.input_descuento_1.text()), 2)
                nuevo_descuento_2 = round(float(self.input_descuento_2.text()), 2)
                nuevo_iva = round(float(self.input_iva.text()), 2)
                nuevo_aumento_efectivo = round(
                    float(self.input_aumento_efectivo.text()), 2
                )
                nuevo_aumento_mercadolibre = round(
                    float(self.input_aumento_mercadolibre.text()), 2
                )
                nuevo_aumento_constructores = round(
                    float(self.input_aumento_constructores.text()), 2
                )
                self.base_datos.modificar_producto_de_stock(
                    self.id_producto_a_modificar,
                    nuevo_producto,
                    nuevo_stock,
                    nuevo_costo_inicial,
                    nuevo_iva,
                    nuevo_descuento_1,
                    nuevo_descuento_2,
                    nuevo_aumento_efectivo,
                    nuevo_aumento_mercadolibre,
                    nuevo_aumento_constructores,
                )
                self.actualizar_treeview_productos()
                QtWidgets.QMessageBox.information(
                    self, "Confirmacion", "Producto modificado con exito"
                )
                self.ocultar_campos()
                self.mostrar_productos()
        except ValueError:
            self.mostrar_error_temporal(self.label_error, "Campos no validos.")

    def confirmar_modificar_costo_inicial(self):
        try:
            porcentaje = round(float(self.input_nuevo_porcentaje.text()), 2)
            self.base_datos.aumentar_costo_inicial_general("fara", porcentaje)
            QtWidgets.QMessageBox.information(
                self, "Confirmacion", "Precios actualizados con exito."
            )
            self.actualizar_treeview_productos()
            self.ocultar_campos()
            self.limpiar_campos()
            self.widget_lista_productos.setVisible(True)
        except ValueError:
            self.mostrar_error_temporal(
                self.label_ingrese_porcentaje_valido, "Ingrese un porcentaje valido"
            )

    def confirmar_modificar_gral(self, columna):
        try:
            porcentaje = round(float(self.input_nuevo_porcentaje.text()), 2)
            self.base_datos.modificar_productos_gral("fara", columna, porcentaje)
            QtWidgets.QMessageBox.information(
                self, "Confirmacion", "Precios actualizados con exito."
            )
            self.actualizar_treeview_productos()
            self.ocultar_campos()
            self.limpiar_campos()
            self.widget_lista_productos.setVisible(True)
        except ValueError:
            self.mostrar_error_temporal(
                self.label_ingrese_porcentaje_valido, "Ingrese un porcentaje valido"
            )


class VentanaStockFontana(VentanaStock, Ui_StockFontana):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        global base_datos
        self.base_datos = base_datos
        self.ocultar_campos()

        self.mostrar_productos()
        self.actualizar_treeview_productos()
        self.boton_volver.clicked.connect(self.volver)
        self.boton_buscar_producto.clicked.connect(self.buscar_y_enfocar_producto)
        self.boton_agregar_producto.clicked.connect(self.agregar_producto)
        self.boton_confirmar_registro.clicked.connect(self.confirmar_registro)
        self.boton_eliminar_producto.clicked.connect(self.eliminar_producto)
        self.boton_modificar_producto.clicked.connect(self.modificar_producto)
        self.boton_confirmar_modificacion.clicked.connect(self.confirmar_modificacion)
        self.boton_cancelar_modificacion.clicked.connect(self.cancelar_modificacion)
        self.boton_modificar_productos_gral.clicked.connect(
            self.modificar_productos_gral
        )
        self.boton_modificar_costo_inicial.clicked.connect(self.modificar_costo_inicial)
        self.boton_modificar_iva.clicked.connect(self.modificar_iva)
        self.boton_modificar_aumento_efectivo.clicked.connect(
            self.modificar_aumento_efectivo
        )
        self.boton_modificar_aumento_mercadolibre.clicked.connect(
            self.modificar_aumento_mercadolibre
        )
        self.boton_modificar_aumento_constructores.clicked.connect(
            self.modificar_aumento_constructores
        )
        self.boton_cancelar_modificacion_gral.clicked.connect(
            self.cancelar_modificacion_gral
        )

    def actualizar_treeview_productos(self):
        productos_fontana = self.base_datos.obtener_productos_filtrados("fontana")
        self.actualizar(productos_fontana)

    def actualizar(self, productos):
        self.actualizar_treeview(
            self.treeview_productos,
            self.modelo_productos,
            productos,
            [
                "id_producto",
                "producto",
                "stock",
                "costo_inicial",
                "iva",
                "costo_total",
                "aumento_efectivo",
                "precio_efectivo",
                "aumento_mercadolibre",
                "precio_mercadolibre",
                "aumento_constructores",
                "precio_constructores",
            ],
        )

    def confirmar_registro(self):
        try:
            nuevo_producto = self.input_nombre_producto.text()
            stock = int(self.input_stock.text())
            costo_inicial = round(float(self.input_costo_inicial.text()), 2)
            iva = round(float(self.input_iva.text()), 2)
            aumento_efectivo = round(float(self.input_aumento_efectivo.text()), 2)
            aumento_mercadolibre = round(
                float(self.input_aumento_mercadolibre.text()), 2
            )
            aumento_constructores = round(
                float(self.input_aumento_constructores.text()), 2
            )
            if not self.base_datos.producto_repetido_en_stock(nuevo_producto):
                self.base_datos.agregar_producto_a_stock(
                    nuevo_producto,
                    "fontana",
                    stock,
                    costo_inicial,
                    iva,
                    aumento_efectivo=aumento_efectivo,
                    aumento_mercadolibre=aumento_mercadolibre,
                    aumento_constructores=aumento_constructores,
                )
                QtWidgets.QMessageBox.information(
                    self, "Confirmacion", "Nuevo producto registrado con exito."
                )
                self.actualizar_treeview_productos()
                self.ocultar_campos()
                self.mostrar_productos()
                self.limpiar_campos()
            else:
                self.mostrar_error_temporal(self.label_error, "Producto ya existente")
        except ValueError:
            self.mostrar_error_temporal(self.label_error, "Campos no validos.")

    def actualizar_lineedits_producto_seleccionado(self):
        producto_info = self.base_datos.buscar_informacion_producto(
            self.id_producto_a_modificar
        )
        self.nombre_viejo_producto = producto_info.producto

        self.input_nombre_producto.setText(producto_info.producto)
        self.input_stock.setText(str(producto_info.stock))
        self.input_costo_inicial.setText(str(producto_info.costo_inicial))
        self.input_iva.setText(str(producto_info.iva))
        self.input_aumento_efectivo.setText(str(producto_info.aumento_efectivo))
        self.input_aumento_mercadolibre.setText(str(producto_info.aumento_mercadolibre))
        self.input_aumento_constructores.setText(
            str(producto_info.aumento_constructores)
        )

    def confirmar_modificacion(self):
        try:
            nuevo_producto = self.input_nombre_producto.text()
            if (
                self.nombre_viejo_producto.lower() != nuevo_producto.lower()
                and self.base_datos.producto_repetido_en_stock(nuevo_producto)
            ):
                self.mostrar_error_temporal(self.label_error, "Producto ya existente")
            else:
                nuevo_stock = int(self.input_stock.text())
                nuevo_costo_inicial = round(float(self.input_costo_inicial.text()), 2)
                nuevo_iva = round(float(self.input_iva.text()), 2)
                nuevo_aumento_efectivo = round(
                    float(self.input_aumento_efectivo.text()), 2
                )
                nuevo_aumento_mercadolibre = round(
                    float(self.input_aumento_mercadolibre.text()), 2
                )
                nuevo_aumento_constructores = round(
                    float(self.input_aumento_constructores.text()), 2
                )
                self.base_datos.modificar_producto_de_stock(
                    self.id_producto_a_modificar,
                    nuevo_producto,
                    nuevo_stock,
                    nuevo_costo_inicial,
                    nuevo_iva,
                    nuevo_aumento_efectivo=nuevo_aumento_efectivo,
                    nuevo_aumento_mercadolibre=nuevo_aumento_mercadolibre,
                    nuevo_aumento_constructores=nuevo_aumento_constructores,
                )
                self.actualizar_treeview_productos()
                QtWidgets.QMessageBox.information(
                    self, "Confirmacion", "Producto modificado con exito"
                )
                self.ocultar_campos()
                self.mostrar_productos()
        except ValueError:
            self.mostrar_error_temporal(self.label_error, "Campos no validos.")

    def confirmar_modificar_costo_inicial(self):
        try:
            porcentaje = round(float(self.input_nuevo_porcentaje.text()), 2)
            self.base_datos.aumentar_costo_inicial_general("fontana", porcentaje)
            QtWidgets.QMessageBox.information(
                self, "Confirmacion", "Precios actualizados con exito."
            )
            self.actualizar_treeview_productos()
            self.ocultar_campos()
            self.limpiar_campos()
            self.widget_lista_productos.setVisible(True)
        except ValueError:
            self.mostrar_error_temporal(
                self.label_ingrese_porcentaje_valido, "Ingrese un porcentaje valido"
            )

    def confirmar_modificar_gral(self, columna):
        try:
            porcentaje = round(float(self.input_nuevo_porcentaje.text()), 2)
            self.base_datos.modificar_productos_gral("fontana", columna, porcentaje)
            QtWidgets.QMessageBox.information(
                self, "Confirmacion", "Precios actualizados con exito."
            )
            self.actualizar_treeview_productos()
            self.ocultar_campos()
            self.limpiar_campos()
            self.widget_lista_productos.setVisible(True)
        except ValueError:
            self.mostrar_error_temporal(
                self.label_ingrese_porcentaje_valido, "Ingrese un porcentaje valido"
            )


class VentanaRegistrarCompras(Ventana, Ui_RegistrarCompras):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boton_volver.clicked.connect(self.volver)
        self.boton_buscar_producto.clicked.connect(self.buscar_y_enfocar_producto)
        self.boton_registrar_compra.clicked.connect(self.registrar_compra)
        self.boton_filtrar_cregar.clicked.connect(
            lambda: self.filtrar_productos("cregar")
        )
        self.boton_filtrar_fara.clicked.connect(lambda: self.filtrar_productos("fara"))
        self.boton_filtrar_fontana.clicked.connect(
            lambda: self.filtrar_productos("fontana")
        )
        self.boton_todos.clicked.connect(self.actualizar_treeview_productos)

        global base_datos, ventana_principal_usuario_autorizado
        self.base_datos = base_datos
        self.ventana_anterior = ventana_principal_usuario_autorizado

        self.actualizar_treeviews()

    def filtrar_productos(self, filtro):
        productos_filtrados = self.base_datos.obtener_productos_filtrados(filtro)
        self.actualizar_treeview(
            self.treeview_productos,
            self.modelo_productos,
            productos_filtrados,
            [
                "id_producto",
                "producto",
                "empresa",
                "stock",
                "costo_total",
            ],
        )

    def actualizar_treeview_productos(self):
        productos = self.base_datos.obtener_productos_para_compra()
        self.actualizar_treeview(
            self.treeview_productos,
            self.modelo_productos,
            productos,
            [
                "id_producto",
                "producto",
                "empresa",
                "stock",
                "costo_total",
            ],
        )

    def actualizar_treeview_compras(self):
        compras = self.base_datos.obtener_compras_ordenadas()
        self.actualizar_treeview(
            self.treeview_compras,
            self.modelo_compras,
            compras,
            [
                "id_compra",
                "fecha",
                "empresa",
                "producto",
                "cantidad",
                "costo_unitario",
                "costo_total",
            ],
        )

    def actualizar_treeviews(self):
        self.actualizar_treeview_compras()
        self.actualizar_treeview_productos()

    def buscar_y_enfocar_producto(self):
        nombre_producto = self.input_buscar_producto.text().lower()
        if len(nombre_producto) > 0:
            items = self.modelo_productos.findItems(
                nombre_producto, QtCore.Qt.MatchContains, 1
            )  # Columna 0 es la columna de "Producto"

            if items:
                item = items[0]
                index = self.modelo_productos.indexFromItem(item)
                self.treeview_productos.setCurrentIndex(index)
                self.treeview_productos.scrollTo(index)
            else:
                self.mostrar_error_temporal(
                    self.producto_no_encontrado, "Producto no encontrado"
                )
        else:
            self.mostrar_error_temporal(
                self.producto_no_encontrado, "Producto no encontrado"
            )

    def registrar_compra(self):
        self.producto_seleccionado = self.treeview_productos.currentIndex()
        if self.producto_seleccionado.isValid():
            id_producto_comprado = self.modelo_productos.itemFromIndex(
                self.producto_seleccionado.siblingAtColumn(0)
            ).text()
            fecha = date.today()
            try:
                cantidad_comprada = int(self.input_cantidad_comprada.text())

                self.base_datos.registrar_compra(
                    fecha, id_producto_comprado, cantidad_comprada
                )
                QtWidgets.QMessageBox.information(
                    self, "Confirmacion", "Compra cargada con exito"
                )
                self.actualizar_treeviews()
            except ValueError:
                self.mostrar_error_temporal(
                    self.label_error_al_registrar, "Campos no validos"
                )
        else:
            self.mostrar_error_temporal(
                self.label_producto_no_seleccionado,
                "Seleccione un producto de la lista",
            )

    def ocultar_campos(self):
        pass


class VentanaHistorialCompras(Ventana, Ui_HistorialCompras):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boton_volver.clicked.connect(self.volver)
        self.boton_modificar_compra.clicked.connect(self.modificar_compra)
        self.boton_confirmar_modificacion.clicked.connect(self.confirmar_modificacion)
        self.boton_eliminar_compra.clicked.connect(self.eliminar_compra)
        self.boton_consultar_costos.clicked.connect(self.consultar_costos)
        self.boton_consultar.clicked.connect(self.confirmar_consulta)
        self.boton_mostrar_compras_totales.clicked.connect(self.actualizar_treeviews)
        self.boton_filtrar_compras_cregar.clicked.connect(
            lambda: self.filtrar_empresa_treeview("cregar")
        )
        self.boton_filtrar_compras_fara.clicked.connect(
            lambda: self.filtrar_empresa_treeview("fara")
        )
        self.boton_filtrar_compras_fontana.clicked.connect(
            lambda: self.filtrar_empresa_treeview("fontana")
        )
        global base_datos, ventana_principal_usuario_autorizado
        self.base_datos = base_datos
        self.ventana_anterior = ventana_principal_usuario_autorizado

        self.actualizar_treeviews()
        self.ocultar_campos()

    def actualizar_treeviews(self):
        self.actualizar_treeview_compras()

    def actualizar_treeview_compras(self):
        compras = self.base_datos.obtener_compras_ordenadas()
        self.actualizar(compras)

    def filtrar_empresa_treeview(self, empresa):
        compras_filtradas = self.base_datos.obtener_compras_segun_empresa(empresa)
        self.actualizar(compras_filtradas)

    def actualizar(self, compras):
        self.actualizar_treeview(
            self.treeview_compras,
            self.modelo_compras,
            compras,
            [
                "id_compra",
                "fecha",
                "empresa",
                "producto",
                "cantidad",
                "costo_unitario",
                "costo_total",
            ],
        )

    def modificar_compra(self):
        self.ocultar_campos()
        self.compra = self.treeview_compras.currentIndex()
        if self.compra.isValid():
            self.id_compra_a_modificar = int(
                self.modelo_compras.itemFromIndex(self.compra.siblingAtColumn(0)).text()
            )
            self.mostrar_campos_modificar_compra()
            self.actualizar_lineedits_compra_seleccionada()
        else:
            self.mostrar_error_temporal(
                self.label_modificar_compra,
                "Seleccione una compra de la lista",
            )

    def actualizar_lineedits_compra_seleccionada(self):
        compra = self.base_datos.obtener_datos_compra(self.id_compra_a_modificar)

        venta_anio = str(compra.fecha.year)
        venta_mes = str(compra.fecha.month)
        venta_dia = str(compra.fecha.day)
        self.input_fecha_dia.setText(venta_dia)
        self.input_fecha_mes.setText(venta_mes)
        self.input_fecha_anio.setText(venta_anio)
        self.input_nombre_producto.setText(str(compra.producto))
        self.input_stock.setText(str(compra.cantidad))
        self.input_costo_unitario.setText(str(compra.costo_unitario))
        if compra.empresa == "cregar":
            self.eleccion_cregar.setChecked(True)
        elif compra.empresa == "fara":
            self.eleccion_fara.setChecked(True)
        elif compra.empresa == "fontana":
            self.eleccion_fontana.setChecked(True)

    def confirmar_modificacion(self):
        try:
            nueva_fecha = date(
                int(self.input_fecha_anio.text()),
                int(self.input_fecha_mes.text()),
                int(self.input_fecha_dia.text()),
            )
            nuevo_nombre = self.input_nombre_producto.text()
            nueva_cantidad = int(self.input_stock.text())
            nuevo_costo_unitario = round(float(self.input_costo_unitario.text()), 2)
            nuevo_costo_total = nueva_cantidad * nuevo_costo_unitario

            self.base_datos.modificar_compra(
                self.id_compra_a_modificar,
                nueva_fecha,
                nuevo_nombre,
                nueva_cantidad,
                nuevo_costo_unitario,
                nuevo_costo_total,
            )
            self.ocultar_campos()
            self.actualizar_treeviews()
            QtWidgets.QMessageBox.information(
                self, "Confirmacion", "Compra modificada cone exito."
            )
        except ValueError:
            self.mostrar_error_temporal(
                self.label_campos_no_validos, "Campos no validos"
            )

    def consultar_costos(self):
        self.ocultar_campos()
        self.mostrar_campos_consultar_costos()

    def confirmar_consulta(self):
        try:
            fecha_inicial = date(
                int(self.input_anio_inicial.text()),
                int(self.input_mes_inicial.text()),
                int(self.input_dia_inicial.text()),
            )
            fecha_final = date(
                int(self.input_anio_final.text()),
                int(self.input_mes_final.text()),
                int(self.input_dia_final.text()),
            )
            if self.eleccion_cregar.isChecked():
                total_gastado = self.base_datos.consultar_total_gastado_segun_empresa(
                    fecha_inicial, fecha_final, "cregar"
                )
                self.label_resultado_total_gastado.setText(str(round(total_gastado, 2)))
            elif self.eleccion_fara.isChecked():
                total_gastado = self.base_datos.consultar_total_gastado_segun_empresa(
                    fecha_inicial, fecha_final, "fara"
                )
                self.label_resultado_total_gastado.setText(str(round(total_gastado, 2)))
            elif self.eleccion_fontana.isChecked():
                total_gastado = self.base_datos.consultar_total_gastado_segun_empresa(
                    fecha_inicial, fecha_final, "fontana"
                )
                self.label_resultado_total_gastado.setText(str(round(total_gastado, 2)))
            elif self.eleccion_todas.isChecked():
                total_gastado = self.base_datos.consultar_total_gastado(
                    fecha_inicial, fecha_final
                )
                self.label_resultado_total_gastado.setText(str(round(total_gastado, 2)))
            else:
                self.mostrar_error_temporal(
                    self.label_seleccione_opcion, "Seleccione una opcion"
                )
        except ValueError:
            self.mostrar_error_temporal(
                self.label_fecha_no_valida, "Ingrese fechas validas"
            )

    def mostrar_campos_modificar_compra(self):
        self.widget_modificar_compra.setVisible(True)

    def mostrar_campos_consultar_costos(self):
        self.widget_consultar_costos.setVisible(True)

    def eliminar_compra(self):
        self.ocultar_campos()
        compra = self.treeview_compras.currentIndex()
        if compra.isValid():
            respuesta = QtWidgets.QMessageBox.question(
                self,
                "Confirmación",
                "¿Está seguro de que desea eliminar esta compra?",
            )
            if respuesta == QtWidgets.QMessageBox.Yes:
                id_compra = int(
                    self.modelo_compras.itemFromIndex(compra.siblingAtColumn(0)).text()
                )
                self.base_datos.eliminar_compra(id_compra)
                QtWidgets.QMessageBox.information(
                    self, "Confirmacion", "Compra eliminada con exito."
                )
                self.actualizar_treeviews()
        else:
            self.mostrar_error_temporal(
                self.label_eliminar_compra,
                "Seleccione una compra de la lista",
            )

    def ocultar_campos(self):
        self.widget_modificar_compra.setVisible(False)
        self.widget_consultar_costos.setVisible(False)


class VentanaHistorialVentas(Ventana, Ui_HistorialVentas):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boton_volver.clicked.connect(self.volver)
        self.boton_modificar_venta.clicked.connect(self.modificar_venta)
        self.boton_confirmar_modificacion.clicked.connect(self.confirmar_modificacion)
        self.boton_eliminar_venta.clicked.connect(self.eliminar_venta)
        self.boton_consultar_ganancias.clicked.connect(self.consultar_ganancias)
        self.boton_consultar.clicked.connect(self.confirmar_consulta)
        self.boton_mostrar_ventas_totales.clicked.connect(self.actualizar_treeviews)
        self.boton_filtrar_ventas_efectivo.clicked.connect(
            lambda: self.filtrar_tipo_pago_treeview("efectivo")
        )
        self.boton_filtrar_ventas_posnet.clicked.connect(
            lambda: self.filtrar_tipo_pago_treeview("posnet")
        )
        self.boton_filtrar_ventas_mercadolibre.clicked.connect(
            lambda: self.filtrar_tipo_pago_treeview("mercadolibre")
        )
        global base_datos, ventana_principal_usuario_autorizado
        self.base_datos = base_datos
        self.ventana_anterior = ventana_principal_usuario_autorizado

        self.actualizar_treeviews()
        self.ocultar_campos()

    def actualizar_treeviews(self):
        self.actualizar_treeview_ventas()

    def actualizar_treeview_ventas(self):
        ventas = self.base_datos.obtener_ventas_ordenadas()
        self.actualizar(ventas)

    def filtrar_tipo_pago_treeview(self, tipo_pago):
        ventas_filtradas = self.base_datos.obtener_ventas_segun_tipo_pago(tipo_pago)
        self.actualizar(ventas_filtradas)

    def actualizar(self, ventas):
        self.actualizar_treeview(
            self.treeview_ventas,
            self.modelo_ventas,
            ventas,
            [
                "id_venta",
                "fecha",
                "producto",
                "cantidad",
                "precio_unitario",
                "precio_total",
                "tipo_pago",
                "ingreso_neto",
            ],
        )

    def modificar_venta(self):
        self.ocultar_campos()
        self.venta = self.treeview_ventas.currentIndex()
        if self.venta.isValid():
            self.id_venta_a_modificar = int(
                self.modelo_ventas.itemFromIndex(self.venta.siblingAtColumn(0)).text()
            )
            self.mostrar_campos_modificar_venta()
            self.actualizar_lineedits_venta_seleccionada()
        else:
            self.mostrar_error_temporal(
                self.label_modificar_venta,
                "Seleccione una venta de la lista",
            )

    def actualizar_lineedits_venta_seleccionada(self):
        venta = self.base_datos.obtener_datos_venta(self.id_venta_a_modificar)

        venta_anio = str(venta.fecha.year)
        venta_mes = str(venta.fecha.month)
        venta_dia = str(venta.fecha.day)
        self.input_fecha_dia.setText(venta_dia)
        self.input_fecha_mes.setText(venta_mes)
        self.input_fecha_anio.setText(venta_anio)
        self.input_nombre_producto.setText(str(venta.producto))
        self.input_stock.setText(str(venta.cantidad))
        self.input_precio_unitario.setText(str(venta.precio_unitario))

        if venta.tipo_pago == "efectivo":
            self.eleccion_efectivo.setChecked(True)
        elif venta.tipo_pago == "posnet":
            self.eleccion_posnet.setChecked(True)
        elif venta.tipo_pago == "mercadolibre":
            self.eleccion_mercadolibre.setChecked(True)

    def confirmar_modificacion(self):
        try:
            nueva_fecha = date(
                int(self.input_fecha_anio.text()),
                int(self.input_fecha_mes.text()),
                int(self.input_fecha_dia.text()),
            )
            nuevo_nombre = self.input_nombre_producto.text()
            nueva_cantidad = int(self.input_stock.text())
            nuevo_precio_unitario = round(float(self.input_precio_unitario.text()), 2)
            nuevo_precio_total = nueva_cantidad * nuevo_precio_unitario
            if self.eleccion_efectivo.isChecked():
                nuevo_tipo_pago = "efectivo"
            elif self.eleccion_posnet.isChecked():
                nuevo_tipo_pago = "posnet"
            elif self.eleccion_mercadolibre.isChecked():
                nuevo_tipo_pago = "mercadolibre"
            else:
                self.mostrar_error_temporal(
                    self.label_seleccione_tipo_pago, "Seleccione un tipo de pago"
                )
                return

            self.base_datos.modificar_venta(
                self.id_venta_a_modificar,
                nueva_fecha,
                nuevo_nombre,
                nueva_cantidad,
                nuevo_precio_unitario,
                nuevo_precio_total,
                nuevo_tipo_pago,
            )
            self.ocultar_campos()
            self.actualizar_treeviews()
            QtWidgets.QMessageBox.information(
                self, "Confirmacion", "Venta modificada con exito."
            )
        except ValueError:
            self.mostrar_error_temporal(
                self.label_campos_no_validos, "Campos no validos"
            )

    def consultar_ganancias(self):
        self.ocultar_campos()
        self.mostrar_campos_consultar_ganancias()

    def confirmar_consulta(self):
        try:
            fecha_inicial = date(
                int(self.input_anio_inicial.text()),
                int(self.input_mes_inicial.text()),
                int(self.input_dia_inicial.text()),
            )
            fecha_final = date(
                int(self.input_anio_final.text()),
                int(self.input_mes_final.text()),
                int(self.input_dia_final.text()),
            )
            if self.eleccion_efectivo_2.isChecked():
                total_ganado = self.base_datos.consultar_total_vendido_segun_tipo_pago(
                    fecha_inicial, fecha_final, "efectivo"
                )
                self.label_resultado_total_ganado.setText(str(round(total_ganado, 2)))
            elif self.eleccion_posnet_2.isChecked():
                total_ganado = self.base_datos.consultar_total_vendido_segun_tipo_pago(
                    fecha_inicial, fecha_final, "posnet"
                )
                self.label_resultado_total_ganado.setText(str(round(total_ganado, 2)))
            elif self.eleccion_mercadolibre_2.isChecked():
                total_ganado = self.base_datos.consultar_total_vendido_segun_tipo_pago(
                    fecha_inicial, fecha_final, "mercadolibre"
                )
                self.label_resultado_total_ganado.setText(str(round(total_ganado, 2)))
            elif self.eleccion_total.isChecked():
                total_ganado = self.base_datos.consultar_total_vendido(
                    fecha_inicial, fecha_final
                )
                self.label_resultado_total_ganado.setText(str(round(total_ganado, 2)))
            else:
                self.mostrar_error_temporal(
                    self.label_seleccione_tipo_pago, "Seleccione un tipo de pago"
                )
        except ValueError:
            self.mostrar_error_temporal(
                self.label_fecha_no_valida, "Ingrese fechas validas"
            )

    def mostrar_campos_modificar_venta(self):
        self.widget_modificar_venta.setVisible(True)

    def mostrar_campos_consultar_ganancias(self):
        self.widget_consultar_ingresos.setVisible(True)

    def eliminar_venta(self):
        self.ocultar_campos()
        venta = self.treeview_ventas.currentIndex()
        if venta.isValid():
            respuesta = QtWidgets.QMessageBox.question(
                self,
                "Confirmación",
                "¿Está seguro de que desea eliminar esta venta?",
            )
            if respuesta == QtWidgets.QMessageBox.Yes:
                id_venta = int(
                    self.modelo_ventas.itemFromIndex(venta.siblingAtColumn(0)).text()
                )
                self.base_datos.eliminar_venta(id_venta)
                QtWidgets.QMessageBox.information(
                    self, "Confirmacion", "Venta eliminada con exito."
                )
                self.actualizar_treeviews()
        else:
            self.mostrar_error_temporal(
                self.label_eliminar_venta,
                "Seleccione una venta de la lista",
            )

    def ocultar_campos(self):
        self.widget_consultar_ingresos.setVisible(False)
        self.widget_modificar_venta.setVisible(False)


class VentanaConsultarGanancias(Ventana, Ui_ConsultarGanancias):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boton_volver.clicked.connect(self.volver)
        self.boton_consultar.clicked.connect(self.consultar_ganado)
        global base_datos, ventana_principal_usuario_autorizado
        self.base_datos = base_datos
        self.ventana_anterior = ventana_principal_usuario_autorizado

    def actualizar_treeviews(self):
        pass

    def consultar_ganado(self):
        try:
            fecha_inicial = date(
                int(self.input_anio_inicial.text()),
                int(self.input_mes_inicial.text()),
                int(self.input_dia_inicial.text()),
            )
            fecha_final = date(
                int(self.input_anio_final.text()),
                int(self.input_mes_final.text()),
                int(self.input_dia_final.text()),
            )
            if self.eleccion_efectivo.isChecked():
                total_ganado = self.base_datos.consultar_ganancias_segun_tipo_pago(
                    fecha_inicial, fecha_final, "efectivo"
                )
                self.label_resultado_total_ganado.setText(str(round(total_ganado, 2)))
            elif self.eleccion_posnet.isChecked():
                total_ganado = self.base_datos.consultar_ganancias_segun_tipo_pago(
                    fecha_inicial, fecha_final, "posnet"
                )
                self.label_resultado_total_ganado.setText(str(round(total_ganado, 2)))
            elif self.eleccion_mercadolibre.isChecked():
                total_ganado = self.base_datos.consultar_ganancias_segun_tipo_pago(
                    fecha_inicial, fecha_final, "mercadolibre"
                )
                self.label_resultado_total_ganado.setText(str(round(total_ganado, 2)))
            elif self.eleccion_total.isChecked():
                total_ganado = self.base_datos.consultar_ganancias_totales(
                    fecha_inicial, fecha_final
                )
                self.label_resultado_total_ganado.setText(str(round(total_ganado, 2)))
            else:
                self.mostrar_error_temporal(
                    self.label_seleccione_tipo_pago, "Seleccione un pago"
                )
        except ValueError:
            self.mostrar_error_temporal(self.label_fecha_no_valida, "Fecha no valida")

    def ocultar_campos(self):
        pass


class VentanaModificarComisiones(Ventana, Ui_ModificarComisiones):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        global base_datos, ventana_principal_usuario_autorizado
        self.base_datos = base_datos
        self.ventana_anterior = ventana_principal_usuario_autorizado

        self.ocultar_campos()
        self.boton_volver.clicked.connect(self.volver)
        self.boton_modificar_comision_mercadolibre.clicked.connect(
            lambda: self.modificar_comision(
                "Nuevo porcentaje de comision de MercadoLibre", "mercadolibre"
            )
        )
        self.boton_modificar_comision_posnet.clicked.connect(
            lambda: self.modificar_comision(
                "Nuevo porcentaje de comision por Posnet", "posnet"
            )
        )

    def modificar_comision(self, titulo, tipo_pago):
        self.ocultar_campos()
        self.mostrar_campos_modificar_comision()
        self.label_ingrese_porcentaje.setText(titulo)
        comision = str(self.base_datos.obtener_comision(tipo_pago))
        self.input_porcentaje_comision.setText(comision)
        try:
            self.boton_modificar_comision.clicked.disconnect()
        except TypeError:
            pass
        self.boton_modificar_comision.clicked.connect(
            lambda: self.confirmar_modificacion_comision(tipo_pago)
        )

    def confirmar_modificacion_comision(self, tipo_pago):
        try:
            nueva_comision = float(self.input_porcentaje_comision.text())
            self.base_datos.modificar_impuesto(tipo_pago, nueva_comision)
            self.ocultar_campos()
            QtWidgets.QMessageBox.information(
                self, "Exito", "Comision modificada correctamente."
            )
        except ValueError:
            self.mostrar_error_temporal(
                self.label_porcentaje_no_valido, "Ingrese un porcentaje valido"
            )

    def mostrar_campos_modificar_comision(self):
        self.widget_modificar_comision.setVisible(True)

    def ocultar_campos(self):
        self.widget_modificar_comision.setVisible(False)

    def actualizar_treeviews(self):
        pass


def generar_ventanas(base):
    global base_datos, ventana_bienvenida, ventana_login, ventana_registrar_ventas_autorizado, ventana_registrar_ventas, ventana_principal_usuario_autorizado, ventana_usuarios, ventana_elegir_empresa, ventana_stock_cregar, ventana_stock_fara, ventana_stock_fontana, ventana_registrar_compras, ventana_historial_compras, ventana_historial_ventas, ventana_consultar_ganancias, ventana_modificar_comisiones
    base_datos = base
    ventana_bienvenida = VentanaBienvenida()
    ventana_login = VentanaLogin()
    ventana_registrar_ventas = VentanaRegistrarVentasVendedor()
    ventana_principal_usuario_autorizado = VentanaPrincipalUsuarioAutorizado()
    ventana_registrar_ventas_autorizado = VentanaRegistrarVentasAutorizado()
    ventana_usuarios = VentanaUsuarios()
    ventana_elegir_empresa = VentanaElegirEmpresa()
    ventana_stock_cregar = VentanaStockCregar()
    ventana_stock_fara = VentanaStockFara()
    ventana_stock_fontana = VentanaStockFontana()
    ventana_registrar_compras = VentanaRegistrarCompras()
    ventana_historial_compras = VentanaHistorialCompras()
    ventana_historial_ventas = VentanaHistorialVentas()
    ventana_consultar_ganancias = VentanaConsultarGanancias()
    ventana_modificar_comisiones = VentanaModificarComisiones()
    return ventana_bienvenida
