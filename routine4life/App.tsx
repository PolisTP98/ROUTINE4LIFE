import React, {useEffect, useState} from "react";
import {View, Text, StyleSheet} from "react-native";
import {checkConnection} from "./src/services/queries";

// -------------------------------------------
// | EJECUTAR LA API EN EL DISPOSITIVO MÓVIL |
// -------------------------------------------

export default function App() {
  const [response, setResponse] = useState("Conectando a la API...");

  useEffect(() => {
    checkConnection()
      .then((data) => setResponse(JSON.stringify(data, null, 2)))
      .catch((err) => setResponse("Error: " + err));
  }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Estado de la API:</Text>
      <Text style={styles.response}>{response}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {padding: 20, marginTop: 40},
  title: {fontSize: 22, fontWeight: "bold"},
  response: {fontFamily: "monospace", fontSize: 16, marginTop: 10},
});