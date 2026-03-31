import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, KeyboardAvoidingView, Platform, ScrollView, Alert, ActivityIndicator } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { COLORS } from '../styles/theme';

const RecoverPasswordStep2Screen = ({ route, navigation }) => {
  // Recuperamos el email pasado desde la Step 1
  const { email } = route.params || {};

  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [secureTextEntry1, setSecureTextEntry1] = useState(true);
  const [secureTextEntry2, setSecureTextEntry2] = useState(true);
  const [isLoading, setIsLoading] = useState(false);

  const reqLength = password.length >= 8;
  const reqUpper = /[A-Z]/.test(password);
  const reqSpecial = /[0-9!@#$/()={}=.,;:_]/.test(password);
  const reqNoSeq = password.length > 0 && !/(.)\1{2}/.test(password);
  const doMatch = password.length > 0 && password === confirmPassword;

  const isButtonEnabled = reqLength && reqUpper && reqSpecial && reqNoSeq && doMatch;

  const handleReset = () => {
    if (isButtonEnabled) {
      setIsLoading(true);

      // Simulamos un pequeño tiempo de carga de 1 segundo para que se vea el ActivityIndicator
      setTimeout(() => {
        setIsLoading(false);
        
        // Mostramos el mensaje y, AL PRESIONAR "Aceptar", redirigimos al Login
        Alert.alert(
          "Éxito", 
          "Contraseña actualizada correctamente.",
          [
            { 
              text: "Aceptar", 
              onPress: () => navigation.navigate('Login', { recovered: true }) 
            }
          ]
        );

      }, 1000);

      /* // === CÓDIGO REAL PARA EL BACKEND (Comentado para la simulación) ===
      // Asegúrate de definir const API_URL = 'http://TU_IP:8000'; arriba cuando lo uses
      
      try {
        const response = await fetch(`${API_URL}/auth-movil/restablecer-contrasena`, {
          method: 'PUT',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ email: email, nueva_contrasena: password }),
        });
        const data = await response.json();
        if (response.ok) {
          Alert.alert("Éxito", data.mensaje || "Contraseña actualizada correctamente.", [
            { text: "Aceptar", onPress: () => navigation.navigate('Login', { recovered: true }) }
          ]);
        } else {
          Alert.alert("Error", data.detail || "No se pudo actualizar la contraseña.");
        }
      } catch (error) {
        console.error("Error:", error);
        Alert.alert("Error", "No se pudo conectar con el servidor.");
      } finally {
        setIsLoading(false);
      }
      */
    }
  };

  const RequirementItem = ({ text, isMet }) => {
    const iconName = isMet ? "checkmark" : "close";
    const statusColor = isMet ? COLORS.success : COLORS.error;
    return (
      <View style={styles.reqRow}>
        <Ionicons name={iconName} size={16} color={statusColor} style={styles.reqIcon} />
        <Text style={[styles.reqText, { color: statusColor }]}>{text}</Text>
      </View>
    );
  };

  return (
    <KeyboardAvoidingView style={styles.container} behavior={Platform.OS === 'ios' ? 'padding' : 'height'}>
      <ScrollView contentContainerStyle={styles.scroll} showsVerticalScrollIndicator={false}>
        <Text style={styles.title}>Restablecer{'\n'}contraseña</Text>

        <View style={styles.form}>
          <View style={styles.inputWrapper}>
            <TextInput
              style={styles.input}
              placeholder="Nueva contraseña"
              placeholderTextColor={COLORS.inputText + '80'}
              value={password}
              onChangeText={setPassword}
              secureTextEntry={secureTextEntry1}
            />
            <TouchableOpacity onPress={() => setSecureTextEntry1(!secureTextEntry1)}>
              <Ionicons name={secureTextEntry1 ? "eye-off" : "eye"} size={24} color={COLORS.primary} />
            </TouchableOpacity>
          </View>

          <View style={styles.reqList}>
            <RequirementItem text="La contraseña debe tener mínimo 8 caracteres" isMet={reqLength} />
            <RequirementItem text="La contraseña debe incluir letras en mayúscula" isMet={reqUpper} />
            <RequirementItem text="La contraseña debe incluir números y caracteres especiales: *?!@#$/()={}=.,;:_" isMet={reqSpecial} />
            <RequirementItem text="La contraseña no debe tener más de dos caracteres repetidos o números en secuencia" isMet={reqNoSeq} />
          </View>

          <View style={styles.inputWrapper}>
            <TextInput
              style={styles.input}
              placeholder="Confirmar contraseña"
              placeholderTextColor={COLORS.inputText + '80'}
              value={confirmPassword}
              onChangeText={setConfirmPassword}
              secureTextEntry={secureTextEntry2}
            />
            <TouchableOpacity onPress={() => setSecureTextEntry2(!secureTextEntry2)}>
              <Ionicons name={secureTextEntry2 ? "eye-off" : "eye"} size={24} color={COLORS.primary} />
            </TouchableOpacity>
          </View>

          <View style={styles.reqList}>
            <RequirementItem text="Las contraseñas coinciden" isMet={doMatch} />
          </View>
        </View>

        <View style={styles.footer}>
          <TouchableOpacity
            style={[styles.btn, isButtonEnabled && !isLoading ? styles.btnActive : styles.btnDisabled]}
            disabled={!isButtonEnabled || isLoading}
            onPress={handleReset}
          >
            {isLoading ? (
              <ActivityIndicator color={COLORS.buttonLight} size="small" />
            ) : (
              <Text style={styles.btnText}>Restablecer</Text>
            )}
          </TouchableOpacity>

          <Text style={styles.loginLink}>
            ¿Ya tienes una cuenta? <Text style={styles.linkRed} onPress={() => navigation.navigate('Login')}>Iniciar sesión</Text>
          </Text>
        </View>
      </ScrollView>
    </KeyboardAvoidingView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: COLORS.background },
  scroll: { flexGrow: 1, padding: 30, alignItems: 'center', paddingTop: '20%' },
  title: { fontSize: 48, fontWeight: 'bold', color: COLORS.primary, textAlign: 'center', marginBottom: 50 },
  form: { width: '100%' },
  inputWrapper: { flexDirection: 'row', backgroundColor: COLORS.inputBackground, borderRadius: 25, height: 55, alignItems: 'center', paddingHorizontal: 20, marginBottom: 10 },
  input: { flex: 1, color: COLORS.inputText, fontSize: 18 },
  reqList: { paddingHorizontal: 20, marginBottom: 20 },
  reqRow: { flexDirection: 'row', alignItems: 'flex-start', marginBottom: 6 },
  reqIcon: { marginTop: 2, marginRight: 8 },
  reqText: { fontSize: 14, flex: 1, fontWeight: '500' },
  footer: { width: '100%', alignItems: 'center', marginTop: 20 },
  btn: { width: '100%', height: 60, borderRadius: 30, justifyContent: 'center', alignItems: 'center', marginBottom: 20 },
  btnDisabled: { backgroundColor: COLORS.disabled },
  btnActive: { backgroundColor: COLORS.primary },
  btnText: { color: COLORS.buttonLight, fontSize: 22, fontWeight: 'bold' },
  loginLink: { color: COLORS.primary, fontSize: 16 },
  linkRed: { color: COLORS.error, fontWeight: 'bold' }
});

export default RecoverPasswordStep2Screen;