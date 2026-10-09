CREATE DATABASE pyme;

USE pyme;

CREATE TABLE direccion (
    id_direccion INT AUTO_INCREMENT,
    numero_lugar VARCHAR(30)  NOT NULL,
    calle        VARCHAR(100) NOT NULL,
    comuna       VARCHAR(100) NOT NULL,
    region       VARCHAR(100) NOT NULL,

    CONSTRAINT pk_direccion
    PRIMARY KEY (id_direccion)
) COMMENT = 'Tabla para registrar las Direcciones';

CREATE TABLE proveedor (
    rut                VARCHAR(15) NOT NULL,
    nombre_proveedor   VARCHAR(30) NOT NULL,
    correo_proveedor   VARCHAR(50),
    id_direccion       INT NOT NULL,
    telefono_proveedor VARCHAR(15),

    CONSTRAINT pk_proveedor
    PRIMARY KEY (rut),

    CONSTRAINT fk_p_direccion
    FOREIGN KEY (id_direccion) REFERENCES direccion(id_direccion)
    ON DELETE RESTRICT ON UPDATE CASCADE
) COMMENT = 'Esta tabla sirve para que se registre el proveedor';

CREATE TABLE categoria (
    id_categoria          INT AUTO_INCREMENT,
    nombre_categoria      VARCHAR(35) NOT NULL,
    descripcion_categoria TEXT NULL,

    CONSTRAINT pk_categoria
    PRIMARY KEY (id_categoria)
) COMMENT = 'Esta tabla sirve para el registro de las Categorias de los Productos, junto con una descripcion general';

CREATE TABLE producto (
    gtin                 VARCHAR(14)   NOT NULL,
    nombre_producto      VARCHAR(50)   NOT NULL,
    descripcion_producto TEXT NULL,
    precio_compra        DECIMAL(10,2) NOT NULL,
    perecible            VARCHAR(2)    NOT NULL,
    fecha_vencimiento    DATE NULL,

    CONSTRAINT pk_producto
    PRIMARY KEY (gtin),

    CONSTRAINT ck_producto_precio
    CHECK (precio_compra >= 0),

    CONSTRAINT ck_producto_perecible
    CHECK (perecible IN ('SI', 'NO')),

    CONSTRAINT ck_producto_vencimiento
    CHECK (perecible = 'NO' OR fecha_vencimiento IS NOT NULL)
) COMMENT = 'Esta tabla es para registrar los Productos';

CREATE TABLE almacen (
    id_almacen     INT AUTO_INCREMENT,
    nombre_almacen VARCHAR(50) NOT NULL,
    id_direccion   INT NOT NULL,

    CONSTRAINT pk_almacen
    PRIMARY KEY (id_almacen),

    CONSTRAINT fk_a_direccion
    FOREIGN KEY (id_direccion) REFERENCES direccion(id_direccion)
    ON DELETE RESTRICT ON UPDATE CASCADE
) COMMENT = 'Esta tabla es para registrar los Almacenes';

CREATE TABLE ingresos (
    id_ingresos         INT AUTO_INCREMENT,
    gtin_producto       VARCHAR(14) NOT NULL,
    id_almacen          INT NOT NULL,
    rut_proveedor       VARCHAR(15) NOT NULL,
    fecha_ingreso       DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    cantidad_ingreso    INT NOT NULL,
    observacion_ingreso TEXT,

    CONSTRAINT pk_ingresos
    PRIMARY KEY (id_ingresos),

    CONSTRAINT ck_ingresos_cantidad
    CHECK (cantidad_ingreso > 0),

    CONSTRAINT fk_ingresos_productos
    FOREIGN KEY (gtin_producto) REFERENCES producto(gtin)
    ON DELETE RESTRICT ON UPDATE CASCADE,

    CONSTRAINT fk_ingresos_proveedores
    FOREIGN KEY (rut_proveedor) REFERENCES proveedor(rut)
    ON DELETE RESTRICT ON UPDATE CASCADE,

    CONSTRAINT fk_ingresos_almacen
    FOREIGN KEY (id_almacen) REFERENCES almacen(id_almacen)
    ON DELETE RESTRICT ON UPDATE CASCADE,

    INDEX idx_ingresos_fecha (fecha_ingreso)
) COMMENT = 'Registro de ingresos de productos a los almacenes';

CREATE TABLE salida (
    id_salidas      INT AUTO_INCREMENT,
    gtin_producto   VARCHAR(14) NOT NULL,
    id_almacen      INT NOT NULL,
    cantidad_salida INT NOT NULL,
    fecha_salida    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    motivo_salida   VARCHAR(255),

    CONSTRAINT pk_salidas
    PRIMARY KEY (id_salidas),

    CONSTRAINT ck_salida_cantidad
    CHECK (cantidad_salida > 0),

    CONSTRAINT fk_salidas_productos
    FOREIGN KEY (gtin_producto) REFERENCES producto(gtin)
    ON DELETE RESTRICT ON UPDATE CASCADE,

    CONSTRAINT fk_salidas_almacen
    FOREIGN KEY (id_almacen) REFERENCES almacen(id_almacen)
    ON DELETE RESTRICT ON UPDATE CASCADE,

    INDEX idx_salida_fecha (fecha_salida)
) COMMENT = 'Registro de salidas de productos de los almacenes';

CREATE TABLE proveedor_producto (
    rut_proveedor VARCHAR(15) NOT NULL,
    gtin_producto VARCHAR(14) NOT NULL,

    CONSTRAINT pk_proveedor_producto
    PRIMARY KEY (rut_proveedor, gtin_producto),

    CONSTRAINT fk_pp_proveedor
    FOREIGN KEY (rut_proveedor) REFERENCES proveedor(rut)
    ON DELETE CASCADE ON UPDATE CASCADE,

    CONSTRAINT fk_pp_producto
    FOREIGN KEY (gtin_producto) REFERENCES producto(gtin)
    ON DELETE CASCADE ON UPDATE CASCADE
) COMMENT = 'Esta tabla es para poder saber de que proveedor pertenece cada producto';

CREATE TABLE categoria_producto (
    id_categoria  INT NOT NULL,
    gtin_producto VARCHAR(14) NOT NULL,

    CONSTRAINT pk_categoria_producto
    PRIMARY KEY (id_categoria, gtin_producto),

    CONSTRAINT fk_cp_categoria
    FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria)
    ON DELETE CASCADE ON UPDATE CASCADE,

    CONSTRAINT fk_cp_producto
    FOREIGN KEY (gtin_producto) REFERENCES producto(gtin)
    ON DELETE CASCADE ON UPDATE CASCADE
) COMMENT = 'Esta tabla es para poder saber cuantas Categorias tiene Cada Producto';

CREATE TABLE producto_almacen (
    gtin_producto VARCHAR(14) NOT NULL,
    id_almacen    INT NOT NULL,
    stock         INT NOT NULL DEFAULT 0,

    CONSTRAINT pk_producto_almacen
    PRIMARY KEY (gtin_producto, id_almacen),

    CONSTRAINT ck_pa_stock
    CHECK (stock >= 0),

    CONSTRAINT fk_pa_producto
    FOREIGN KEY (gtin_producto) REFERENCES producto(gtin)
    ON DELETE CASCADE ON UPDATE CASCADE,

    CONSTRAINT fk_pa_almacen
    FOREIGN KEY (id_almacen) REFERENCES almacen(id_almacen)
    ON DELETE CASCADE ON UPDATE CASCADE
) COMMENT = 'Esta tabla es para poder saber cuantos productos esta en cada almacen';