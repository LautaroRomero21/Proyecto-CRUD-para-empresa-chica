from PyQt5 import QtWidgets, QtCore, QtGui
from modulo import base_datos
from datetime import date
from ventanas.bienvenida import Ui_UserSelection
from ventanas.login import Ui_Form
from ventanas.ventana_principal_autorizada import Ui_VentanaPrincipalAutorizada
from ventanas.registrar_ventas_vendedor import Ui_RegistrarVentaVendedor
from ventanas.registrar_ventas_autorizado import Ui_RegistrarVentasAutorizado
from ventanas.usuarios import Ui_Usuarios
from ventanas.stock_disponible import Ui_StockDisponible
from ventanas.elegir_tipo_compra import Ui_ElegirTipoCompra
from ventanas.registrar_compra_producto_listado import Ui_RegistrarCompraProductoListado
from ventanas.registrar_compra_producto_nuevo import Ui_RegistrarCompraProductoNuevo
from ventanas.consultar_ganancias import Ui_ConsultarGanancias
from ventanas.historial_compras import Ui_HistorialCompras
from ventanas.historial_ventas import Ui_HistorialVentas


class Ventana(QtWidgets.QWidget):
    def mostrar_error_temporal(self, label, mensaje):
        self.tiempo_ocultar = QtCore.QTimer()
        label.setText(mensaje)
        self.tiempo_ocultar.timeout.connect(lambda: self.ocultar_label_temporal(label))
        self.tiempo_ocultar.start(2000)

    def ocultar_label_temporal(self, label):
        label.clear()
        self.tiempo_ocultar.stop()

    def actualizar_treeview(self, treeview, modelo, columnas, datos, tamanios_columnas):
        modelo.clear()
        treeview.setModel(modelo)
        modelo.setHorizontalHeaderLabels(columnas)

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        header = treeview.header()
        header.setDefaultAlignment(QtCore.Qt.AlignHCenter)
        header.setFont(font)

        for dato in datos:
            items = [QtGui.QStandardItem(str(getattr(dato, col))) for col in columnas]

            for item in items:
                item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)

            modelo.appendRow(items)

        for i, tamano in enumerate(tamanios_columnas):
            treeview.setColumnWidth(i, tamano)

    def volver(self):
        self.hide()
        self.ocultar_campos()
        self.ventana_anterior.show()


class VentanaBienvenida(QtWidgets.QWidget, Ui_UserSelection):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boton_vendedor.clicked.connect(self.ir_a_login_como_vendedor)
        self.boton_usuario_autorizado.clicked.connect(
            self.ir_a_login_como_usuario_autorizado
        )
        self.tipo_usuario = None

    def ir_a_login_como_vendedor(self):
        self.hide()
        self.tipo_usuario = "vendedor"
        ventana_login.show()

    def ir_a_login_como_usuario_autorizado(self):
        self.hide()
        self.tipo_usuario = "usuario_autorizado"
        ventana_login.show()


class VentanaLogin(Ventana, Ui_Form):
    def __init__(self, base_datos, ventana_anterior):
        super().__init__()
        self.setupUi(self)
        self.boton_ingresar.clicked.connect(self.verificar_usuario)
        self.boton_volver.clicked.connect(self.volver)
        self.base_datos = base_datos
        self.ventana_anterior = ventana_anterior

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
    def __init__(self, base_datos):
        super().__init__()
        self.setupUi(self)
        self.boton_buscar_producto.clicked.connect(self.buscar_y_enfocar_producto)
        self.boton_registrar_venta.clicked.connect(self.verificar_cantidad_a_vender)
        self.base_datos = base_datos

        self.modelo_productos = QtGui.QStandardItemModel(self)
        self.modelo_ventas = QtGui.QStandardItemModel(self)

        self.actualizar_treeviews()

    def actualizar_treeview_productos(self):
        columnas = ["id", "producto", "stock", "precio_unitario"]
        datos = self.base_datos.obtener_productos_stock()
        lista_widths = [80, 340, 50, 50]
        self.actualizar_treeview(
            self.treeview_productos,
            self.modelo_productos,
            columnas,
            datos,
            lista_widths,
        )

    def actualizar_treeview_ventas(self):
        columnas = [
            "id_venta",
            "fecha",
            "producto",
            "cantidad",
            "precio_unitario",
            "precio_total",
            "tipo_pago",
        ]
        datos = self.base_datos.obtener_ventas_ordenadas()
        lista_widths = [70, 95, 90, 75, 100, 100, 85]
        self.actualizar_treeview(
            self.treeview_ventas,
            self.modelo_ventas,
            columnas,
            datos,
            lista_widths,
        )

    def actualizar_treeviews(self):
        self.actualizar_treeview_productos()
        self.actualizar_treeview_ventas()

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

    def verificar_cantidad_a_vender(self):
        producto_seleccionado = self.treeview_productos.currentIndex()

        if producto_seleccionado.isValid():
            cantidad_stock = int(
                self.modelo_productos.itemFromIndex(
                    producto_seleccionado.siblingAtColumn(2)
                ).text()
            )
            try:
                cantidad_a_vender = int(self.input_cantidad_vendida.text())
                if cantidad_a_vender > cantidad_stock:
                    self.mostrar_error_temporal(
                        self.label_cantidad_invalida,
                        "No hay stock suficiente para esa venta",
                    )
                elif cantidad_a_vender < 1:
                    self.mostrar_error_temporal(
                        self.label_cantidad_invalida,
                        "Por favor Ingrese una cantidad valida",
                    )
                else:
                    id_producto = int(
                        self.modelo_productos.itemFromIndex(
                            producto_seleccionado.siblingAtColumn(0)
                        ).text()
                    )
                    if self.eleccion_efectivo.isChecked():
                        self.base_datos.registrar_venta(
                            id_producto, cantidad_a_vender, "efectivo"
                        )
                        QtWidgets.QMessageBox.information(
                            self, "Venta Cargada", "Venta registrada con exito"
                        )
                    elif self.eleccion_posnet.isChecked():
                        self.base_datos.registrar_venta(
                            id_producto, cantidad_a_vender, "posnet"
                        )
                        QtWidgets.QMessageBox.information(
                            self, "Venta Cargada", "Venta registrada con exito"
                        )
                    elif self.eleccion_mercadopago.isChecked():
                        self.base_datos.registrar_venta(
                            id_producto, cantidad_a_vender, "mercadopago"
                        )
                        QtWidgets.QMessageBox.information(
                            self, "Venta Cargada", "Venta registrada con exito"
                        )
                    else:
                        self.mostrar_error_temporal(
                            self.label_tipo_pago_no_elegido,
                            "Seleccione un tipo de pago",
                        )
                    self.actualizar_treeview_productos()
                    self.actualizar_treeview_ventas()

            except ValueError:
                self.mostrar_error_temporal(
                    self.label_cantidad_invalida,
                    "Por favor ingrese una cantidad valida",
                )
        else:
            self.mostrar_error_temporal(
                self.label_cantidad_invalida,
                "Seleccione un producto primero",
            )

    def ocultar_campos(self):
        pass


class VentanaRegistrarVentasVendedor(VentanaRegistrarVentas, Ui_RegistrarVentaVendedor):
    def __init__(self, base_datos):
        super().__init__(base_datos)


class VentanaRegistrarVentasAutorizado(
    VentanaRegistrarVentas, Ui_RegistrarVentasAutorizado
):
    def __init__(self, base_datos, ventana_anterior):
        super().__init__(base_datos)
        self.boton_volver.clicked.connect(self.volver)
        self.ventana_anterior = ventana_anterior


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
            lambda: self.abrir_ventana_seleccionada(ventana_stock_disponible)
        )
        self.boton_registrar_compras.clicked.connect(
            lambda: self.abrir_ventana_seleccionada(ventana_elegir_tipo_compra)
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
    def __init__(self, base_datos, ventana_anterior):
        super().__init__()
        self.setupUi(self)
        self.confirmar = None
        self.base_datos = base_datos
        self.ventana_anterior = ventana_anterior

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

        self.modelo_vendedores = QtGui.QStandardItemModel(self)
        self.modelo_usuarios_autorizados = QtGui.QStandardItemModel(self)

        self.actualizar_treeview_vendedores()
        self.actualizar_treeview_usuarios_autorizados()

    def actualizar_treeview_vendedores(self):
        self.modelo_vendedores.clear()
        self.treeview_vendedores.setModel(self.modelo_vendedores)
        self.modelo_vendedores.setHorizontalHeaderLabels(["Usuario", "Contraseña"])

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        header_vendedores = self.treeview_vendedores.header()
        header_vendedores.setDefaultAlignment(QtCore.Qt.AlignHCenter)
        header_vendedores.setFont(font)

        vendedores = self.base_datos.obtener_vendedores_ordenados()

        for vendedor in vendedores:
            item_usuario = QtGui.QStandardItem(vendedor.usuario)
            item_contrasenia = QtGui.QStandardItem(vendedor.contraseña)

            item_usuario.setFlags(item_usuario.flags() & ~QtCore.Qt.ItemIsEditable)
            item_contrasenia.setFlags(
                item_contrasenia.flags() & ~QtCore.Qt.ItemIsEditable
            )

            self.modelo_vendedores.appendRow([item_usuario, item_contrasenia])

        self.treeview_vendedores.setColumnWidth(0, 150)
        self.treeview_vendedores.setColumnWidth(1, 150)

    def actualizar_treeview_usuarios_autorizados(self):
        self.modelo_usuarios_autorizados.clear()
        self.treeview_usuarios_autorizados.setModel(self.modelo_usuarios_autorizados)
        self.modelo_usuarios_autorizados.setHorizontalHeaderLabels(
            ["Usuario", "Contraseña"]
        )

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        header_usuarios_autorizados = self.treeview_usuarios_autorizados.header()
        header_usuarios_autorizados.setDefaultAlignment(QtCore.Qt.AlignHCenter)
        header_usuarios_autorizados.setFont(font)

        usuarios_autorizados = self.base_datos.obtener_usuarios_autorizados_ordenados()

        for usuario in usuarios_autorizados:
            item_usuario = QtGui.QStandardItem(usuario.usuario)
            item_contrasenia = QtGui.QStandardItem(usuario.contraseña)

            item_usuario.setFlags(item_usuario.flags() & ~QtCore.Qt.ItemIsEditable)
            item_contrasenia.setFlags(
                item_contrasenia.flags() & ~QtCore.Qt.ItemIsEditable
            )

            self.modelo_usuarios_autorizados.appendRow([item_usuario, item_contrasenia])

        self.treeview_usuarios_autorizados.setColumnWidth(0, 150)
        self.treeview_usuarios_autorizados.setColumnWidth(1, 150)

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


class VentanaStockDisponible(Ventana, Ui_StockDisponible):
    def __init__(self, base_datos, ventana_anterior):
        super().__init__()
        self.setupUi(self)
        self.base_datos = base_datos
        self.ventana_anterior = ventana_anterior

        self.modelo_productos = QtGui.QStandardItemModel(self)
        self.actualizar_treeview_productos()
        self.boton_buscar_producto.clicked.connect(self.buscar_y_enfocar_producto)
        self.boton_volver.clicked.connect(self.volver)
        self.boton_agregar_producto.clicked.connect(self.agregar_producto)
        self.boton_eliminar_producto.clicked.connect(self.eliminar_producto)
        self.boton_modificar_producto.clicked.connect(self.modificar_producto)
        self.boton_modificar_precio_general.clicked.connect(
            self.modificar_precio_general
        )
        self.boton_confirmar_porcentaje.clicked.connect(
            self.confirmar_modificacion_precio_general
        )
        self.boton_confirmar_registro.clicked.connect(self.confirmar_registro)
        self.boton_confirmar_modificacion.clicked.connect(self.confirmar_modificacion)

        self.ocultar_campos()

    def actualizar_treeview_productos(self):
        columnas = ["id", "producto", "stock", "precio_unitario"]
        datos = self.base_datos.obtener_productos_stock()
        lista_widths = [80, 270, 50, 50]
        self.actualizar_treeview(
            self.treeview_productos,
            self.modelo_productos,
            columnas,
            datos,
            lista_widths,
        )

    def actualizar_treeviews(self):
        self.actualizar_treeview_productos()

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

    def agregar_producto(self):
        self.mostrar_campos_registrar_producto()

    def confirmar_registro(self):
        try:
            nuevo_producto = self.input_nombre_producto.text()
            stock_inicial = int(self.input_stock.text())
            precio_unitario = round(float(self.input_precio_unitario.text()), 2)
            if not self.base_datos.producto_repetido_en_stock(nuevo_producto):
                self.base_datos.agregar_producto_a_stock(
                    nuevo_producto, stock_inicial, precio_unitario
                )
                QtWidgets.QMessageBox.information(
                    self, "Confirmacion", "Nuevo producto registrado con exito."
                )
                self.actualizar_treeview_productos()
            else:
                self.mostrar_error_temporal(self.label_error, "Producto ya existente")
        except ValueError:
            self.mostrar_error_temporal(self.label_error, "Campos no validos.")

    def eliminar_producto(self):
        self.ocultar_campos()
        producto = self.treeview_productos.currentIndex()
        if producto.isValid():
            respuesta = QtWidgets.QMessageBox.question(
                self,
                "Confirmación",
                "¿Está seguro de que desea eliminar este producto?",
            )
            if respuesta == QtWidgets.QMessageBox.Yes:
                id_producto = int(
                    self.modelo_productos.itemFromIndex(
                        producto.siblingAtColumn(0)
                    ).text()
                )
                self.base_datos.eliminar_producto_en_stock(id_producto)
                QtWidgets.QMessageBox.information(
                    self, "Confirmacion", "Venta eliminada con exito."
                )
                self.actualizar_treeview_productos()
        else:
            self.mostrar_error_temporal(
                self.label_eliminar_producto,
                "Seleccione un producto de la lista",
            )

    def modificar_producto(self):
        self.ocultar_campos()
        self.producto = self.treeview_productos.currentIndex()
        if self.producto.isValid():
            self.id_producto_a_modificar = int(
                self.modelo_productos.itemFromIndex(
                    self.producto.siblingAtColumn(0)
                ).text()
            )
            self.mostrar_campos_modificar_producto()
            self.actualizar_lineedits_producto_seleccionado(self.producto)
        else:
            self.mostrar_error_temporal(
                self.label_modificar_producto,
                "Seleccione un producto de la lista",
            )

    def actualizar_lineedits_producto_seleccionado(self, producto_index):
        id_producto = int(
            self.modelo_productos.itemFromIndex(
                producto_index.siblingAtColumn(0)
            ).text()
        )
        producto = self.base_datos.obtener_datos_producto(id_producto)

        self.input_nombre_producto.setText(producto.producto)
        self.input_stock.setText(str(producto.stock))
        self.input_precio_unitario.setText(str(producto.precio_unitario))

    def confirmar_modificacion(self):
        try:
            nuevo_nombre = self.input_nombre_producto.text()
            nuevo_stock = int(self.input_stock.text())
            nuevo_precio_unitario = round(float(self.input_precio_unitario.text()), 2)
            self.base_datos.modificar_producto_en_stock(
                self.id_producto_a_modificar,
                nuevo_nombre,
                nuevo_stock,
                nuevo_precio_unitario,
            )
            self.actualizar_treeview_productos()
            QtWidgets.QMessageBox.information(
                self, "Confirmacion", "Venta modificada con exito"
            )
            self.ocultar_campos()
        except ValueError:
            self.mostrar_error_temporal(self.label_error, "Campos no validos.")

    def modificar_precio_general(self):
        self.ocultar_campos()
        self.mostrar_campos_modificar_precio_general()

    def confirmar_modificacion_precio_general(self):
        try:
            porcentaje = float(self.input_porcentaje.text())
            self.base_datos.modificar_precio_general_stock(porcentaje)
            QtWidgets.QMessageBox.information(
                self, "Confirmacion", "Precios actualizados con exito."
            )
            self.ocultar_campos()
            self.actualizar_treeview_productos()
        except ValueError:
            self.mostrar_error_temporal(
                self.label_ingresar_porcentaje_error,
                "Ingrese un porcentaje valido",
            )

    def mostrar_campos_registrar_producto(self):
        self.ocultar_campos()
        self.label_nombre_producto.setVisible(True)
        self.label_nombre_producto.setText("Nombre del nuevo producto:")
        self.input_nombre_producto.setVisible(True)
        self.label_stock.setVisible(True)
        self.label_stock.setText("Stock Inicial:")
        self.input_stock.setVisible(True)
        self.label_precio_unitario.setVisible(True)
        self.label_precio_unitario.setText("Precio Unitario:")
        self.input_precio_unitario.setVisible(True)
        self.label_error.setVisible(True)
        self.boton_confirmar_registro.setVisible(True)
        self.label_signo_peso.setVisible(True)

    def mostrar_campos_modificar_producto(self):
        self.ocultar_campos()
        self.mostrar_campos_registrar_producto()
        self.boton_confirmar_registro.setVisible(False)
        self.label_nombre_producto.setText("Nombre del producto:")
        self.label_stock.setText("Stock:")
        self.boton_confirmar_modificacion.setVisible(True)

    def mostrar_campos_modificar_precio_general(self):
        self.ocultar_campos()
        self.label_ingresar_porcentaje.setVisible(True)
        self.input_porcentaje.setVisible(True)
        self.label_porcentaje.setVisible(True)
        self.boton_confirmar_porcentaje.setVisible(True)
        self.label_ingresar_porcentaje_error.setVisible(True)

    def ocultar_campos(self):
        self.label_nombre_producto.setVisible(False)
        self.input_nombre_producto.setVisible(False)
        self.input_nombre_producto.clear()
        self.label_stock.setVisible(False)
        self.input_stock.setVisible(False)
        self.input_stock.clear()
        self.label_precio_unitario.setVisible(False)
        self.input_precio_unitario.setVisible(False)
        self.label_error.setVisible(False)
        self.boton_confirmar_registro.setVisible(False)
        self.boton_confirmar_modificacion.setVisible(False)
        self.label_ingresar_porcentaje.setVisible(False)
        self.input_porcentaje.setVisible(False)
        self.input_precio_unitario.clear()
        self.label_porcentaje.setVisible(False)
        self.label_signo_peso.setVisible(False)
        self.boton_confirmar_porcentaje.setVisible(False)
        self.label_ingresar_porcentaje_error.setVisible(False)
        self.label_ingresar_porcentaje_error.clear()


class VentanaElegirTipoCompra(QtWidgets.QWidget, Ui_ElegirTipoCompra):
    def __init__(self, ventana_anterior):
        super().__init__()
        self.setupUi(self)
        self.ventana_anterior = ventana_anterior

        self.boton_volver.clicked.connect(self.volver)
        self.boton_producto_en_stock.clicked.connect(
            self.ir_a_registrar_compra_producto_listado
        )
        self.boton_nuevo_producto.clicked.connect(
            self.ir_a_registrar_compra_producto_nuevo
        )
        self.base_datos = base_datos

    def ir_a_registrar_compra_producto_nuevo(self):
        self.hide()
        ventana_registrar_compra_producto_nuevo.show()
        ventana_registrar_compra_producto_nuevo.actualizar_treeviews()

    def ir_a_registrar_compra_producto_listado(self):
        self.hide()
        ventana_registrar_compra_producto_listado.show()
        ventana_registrar_compra_producto_listado.actualizar_treeviews()

    def actualizar_treeviews(self):
        pass

    def volver(self):
        self.hide()
        self.ventana_anterior.show()


class VentanaRegistrarCompras(Ventana):
    def __init__(self, base_datos, ventana_anterior):
        super().__init__()
        self.setupUi(self)
        self.boton_volver.clicked.connect(self.volver)
        self.boton_buscar_producto.clicked.connect(self.buscar_y_enfocar_producto)
        self.boton_registrar_compra.clicked.connect(self.registrar_compra)
        self.base_datos = base_datos
        self.ventana_anterior = ventana_anterior

        # Inicializar los modelos como atributos de la clase
        self.modelo_productos = QtGui.QStandardItemModel(self)
        self.modelo_compras = QtGui.QStandardItemModel(self)

        self.actualizar_treeview_productos()
        self.actualizar_treeview_compras()

    def actualizar_treeview_productos(self):
        columnas = ["id", "producto", "stock", "precio_unitario"]
        datos = self.base_datos.obtener_productos_stock()
        lista_widths = [80, 300, 50, 50]
        self.actualizar_treeview(
            self.treeview_productos,
            self.modelo_productos,
            columnas,
            datos,
            lista_widths,
        )

    def actualizar_treeview_compras(self):
        columnas = [
            "id_compra",
            "fecha",
            "producto",
            "cantidad",
            "costo_unitario",
            "costo_total",
            "tipo_pago",
        ]
        datos = self.base_datos.obtener_compras_ordenadas()
        lista_widths = [95, 95, 90, 75, 90, 95, 85]
        self.actualizar_treeview(
            self.treeview_compras,
            self.modelo_compras,
            columnas,
            datos,
            lista_widths,
        )

    def actualizar_treeviews(self):
        self.actualizar_treeview_compras()
        self.actualizar_treeview_productos()

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

    def registrar_compra(self):
        pass

    def ocultar_campos(self):
        pass


class VentanaRegistrarCompraProductoNuevo(
    VentanaRegistrarCompras, Ui_RegistrarCompraProductoNuevo
):
    def __init__(self, base_datos, ventana_anterior):
        super().__init__(base_datos, ventana_anterior)

    def registrar_compra(self):
        try:
            tipo_pago = None
            fecha = date.today()
            nombre_producto = self.input_nombre_producto.text()
            cantidad_comprada = int(self.input_cantidad_comprada.text())
            costo_unitario = round(float(self.input_costo_unitario.text()), 2)
            precio_unitario = round(float(self.input_precio_unitario.text()), 2)
            if self.eleccion_efectivo.isChecked():
                tipo_pago = "efectivo"
            elif self.eleccion_posnet.isChecked():
                tipo_pago = "posnet"
            elif self.eleccion_mercadopago.isChecked():
                tipo_pago = "mercadopago"

            if tipo_pago is not None:
                if not self.base_datos.producto_repetido_en_stock(nombre_producto):
                    self.base_datos.registrar_compra(
                        fecha,
                        nombre_producto,
                        cantidad_comprada,
                        costo_unitario,
                        tipo_pago,
                    )
                    QtWidgets.QMessageBox.information(
                        self, "Confirmacion", "Compra cargada con exito"
                    )
                    self.base_datos.agregar_producto_a_stock(
                        nombre_producto, cantidad_comprada, precio_unitario
                    )
                    self.actualizar_treeviews()
                else:
                    self.mostrar_error_temporal(
                        self.label_error_al_registrar, "El producto ya existe"
                    )
            else:
                self.mostrar_error_temporal(
                    self.label_error_al_registrar, "Elija un tipo de pago"
                )

        except ValueError:
            self.mostrar_error_temporal(
                self.label_error_al_registrar, "Campos no validos"
            )


class VentanaRegistrarCompraProductoListado(
    VentanaRegistrarCompras, Ui_RegistrarCompraProductoListado
):
    def __init__(self, base_datos, ventana_anterior):
        super().__init__(
            base_datos,
            ventana_anterior,
        )

    def registrar_compra(self):
        self.producto_seleccionado = self.treeview_productos.currentIndex()
        tipo_pago = None
        if self.producto_seleccionado.isValid():
            id_producto_a_modificar = int(
                self.modelo_productos.itemFromIndex(
                    self.producto_seleccionado.siblingAtColumn(0)
                ).text()
            )
            try:
                fecha = date.today()
                nombre_producto = self.modelo_productos.itemFromIndex(
                    self.producto_seleccionado.siblingAtColumn(1)
                ).text()
                cantidad_comprada = int(self.input_cantidad_comprada.text())
                costo_unitario = round(float(self.input_costo_unitario.text()), 2)

                if self.eleccion_efectivo.isChecked():
                    tipo_pago = "efectivo"
                elif self.eleccion_posnet.isChecked():
                    tipo_pago = "posnet"
                elif self.eleccion_mercadopago.isChecked():
                    tipo_pago = "mercadopago"

                if tipo_pago is not None:
                    self.base_datos.registrar_compra(
                        fecha,
                        nombre_producto,
                        cantidad_comprada,
                        costo_unitario,
                        tipo_pago,
                    )
                    self.base_datos.aumentar_stock_producto(
                        id_producto_a_modificar, cantidad_comprada
                    )

                    QtWidgets.QMessageBox.information(
                        self, "Confirmacion", "Compra cargada con exito"
                    )
                    self.actualizar_treeviews()
                else:
                    self.mostrar_error_temporal(
                        self.label_error_al_registrar, "Elija un tipo de pago"
                    )
            except ValueError:
                self.mostrar_error_temporal(
                    self.label_error_al_registrar, "Campos no validos"
                )
        else:
            self.mostrar_error_temporal(
                self.label_producto_no_seleccionado,
                "Seleccione un producto de la lista",
            )


class VentanaHistorialCompras(Ventana, Ui_HistorialCompras):
    def __init__(self, base_datos, ventana_anterior):
        super().__init__()
        self.setupUi(self)
        self.boton_volver.clicked.connect(self.volver)
        self.boton_agregar_compra.clicked.connect(self.agregar_compra)
        self.boton_modificar_compra.clicked.connect(self.modificar_compra)
        self.boton_confirmar_modificacion.clicked.connect(self.confirmar_modificacion)
        self.boton_confirmar_registro.clicked.connect(self.confirmar_compra)
        self.boton_eliminar_compra.clicked.connect(self.eliminar_compra)
        self.boton_consultar_costos.clicked.connect(self.consultar_costos)
        self.boton_consultar.clicked.connect(self.confirmar_consulta)
        self.boton_mostrar_compras_totales.clicked.connect(self.actualizar_treeviews)
        self.boton_filtrar_compras_efectivo.clicked.connect(
            lambda: self.filtrar_tipo_pago_treeview("efectivo")
        )
        self.boton_filtrar_compras_posnet.clicked.connect(
            lambda: self.filtrar_tipo_pago_treeview("posnet")
        )
        self.boton_filtrar_compras_mercadopago.clicked.connect(
            lambda: self.filtrar_tipo_pago_treeview("mercadopago")
        )
        self.base_datos = base_datos
        self.ventana_anterior = ventana_anterior

        self.modelo_compras = QtGui.QStandardItemModel(self)

        self.actualizar_treeviews()
        self.ocultar_campos()

    def actualizar_treeviews(self):
        self.actualizar_treeview_compras()

    def actualizar_treeview_compras(self):
        columnas = [
            "id_compra",
            "fecha",
            "producto",
            "cantidad",
            "costo_unitario",
            "costo_total",
            "tipo_pago",
        ]
        datos = self.base_datos.obtener_compras_ordenadas()
        lista_widths = [95, 95, 90, 75, 90, 95, 85]
        self.actualizar_treeview(
            self.treeview_compras,
            self.modelo_compras,
            columnas,
            datos,
            lista_widths,
        )

    def filtrar_tipo_pago_treeview(self, tipo_pago):
        self.modelo_compras.removeRows(0, self.modelo_compras.rowCount())

        compras = self.base_datos.obtener_compras_segun_tipo_pago(tipo_pago)

        for compra in compras:
            item_id_compra = QtGui.QStandardItem(str(compra.id_compra))
            item_fecha = QtGui.QStandardItem(str(compra.fecha))
            item_producto = QtGui.QStandardItem(compra.producto)
            item_cantidad = QtGui.QStandardItem(str(compra.cantidad))
            item_costo_unitario = QtGui.QStandardItem("$" + str(compra.costo_unitario))
            item_costo_total = QtGui.QStandardItem("$" + str(compra.costo_total))
            item_tipo_pago = QtGui.QStandardItem(compra.tipo_pago)

            item_id_compra.setFlags(item_id_compra.flags() & ~QtCore.Qt.ItemIsEditable)
            item_fecha.setFlags(item_fecha.flags() & ~QtCore.Qt.ItemIsEditable)
            item_producto.setFlags(item_producto.flags() & ~QtCore.Qt.ItemIsEditable)
            item_cantidad.setFlags(item_cantidad.flags() & ~QtCore.Qt.ItemIsEditable)
            item_costo_unitario.setFlags(
                item_costo_unitario.flags() & ~QtCore.Qt.ItemIsEditable
            )
            item_costo_total.setFlags(
                item_costo_total.flags() & ~QtCore.Qt.ItemIsEditable
            )
            item_tipo_pago.setFlags(item_tipo_pago.flags() & ~QtCore.Qt.ItemIsEditable)

            self.modelo_compras.appendRow(
                [
                    item_id_compra,
                    item_fecha,
                    item_producto,
                    item_cantidad,
                    item_costo_unitario,
                    item_costo_total,
                    item_tipo_pago,
                ]
            )

    def agregar_compra(self):
        self.input_fecha_dia.clear()
        self.input_fecha_mes.clear()
        self.input_fecha_anio.clear()
        self.input_nombre_producto.clear()
        self.input_stock.clear()
        self.input_costo_unitario.clear()
        self.ocultar_campos()
        self.mostrar_campos_modificar_compra()
        self.boton_confirmar_modificacion.setVisible(False)
        self.boton_confirmar_registro.setVisible(True)

    def confirmar_compra(self):
        try:
            nuevo_tipo_pago = None
            nueva_fecha = date(
                int(self.input_fecha_anio.text()),
                int(self.input_fecha_mes.text()),
                int(self.input_fecha_dia.text()),
            )
            nuevo_nombre = self.input_nombre_producto.text()
            nueva_cantidad = int(self.input_stock.text())
            nuevo_costo_unitario = round(float(self.input_costo_unitario.text()), 2)
            if self.eleccion_efectivo.isChecked():
                nuevo_tipo_pago = "efectivo"
            elif self.eleccion_posnet.isChecked():
                nuevo_tipo_pago = "posnet"
            elif self.eleccion_mercadopago.isChecked():
                nuevo_tipo_pago = "mercadopago"
            if nuevo_tipo_pago is not None:
                self.base_datos.registrar_compra(
                    nueva_fecha,
                    nuevo_nombre,
                    nueva_cantidad,
                    nuevo_costo_unitario,
                    nuevo_tipo_pago,
                )
                QtWidgets.QMessageBox.information(
                    self, "Confirmacion", "Compra agregada con exito."
                )
                self.ocultar_campos()
                self.actualizar_treeviews()
            else:
                self.mostrar_error_temporal(
                    self.label_seleccione_tipo_pago, "Seleccione un tipo de pago"
                )
        except ValueError:
            self.mostrar_error_temporal(
                self.label_campos_no_validos, "Campos no validos"
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
        if compra.tipo_pago == "efectivo":
            self.eleccion_efectivo.setChecked(True)
        elif compra.tipo_pago == "posnet":
            self.eleccion_posnet.setChecked(True)
        elif compra.tipo_pago == "mercadopago":
            self.eleccion_mercadopago.setChecked(True)

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
            if self.eleccion_efectivo.isChecked():
                nuevo_tipo_pago = "efectivo"
            elif self.eleccion_posnet.isChecked():
                nuevo_tipo_pago = "posnet"
            elif self.eleccion_mercadopago.isChecked():
                nuevo_tipo_pago = "mercadopago"

            self.base_datos.modificar_compra(
                self.id_compra_a_modificar,
                nueva_fecha,
                nuevo_nombre,
                nueva_cantidad,
                nuevo_costo_unitario,
                nuevo_costo_total,
                nuevo_tipo_pago,
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
            if self.eleccion_efectivo_2.isChecked():
                total_gastado = self.base_datos.consultar_total_gastado_segun_tipo_pago(
                    fecha_inicial, fecha_final, "efectivo"
                )
                self.label_resultado_total_gastado.setText(str(round(total_gastado, 2)))
            elif self.eleccion_posnet_2.isChecked():
                total_gastado = self.base_datos.consultar_total_gastado_segun_tipo_pago(
                    fecha_inicial, fecha_final, "posnet"
                )
                self.label_resultado_total_gastado.setText(str(round(total_gastado, 2)))
            elif self.eleccion_mercadopago_2.isChecked():
                total_gastado = self.base_datos.consultar_total_gastado_segun_tipo_pago(
                    fecha_inicial, fecha_final, "mercadopago"
                )
                self.label_resultado_total_gastado.setText(str(round(total_gastado, 2)))
            elif self.eleccion_total.isChecked():
                total_gastado = self.base_datos.consultar_total_gastado(
                    fecha_inicial, fecha_final
                )
                self.label_resultado_total_gastado.setText(str(round(total_gastado, 2)))
            else:
                self.mostrar_error_temporal(
                    self.label_seleccione_tipo_pago, "Seleccione un tipo de pago"
                )
        except ValueError:
            self.mostrar_error_temporal(
                self.label_fecha_no_valida, "Ingrese fechas validas"
            )

    def mostrar_campos_modificar_compra(self):
        self.label_fecha.setVisible(True)
        self.input_fecha_dia.setVisible(True)
        self.input_fecha_mes.setVisible(True)
        self.input_fecha_anio.setVisible(True)
        self.label_nombre_producto.setVisible(True)
        self.input_nombre_producto.setVisible(True)
        self.label_stock.setVisible(True)
        self.input_stock.setVisible(True)
        self.label_costo_unitario.setVisible(True)
        self.input_costo_unitario.setVisible(True)
        self.label_signo_peso.setVisible(True)
        self.label_tipo_pago.setVisible(True)
        self.eleccion_efectivo.setVisible(True)
        self.eleccion_posnet.setVisible(True)
        self.eleccion_mercadopago.setVisible(True)
        self.boton_confirmar_modificacion.setVisible(True)

    def mostrar_campos_consultar_costos(self):
        self.label_fecha_inicial.setVisible(True)
        self.input_dia_inicial.setVisible(True)
        self.input_mes_inicial.setVisible(True)
        self.input_anio_inicial.setVisible(True)
        self.label_fecha_final.setVisible(True)
        self.input_dia_final.setVisible(True)
        self.input_mes_final.setVisible(True)
        self.input_anio_final.setVisible(True)
        self.boton_consultar.setVisible(True)
        self.label_total_gastado.setVisible(True)
        self.label_resultado_total_gastado.setVisible(True)
        self.eleccion_efectivo_2.setVisible(True)
        self.eleccion_posnet_2.setVisible(True)
        self.eleccion_mercadopago_2.setVisible(True)
        self.eleccion_total.setVisible(True)
        self.label_tipo_pago_consulta.setVisible(True)

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
        self.label_fecha_inicial.setVisible(False)
        self.input_dia_inicial.setVisible(False)
        self.input_mes_inicial.setVisible(False)
        self.input_anio_inicial.setVisible(False)
        self.label_fecha_final.setVisible(False)
        self.input_dia_final.setVisible(False)
        self.input_mes_final.setVisible(False)
        self.input_anio_final.setVisible(False)
        self.boton_consultar.setVisible(False)
        self.label_total_gastado.setVisible(False)
        self.label_resultado_total_gastado.setVisible(False)
        self.label_fecha.setVisible(False)
        self.input_fecha_dia.setVisible(False)
        self.input_fecha_mes.setVisible(False)
        self.input_fecha_anio.setVisible(False)
        self.label_nombre_producto.setVisible(False)
        self.input_nombre_producto.setVisible(False)
        self.label_stock.setVisible(False)
        self.input_stock.setVisible(False)
        self.label_costo_unitario.setVisible(False)
        self.input_costo_unitario.setVisible(False)
        self.label_signo_peso.setVisible(False)
        self.label_tipo_pago.setVisible(False)
        self.eleccion_efectivo.setVisible(False)
        self.eleccion_posnet.setVisible(False)
        self.eleccion_mercadopago.setVisible(False)
        self.boton_confirmar_modificacion.setVisible(False)
        self.boton_confirmar_registro.setVisible(False)
        self.label_fecha_no_valida.setVisible(False)
        self.eleccion_efectivo_2.setVisible(False)
        self.eleccion_posnet_2.setVisible(False)
        self.eleccion_mercadopago_2.setVisible(False)
        self.eleccion_total.setVisible(False)
        self.label_tipo_pago_consulta.setVisible(False)


class VentanaHistorialVentas(Ventana, Ui_HistorialVentas):
    def __init__(self, base_datos, ventana_anterior):
        super().__init__()
        self.setupUi(self)
        self.boton_volver.clicked.connect(self.volver)
        self.boton_agregar_venta.clicked.connect(self.agregar_venta)
        self.boton_modificar_venta.clicked.connect(self.modificar_venta)
        self.boton_confirmar_modificacion.clicked.connect(self.confirmar_modificacion)
        self.boton_confirmar_registro.clicked.connect(self.confirmar_venta)
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
        self.boton_filtrar_ventas_mercadopago.clicked.connect(
            lambda: self.filtrar_tipo_pago_treeview("mercadopago")
        )
        self.base_datos = base_datos
        self.ventana_anterior = ventana_anterior

        self.modelo_ventas = QtGui.QStandardItemModel(self)

        self.actualizar_treeviews()
        self.ocultar_campos()

    def actualizar_treeviews(self):
        self.actualizar_treeview_ventas()

    def actualizar_treeview_ventas(self):
        columnas = [
            "id_venta",
            "fecha",
            "producto",
            "cantidad",
            "precio_unitario",
            "precio_total",
            "tipo_pago",
        ]
        datos = self.base_datos.obtener_ventas_ordenadas()
        lista_widths = [70, 95, 90, 75, 100, 100, 85]
        self.actualizar_treeview(
            self.treeview_ventas,
            self.modelo_ventas,
            columnas,
            datos,
            lista_widths,
        )

    def filtrar_tipo_pago_treeview(self, tipo_pago):
        self.modelo_ventas.removeRows(0, self.modelo_ventas.rowCount())

        ventas = self.base_datos.obtener_ventas_segun_tipo_pago(tipo_pago)

        for venta in ventas:
            item_id_venta = QtGui.QStandardItem(str(venta.id_venta))
            item_fecha = QtGui.QStandardItem(str(venta.fecha))
            item_producto = QtGui.QStandardItem(venta.producto)
            item_cantidad = QtGui.QStandardItem(str(venta.cantidad))
            item_precio_unitario = QtGui.QStandardItem("$" + str(venta.precio_unitario))
            item_precio_total = QtGui.QStandardItem("$" + str(venta.precio_total))
            item_tipo_pago = QtGui.QStandardItem(venta.tipo_pago)

            item_id_venta.setFlags(item_id_venta.flags() & ~QtCore.Qt.ItemIsEditable)
            item_fecha.setFlags(item_fecha.flags() & ~QtCore.Qt.ItemIsEditable)
            item_producto.setFlags(item_producto.flags() & ~QtCore.Qt.ItemIsEditable)
            item_cantidad.setFlags(item_cantidad.flags() & ~QtCore.Qt.ItemIsEditable)
            item_precio_unitario.setFlags(
                item_precio_unitario.flags() & ~QtCore.Qt.ItemIsEditable
            )
            item_precio_total.setFlags(
                item_precio_total.flags() & ~QtCore.Qt.ItemIsEditable
            )
            item_tipo_pago.setFlags(item_tipo_pago.flags() & ~QtCore.Qt.ItemIsEditable)

            self.modelo_ventas.appendRow(
                [
                    item_id_venta,
                    item_fecha,
                    item_producto,
                    item_cantidad,
                    item_precio_unitario,
                    item_precio_total,
                    item_tipo_pago,
                ]
            )

    def agregar_venta(self):
        self.input_fecha_dia.clear()
        self.input_fecha_mes.clear()
        self.input_fecha_anio.clear()
        self.input_nombre_producto.clear()
        self.input_stock.clear()
        self.input_precio_unitario.clear()
        self.ocultar_campos()
        self.mostrar_campos_modificar_venta()
        self.boton_confirmar_modificacion.setVisible(False)
        self.boton_confirmar_registro.setVisible(True)

    def confirmar_venta(self):
        try:
            nuevo_tipo_pago = None
            nueva_fecha = date(
                int(self.input_fecha_anio.text()),
                int(self.input_fecha_mes.text()),
                int(self.input_fecha_dia.text()),
            )
            nuevo_nombre = self.input_nombre_producto.text()
            nueva_cantidad = int(self.input_stock.text())
            nuevo_precio_unitario = round(float(self.input_precio_unitario.text()), 2)
            if self.eleccion_efectivo.isChecked():
                nuevo_tipo_pago = "efectivo"
            elif self.eleccion_posnet.isChecked():
                nuevo_tipo_pago = "posnet"
            elif self.eleccion_mercadopago.isChecked():
                nuevo_tipo_pago = "mercadopago"
            if nuevo_tipo_pago is not None:
                self.base_datos.agregar_venta(
                    nueva_fecha,
                    nuevo_nombre,
                    nueva_cantidad,
                    nuevo_precio_unitario,
                    nuevo_tipo_pago,
                )
                self.ocultar_campos()
                self.actualizar_treeviews()
                QtWidgets.QMessageBox.information(
                    self, "Confirmacion", "Compra agregada con exito."
                )
            else:
                self.mostrar_error_temporal(
                    self.label_seleccione_tipo_pago, "Seleccione un tipo de pago"
                )
        except ValueError:
            self.mostrar_error_temporal(
                self.label_campos_no_validos, "Campos no validos"
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
        elif venta.tipo_pago == "mercadopago":
            self.eleccion_mercadopago.setChecked(True)

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
            elif self.eleccion_mercadopago.isChecked():
                nuevo_tipo_pago = "mercadopago"

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
                self, "Confirmacion", "Venta modificada cone exito."
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
            elif self.eleccion_mercadopago_2.isChecked():
                total_ganado = self.base_datos.consultar_total_vendido_segun_tipo_pago(
                    fecha_inicial, fecha_final, "mercadopago"
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
        self.label_fecha.setVisible(True)
        self.input_fecha_dia.setVisible(True)
        self.input_fecha_mes.setVisible(True)
        self.input_fecha_anio.setVisible(True)
        self.label_nombre_producto.setVisible(True)
        self.input_nombre_producto.setVisible(True)
        self.label_stock.setVisible(True)
        self.input_stock.setVisible(True)
        self.label_precio_unitario.setVisible(True)
        self.input_precio_unitario.setVisible(True)
        self.label_signo_peso.setVisible(True)
        self.label_tipo_pago.setVisible(True)
        self.eleccion_efectivo.setVisible(True)
        self.eleccion_posnet.setVisible(True)
        self.eleccion_mercadopago.setVisible(True)
        self.boton_confirmar_modificacion.setVisible(True)

    def mostrar_campos_consultar_ganancias(self):
        self.label_fecha_inicial.setVisible(True)
        self.input_dia_inicial.setVisible(True)
        self.input_mes_inicial.setVisible(True)
        self.input_anio_inicial.setVisible(True)
        self.label_fecha_final.setVisible(True)
        self.input_dia_final.setVisible(True)
        self.input_mes_final.setVisible(True)
        self.input_anio_final.setVisible(True)
        self.boton_consultar.setVisible(True)
        self.label_total_ganado.setVisible(True)
        self.label_resultado_total_ganado.setVisible(True)
        self.eleccion_efectivo_2.setVisible(True)
        self.eleccion_posnet_2.setVisible(True)
        self.eleccion_mercadopago_2.setVisible(True)
        self.eleccion_total.setVisible(True)
        self.label_tipo_pago_consulta.setVisible(True)

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
        self.label_fecha_inicial.setVisible(False)
        self.input_dia_inicial.setVisible(False)
        self.input_mes_inicial.setVisible(False)
        self.input_anio_inicial.setVisible(False)
        self.label_fecha_final.setVisible(False)
        self.input_dia_final.setVisible(False)
        self.input_mes_final.setVisible(False)
        self.input_anio_final.setVisible(False)
        self.boton_consultar.setVisible(False)
        self.label_total_ganado.setVisible(False)
        self.label_resultado_total_ganado.setVisible(False)
        self.label_fecha.setVisible(False)
        self.input_fecha_dia.setVisible(False)
        self.input_fecha_mes.setVisible(False)
        self.input_fecha_anio.setVisible(False)
        self.label_nombre_producto.setVisible(False)
        self.input_nombre_producto.setVisible(False)
        self.label_stock.setVisible(False)
        self.input_stock.setVisible(False)
        self.label_precio_unitario.setVisible(False)
        self.input_precio_unitario.setVisible(False)
        self.label_signo_peso.setVisible(False)
        self.label_tipo_pago.setVisible(False)
        self.eleccion_efectivo.setVisible(False)
        self.eleccion_posnet.setVisible(False)
        self.eleccion_mercadopago.setVisible(False)
        self.boton_confirmar_modificacion.setVisible(False)
        self.boton_confirmar_registro.setVisible(False)
        self.label_fecha_no_valida.setVisible(False)
        self.eleccion_efectivo_2.setVisible(False)
        self.eleccion_posnet_2.setVisible(False)
        self.eleccion_mercadopago_2.setVisible(False)
        self.eleccion_total.setVisible(False)
        self.label_tipo_pago_consulta.setVisible(False)


class VentanaConsultarGanancias(Ventana, Ui_ConsultarGanancias):
    def __init__(self, base_datos, ventana_anterior):
        super().__init__()
        self.setupUi(self)
        self.boton_volver.clicked.connect(self.volver)
        self.boton_consultar.clicked.connect(self.consultar_ganado)
        self.base_datos = base_datos
        self.ventana_anterior = ventana_anterior

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
            elif self.eleccion_mercadopago.isChecked():
                total_ganado = self.base_datos.consultar_ganancias_segun_tipo_pago(
                    fecha_inicial, fecha_final, "mercadopago"
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


if __name__ == "__main__":

    app = QtWidgets.QApplication([])

    ventana_bienvenida = VentanaBienvenida()
    ventana_login = VentanaLogin(base_datos, ventana_bienvenida)

    ventana_registrar_ventas = VentanaRegistrarVentasVendedor(base_datos)
    ventana_principal_usuario_autorizado = VentanaPrincipalUsuarioAutorizado()
    ventana_registrar_ventas_autorizado = VentanaRegistrarVentasAutorizado(
        base_datos,
        ventana_principal_usuario_autorizado,
    )

    ventana_usuarios = VentanaUsuarios(base_datos, ventana_principal_usuario_autorizado)

    ventana_stock_disponible = VentanaStockDisponible(
        base_datos,
        ventana_principal_usuario_autorizado,
    )

    ventana_elegir_tipo_compra = VentanaElegirTipoCompra(
        ventana_principal_usuario_autorizado
    )
    ventana_registrar_compra_producto_nuevo = VentanaRegistrarCompraProductoNuevo(
        base_datos,
        ventana_elegir_tipo_compra,
    )
    ventana_registrar_compra_producto_listado = VentanaRegistrarCompraProductoListado(
        base_datos,
        ventana_elegir_tipo_compra,
    )
    ventana_historial_compras = VentanaHistorialCompras(
        base_datos,
        ventana_principal_usuario_autorizado,
    )
    ventana_historial_ventas = VentanaHistorialVentas(
        base_datos,
        ventana_principal_usuario_autorizado,
    )
    ventana_consultar_ganancias = VentanaConsultarGanancias(
        base_datos,
        ventana_principal_usuario_autorizado,
    )
    ventana_bienvenida.show()
    app.exec_()
