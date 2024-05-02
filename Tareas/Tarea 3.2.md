# Tarea 3.2 Caso practico Automata Finito

## Introducción

Los autómatas finitos son herramientas poderosas en el campo de la informática y la ingeniería, utilizados para modelar y resolver una amplia gama de problemas. En este caso de uso real, exploraremos la aplicación e implementación de un autómata finito en el contexto de un sistema de control de acceso.

## Caso de Uso: Sistema de Control de Acceso con Autómata Finito

En un edificio de oficinas, se requiere un sistema de control de acceso para garantizar la seguridad de las instalaciones. Este sistema debe permitir a los empleados autorizados ingresar a ciertas áreas del edificio mientras restringe el acceso a personas no autorizadas. Para lograr esto, se implementa un autómata finito como parte del software de control de acceso.

### Elementos del Sistema:

1. **Estados del Autómata**:
   - **Estado Inicial (Idle)**: El sistema está esperando una solicitud de acceso.
   - **Estado de Acceso Autorizado (Authorized)**: Se concede acceso a un empleado autorizado.
   - **Estado de Acceso Denegado (Denied)**: Se rechaza el acceso a una persona no autorizada.

2. **Entradas**:
   - **Tarjeta de Acceso**: La entrada que se escanea para solicitar acceso a una determinada área.
   - **Base de Datos de Empleados**: Almacena la información sobre los empleados autorizados y sus privilegios de acceso.

3. **Transiciones entre Estados**:
   - Cuando se escanea una tarjeta de acceso:
     - Si la tarjeta está registrada en la base de datos de empleados, el sistema pasa al estado de acceso autorizado y abre la puerta correspondiente.
     - Si la tarjeta no está registrada, el sistema pasa al estado de acceso denegado y registra el intento de acceso no autorizado.

## Conclusión

En este caso de uso, se ha visto cómo un autómata finito se implementa como parte de un sistema de control de acceso. Esta aplicación demuestra la versatilidad de los autómatas finitos en la resolución de problemas del mundo real, proporcionando una solución eficiente y escalable para garantizar la seguridad de las instalaciones. Además, el uso de un autómata finito facilita la comprensión y el mantenimiento del sistema, lo que lo convierte en una opción ideal para aplicaciones de control y gestión de acceso.
