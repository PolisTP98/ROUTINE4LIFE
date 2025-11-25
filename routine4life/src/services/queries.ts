import {apiGet} from "./api";

// -----------------------------------------------------------------
// | CONSULTAS DE LA API QUE SE EJECUTARÁN EN EL DISPOSITICO MÓVIL |
// -----------------------------------------------------------------

// INTERFAZ PARA TIPAR LA RESPUESTA DE LA API
export interface ConnectionStatus {
  status: string;
  database_connection: string;
  message: string;
}

// SERVICIO QUE CONSULTA LA RUTA DE FLASK
export async function checkConnection(): Promise<ConnectionStatus> {
  return await apiGet<ConnectionStatus>("/connectionStatus");
}