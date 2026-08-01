import streamlit as st
import pandas as pd

import database

st.set_page_config(
    page_title="Sistema de Inventario",
    page_icon="📦",
    layout="wide"
)

st.title("📦 Sistema de Inventario")

# ==========================
# MÉTRICAS
# ==========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Productos registrados",
        database.contar_productos()
    )

valor = database.obtener_valor_inventario()

if valor is None:
    valor = 0

with col2:
    st.metric(
        "Valor del inventario",
        f"${valor:,.2f}"
    )

st.divider()

producto_caro = database.obtener_producto_mas_caro()

with col3:

    if producto_caro:

        st.metric(
            "💎 Producto más caro",
            producto_caro[1],
            f"${producto_caro[3]:,.2f}"
        )

producto_stock = database.obtener_producto_mas_stock()

with col4:

    if producto_stock:

        st.metric(
            "📦 Mayor stock",
            producto_stock[1],
            f"{producto_stock[4]} unidades"
        )

st.divider()


# ==========================
# FORMULARIO
# ==========================

st.subheader("➕ Agregar producto")

with st.form("agregar_producto"):

    nombre = st.text_input("Nombre")

    categoria = st.text_input("Categoría")

    precio = st.number_input(
        "Precio",
        min_value=0.0,
        step=100.0
    )

    stock = st.number_input(
        "Stock",
        min_value=0,
        step=1
    )

    enviar = st.form_submit_button("Agregar")

    if enviar:

        if nombre.strip() == "" or categoria.strip() == "":

            st.warning("Complete todos los campos.")

        else:

            database.agregar_producto(
                nombre,
                categoria,
                precio,
                stock
            )

            st.success("Producto agregado correctamente.")

            st.rerun()

st.divider()

# ==========================
# INVENTARIO
# ==========================

st.subheader("📋 Inventario")

buscar = st.text_input("🔍 Buscar producto")

productos = database.obtener_productos()

if productos:

    df = pd.DataFrame(
        productos,
        columns=[
            "ID",
            "Nombre",
            "Categoría",
            "Precio",
            "Stock"
        ]
    )

    if buscar:

        df = df[
            df["Nombre"].str.contains(
                buscar,
                case=False,
                na=False
            )
        ]

        st.subheader("📊 Productos por categoría")

        grafico = (
            df.groupby("Categoría")
            .size()
            .reset_index(name="Cantidad")
        )

        st.bar_chart(
            grafico.set_index("Categoría")
        )

        st.info(
            "La tabla permite revisar y editar visualmente los datos. "
            "Para guardar cambios en la base de datos utiliza el formulario de edición inferior."
        )

    tabla_editable = st.data_editor(
        df,
        use_container_width=True,
        num_rows="fixed",
        hide_index=True
    )

    st.divider()

    st.subheader("✏️ Modificar producto")

    productos = database.obtener_productos()

    if productos:

        opciones = {
            f"{p[0]} - {p[1]}": p
            for p in productos
        }

        seleccionado = st.selectbox(
            "Seleccione un producto",
            list(opciones.keys())
        )

        producto = opciones[seleccionado]

        with st.form("editar_producto"):

            nombre = st.text_input(
                "Nombre",
                value=producto[1]
            )

            categoria = st.text_input(
                "Categoría",
                value=producto[2]
            )

            precio = st.number_input(
                "Precio",
                value=float(producto[3]),
                min_value=0.0,
                step=100.0
            )

            stock = st.number_input(
                "Stock",
                value=int(producto[4]),
                min_value=0,
                step=1
            )

            guardar = st.form_submit_button("💾 Guardar cambios")

            if guardar:

                filas = database.modificar_producto(
                    producto[0],
                    nombre,
                    categoria,
                    precio,
                    stock
                )

                if filas:

                    st.success("Producto actualizado correctamente.")

                    st.rerun()

                else:

                    st.error("No fue posible actualizar el producto.")

    st.divider()

    st.subheader("🗑 Eliminar producto")

    productos = database.obtener_productos()

    if productos:

        opciones = {
            f"{p[0]} - {p[1]}": p
            for p in productos
        }

        seleccionado = st.selectbox(
            "Producto a eliminar",
            list(opciones.keys()),
            key="eliminar_producto"
        )

        producto = opciones[seleccionado]

        confirmar = st.checkbox(
            "Confirmo que deseo eliminar este producto"
        )

        if st.button("🗑 Eliminar"):

            if confirmar:

                filas = database.eliminar_producto(producto[0])

                if filas:

                    st.success("Producto eliminado correctamente.")

                    st.rerun()

                else:

                    st.error("No fue posible eliminar el producto.")

            else:

                st.warning("Debe confirmar la eliminación.")

else:

    st.info("No hay productos registrados.")