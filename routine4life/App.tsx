// -------------------------------
// | IMPORTAR MÓDULOS NECESARIOS |
// -------------------------------

import React, {useEffect, useState} from "react";
import {View, Text, StyleSheet} from "react-native";
import {check_connection} from "./src/services/queries";


// -------------------------------------------
// | EJECUTAR LA API EN EL DISPOSITIVO MÓVIL |
// -------------------------------------------

export default function app() {
  const [response, setResponse] = useState("CONNECTING TO THE API...");
  useEffect(() => {
    check_connection()
      .then((data) => setResponse(JSON.stringify(data, null, 2)))
      .catch((err) => setResponse("ERROR: " + err));
  }, []);
  return (
    <View style={styles.container}>
      <Text style={styles.title}>API STATUS:</Text>
      <Text style={styles.response}>{response}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {padding: 20, marginTop: 40},
  title: {fontSize: 22, fontWeight: "bold"},
  response: {fontFamily: "monospace", fontSize: 16, marginTop: 10},
});