// ----------------------------------------------
// | SERVICIOS DE LA API (GET AND POST REQUEST) |
// ----------------------------------------------

// API DE ROUTINE4LIFE MOBILE
const BASE_URL = "http://10.0.2.2:5000/api/v0.0.0";

// GET REQUEST
export async function apiGet<T>(endpoint: string): Promise<T> {
    try {
        const response = await fetch(`${BASE_URL}${endpoint}`);
        
        if(!response.ok) {
            throw new Error(`Error ${response.status}: ${response.statusText}`);
        }
        
        const data: T = await response.json();
        return data;
    }
    catch(error) {
        console.error("API GET ERROR: ", error);
        throw error;
    }
}

// POST REQUEST
export async function apiPost<T>(endpoint: string, body: object): Promise<T> {
    try {
        const response = await fetch(`${BASE_URL}${endpoint}`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(body),
        });

        if (!response.ok) {
        throw new Error(`Error ${response.status}: ${response.statusText}`);
        }

        const data: T = await response.json();
        return data;
    }
    catch (error) {
        console.error("API POST ERROR: ", error);
        throw error;
    }
}