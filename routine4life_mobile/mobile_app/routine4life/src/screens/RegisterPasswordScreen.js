import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, KeyboardAvoidingView, Platform, ScrollView } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { COLORS } from '../styles/theme';

// CORRECCIÓN: Agregamos "route" para recibir los parámetros de la pantalla anterior
const RegisterPasswordScreen = ({ navigation, route }) => {
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [secureTextEntry1, setSecureTextEntry1] = useState(true);
  const [secureTextEntry2, setSecureTextEntry2] = useState(true);

  // Extraemos los datos que venían de la pantalla 1
  const formData = route.params?.formData || {};

  const reqLength = password.length >= 8;
  const reqUpper = /[A-Z]/.test(password);
  const reqSpecial = /[0-9!@#$/()={}=.,;:_]/.test(password);
  const reqNoSeq = password.length > 0 && !/(.)\1{2}/.test(password);
  const doMatch = password.length > 0 && password === confirmPassword;

  const isButtonEnabled = reqLength && reqUpper && reqSpecial && reqNoSeq && doMatch;

  const handleFinalRegister = () => {
    if (isButtonEnabled) {
      // Aquí es donde uniremos formData + password para enviarlo a FastAPI. 
      // Por ahora, navegamos al Login mostrando el éxito.
      console.log("Datos listos para enviar:", { ...formData, password });
      navigation.navigate('Login', { registered: true });
    }
  };

  const RequirementItem = ({ text, isMet }) => (
    <View style={styles.reqRow}>
      <Ionicons name={isMet ? "checkmark" : "close"} size={16} color={isMet ? COLORS.success : COLORS.error} />
      <Text style={[styles.reqText, { color: isMet ? COLORS.success : COLORS.error }]}>{text}</Text>
    </View>
  );

  return (
    <KeyboardAvoidingView style={styles.container} behavior={Platform.OS === 'ios' ? 'padding' : 'height'}>
      <View style={styles.header}>
        <TouchableOpacity onPress={() => navigation.goBack()}>
          <Ionicons name="chevron-back" size={35} color={COLORS.primary} />
        </TouchableOpacity>
      </View>
      <ScrollView contentContainerStyle={styles.scroll} showsVerticalScrollIndicator={false}>
        <Text style={styles.title}>Registrarse</Text>
        <View style={styles.form}>
          <View style={styles.inputWrapper}>
            <TextInput
              style={styles.input}
              placeholder="Contraseña"
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
            style={[styles.btn, isButtonEnabled ? styles.btnActive : styles.btnDisabled]}
            disabled={!isButtonEnabled}
            onPress={handleFinalRegister}
          >
            <Text style={styles.btnText}>Registrarse</Text>
          </TouchableOpacity>
        </View>
      </ScrollView>
    </KeyboardAvoidingView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: COLORS.background },
  header: { paddingHorizontal: 20, paddingTop: 50 },
  scroll: { flexGrow: 1, padding: 30, alignItems: 'center' },
  title: { fontSize: 52, fontWeight: 'bold', color: COLORS.primary, marginBottom: 40 },
  form: { width: '100%' },
  inputWrapper: { flexDirection: 'row', backgroundColor: COLORS.inputBackground, borderRadius: 25, height: 55, alignItems: 'center', paddingHorizontal: 20, marginBottom: 10 },
  input: { flex: 1, color: COLORS.inputText, fontSize: 18 },
  reqList: { paddingHorizontal: 15, marginBottom: 20 },
  reqRow: { flexDirection: 'row', alignItems: 'flex-start', marginBottom: 5 },
  reqText: { fontSize: 14, flex: 1, marginLeft: 8, fontWeight: '500' },
  footer: { width: '100%', alignItems: 'center', marginTop: 10 },
  btn: { width: '100%', height: 60, borderRadius: 30, justifyContent: 'center', alignItems: 'center' },
  btnDisabled: { backgroundColor: COLORS.disabled },
  btnActive: { backgroundColor: COLORS.primary },
  btnText: { color: COLORS.buttonLight, fontSize: 24, fontWeight: 'bold' },
});

export default RegisterPasswordScreen;