import React, { useState } from 'react';
import { 
  View, 
  Text, 
  TextInput, 
  TouchableOpacity, 
  StyleSheet, 
  KeyboardAvoidingView, 
  Platform, 
  ScrollView,
  ActivityIndicator
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import { COLORS } from '../styles/theme';
import { API_URL } from '../api/config';

const RequirementItem = ({ text, isMet }) => (
  <View style={styles.reqRow}>
    <Ionicons name={isMet ? "checkmark" : "close"} size={16} color={isMet ? COLORS.success : COLORS.error} />
    <Text style={[styles.reqText, { color: isMet ? COLORS.success : COLORS.error }]}>{text}</Text>
  </View>
);

const RegisterPasswordScreen = ({ navigation, route }) => {
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [secureTextEntry1, setSecureTextEntry1] = useState(true);
  const [secureTextEntry2, setSecureTextEntry2] = useState(true);
  const [isLoading, setIsLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState('');

  const formData = route.params?.formData || {};

  const reqLength = password.length >= 8;
  const reqUpper = /[A-Z]/.test(password);
  const reqSpecial = /[0-9!@#$/()={}=.,;:_]/.test(password);
  const reqNoSeq = password.length > 0 && !/(.)\1{2}/.test(password);
  const doMatch = password.length > 0 && password === confirmPassword;

  const isButtonEnabled = reqLength && reqUpper && reqSpecial && reqNoSeq && doMatch;

  const handleFinalRegister = async () => {
    if (!isButtonEnabled) return;

    setErrorMessage('');
    setIsLoading(true);

    try {
      const response = await fetch(`${API_URL}/auth-movil/registro`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          nombre_completo: formData.fullName,
          fecha_nacimiento: formData.birthDate,
          sexo: formData.gender,
          email: formData.email,
          telefono: formData.phone,
          contrasena: password,
        }),
      });

      const data = await response.json();

      if (response.ok) {
        navigation.navigate('Login', { registered: true });
      } else {
        const errorMsg = typeof data.detail === 'string' ? data.detail : 'No se pudo completar el registro.';
        setErrorMessage(errorMsg);
      }
    } catch (error) {
      setErrorMessage('Error de conexión. Verifica tu red o el servidor.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <SafeAreaView style={styles.container}>
      <KeyboardAvoidingView 
        style={{ flex: 1 }} 
        behavior={Platform.OS === 'ios' ? 'padding' : undefined}
      >
        <View style={styles.header}>
          <TouchableOpacity 
            onPress={() => navigation.goBack()}
            activeOpacity={0.7}
            hitSlop={{ top: 10, bottom: 10, left: 10, right: 10 }} 
          >
            <Ionicons name="chevron-back" size={35} color={COLORS.primary} />
          </TouchableOpacity>
        </View>

        <ScrollView 
          contentContainerStyle={styles.scroll} 
          showsVerticalScrollIndicator={false}
          keyboardShouldPersistTaps="handled"
        >
          <Text style={styles.title}>Registrarse</Text>
          
          <View style={styles.form}>
            <View style={styles.inputWrapper}>
              <TextInput
                style={styles.input}
                placeholder="Contraseña"
                placeholderTextColor={COLORS.inputText + '80'}
                value={password}
                onChangeText={(text) => {
                  setPassword(text);
                  setErrorMessage('');
                }}
                secureTextEntry={secureTextEntry1}
              />
              <TouchableOpacity onPress={() => setSecureTextEntry1(!secureTextEntry1)}>
                <Ionicons name={secureTextEntry1 ? "eye-off" : "eye"} size={24} color={COLORS.primary} />
              </TouchableOpacity>
            </View>

            <View style={styles.reqList}>
              <RequirementItem text="La contraseña debe tener mínimo 8 caracteres" isMet={reqLength} />
              <RequirementItem text="La contraseña debe incluir letras en mayúscula" isMet={reqUpper} />
              <RequirementItem text="La contraseña debe incluir números y caracteres especiales" isMet={reqSpecial} />
              <RequirementItem text="No debe tener más de dos caracteres repetidos o números en secuencia" isMet={reqNoSeq} />
            </View>

            <View style={styles.inputWrapper}>
              <TextInput
                style={styles.input}
                placeholder="Confirmar contraseña"
                placeholderTextColor={COLORS.inputText + '80'}
                value={confirmPassword}
                onChangeText={(text) => {
                  setConfirmPassword(text);
                  setErrorMessage('');
                }}
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
            {errorMessage !== '' && (
              <Text style={styles.errorText}>{errorMessage}</Text>
            )}

            <TouchableOpacity
              style={[styles.btn, isButtonEnabled && !isLoading ? styles.btnActive : styles.btnDisabled]}
              disabled={!isButtonEnabled || isLoading}
              onPress={handleFinalRegister}
              activeOpacity={0.8}
            >
              {isLoading ? (
                <ActivityIndicator color={COLORS.buttonLight} size="large" />
              ) : (
                <Text style={styles.btnText}>Registrarse</Text>
              )}
            </TouchableOpacity>
          </View>
        </ScrollView>
      </KeyboardAvoidingView>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: COLORS.background },
  header: { paddingHorizontal: 20, paddingTop: 10 }, 
  scroll: { flexGrow: 1, paddingHorizontal: 30, paddingBottom: 30, alignItems: 'center' },
  title: { fontSize: 50, fontWeight: 'bold', color: COLORS.primary, marginBottom: 40 },
  form: { width: '100%' },
  inputWrapper: { flexDirection: 'row', backgroundColor: COLORS.inputBackground, borderRadius: 25, height: 55, alignItems: 'center', paddingHorizontal: 20, marginBottom: 10 },
  input: { flex: 1, color: COLORS.inputText, fontSize: 18 },
  reqList: { paddingHorizontal: 15, marginBottom: 20 },
  reqRow: { flexDirection: 'row', alignItems: 'flex-start', marginBottom: 5 },
  reqText: { fontSize: 14, flex: 1, marginLeft: 8, fontWeight: '500' },
  footer: { width: '100%', alignItems: 'center', marginTop: 10 },
  errorText: { color: COLORS.error, fontSize: 14, fontWeight: '500', marginBottom: 15, textAlign: 'center', paddingHorizontal: 10 },
  btn: { width: '100%', height: 60, borderRadius: 30, justifyContent: 'center', alignItems: 'center' },
  btnDisabled: { backgroundColor: COLORS.disabled },
  btnActive: { backgroundColor: COLORS.primary },
  btnText: { color: COLORS.buttonLight, fontSize: 24, fontWeight: 'bold' },
});

export default RegisterPasswordScreen;