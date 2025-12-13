// -------------------------------
// | IMPORTAR MÓDULOS NECESARIOS |
// -------------------------------

import {api_get} from "./api";


// -----------------------------------------------------------------
// | CONSULTAS DE LA API QUE SE EJECUTARÁN EN EL DISPOSITIVO MÓVIL |
// -----------------------------------------------------------------

// INTERFAZ PARA TIPAR LA RESPUESTA DE LA API (ConnectionStatus)
export interface connection_status {
  status: string;
  database_connection: string;
  message: string;
}

// CONSULTAR LA RUTA DE FLASK
export async function check_connection(): Promise<connection_status> {
  return await api_get<connection_status>("/connection_status");
}