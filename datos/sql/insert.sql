USE pyme;

INSERT INTO direccion (numero_lugar, calle, comuna, region) VALUES
('1250', 'Av. Alemania',          'Temuco',          'La Araucanía'),
('340',  'Calle Bulnes',          'Temuco',          'La Araucanía'),
('88',   'Av. Pedro de Valdivia', 'Padre Las Casas', 'La Araucanía'),
('2100', 'Ruta 5 Sur km 675',     'Temuco',          'La Araucanía'),
('45',   'Calle Caupolicán',      'Villarrica',      'La Araucanía');

INSERT INTO proveedor (rut, nombre_proveedor, correo_proveedor, id_direccion, telefono_proveedor) VALUES
('76.123.456-7', 'Lácteos del Sur',     'ventas@lacteossur.cl',    1, '+56 45 2123456'),
('77.654.321-K', 'Distribuidora Andes', 'contacto@dandes.cl',      2, '+56 45 2765432'),
('78.987.654-3', 'Comercial Araucanía', 'pedidos@comaraucania.cl', 3, '+56 9 87654321');

INSERT INTO categoria (nombre_categoria, descripcion_categoria) VALUES
('Lácteos',   'Leche, yogurt, quesos y derivados'),
('Despensa',  'Abarrotes y productos no perecibles'),
('Aseo',      'Productos de limpieza para el hogar'),
('Panadería', 'Pan y productos de panificación'),
('Bebidas',   'Jugos, aguas y bebidas en general');

INSERT INTO producto (gtin, nombre_producto, descripcion_producto, precio_compra, perecible, fecha_vencimiento) VALUES
('7801610001012', 'Leche Entera 1L',       'Leche entera larga vida',      890.00,  'SI', '2026-12-15'),
('7801610001029', 'Yogurt Frutilla 120g',  'Yogurt batido sabor frutilla', 350.00,  'SI', '2026-11-20'),
('7802820002013', 'Arroz Grado 1 1kg',     'Arroz grano largo',            1290.00, 'NO', NULL),
('7802820002020', 'Fideos Espagueti 400g', 'Fideos de sémola',             780.00,  'NO', NULL),
('7803900003011', 'Aceite Maravilla 1L',   'Aceite vegetal',               2490.00, 'NO', NULL),
('7803900003028', 'Detergente Líquido 3L', 'Detergente para ropa',         5990.00, 'NO', NULL),
('7804650004015', 'Pan de Molde Blanco',   'Pan de molde 600g',            1590.00, 'SI', '2026-10-25'),
('7804650004022', 'Jugo Naranja 1L',       'Jugo néctar de naranja',       1190.00, 'SI', '2027-03-10');

INSERT INTO almacen (nombre_almacen, id_direccion) VALUES
('Bodega Central', 4),
('Bodega Sur',     5);

INSERT INTO ingresos (gtin_producto, id_almacen, rut_proveedor, cantidad_ingreso, observacion_ingreso) VALUES
('7801610001012', 1, '76.123.456-7', 200, 'Pedido semanal'),
('7801610001029', 1, '76.123.456-7', 150, NULL),
('7802820002013', 1, '77.654.321-K', 300, 'Compra mayorista'),
('7802820002020', 1, '77.654.321-K', 250, NULL),
('7803900003011', 2, '77.654.321-K', 120, NULL),
('7803900003028', 2, '78.987.654-3', 80,  NULL),
('7804650004015', 2, '78.987.654-3', 100, 'Entrega diaria'),
('7804650004022', 1, '76.123.456-7', 90,  NULL),
('7801610001012', 2, '76.123.456-7', 100, NULL),
('7802820002013', 2, '77.654.321-K', 150, NULL);

INSERT INTO salida (gtin_producto, id_almacen, cantidad_salida, motivo_salida) VALUES
('7801610001012', 1, 40, 'Venta'),
('7801610001029', 1, 20, 'Merma por vencimiento'),
('7802820002013', 1, 60, 'Venta'),
('7803900003011', 2, 30, 'Venta'),
('7803900003028', 2, 10, 'Venta'),
('7804650004015', 2, 25, 'Venta'),
('7802820002013', 2, 50, 'Venta');

INSERT INTO proveedor_producto (rut_proveedor, gtin_producto) VALUES
('76.123.456-7', '7801610001012'),
('76.123.456-7', '7801610001029'),
('76.123.456-7', '7804650004022'),
('77.654.321-K', '7802820002013'),
('77.654.321-K', '7802820002020'),
('77.654.321-K', '7803900003011'),
('78.987.654-3', '7803900003028'),
('78.987.654-3', '7804650004015');

INSERT INTO categoria_producto (id_categoria, gtin_producto) VALUES
(1, '7801610001012'),
(1, '7801610001029'),
(2, '7802820002013'),
(2, '7802820002020'),
(2, '7803900003011'),
(3, '7803900003028'),
(4, '7804650004015'),
(5, '7804650004022');

-- stock = ingresos - salidas
INSERT INTO producto_almacen (gtin_producto, id_almacen, stock) VALUES
('7801610001012', 1, 160),
('7801610001012', 2, 100),
('7801610001029', 1, 130),
('7802820002013', 1, 240),
('7802820002013', 2, 100),
('7802820002020', 1, 250),
('7803900003011', 2, 90),
('7803900003028', 2, 70),
('7804650004015', 2, 75),
('7804650004022', 1, 90);